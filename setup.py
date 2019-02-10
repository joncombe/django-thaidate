# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-thaidate',
    version='1.0.0',
    author=u'Jon Combe',
    author_email='jon@naremit.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    url='https://naremit.com',
    license='BSD licence, see LICENCE file',
    description='Replacement for the "date" Django template tag to show Thai years',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
