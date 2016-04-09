#!/bin/env python3

import sys

from setuptools import setup

pack_name = 'ezcrypt'

from ezcrypt import __version__


def readme():
    with open('README.rst') as f:
        return f.read()

print('Current version: ', __version__)
version = __version__.split('.')


if sys.argv[-1] == 'minor':
    version[2] = str(int(version[2]) + 1)
    del sys.argv[-1]
elif sys.argv[-1] == 'major':
    version[1] = str(int(version[1]) + 1)
    version[2] = '0'
    del sys.argv[-1]
elif sys.argv[-1] == 'huge':
    version[0] = str(int(version[0]) + 1)
    version[1] = '0'
    version[2] = '0'
    del sys.argv[-1]


version = '.'.join(version)

setup(
    name=pack_name,
    packages=[pack_name], # this must be the same as the name above
    version=version,
    include_package_data=True,
#    license='MIT',
    description='A helper for encrypting bytes',
    long_description=readme(),
    author='Christoffer Zakrisson',
    author_email='christoffer_zakrisson@hotmail.com',
    url='https://github.com/Zaeb0s/ez-crypt',
    keywords=['crypt', 'encrypt', 'decrypt', 'key', 'iv', 'easy'],
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python :: 3.5',
                 'Operating System :: POSIX :: Linux',
                 'License :: OSI Approved :: MIT License'],

    install_requires=['pycrypto']
)
with open(pack_name + '/version', 'w') as f:
    f.write(version)

print('Installed version: ' + version)
