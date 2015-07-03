#!/usr/bin/env python3

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='Logfind',
    version='0.1',
    url='http://github.com/datruth29/logfind',
    author='Adam Collado',
    author_email='adam.collado@gmail.com',
    description='A log searching tool',
    install_requires=['nose'],
    packages=['logfind'],
    license='CC 1.0 Universal',
    entry_points={
        'console_scripts': ['logfind=logfind:main']
    }
)
