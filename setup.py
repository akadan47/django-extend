# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import django_extend

setup(
    name='django-extend',
    version=django_extend.__version__,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/akadan47/django-extend',
    license='MIT',
    author='Denis Popov',
    author_email='akadan47@gmail.com',
    description='Some django stuff...',
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.6',
        'pytils>=0.3',
    ],
)