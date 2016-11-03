"""Setup for ii_charts XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='ii_charts-xblock',
    version='0.1',
    description='ii_charts XBlock',   # TODO: write a better description.
    license='MIT',          # TODO: choose a license: 'AGPL v3' and 'Apache 2.0' are popular.
    packages=[
        'ii_charts',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'ii_charts = ii_charts:ChartsXBlock',
        ]
    },
    package_data=package_data("ii_charts", ["static", "public"]),
)
