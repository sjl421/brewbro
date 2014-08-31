#!/usr/bin/env python

from distutils.core import setup

execfile('brewbro/version.py')

setup(
    name = 'BrewBro',
    version = __version__,
    description = 'A small web app for managing brews',
    long_description = open('README.md').read() + "\n\n" + open('HISTORY.md').read(),
    author = 'Fredrik Allansson',
    author_email = 'fredrik.allansson@gmail.com',
    url = 'https://github.com/skaggmannen/brewbro',
    packages = [
        'brewbro'
    ],
)