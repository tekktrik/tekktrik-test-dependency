# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tekktrik-test-dependency",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Test dependency for testing Dependabot",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # The project's main homepage.
    url="https://github.com/tekktrik/tekktrik-test-dependency",
    # Author details
    author="Tekktrik",
    author_email="tekktrik@gmail.com",
    # Choose your license
    license="MIT",
    # What does your project relate to?
    keywords="test dependency tekktrik",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # TODO: IF LIBRARY FILES ARE A PACKAGE FOLDER,
    #       CHANGE `py_modules=['...']` TO `packages=['...']`
    py_modules=["tekktrik_test_dependency"],
)
