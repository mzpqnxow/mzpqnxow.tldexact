#!/usr/bin/env python3
"""
Example! modify for your package!

This is the setup.py for company.group.pypackagedir

Perform tasks

Includes a package, an application and some data files
"""
from glob import glob
from os import walk
from os.path import (
    abspath,
    dirname,
    join as join_path)
from setuptools import (
    setup,
    find_packages)
# You will need versioneer installed, or you can remove this if you don't plan to
# use versioneer
import versioneer


def enumerate_static_content(basedir_list):
    """Helper file to recursively enumerate static content to easily include data_files="""
    file_list = []
    for basedir in basedir_list:
        for path, _, files in walk(basedir):
            file_list.append((path, [join_path(path, filename) for filename in files if filename not in EXCLUDE_FILES]))
    return file_list


CURDIR = abspath(dirname(__file__))

# Assume your package directory is mylib
# Your full package name will be company.group.pypackagedir
# This is based on the below
# This is done for purposes of keeping a package repository
# namespace "clean" so as to avoid collisions with other users'
# packages

PACKAGE = 'packagedir'
PROJECT_NAME = 'py{}'.format(PACKAGE)

ORG = 'company'
OU = 'group'
NAMESPACE = [ORG, OU]
NAME = '.'.join(NAMESPACE + [PROJECT_NAME])

AUTHOR = 'John Q. Doe'
DESCRIPTION = 'A package for doing various things'
EMAIL = 'jqdoe@company.com'
EXCLUDE_FILES = (
    '.keep',
    'constraints.txt',
    'interactive',
    'pip.ini',
    'pip.ini.socks')
LICENSE = 'Proprietary'
# Include data files when installed
PACKAGE_DATA_DIRS = ['etc/packagedir']
PYTHON_REQUIRES = '>=3'

# Keep this in sync with venv/requirements-project.txt for a nice development experience
REQUIRED = ['package1', 'package2', 'package3']
SCRIPTS = glob('bin/*')
URL = 'https://www.company.com'

DATA_FILE_LIST = enumerate_static_content(PACKAGE_DATA_DIRS)

# The below version uses versioneer, you'll need to remove `cmdclass` and change
# `version` to a fixed string like `0.0.1` if you don't want to use versioneer
# If you *do* want versioneer, you'll need to do `versioneer install` inside
# the root of the project to bootstrap it, then make some changes to setup.cfg
setup(
    author=AUTHOR,
    author_email=EMAIL,
    cmdclass=versioneer.get_cmdclass(),
    data_files=DATA_FILE_LIST,
    description=DESCRIPTION,
    include_package_data=True,
    install_requires=REQUIRED,
    license=LICENSE,
    name=NAME,
    packages=find_packages(),
    python_requires=PYTHON_REQUIRES,
    scripts=SCRIPTS,
    url=URL,
    version=versioneer.get_version(),
    zip_safe=False)


#
# The above is a very barebones versioneer capable setuptools installer
#
# Here is an example for using
# setuptools.setup() with a more exotic dependency
#
# setuptools.setup(
#     ...
#     required=['jq @ git+https://github.com/mzpqnxow/jq.py@setuptools-build#egg=jq']
#     ...)
#
# Users have a way to force this behavior when installing as well by using constraints.txt
#
# If the above was written as:
#
# setuptools.setup(
#     ...
#     required=['jq']
#     ...)
#
# ... then a constraints.txt file could be used as follows to force the jq package to use
# the fork and specific branch with a line like this in the constraints file:
#
# ...
# git+https://github.com/mzpqnxow/jq.py@setuptools-build#egg=jq
# ...
#
# When pip goes to get the jq package, it consults the constraints before going
# to any indexes that may be defined (e.g. PyPi) and honors this constraint. This
# gives an end-user some control over packages that they don't maintain when there
# are broken or "not-quite right" dependencies
#