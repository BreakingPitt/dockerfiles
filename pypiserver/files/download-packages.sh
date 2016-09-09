#!/bin/bash
PYTHON=/usr/share/pypiserver/senv/bin/python
PACKAGES_DIR=/var/lib/pypiserver/packages
SCRIPT=/var/lib/pypiserver/scripts/download-packages.py

echo "`date --rfc-3339 s`: Updating pypiserver packages"
$PYTHON $SCRIPT download --pkgdir $PACKAGES_DIR --missing
echo "`date --rfc-3339 s`: Finished updating pypiserver packages"
