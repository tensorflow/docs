
<!-- Copyright 2018 The TensorFlow Hub Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================-->

# Creating the TensorFlow Hub pip package using Linux

Note: This document is for developers interested in modifying TensorFlow Hub
itself. To _use_ TensorFlow Hub, see the [Install instructions](installation.md)

If you make changes to TensorFlow Hub pip package, you will likely want to
rebuild the pip package from source to try out your changes.

This requires:

*   Python
*   TensorFlow
*   Git
*   [Bazel](https://docs.bazel.build/versions/master/install.html)

Alternatively, if you install the protobuf compiler you can
[try out your changes without using bazel](#develop).

## Setup a virtualenv {:#setup}

### Activate virtualenv

Install virtualenv if it's not installed already:

```shell
~$ sudo apt-get install python-virtualenv
```

Create a virtual environment for the package creation:

```shell
~$ virtualenv --system-site-packages tensorflow_hub_env
```

And activate it:

```shell
~$ source ~/tensorflow_hub_env/bin/activate  # bash, sh, ksh, or zsh
~$ source ~/tensorflow_hub_env/bin/activate.csh  # csh or tcsh
```

### Clone the TensorFlow Hub repository.

```shell
(tensorflow_hub_env)~/$ git clone https://github.com/tensorflow/hub
(tensorflow_hub_env)~/$ cd hub
```

## Test your changes

### Run TensorFlow Hub's tests

```shell
(tensorflow_hub_env)~/hub/$ bazel test tensorflow_hub:all
```

## Build and install the package

### Build TensorFlow Hub pip packaging script

To build a pip package for TensorFlow Hub:

```shell
(tensorflow_hub_env)~/hub/$ bazel build tensorflow_hub/pip_package:build_pip_package
```

### Create the TensorFlow Hub pip package

```shell
(tensorflow_hub_env)~/hub/$ bazel-bin/tensorflow_hub/pip_package/build_pip_package \
/tmp/tensorflow_hub_pkg
```

### Install and test the pip package (optional)

Run the following commands to install the pip package.

```shell
(tensorflow_hub_env)~/hub/$ pip install /tmp/tensorflow_hub_pkg/*.whl
```

Test import TensorFlow Hub:

```shell
(tensorflow_hub_env)~/hub/$ cd ..  # exit the directory to avoid confusion
(tensorflow_hub_env)~/$ python -c "import tensorflow_hub as hub"
```

## "Developer" install (experimental)

<a id="develop"></a>

Warning: This approach to running TensorFlow is experimental, and not officially
supported by the TensorFlow Hub team.

Building the package with bazel is the only officially supported method. However
if you are unfamiliar with bazel simpler to work with open source tools. For
that you can do a "developer install" of the package.

This installation method allows you to install the working directory into your
python environment, so that ongoing changes are reflected when you import the
package.

### Setup the repository

First setup the virtualenv and repository, as described [above](#setup).

### Install `protoc`

Because TensorFlow Hub uses protobufs you will need the protobuf compiler to
create the necessary python `_pb2.py` files from the `.proto` files.

#### On a Mac:

```
(tensorflow_hub_env)~/hub/$ brew install protobuf
```

#### On Linux

```
(tensorflow_hub_env)~/hub/$ sudo apt install protobuf-compiler
```

### Compile the `.proto` files

Initially there are no `_pb2.py` files in the directory:

```
(tensorflow_hub_env)~/hub/$ ls -1 tensorflow_hub/*_pb2.py
```

Run `protoc` to create them:

```
(tensorflow_hub_env)~/hub/$ protoc -I=tensorflow_hub --python_out=tensorflow_hub tensorflow_hub/*.proto
(tensorflow_hub_env)~/hub/$ ls -1 tensorflow_hub/*_pb2.py
```

<pre>
tensorflow_hub/image_module_info_pb2.py
tensorflow_hub/module_attachment_pb2.py
tensorflow_hub/module_def_pb2.py
</pre>

Note: Don't forget to recompile the `_pb2.py` files if you make changes to the
`.proto` definitions.

### Import directly from the repository

With the `_pb2.py` files in place, you can use try out your modifications
directly from the TensorFlow Hub directory:

```
(tensorflow_hub_env)~/$ python -c "import tensorflow_hub as hub"
```

### Install in "developer" mode

Or to use this from outside the repository root, you can use the `setup.py
develop` installation:

```
(tensorflow_hub_env)~/hub/$ python tensorflow_hub/pip_package/setup.py develop
```

Now you can use your local changes in a regular python virtualenv, without the
need to rebuild and install the pip package for each new change:

```shell
(tensorflow_hub_env)~/hub/$ cd ..  # exit the directory to avoid confusion
(tensorflow_hub_env)~/$ python -c "import tensorflow_hub as hub"
```

## De-activate the virtualenv

```shell
(tensorflow_hub_env)~/hub/$ deactivate
```
