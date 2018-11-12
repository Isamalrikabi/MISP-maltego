#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='MISP_maltego',
    author='Christophe Vandeplas',
    version='1.0',
    author_email='christophe@vandeplas.com',
    description='Maltego transform for interacting with a MISP Threat Sharing community.',
    license='AGPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    package_data={
        '': ['*.gif', '*.png', '*.conf', '*.mtz', '*.machine']  # list of resources
    },
    install_requires=[
        'canari>=3.3.9,<4',
        'PyMISP'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
