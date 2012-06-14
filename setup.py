# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='imagefit',
    version='0.1',
    description='Render an optimized version of your original image without modifying it.',
    long_description=open('README.md').read(),
    author='Vincent Agnano',
    author_email='vincent.agnano@particul.es',
    url='http://github.com/vinyll/django-imagefit',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ]
)