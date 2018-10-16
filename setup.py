#!/usr/bin/env python
import os

import setuptools

readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')

try:
    from m2r import parse_from_file

    README = parse_from_file(readme_file)
except ImportError:
    # m2r may not be installed in user environment
    with open(readme_file) as f:
        README = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def _read(relpath):
    fullpath = os.path.join(os.path.dirname(__file__), relpath)
    with open(fullpath) as f:
        return f.read()


def _read_reqs(relpath):
    fullpath = os.path.join(os.path.dirname(__file__), relpath)
    with open(fullpath) as f:
        return [s.strip() for s in f.readlines()
                if (s.strip() and not s.startswith("#"))]


_REQUIREMENTS_TXT = _read_reqs("requirements.txt")
_TESTS_REQUIREMENTS_TXT = _read_reqs("tests-requirements.txt")
_DEPENDENCY_LINKS = [l for l in _REQUIREMENTS_TXT if "://" in l]
_INSTALL_REQUIRES = [l for l in _REQUIREMENTS_TXT if "://" not in l]
_TEST_REQUIRE = [l for l in _TESTS_REQUIREMENTS_TXT if "://" not in l]

setuptools.setup(
    name='make-songbook',
    version='0.0.1',
    packages=['makesongbook'],
    include_package_data=True,
    license='GPLv3',
    install_requires=_INSTALL_REQUIRES,
    dependency_links=_DEPENDENCY_LINKS,
    tests_require=_TEST_REQUIRE,
    description='Digital songbook maker.',
    long_description=README,
    url='http://github.com/adericbourg/make-songbook',
    author='Alban Dericbourg',
    author_email='alban@dericbourg.net',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'make-songbook.pex = makesongbook.make_songbook:main'
        ],
    },
)
