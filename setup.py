from distutils.core import setup
from setuptools import setup, find_packages

setup (
    name = 'SevenFt10.C4.Diagrams',
    version = '0.1dev0',
    author = 'Mike Burns',
    author_email = 'mike@7ft10.com',
    packages = find_packages(),
    long_description = open('README.md').read()
)
