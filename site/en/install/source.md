# Build from source

Build a TensorFlow *pip* package from source and install it on Ubuntu Linux and
macOS. While the instructions might work for other systems, it is only tested and
supported for Ubuntu and macOS.

Note: We already provide well-tested, pre-built [TensorFlow packages](./pip.md)
for Linux and macOS systems.


## Setup for Linux and macOS

Install the following build tools to configure your development environment.

### Install Python and the TensorFlow package dependencies

<div class="ds-selector-tabs">
<section>
<h3>Ubuntu</h3>
<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">sudo apt install python-dev python-pip  # or python3-dev python3-pip</code>
</pre>
</section>
<section>
<h3>mac OS</h3>
<p>Requires Xcode 8.3 or later.</p>
<p>Install using the <a href="https://brew.sh/" class="external">Homebrew</a> package manager:</p>
<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"</code>
<code class="devsite-terminal">export PATH="/usr/local/bin:/usr/local/sbin:$PATH"</code>
<code class="devsite-terminal">brew install python@2  # or python (Python 3)</code>
</pre>
</section>
</div><!--/ds-selector-tabs-->

Install the TensorFlow *pip* package dependencies (if using a virtual environment,
omit the `--user` argument):

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install -U --user pip six numpy wheel mock</code>
<code class="devsite-terminal">pip install -U --user keras_applications==1.0.5 --no-deps</code>
<code class="devsite-terminal">pip install -U --user keras_preprocessing==1.0.3 --no-deps</code>
</pre>

The dependencies are listed in the
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/pip_package/setup.py" class="external"><code>setup.py</code></a>
file under `REQUIRED_PACKAGES`.

### Install Bazel

[Install Bazel](https://docs.bazel.build/versions/master/install.html){:.external},
the build tool used to compile TensorFlow.

Add the location of the Bazel executable to your `PATH` environment variable.

### Install GPU support (optional, Linux only)

There is *no* GPU support for macOS.

Read the [GPU support](./gpu.md) guide to install the drivers and additional
software required to run TensorFlow on a GPU.

Note: It is easier to set up one of TensorFlow's GPU-enabled [Docker images](#docker_linux_builds).

### Download the TensorFlow source code

Use [Git](https://git-scm.com/){:.external} to clone the
[TensorFlow repository](https://github.com/tensorflow/tensorflow){:.external}:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow.git</code>
<code class="devsite-terminal">cd tensorflow</code>
</pre>

The repo defaults to the `master` development branch. You can also checkout a
[release branch](https://github.com/tensorflow/tensorflow/releases){:.external}
to build:

<pre class="devsite-terminal prettyprint lang-bsh">
git checkout <em>branch_name</em>  # r1.9, r1.10, etc.
</pre>

To test your copy of the source tree, run the following test (this may take a while):

<pre class="devsite-terminal prettyprint lang-bsh">
bazel test -c opt -- //tensorflow/... -//tensorflow/compiler/... -//tensorflow/contrib/lite/...
</pre>

Key Point: If you're having build problems on the latest development branch, try
a release branch that is known to work.


## Configure the build

Configure your system build by running the following at the root of your
TensorFlow source tree:

<pre class="devsite-terminal devsite-click-to-copy">
./configure
</pre>

This script prompts you for the location of TensorFlow dependencies and asks for
additional build configuration options (compiler flags, for example). The
following shows a sample run of `./configure` (your session may differ):

<section class="expandable">
<h4 class="showalways">View sample configuration session</h4>
<pre class="devsite-terminal">
./configure
You have bazel 0.15.0 installed.
Please specify the location of python. [Default is /usr/bin/python]: <b>/usr/bin/python2.7</b>

Found possible Python library paths:
  /usr/local/lib/python2.7/dist-packages
  /usr/lib/python2.7/dist-packages
Please input the desired Python library path to use.  Default is [/usr/lib/python2.7/dist-packages]

Do you wish to build TensorFlow with jemalloc as malloc support? [Y/n]:
jemalloc as malloc support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Google Cloud Platform support? [Y/n]:
Google Cloud Platform support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Hadoop File System support? [Y/n]:
Hadoop File System support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Amazon AWS Platform support? [Y/n]:
Amazon AWS Platform support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Apache Kafka Platform support? [Y/n]:
Apache Kafka Platform support will be enabled for TensorFlow.

Do you wish to build TensorFlow with XLA JIT support? [y/N]:
No XLA JIT support will be enabled for TensorFlow.

Do you wish to build TensorFlow with GDR support? [y/N]:
No GDR support will be enabled for TensorFlow.

Do you wish to build TensorFlow with VERBS support? [y/N]:
No VERBS support will be enabled for TensorFlow.

Do you wish to build TensorFlow with OpenCL SYCL support? [y/N]:
No OpenCL SYCL support will be enabled for TensorFlow.

Do you wish to build TensorFlow with CUDA support? [y/N]: <b>Y</b>
CUDA support will be enabled for TensorFlow.

Please specify the CUDA SDK version you want to use. [Leave empty to default to CUDA 9.0]: <b>9.0</b>

Please specify the location where CUDA 9.0 toolkit is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:

Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 7.0]: <b>7.0</b>

Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:

Do you wish to build TensorFlow with TensorRT support? [y/N]:
No TensorRT support will be enabled for TensorFlow.

Please specify the NCCL version you want to use. If NCLL 2.2 is not installed, then you can use version 1.3 that can be fetched automatically but it may have worse performance with multiple GPUs. [Default is 2.2]: 1.3

Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your
build time and binary size. [Default is: 3.5,7.0] <b>6.1</b>

Do you want to use clang as CUDA compiler? [y/N]:
nvcc will be used as CUDA compiler.

Please specify which gcc should be used by nvcc as the host compiler. [Default is /usr/bin/gcc]:

Do you wish to build TensorFlow with MPI support? [y/N]:
No MPI support will be enabled for TensorFlow.

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native]:

Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]:
Not configuring the WORKSPACE for Android builds.

Preconfigured Bazel build configs. You can use any of the below by adding "--config=<>" to your build command. See tools/bazel.rc for more details.
    --config=mkl            # Build with MKL support.
    --config=monolithic     # Config for mostly static monolithic build.
Configuration finished
</pre>
</section>

### Configuration options

For [GPU support](./gpu.md), specify the versions of CUDA and cuDNN. If your
system has multiple versions of CUDA or cuDNN installed, explicitly set the
version instead of relying on the default. `./configure` creates symbolic links
to your system's CUDA libraries—so if you update your CUDA library paths, this
configuration step must be run again before building.

For compilation optimization flags, the default (`-march=native`) optimizes the
generated code for your machine's CPU type. However, if building TensorFlow for a
different CPU type, consider a more specific optimization flag. See the
[GCC manual](https://gcc.gnu.org/onlinedocs/gcc-4.5.3/gcc/i386-and-x86_002d64-Options.html){:.external}
for examples.

There are some preconfigured build configs available that can be added to the
`bazel build` command, for example:

* `--config=mk1` —Support for the [Intel® MKL-DNN](https://github.com/intel/mkl-dnn){:.external}.
* `--config=monolithic` —Configuration for a mostly static, monolithic build.

Note: Starting with TensorFlow 1.6, binaries use AVX instructions which may not
run on older CPUs.


## Build the pip package

### Bazel build

#### CPU-only

Use `bazel` to make the TensorFlow package builder with CPU-only support:

<pre class="devsite-terminal devsite-click-to-copy">
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
</pre>

#### GPU support

To make the TensorFlow package builder with GPU support:

<pre class="devsite-terminal devsite-click-to-copy">
bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
</pre>

#### Bazel build options

Building TensorFlow from source can use a lot of RAM. If your system is
memory-constrained, limit Bazel's RAM usage with: `--local_resources 2048,.5,1.0`.

The [official TensorFlow packages](./pip.md) are built with GCC 4 and use the
older ABI. For GCC 5 and later, make your build compatible with the older ABI
using: `--cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0"`. ABI compatibility ensures that
custom ops built against the official TensorFlow package continue to work with
the GCC 5 built package.

### Build the package

The `bazel build` command creates an executable named `build_pip_package`—this
is the program that builds the `pip` package. For example, the following builds a
`.whl` package in the `/tmp/tensorflow_pkg` directory:

<pre class="devsite-terminal devsite-click-to-copy">
./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
</pre>

Although it is possible to build both CUDA and non-CUDA configurations under the
same source tree, it's recommended to run `bazel clean` when switching between
these two configurations in the same source tree.

### Install the package

The filename of the generated `.whl` file depends on the TensorFlow version and
your platform. Use `pip install` to install the package, for example:

<pre class="devsite-terminal prettyprint lang-bsh">
pip install /tmp/tensorflow_pkg/tensorflow-<var>version</var>-cp27-cp27mu-linux_x86_64.whl
</pre>

Success: TensorFlow is now installed.


## Docker Linux builds

TensorFlow's Docker development images are an easy way to set up an environment
to build Linux packages from source. These images already contain the source
code and dependencies required to build TensorFlow. See the TensorFlow
[Docker guide](./docker.md) for installation and the
[list of available image tags](https://hub.docker.com/r/tensorflow/tensorflow/tags/){:.external}.

### CPU-only

The following example uses the `:nightly-devel` image to build a CPU-only
Python&nbsp;2 package from the latest TensorFlow source code. See the
[Docker guide](./docker.md) for available TensorFlow `-devel` tags.

Download the latest development image and start a Docker container that we'll
use to build the *pip* package:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow<var>:nightly-devel</var></code>
<code class="devsite-terminal">docker run -it -w /tensorflow -v $PWD:/mnt -e HOST_PERMS="$(id -u):$(id -g)" \
    tensorflow/tensorflow<var>:nightly-devel</var> bash</code>

<code class="devsite-terminal tfo-terminal-root">git pull  # within the container, download the latest source code</code>
</pre>

The above `docker run` command starts a shell in the `/tensorflow` directory—the
root of the source tree. It mounts the host's current directory in the container's
`/mnt` directory, and passes the host user's information to the container through
an environmental variable (used to set permissions—Docker can make this tricky).

Alternatively, to build a host copy of TensorFlow within a container, mount the
host source tree at the container's `/tensorflow` directory:

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it -w /tensorflow -v <var>/path/to/tensorflow</var>:/tensorflow -v $PWD:/mnt \
    -e HOST_PERMS="$(id -u):$(id -g)" tensorflow/tensorflow:<var>nightly-devel</var> bash
</pre>

With the source tree set up, build the TensorFlow package within the container's
virtual environment:

1. Configure the build—this prompts the user to answer build configuration questions.
2. Build the tool used to create the *pip* package.
3. Run the tool to create the *pip* package.
4. Adjust the ownership permissions of the file for outside the container.

<pre class="devsite-disable-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">./configure  # answer prompts or use defaults</code>

<code class="devsite-terminal tfo-terminal-root">bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package</code>

<code class="devsite-terminal tfo-terminal-root">./bazel-bin/tensorflow/tools/pip_package/build_pip_package /mnt  # create package</code>

<code class="devsite-terminal tfo-terminal-root">chown $HOST_PERMS /mnt/tensorflow-<var>version</var>-cp27-cp27mu-linux_x86_64.whl</code>
</pre>

Install and verify the package within the container:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">pip uninstall tensorflow  # remove current version</code>

<code class="devsite-terminal tfo-terminal-root">pip install /mnt/tensorflow-<var>version</var>-cp27-cp27mu-linux_x86_64.whl</code>
<code class="devsite-terminal tfo-terminal-root">cd /tmp  # don't import from source directory</code>
<code class="devsite-terminal tfo-terminal-root">python -c "import tensorflow as tf; print(tf.__version__)"</code>
</pre>

Success: TensorFlow is now installed.

On your host machine, the TensorFlow *pip* package is in the current directory
(with host user permissions): <code>./tensorflow-<var>version</var>-cp27-cp27mu-linux_x86_64.whl</code>

### GPU support

Docker is the easiest way to build GPU support for TensorFlow since the *host*
machine only requires the
[NVIDIA®&nbsp;driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}
(the *NVIDIA® CUDA® Toolkit* doesn't have to be installed). See the
[GPU support guide](./gpu.md) and the TensorFlow [Docker guide](./docker.md)
to set up [nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external} (Linux only).

The following example downloads the TensorFlow `:nightly-devel-gpu-py3` image
and uses `nvidia-docker` to run the GPU-enabled container. This development image
is configured to build a Python 3 *pip* package with GPU support:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow<var>:nightly-devel-gpu-py3</var></code>
<code class="devsite-terminal">docker run --runtime=nvidia -it -w /tensorflow -v $PWD:/mnt -e HOST_PERMS="$(id -u):$(id -g)" \
    tensorflow/tensorflow<var>:nightly-devel-gpu-py3</var> bash</code>
</pre>

Then, within the container's virtual environment, build the TensorFlow package
with GPU support:

<pre class="devsite-disable-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">./configure  # answer prompts or use defaults</code>

<code class="devsite-terminal tfo-terminal-root">bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package</code>

<code class="devsite-terminal tfo-terminal-root">./bazel-bin/tensorflow/tools/pip_package/build_pip_package /mnt  # create package</code>

<code class="devsite-terminal tfo-terminal-root">chown $HOST_PERMS /mnt/tensorflow-<var>version</var>-cp35-cp35m-linux_x86_64.whl</code>
</pre>

Install and verify the package within the container and check for a GPU:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">pip uninstall tensorflow  # remove current version</code>

<code class="devsite-terminal tfo-terminal-root">pip install /mnt/tensorflow-<var>version</var>-cp27-cp27mu-linux_x86_64.whl</code>
<code class="devsite-terminal tfo-terminal-root">cd /tmp  # don't import from source directory</code>
<code class="devsite-terminal tfo-terminal-root">python -c "import tensorflow as tf; print(tf.contrib.eager.num_gpus())"</code>
</pre>

Success: TensorFlow is now installed.


## Tested build configurations

### Linux

<table>
<tr><th>Version</th><th>CPU/GPU</th><th>Python version</th><th>Compiler</th><th>Build tools</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow-1.11.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.10.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.9.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.11.0</td></tr>
  <tr><td>tensorflow-1.8.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.10.0</td></tr>
<tr><td>tensorflow-1.7.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.10.0</td></tr>
<tr><td>tensorflow-1.6.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.9.0</td></tr>
<tr><td>tensorflow-1.5.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.8.0</td></tr>
<tr><td>tensorflow-1.4.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.5.4</td></tr>
<tr><td>tensorflow-1.3.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.2.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.1.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.2</td></tr>
<tr><td>tensorflow-1.0.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.2</td></tr>
</table>

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow_gpu-1.11.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.10.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.9.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.11.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.8.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.9.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.7.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.9.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.6.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.9.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.5.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.8.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.4.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.5.4</td><td>6</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.3.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.5</td><td>6</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.2.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.5</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.1.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.0.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
</table>

### macOS

<table>
<tr><th>Version</th><th>CPU/GPU</th><th>Python version</th><th>Compiler</th><th>Build tools</th></tr>
<tr><td>tensorflow-1.11.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.11.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.10.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.9.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.11.0</td></tr>
<tr><td>tensorflow-1.8.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.10.1</td></tr>
<tr><td>tensorflow-1.7.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.10.1</td></tr>
<tr><td>tensorflow-1.6.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.8.1</td>
<tr><td>tensorflow-1.5.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.8.1</td>
<tr><td>tensorflow-1.4.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.5.4</td></tr>
<tr><td>tensorflow-1.3.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.2.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.1.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td></tr>
<tr><td>tensorflow-1.0.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td></tr>
</table>

<table>
<tr><th>Version</th><th>CPU/GPU</th><th>Python version</th><th>Compiler</th><th>Build tools</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow_gpu-1.1.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.0.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
</table>
