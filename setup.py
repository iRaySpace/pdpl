# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pdpl/__init__.py
from pdpl import __version__ as version

setup(
	name='pdpl',
	version=version,
	description='Personal Data Protection Law',
	author='9T9IT',
	author_email='info@9t9it.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
