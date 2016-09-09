#!/bin/sh
# Downloads missing python packages in the pypiserver
#
# When a user requests a package non present in the server, a HTTP 302 redirect
# to pypi.python.org is returned instead, so the package gets downloaded from
# the main index.
#
# This task checks all HTTP 302 responses and downloads the missing package
# from the main index, so further requests wont fail, improving the caching
# behaviour of the pypiserver.
#
PIP=/usr/share/pypiserver/env/bin/pip
PYPI_URL=https://pypi.python.org/simple
PACKAGES_DIR=/var/lib/pypiserver/packages
LOGFILE=/var/log/nginx/pypiserver.access.log
PACKAGES=$(grep "/simple/\(\w\+\)/ HTTP/1.1\" 302" ${LOGFILE} | sed -e "s|.*/simple/\(\w\+\).*|\1|" | sort -u)

echo "`date --rfc-3339 s` Fetching missed packages: `echo "$PACKAGES" | tr '\n' ' '`"
for package in $PACKAGES
do
  COMMAND="${PIP} -q install -i ${PYPI_URL} -d ${PACKAGES_DIR}  ${package}"
  echo "`date --rfc-3339 s` Downloading ${package} to /var/lib/pypiserver/packages "
  echo "`date --rfc-3339 s` ${COMMAND}"
  $COMMAND || echo "Failed"
done
echo "`date --rfc-3339 s`: Finished fetching missed packages"
