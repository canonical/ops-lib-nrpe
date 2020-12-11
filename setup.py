# This file is part of the ops-lib-nrpe component for Juju Operator
# Framework Charms.
# Copyright 2020 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.


import setuptools


def get_long_description():
    with open("README.md", "r") as f:
        return f.read()


setuptools.setup(
    name="ops-lib-nrpe",
    version='0.1.0',
    author="Enzo Aguado",
    author_email="enzo.aguado@canonical.com",
    description="NRPE plugin relation for Juju Operator Framework Charms",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/canonical/ops-lib-nrpe",
    packages=["nrpe"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords="juju charm opslib nrpe nagios alterting",
    project_urls={
        "Juju": "https://juju.is/",
        "Juju Operator Framework": "https://pypi.org/project/ops/",
    },
    python_requires=">=3.6",
    install_requires=["ops >= 0.8.0", "PyYAML"],
)