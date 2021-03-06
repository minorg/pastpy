from pathlib import Path

from setuptools import setup, find_packages

# MY_DIR_PATH = Path(__file__).parent.absolute()

# with open(os.path.join(MY_DIR_PATH, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()

setup(
    author="Minor Gordon",
    author_email="pastpy@minorgordon.net",
    name="pastpy",
    description="Python library for working with PastPerfect databases",
    license="BSD",
    # long_description=long_description,
    url="https://github.com/minorg/pastpy",
    version="1.0.3",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ],
    entry_points={"console_scripts": ["pastpy=pastpy.cli:main"],},
    install_requires=("beautifulsoup4", "dbf", "enum34"),
    # What does your project relate to?
    keywords="pastperfect",
    packages=find_packages(),
)
