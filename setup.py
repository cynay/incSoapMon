# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Yannic Schneider',
    author_email='v@vendetta.ch',
    url='https://github.com/cynay/xxx',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

