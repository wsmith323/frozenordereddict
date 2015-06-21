import os

from setuptools import setup, find_packages

__version__ = "1.2.0"

def file_read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as flo:
        return flo.read()

setup(
    name = "frozenordereddict",
    version = __version__,
    packages = find_packages(),
    install_requires = [],
    author = "Warren A. Smith",
    author_email = "warren@wandrsmith.net",
    description = "Frozen OrderedDict.",
    long_description = file_read("README.rst"),
    license = "MIT",
    keywords = "ordereddict frozendict frozenordereddict orderedfrozendict ordered frozen dict",
    url = "https://github.com/wsmith323/frozenordereddict",
    test_suite = "tests",
)
