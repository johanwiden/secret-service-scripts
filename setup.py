#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, '__version__.py')) as f:
    exec(f.read(), about)

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/johanwiden/secret-service-scripts',
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: X11 Applications',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Desktop Environment',
        ],
    project_urls = {
        "Bug Tracker": "https://github.com/johanwiden/secret-service-scripts/issues"
    },
    license='MIT License',
    packages=setuptools.find_packages(),
    # packages=['i3-switch-window'],
    install_requires=['SecretStorage','argparse'],
)
