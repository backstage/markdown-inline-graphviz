import os
import sys
from setuptools import setup

VERSION = '1.1.3'

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(VERSION))
    print("  git push --tags")
    sys.exit()

setup(
    name="markdown_graphviz_inline",
    version=VERSION,
    py_modules=["markdown_inline_graphviz"],
    install_requires=['Markdown>=3.0'],
    author="TechDocs Core",
    author_email="protean@spotify.com",
    description="Render inline graphs with Markdown and Graphviz (python3 version)",
    long_description="This is a fork of cesaremorel/markdown-inline-graphviz which is a continuation of sprin/markdown-inline-graphviz for pip3.",
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/backstage/markdown-inline-graphviz",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
