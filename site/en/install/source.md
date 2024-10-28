# Build from source

Build a TensorFlow *pip* package from source and install it on Ubuntu Linux and
macOS. While the instructions might work for other systems, it is only tested
and supported for Ubuntu and macOS.

Note: Well-tested, pre-built [TensorFlow packages](./pip.md) for Linux and macOS
systems are already provided.

## Setup for Linux and macOS

Install the following build tools to configure your development environment.

### Install Python and the TensorFlow package dependencies

<div class="ds-selector-tabs">
<section>
<h3>Ubuntu</h3>
<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">sudo apt install python3-dev python3-pip</code>
</pre>
</section>
<section>
<h3>macOS</h3>
<p>Requires Xcode 9.2 or later.</p>
<p>Install using the <a href="https://brew.sh/" class="external">Homebrew</a> package manager:</p>
<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">brew install python</code>
</pre>
</section>
</div><!--/ds-selector-tabs-->

Install the TensorFlow *pip* package dependencies (if using a virtual
environment, omit the `--user` argument):

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install -U --user pip</code>
</pre>

Note: A `pip` version >19.0 is required to install the TensorFlow 2 `.whl`
package. Additional required dependencies are listed in the
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/pip_package/setup.py" class="external"><code>setup.py</code></a>
file under `REQUIRED_PACKAGES`.

### Install Bazel

To build TensorFlow, you will need to install Bazel.
[Bazelisk](https://github.com/bazelbuild/bazelisk) is an easy way to install
Bazel and automatically downloads the correct Bazel version for TensorFlow. For
ease of use, add Bazelisk as the `bazel` executable in your `PATH`.

If Bazelisk is not available, you can manually
[install Bazel](https://bazel.build/install). Make
sure to install the correct Bazel version from TensorFlow's
[.bazelversion](https://github.com/tensorflow/tensorflow/blob/master/.bazelversion)
file.

### Install Clang (recommended, Linux only)

Clang is a C/C++/Objective-C compiler that is compiled in C++ based on LLVM. It
is the default compiler to build TensorFlow starting with TensorFlow 2.13. The
current supported version is LLVM/Clang 17.

[LLVM Debian/Ubuntu nightly packages](https://apt.llvm.org) provide an automatic
installation script and packages for manual installation on Linux. Make sure you
run the following command if you manually add llvm apt repository to your
package sources:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">sudo apt-get update && sudo apt-get install -y llvm-17 clang-17</code>
</pre>

Now that `/usr/lib/llvm-17/bin/clang` is the actual path to clang in this case.

Alternatively, you can download and unpack the pre-built
[Clang + LLVM 17](https://github.com/llvm/llvm-project/releases/tag/llvmorg-17.0.2).

Below is an example of steps you can take to set up the downloaded Clang + LLVM
17 binaries on Debian/Ubuntu operating systems:

1.  Change to the desired destination directory: `cd <desired directory>`

1.  Load and extract an archive file...(suitable to your architecture):
    <pre class="prettyprint lang-bsh">
    <code class="devsite-terminal">wget https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.2/clang+llvm-17.0.2-x86_64-linux-gnu-ubuntu-22.04.tar.xz
    </code>
    <code class="devsite-terminal">tar -xvf clang+llvm-17.0.2-x86_64-linux-gnu-ubuntu-22.04.tar.xz
    </code>
    </pre>

1.  Copy the extracted contents (directories and files) to `/usr` (you may need
    sudo permissions, and the correct directory may vary by distribution). This
    effectively installs Clang and LLVM, and adds it to the path. You should not
    have to replace anything, unless you have a previous installation, in which
    case you should replace the files:
    <pre class="prettyprint lang-bsh">
    <code class="devsite-terminal">cp -r clang+llvm-17.0.2-x86_64-linux-gnu-ubuntu-22.04/* /usr</code>
    </pre>

1.  Check the obtained Clang + LLVM 17 binaries version:
    <pre class="prettyprint lang-bsh">
    <code class="devsite-terminal">clang --version</code>
    </pre>

1.  Now that `/usr/bin/clang` is the actual path to your new clang. You can run
    the `./configure` script or manually set environment variables `CC` and
    `BAZEL_COMPILER` to this path.

### Install GPU support (optional, Linux only)

There is *no* GPU support for macOS.

Read the [GPU support](./pip.md) guide to install the drivers and additional
software required to run TensorFlow on a GPU.

Note: It is easier to set up one of TensorFlow's GPU-enabled [Docker images](#docker_linux_builds).

### Download the TensorFlow source code

Use [Git](https://git-scm.com/) to clone the
[TensorFlow repository](https://github.com/tensorflow/tensorflow):

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow.git</code>
<code class="devsite-terminal">cd tensorflow</code>
</pre>

The repo defaults to the `master` development branch. You can also check out a
[release branch](https://github.com/tensorflow/tensorflow/releases)
to build:

<pre class="devsite-terminal prettyprint lang-bsh">
git checkout <em>branch_name</em>  # r2.2, r2.3, etc.
</pre>


## Configure the build

TensorFlow builds are configured by the `.bazelrc` file in the repository's
root directory. The `./configure` or `./configure.py` scripts can be used to
adjust common settings.

Please run the `./configure` script from the repository's root directory. This
script will prompt you for the location of TensorFlow dependencies and asks for
additional build configuration options (compiler flags, for example). Refer to
the _Sample session_ section for details.

<pre class="devsite-terminal devsite-click-to-copy">
./configure
</pre>

There is also a python version of this script, `./configure.py`. If using a
virtual environment, `python configure.py` prioritizes paths
within the environment, whereas `./configure` prioritizes paths outside
the environment. In both cases you can change the default.

### Sample session

The following shows a sample run of `./configure` script (your
session may differ):

<section class="expandable">
<h4 class="showalways">View sample configuration session</h4>
<pre class="devsite-terminal">
./configure
You have bazel 6.1.0 installed.
Please specify the location of python. [Default is /Library/Frameworks/Python.framework/Versions/3.9/bin/python3]: 


Found possible Python library paths:
  /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages
Please input the desired Python library path to use.  Default is [/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages]

Do you wish to build TensorFlow with ROCm support? [y/N]:
No ROCm support will be enabled for TensorFlow.

Do you wish to build TensorFlow with CUDA support? [y/N]:
No CUDA support will be enabled for TensorFlow.

Do you want to use Clang to build TensorFlow? [Y/n]:
Clang will be used to compile TensorFlow.

Please specify the path to clang executable. [Default is /usr/lib/llvm-16/bin/clang]:

You have Clang 16.0.4 installed.

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -Wno-sign-compare]:


Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]: n
Not configuring the WORKSPACE for Android builds.

Do you wish to build TensorFlow with iOS support? [y/N]: n
No iOS support will be enabled for TensorFlow.

Preconfigured Bazel build configs. You can use any of the below by adding "--config=<>" to your build command. See .bazelrc for more details.
	--config=mkl         	# Build with MKL support.
	--config=mkl_aarch64 	# Build with oneDNN and Compute Library for the Arm Architecture (ACL).
	--config=monolithic  	# Config for mostly static monolithic build.
	--config=numa        	# Build with NUMA support.
	--config=dynamic_kernels	# (Experimental) Build kernels into separate shared objects.
	--config=v1          	# Build with TensorFlow 1 API instead of TF 2 API.
Preconfigured Bazel build configs to DISABLE default on features:
	--config=nogcp       	# Disable GCP support.
	--config=nonccl      	# Disable NVIDIA NCCL support.

</pre>
</section>

### Configuration options

#### GPU support

##### from v.2.18.0
For [GPU support](./pip.md), set `cuda=Y` during configuration and specify the
versions of CUDA and cuDNN if required. Bazel will download CUDA and CUDNN
packages automatically or point to CUDA/CUDNN/NCCL redistributions on local file
system if required.

##### before v.2.18.0
For [GPU support](./pip.md), set `cuda=Y` during configuration and specify the
versions of CUDA and cuDNN. If your system has multiple versions of CUDA or
cuDNN installed, explicitly set the version instead of relying on the default.
`./configure` creates symbolic links to your system's CUDA libraries—so if you
update your CUDA library paths, this configuration step must be run again before
building.

#### Optimizations

For compilation optimization flags, the default (`-march=native`) optimizes the
generated code for your machine's CPU type. However, if building TensorFlow for
a different CPU type, consider a more specific optimization flag. Check the
[GCC manual](https://gcc.gnu.org/onlinedocs/gcc-4.5.3/gcc/i386-and-x86_002d64-Options.html)
for examples.

#### Preconfigured configurations

There are some preconfigured build configs available that can be added to the
`bazel build` command, for example:

*   `--config=dbg` —Build with debug info. See
    [CONTRIBUTING.md](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md)
    for details.
*   `--config=mkl` —Support for the
    [Intel® MKL-DNN](https://github.com/intel/mkl-dnn).
*   `--config=monolithic` —Configuration for a mostly static, monolithic build.


## Build and install the pip package

#### Bazel build options

Refer to the Bazel
[command-line reference](https://bazel.build/reference/command-line-reference)
for
[build options](https://bazel.build/reference/command-line-reference#build-options).

Building TensorFlow from source can use a lot of RAM. If your system is
memory-constrained, limit Bazel's RAM usage with: `--local_ram_resources=2048`.

The [official TensorFlow packages](./pip.md) are built with a Clang toolchain
that complies with the manylinux2014 package standard.

### Build the package

To build pip package, you need to specify `--repo_env=WHEEL_NAME` flag.
depending on the provided name, package will be created, e.g:

To build tensorflow CPU package:
<pre class="devsite-terminal devsite-click-to-copy">
bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow_cpu
</pre>

To build tensorflow GPU package:
<pre class="devsite-terminal devsite-click-to-copy">
bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow --config=cuda --config=cuda_wheel
</pre>

To build tensorflow TPU package:
<pre class="devsite-terminal devsite-click-to-copy">
bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow_tpu --config=tpu
</pre>

To build nightly package, set `tf_nightly` instead of `tensorflow`, e.g.
to build CPU nightly package:
<pre class="devsite-terminal devsite-click-to-copy">
bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tf_nightly_cpu
</pre>

As a result, generated wheel will be located in
<pre class="devsite-terminal devsite-click-to-copy">
bazel-bin/tensorflow/tools/pip_package/wheel_house/
</pre>

### Install the package

The filename of the generated `.whl` file depends on the TensorFlow version and
your platform. Use `pip install` to install the package, for example:

<pre class="devsite-terminal prettyprint lang-bsh">
pip install bazel-bin/tensorflow/tools/pip_package/wheel_house/tensorflow-<var>version</var>-<var>tags</var>.whl
</pre>

Success: TensorFlow is now installed.


## Docker Linux builds

TensorFlow's Docker development images are an easy way to set up an environment
to build Linux packages from source. These images already contain the source
code and dependencies required to build TensorFlow. Go to the TensorFlow
[Docker guide](./docker.md) for installation instructions and the
[list of available image tags](https://hub.docker.com/r/tensorflow/tensorflow/tags/).

### CPU-only

The following example uses the `:devel` image to build a CPU-only package from
the latest TensorFlow source code. Check the [Docker guide](./docker.md) for
available TensorFlow `-devel` tags.

Download the latest development image and start a Docker container that you'll
use to build the *pip* package:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow<var>:devel</var></code>
<code class="devsite-terminal">docker run -it -w /tensorflow_src -v $PWD:/mnt -e HOST_PERMS="$(id -u):$(id -g)" \
    tensorflow/tensorflow<var>:devel</var> bash</code>

<code class="devsite-terminal tfo-terminal-root">git pull  # within the container, download the latest source code</code>
</pre>

The above `docker run` command starts a shell in the `/tensorflow_src`
directory—the root of the source tree. It mounts the host's current directory in
the container's `/mnt` directory, and passes the host user's information to the
container through an environmental variable (used to set permissions—Docker can
make this tricky).

Alternatively, to build a host copy of TensorFlow within a container, mount the
host source tree at the container's `/tensorflow` directory:

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it -w /tensorflow -v <var>/path/to/tensorflow</var>:/tensorflow -v $PWD:/mnt \
    -e HOST_PERMS="$(id -u):$(id -g)" tensorflow/tensorflow:<var>devel</var> bash
</pre>

With the source tree set up, build the TensorFlow package within the container's
virtual environment:

1.  Optional: Configure the build—this prompts the user to answer build
    configuration questions.
2.  Build the *pip* package.
3.  Adjust the ownership permissions of the file for outside the container.

<pre class="devsite-disable-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">./configure  # if necessary</code>

<code class="devsite-terminal tfo-terminal-root">bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow_cpu --config=opt</code>
`
<code class="devsite-terminal tfo-terminal-root">chown $HOST_PERMS bazel-bin/tensorflow/tools/pip_package/wheel_house/tensorflow-<var>version</var>-<var>tags</var>.whl</code>
</pre>

Install and verify the package within the container:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">pip uninstall tensorflow  # remove current version</code>

<code class="devsite-terminal tfo-terminal-root">pip install bazel-bin/tensorflow/tools/pip_package/wheel_house/tensorflow-<var>version</var>-<var>tags</var>.whl</code>
<code class="devsite-terminal tfo-terminal-root">cd /tmp  # don't import from source directory</code>
<code class="devsite-terminal tfo-terminal-root">python -c "import tensorflow as tf; print(tf.__version__)"</code>
</pre>

Success: TensorFlow is now installed.

On your host machine, the TensorFlow *pip* package is in the current directory
(with host user permissions):
<code>./tensorflow-<var>version</var>-<var>tags</var>.whl</code>

### GPU support

Note: Starting from Tensorflow v.2.18.0 the wheels can be built from
source on a machine without GPUs and without NVIDIA driver installed.

Docker is the easiest way to build GPU support for TensorFlow since the *host*
machine only requires the
[NVIDIA®&nbsp;driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver)
(the *NVIDIA® CUDA® Toolkit* doesn't have to be installed). Refer to the
[GPU support guide](./pip.md) and the TensorFlow [Docker guide](./docker.md) to
set up [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
(Linux only).

The following example downloads the TensorFlow `:devel-gpu` image and uses
`nvidia-docker` to run the GPU-enabled container. This development image is
configured to build a *pip* package with GPU support:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow<var>:devel-gpu</var></code>
<code class="devsite-terminal">docker run --gpus all -it -w /tensorflow -v $PWD:/mnt -e HOST_PERMS="$(id -u):$(id -g)" \
    tensorflow/tensorflow<var>:devel-gpu</var> bash</code>
<code class="devsite-terminal tfo-terminal-root">git pull  # within the container, download the latest source code</code>
</pre>

Then, within the container's virtual environment, build the TensorFlow package
with GPU support:

<pre class="devsite-disable-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">./configure  # if necessary</code>

<code class="devsite-terminal tfo-terminal-root">bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow --config=cuda --config=cuda_wheel --config=opt</code>

<code class="devsite-terminal tfo-terminal-root">chown $HOST_PERMS bazel-bin/tensorflow/tools/pip_package/wheel_house/tensorflow-<var>version</var>-<var>tags</var>.whl</code>
</pre>

Install and verify the package within the container and check for a GPU:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">pip uninstall tensorflow  # remove current version</code>

<code class="devsite-terminal tfo-terminal-root">pip install bazel-bin/tensorflow/tools/pip_package/wheel_house/tensorflow-<var>version</var>-<var>tags</var>.whl</code>
<code class="devsite-terminal tfo-terminal-root">cd /tmp  # don't import from source directory</code>
<code class="devsite-terminal tfo-terminal-root">python -c "import tensorflow as tf; print(\"Num GPUs Available: \", len(tf.config.list_physical_devices('GPU')))"</code>
</pre>

Success: TensorFlow is now installed.


<a name="tested_build_configurations"></a>
## Tested build configurations

### Linux

#### CPU

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th></tr>
<tr><td>tensorflow-2.18.0</td><td>3.9-3.12</td><td>Clang 17.0.6</td><td>Bazel 6.5.0</td></tr>
<tr><td>tensorflow-2.17.0</td><td>3.9-3.12</td><td>Clang 17.0.6</td><td>Bazel 6.5.0</td></tr>
<tr><td>tensorflow-2.16.1</td><td>3.9-3.12</td><td>Clang 17.0.6</td><td>Bazel 6.5.0</td></tr>
<tr><td>tensorflow-2.15.0</td><td>3.9-3.11</td><td>Clang 16.0.0</td><td>Bazel 6.1.0</td></tr>
<tr><td>tensorflow-2.14.0</td><td>3.9-3.11</td><td>Clang 16.0.0</td><td>Bazel 6.1.0</td></tr>
<tr><td>tensorflow-2.13.0</td><td>3.8-3.11</td><td>Clang 16.0.0</td><td>Bazel 5.3.0</td></tr>
<tr><td>tensorflow-2.12.0</td><td>3.8-3.11</td><td>GCC 9.3.1</td><td>Bazel 5.3.0</td></tr>
<tr><td>tensorflow-2.11.0</td><td>3.7-3.10</td><td>GCC 9.3.1</td><td>Bazel 5.3.0</td></tr>
<tr><td>tensorflow-2.10.0</td><td>3.7-3.10</td><td>GCC 9.3.1</td><td>Bazel 5.1.1</td></tr>
<tr><td>tensorflow-2.9.0</td><td>3.7-3.10</td><td>GCC 9.3.1</td><td>Bazel 5.0.0</td></tr>
<tr><td>tensorflow-2.8.0</td><td>3.7-3.10</td><td>GCC 7.3.1</td><td>Bazel 4.2.1</td></tr>
<tr><td>tensorflow-2.7.0</td><td>3.7-3.9</td><td>GCC 7.3.1</td><td>Bazel 3.7.2</td></tr>
<tr><td>tensorflow-2.6.0</td><td>3.6-3.9</td><td>GCC 7.3.1</td><td>Bazel 3.7.2</td></tr>
<tr><td>tensorflow-2.5.0</td><td>3.6-3.9</td><td>GCC 7.3.1</td><td>Bazel 3.7.2</td></tr>
<tr><td>tensorflow-2.4.0</td><td>3.6-3.8</td><td>GCC 7.3.1</td><td>Bazel 3.1.0</td></tr>
<tr><td>tensorflow-2.3.0</td><td>3.5-3.8</td><td>GCC 7.3.1</td><td>Bazel 3.1.0</td></tr>
<tr><td>tensorflow-2.2.0</td><td>3.5-3.8</td><td>GCC 7.3.1</td><td>Bazel 2.0.0</td></tr>
<tr><td>tensorflow-2.1.0</td><td>2.7, 3.5-3.7</td><td>GCC 7.3.1</td><td>Bazel 0.27.1</td></tr>
<tr><td>tensorflow-2.0.0</td><td>2.7, 3.3-3.7</td><td>GCC 7.3.1</td><td>Bazel 0.26.1</td></tr>
<tr><td>tensorflow-1.15.0</td><td>2.7, 3.3-3.7</td><td>GCC 7.3.1</td><td>Bazel 0.26.1</td></tr>
<tr><td>tensorflow-1.14.0</td><td>2.7, 3.3-3.7</td><td>GCC 4.8</td><td>Bazel 0.24.1</td></tr>
<tr><td>tensorflow-1.13.1</td><td>2.7, 3.3-3.7</td><td>GCC 4.8</td><td>Bazel 0.19.2</td></tr>
<tr><td>tensorflow-1.12.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td></tr>
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

#### GPU

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow-2.18.0</td><td>3.9-3.12</td><td>Clang 17.0.6</td><td>Bazel 6.5.0</td><td>9.3</td><td>12.5</td></tr>
<tr><td>tensorflow-2.17.0</td><td>3.9-3.12</td><td>Clang 17.0.6</td><td>Bazel 6.5.0</td><td>8.9</td><td>12.3</td></tr>
<tr><td>tensorflow-2.16.1</td><td>3.9-3.12</td><td>Clang 17.0.6</td><td>Bazel 6.5.0</td><td>8.9</td><td>12.3</td></tr>
<tr><td>tensorflow-2.15.0</td><td>3.9-3.11</td><td>Clang 16.0.0</td><td>Bazel 6.1.0</td><td>8.9</td><td>12.2</td></tr>
<tr><td>tensorflow-2.14.0</td><td>3.9-3.11</td><td>Clang 16.0.0</td><td>Bazel 6.1.0</td><td>8.7</td><td>11.8</td></tr>
<tr><td>tensorflow-2.13.0</td><td>3.8-3.11</td><td>Clang 16.0.0</td><td>Bazel 5.3.0</td><td>8.6</td><td>11.8</td></tr>
<tr><td>tensorflow-2.12.0</td><td>3.8-3.11</td><td>GCC 9.3.1</td><td>Bazel 5.3.0</td><td>8.6</td><td>11.8</td></tr>
<tr><td>tensorflow-2.11.0</td><td>3.7-3.10</td><td>GCC 9.3.1</td><td>Bazel 5.3.0</td><td>8.1</td><td>11.2</td></tr>
<tr><td>tensorflow-2.10.0</td><td>3.7-3.10</td><td>GCC 9.3.1</td><td>Bazel 5.1.1</td><td>8.1</td><td>11.2</td></tr>
<tr><td>tensorflow-2.9.0</td><td>3.7-3.10</td><td>GCC 9.3.1</td><td>Bazel 5.0.0</td><td>8.1</td><td>11.2</td></tr>
<tr><td>tensorflow-2.8.0</td><td>3.7-3.10</td><td>GCC 7.3.1</td><td>Bazel 4.2.1</td><td>8.1</td><td>11.2</td></tr>
<tr><td>tensorflow-2.7.0</td><td>3.7-3.9</td><td>GCC 7.3.1</td><td>Bazel 3.7.2</td><td>8.1</td><td>11.2</td></tr>
<tr><td>tensorflow-2.6.0</td><td>3.6-3.9</td><td>GCC 7.3.1</td><td>Bazel 3.7.2</td><td>8.1</td><td>11.2</td></tr>
<tr><td>tensorflow-2.5.0</td><td>3.6-3.9</td><td>GCC 7.3.1</td><td>Bazel 3.7.2</td><td>8.1</td><td>11.2</td></tr>
<tr><td>tensorflow-2.4.0</td><td>3.6-3.8</td><td>GCC 7.3.1</td><td>Bazel 3.1.0</td><td>8.0</td><td>11.0</td></tr>
<tr><td>tensorflow-2.3.0</td><td>3.5-3.8</td><td>GCC 7.3.1</td><td>Bazel 3.1.0</td><td>7.6</td><td>10.1</td></tr>
<tr><td>tensorflow-2.2.0</td><td>3.5-3.8</td><td>GCC 7.3.1</td><td>Bazel 2.0.0</td><td>7.6</td><td>10.1</td></tr>
<tr><td>tensorflow-2.1.0</td><td>2.7, 3.5-3.7</td><td>GCC 7.3.1</td><td>Bazel 0.27.1</td><td>7.6</td><td>10.1</td></tr>
<tr><td>tensorflow-2.0.0</td><td>2.7, 3.3-3.7</td><td>GCC 7.3.1</td><td>Bazel 0.26.1</td><td>7.4</td><td>10.0</td></tr>
<tr><td>tensorflow_gpu-1.15.0</td><td>2.7, 3.3-3.7</td><td>GCC 7.3.1</td><td>Bazel 0.26.1</td><td>7.4</td><td>10.0</td></tr>
<tr><td>tensorflow_gpu-1.14.0</td><td>2.7, 3.3-3.7</td><td>GCC 4.8</td><td>Bazel 0.24.1</td><td>7.4</td><td>10.0</td></tr>
<tr><td>tensorflow_gpu-1.13.1</td><td>2.7, 3.3-3.7</td><td>GCC 4.8</td><td>Bazel 0.19.2</td><td>7.4</td><td>10.0</td></tr>
<tr><td>tensorflow_gpu-1.12.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.11.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.10.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.9.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.11.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.8.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.10.0</td><td>7</td><td>9</td></tr>
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

#### CPU

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th></tr>
<tr><td>tensorflow-2.16.1</td><td>3.9-3.12</td><td>Clang from Xcode 13.6</td><td>Bazel 6.5.0</td></tr>
<tr><td>tensorflow-2.15.0</td><td>3.9-3.11</td><td>Clang from xcode 10.15</td><td>Bazel 6.1.0</td></tr>
<tr><td>tensorflow-2.14.0</td><td>3.9-3.11</td><td>Clang from xcode 10.15</td><td>Bazel 6.1.0</td></tr>
<tr><td>tensorflow-2.13.0</td><td>3.8-3.11</td><td>Clang from xcode 10.15</td><td>Bazel 5.3.0</td></tr>
<tr><td>tensorflow-2.12.0</td><td>3.8-3.11</td><td>Clang from xcode 10.15</td><td>Bazel 5.3.0</td></tr>
<tr><td>tensorflow-2.11.0</td><td>3.7-3.10</td><td>Clang from xcode 10.14</td><td>Bazel 5.3.0</td></tr>
<tr><td>tensorflow-2.10.0</td><td>3.7-3.10</td><td>Clang from xcode 10.14</td><td>Bazel 5.1.1</td></tr>
<tr><td>tensorflow-2.9.0</td><td>3.7-3.10</td><td>Clang from xcode 10.14</td><td>Bazel 5.0.0</td></tr>
<tr><td>tensorflow-2.8.0</td><td>3.7-3.10</td><td>Clang from xcode 10.14</td><td>Bazel 4.2.1</td></tr>
<tr><td>tensorflow-2.7.0</td><td>3.7-3.9</td><td>Clang from xcode 10.11</td><td>Bazel 3.7.2</td></tr>
<tr><td>tensorflow-2.6.0</td><td>3.6-3.9</td><td>Clang from xcode 10.11</td><td>Bazel 3.7.2</td></tr>
<tr><td>tensorflow-2.5.0</td><td>3.6-3.9</td><td>Clang from xcode 10.11</td><td>Bazel 3.7.2</td></tr>
<tr><td>tensorflow-2.4.0</td><td>3.6-3.8</td><td>Clang from xcode 10.3</td><td>Bazel 3.1.0</td></tr>
<tr><td>tensorflow-2.3.0</td><td>3.5-3.8</td><td>Clang from xcode 10.1</td><td>Bazel 3.1.0</td></tr>
<tr><td>tensorflow-2.2.0</td><td>3.5-3.8</td><td>Clang from xcode 10.1</td><td>Bazel 2.0.0</td></tr>
<tr><td>tensorflow-2.1.0</td><td>2.7, 3.5-3.7</td><td>Clang from xcode 10.1</td><td>Bazel 0.27.1</td></tr>
<tr><td>tensorflow-2.0.0</td><td>2.7, 3.5-3.7</td><td>Clang from xcode 10.1</td><td>Bazel 0.27.1</td></tr>
<tr><td>tensorflow-2.0.0</td><td>2.7, 3.3-3.7</td><td>Clang from xcode 10.1</td><td>Bazel 0.26.1</td></tr>
<tr><td>tensorflow-1.15.0</td><td>2.7, 3.3-3.7</td><td>Clang from xcode 10.1</td><td>Bazel 0.26.1</td></tr>
<tr><td>tensorflow-1.14.0</td><td>2.7, 3.3-3.7</td><td>Clang from xcode</td><td>Bazel 0.24.1</td></tr>
<tr><td>tensorflow-1.13.1</td><td>2.7, 3.3-3.7</td><td>Clang from xcode</td><td>Bazel 0.19.2</td></tr>
<tr><td>tensorflow-1.12.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.11.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.10.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.9.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.11.0</td></tr>
<tr><td>tensorflow-1.8.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.10.1</td></tr>
<tr><td>tensorflow-1.7.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.10.1</td></tr>
<tr><td>tensorflow-1.6.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.8.1</td></tr>
<tr><td>tensorflow-1.5.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.8.1</td></tr>
<tr><td>tensorflow-1.4.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.5.4</td></tr>
<tr><td>tensorflow-1.3.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.2.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.1.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td></tr>
<tr><td>tensorflow-1.0.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td></tr>
</table>

#### GPU

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow_gpu-1.1.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.0.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
</table>
