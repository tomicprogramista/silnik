# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# Based on https://github.com/pypa/sampleproject/blob/master/setup.py
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='silnik',
    version='0.0.1',
    description='silnik do gier pani magister',
    long_description=long_description,
    author='kxkaro, tomicprogramista',
    author_email='tomic@onet.com.pl',
    packages=find_packages(exclude=['tests']),
    install_requires=['pygame', 'numpy', 'pillow'],
)
