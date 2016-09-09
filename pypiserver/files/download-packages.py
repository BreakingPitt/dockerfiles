 -*- coding: utf-8 -*-
"""Downloads all installers available in pypi for already present packages"""
from gevent import monkey; monkey.patch_all()  # noqa

import io
import os
import re
import hashlib
import itertools
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

import click
import requests
from gevent import spawn
from gevent.pool import Pool

try:
    import xmlrpclib as xmlrpc
except ImportError:
    try:
        from xmlrpclib.client import xmlrpc
    except ImportError:
        import xmlrpc.client as xmlrpc

VENV = u"/var/lib/pypiserver/scripts"
PACKAGES_DIR = u"/var/lib/pypiserver/packages"
DEFAULT_INDEX = u"https://pypi.python.org/pypi"
DEFAULT_LOGFILE = u"/var/log/nginx/pypiserver.access.log"


class RequestsTransport(xmlrpc.Transport):
    """Drop in Transport for xmlrpclib that uses Requests instead of httplib"""
    # change our user agent to reflect Requests
    user_agent = "Python XMLRPC with Requests (python-requests.org)"

    # override this if you'd like to https
    use_https = False

    def request(self, host, handler, request_body, verbose):
        """Make an xmlrpc request.  """
        headers = {'User-Agent': self.user_agent, 'Content-Type': 'text/xml'}
        url = self._build_url(host, handler)

        try:
            resp = requests.post(url, data=request_body, headers=headers)
        except ValueError:
            raise
        except Exception:
            raise  # something went wrong

        try:
            resp.raise_for_status()
        except requests.RequestException as e:
            raise xmlrpc.ProtocolError(
                url, resp.status_code, str(e), resp.headers)

        return self.parse_response(resp)

    def parse_response(self, resp):
        """Parse the xmlrpc response.  """
        p, u = self.getparser()
        p.feed(resp.content)
        p.close()
        return u.close()

    def _build_url(self, host, handler):
        """Build a url for our request based on the host, handler and use_http
        property
        """
        scheme = 'https' if self.use_https else 'http'
        return '%s://%s/%s' % (scheme, host, handler)


def make_server(url):
    return xmlrpc.ServerProxy(url, transport=RequestsTransport())


def get_local_packages(path):
    return sorted(set(parse_dist_name(filename) for filename in os.listdir(path)))


def parse_dist_name(filename):
    """Some distribution names include the "-" character in the name"""
    name, ext = filename.rsplit('.', 1)
    fields = name.split('-')
    for i, name in enumerate(fields):
        if name and name[0].isdigit():  # find the "version" field
            return u"-".join(fields[:i])
    return fields[0]


def fetch_releases(url, packages):
    """Fetch last release from a list of packages

    :param url: pypi index url
    :param packages: list of package names eg: ['SQLAlchemy']
    :returns: list of releases eg: [('SQLAlchemy', '1.0.8')]
    """
    click.echo(u'Fetching release_urls for {} packages'.format(len(packages)))
    server = make_server(url)
    tasks = [(name, spawn(server.package_releases, name)) for name in packages]

    for name, task in tasks:
        try:
            # Expects list of version names eg: ['1.0.8']
            value = task.get()
            if value:
                yield name, value[0]
            else:
                click.secho(u'No release for {}'.format(name), fg='yellow')
        except Exception as error:
            click.secho(u'Could not get package_releases for {}: {}'
                        .format(name, error), fg='red', err=True)


def fetch_release_urls(url, releases):
    """Fetch list of files for a each package release

    :param url: pypi index url
    :param releases: list of package releases eg: [('SQLAlchemy', '1.0.8')]
    :returns: list of of package file lists

        [
          [{
           'comment_text': '',
            'downloads': 3163,
            'filename': 'roundup-1.1.2.tar.gz',
            'has_sig': True,
            'md5_digest': '7c395da56412e263d7600fa7f0afa2e5',
            'packagetype': 'sdist',
            'python_version': 'source',
            'size': 876455,
            'upload_time': <DateTime '20060427T06:22:35' at 912fecc>,
            'url': 'http://pypi.python.org/packages/source/r/roundup/roundup-1.1.2.tar.gz'
          }]
        ]
    """
    click.echo(u'Fetching release_urls for {} packages'.format(len(releases)))
    server = make_server(url)
    tasks = [(name, version, spawn(server.release_urls, name, version))
             for name, version in releases]

    for name, version, task in tasks:
        try:
            yield task.get()
        except Exception as error:
            click.secho(u'Could not get release_urls for {} {}: {}'
                        .format(name, version, error), fg='red', err=True)


def stream_to_file(response, path):
    with open(path, 'wb') as stream:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                stream.write(chunk)
                stream.flush()


def file_integrity(path, md5):
    with open(path, 'rb') as stream:
        return hashlib.md5(stream.read()).hexdigest() == md5


def filter_existing_files(pkgdir, release_urls):
    """Skips already present files"""
    pkgs = [pkg for pkg in release_urls
            if not os.path.isfile(os.path.join(pkgdir, pkg['filename']))]

    if len(pkgs) < len(release_urls):
        click.echo(u'skipping {} files already present in {}'
                   .format(len(release_urls) - len(pkgs), pkgdir))

    return pkgs


def fetch_release_files(pkgdir, release_urls, workers):
    """Fetch each given file

    :param pkgdir: destination directory
    :param release_urls: list of dicts with release download definition
    """
    click.echo(u'Fetching release files for {} packages'.format(len(release_urls)))
    pool = Pool(workers)

    def download(pkg):
        return (pkg, requests.get(pkg['url'], stream=True))

    for pkg, response in pool.imap_unordered(download, release_urls):
        path = os.path.join(pkgdir, pkg['filename'])

        try:
            stream_to_file(response, path)
        except Exception as error:
            click.secho(u'Could not get release_file for {}: {}'
                        .format(pkg['filename'], error), fg='red', err=True)
        else:
            if file_integrity(path, pkg['md5_digest']):
                click.secho(u'Downloaded {}'.format(pkg['filename']), fg='green')
            else:
                click.secho(u'Removing corrupted file: {}'.format(path), fg='red', err=True)
                try:
                    os.unlink(path)
                except Exception as error:
                    click.secho(u'Could not remove file {}: {}'.format(path, error))


def parse_missing_packages(path):
    """Parses missing package requests on pypiserver HTTP log

    Cache miss log line:

        "GET /simple/eventlet/ HTTP/1.1" 302

    :param path: path to log file
    :returns: list of package names
    """
    regex = re.compile(r'"GET /simple/(?P<pkg>\w+)/ HTTP/1.1" 302')
    with io.open(path, 'r', encoding='utf-8') as stream:
        return sorted(set(m.group('pkg') for m in map(regex.search, stream) if m))


class Url(click.ParamType):
    name = u'Url'

    def convert(self, value, param, ctx):
        if value:
            parts = urlparse.urlsplit(value)
            if not parts.scheme or not parts.netloc:
                self.fail(u'{} is not a valid URL'.format(value), param, ctx)
            return value


@click.group()
def cli():
    """Handle python installers repository"""


@cli.command()
@click.option('--pkgdir', type=click.Path(file_okay=False),
              default=PACKAGES_DIR, show_default=True)
def packages(pkgdir):
    """Lists local packages"""
    click.echo(u'\n'.join(get_local_packages(pkgdir)))


@cli.command()
@click.option('--logfile', type=click.Path(file_okay=False),
              default=DEFAULT_LOGFILE, show_default=True)
def missing(logfile):
    """Lists not present packages that were requested today"""
    click.echo(u'\n'.join(parse_missing_packages(logfile)))


@cli.command()
@click.option('--pkgdir', type=click.Path(file_okay=False),
              default=PACKAGES_DIR, show_default=True)
@click.option('-i', '--index-url', type=Url(),
              default=DEFAULT_INDEX, show_default=True)
def releases(pkgdir, index_url):
    """Lists available package releases"""
    local_packages = get_local_packages(pkgdir)
    releases = fetch_releases(index_url, local_packages)
    click.echo(u'\n'.join(map(u' '.join, releases)))


@cli.command()
@click.option('-p', '--pkgdir', type=click.Path(file_okay=False),
              default=PACKAGES_DIR, show_default=True)
@click.option('-i', '--index-url', type=Url(),
              default=DEFAULT_INDEX, show_default=True)
@click.option('--dry', is_flag=True, show_default=True)
@click.option('-w', '--workers', default=10, show_default=True)
@click.option('-m', '--missing', is_flag=True, show_default=True,
              help="Adds today's missing packages to the files to download")
@click.option('--logfile', type=click.Path(dir_okay=False),
              default=DEFAULT_LOGFILE, show_default=True)
def download(pkgdir, index_url, dry, workers, missing, logfile):
    packages = get_local_packages(pkgdir)
    click.echo(u'Found {} packages in {}'.format(len(packages), pkgdir))

    if missing:
        click.echo(u'Parsing missing files from {}'.format(logfile))
        packages = parse_missing_packages(logfile) + packages

    releases = list(fetch_releases(index_url, packages))
    release_urls = fetch_release_urls(index_url, releases)  # [[e], [e], ..]
    release_urls = list(itertools.chain.from_iterable(release_urls))  # [e, e, ..]
    release_urls = filter_existing_files(pkgdir, release_urls)

    if dry:
        click.echo(u'Files to be downloaded:')
        click.echo(u'\n'.join(map(lambda pkg: pkg['url'], release_urls)))
        click.echo(u'\nWould have downloaded: {} files into {}'
                   .format(len(release_urls), pkgdir))
        return

    fetch_release_files(pkgdir, release_urls, workers)


if __name__ == "__main__":
    cli()
