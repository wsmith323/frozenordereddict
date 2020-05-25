import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "frozenordereddict", 'VERSION.txt')) as f:
    __version__ = f.read().strip()

setup(
    name = "frozenordereddict",
    version = __version__,
    packages = find_packages(),
    install_requires = [],
    author = "Warren A. Smith",
    author_email = "warren@wandrsmith.net",
    description = "Frozen OrderedDict.",
    long_description = "An immutable wrapper around an OrderedDict",
    long_description_content_type = "text/plain",
    license = "MIT",
    keywords = "ordereddict frozendict frozenordereddict orderedfrozendict ordered frozen dict",
    url = "https://github.com/wsmith323/frozenordereddict",
    test_suite = "tests",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)
