# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""tensorflow_docs is a package for generating python api-reference docs."""

import subprocess
import sys

from setuptools import find_packages
from setuptools import setup

project_name = 'tensorflow-docs'
version = '0.0.0'

try:
  version += subprocess.check_output(['git', 'rev-parse',
                                      'HEAD']).decode('utf-8')
except subprocess.CalledProcessError:
  pass

DOCLINES = __doc__.split('\n')

REQUIRED_PKGS = [
    'astor',
    'absl-py',
    'protobuf>=3.14',
    'pyyaml',
]

# Dataclasses is in-built from py >=3.7. This version is a backport for py 3.6.
if (sys.version_info.major, sys.version_info.minor) == (3, 6):
  REQUIRED_PKGS.append('dataclasses')

VIS_REQURE = [
    'numpy',
    'PILLOW',
    'webp',
]

# https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords
setup(
    name=project_name,
    version=version,
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    author='Google Inc.',
    author_email='packages@tensorflow.org',
    url='http://github.com/tensorflow/docs',
    download_url='https://github.com/tensorflow/docs/tags',
    license='Apache 2.0',
    packages=find_packages('tools'),
    package_dir={'': 'tools'},
    scripts=[],
    install_requires=REQUIRED_PKGS,
    extras_require={'vis': VIS_REQURE},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow api reference',
    # Include_package_data is required for setup.py to recognize the MAINFEST.in
    #   https://python-packaging.readthedocs.io/en/latest/non-code-files.html
    include_package_data=True,
)
