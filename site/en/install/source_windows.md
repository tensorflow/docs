# Build from source on Windows

Build a TensorFlow *pip* package from source and install it on Windows.

Note: We already provide well-tested, pre-built
[TensorFlow packages](./pip.html) for Windows systems.

## Setup for Windows

Install the following build tools to configure your Windows development
environment.

### Install Python and the TensorFlow package dependencies

Install a
[Python 3.6.x 64-bit release for Windows](https://www.python.org/downloads/windows/){:.external}.
Select *pip* as an optional feature and add it to your `%PATH%` environmental
variable.

Install the TensorFlow *pip* package dependencies:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal tfo-terminal-windows">pip3 install six numpy wheel</code>
<code class="devsite-terminal tfo-terminal-windows">pip3 install keras_applications==1.0.6 --no-deps</code>
<code class="devsite-terminal tfo-terminal-windows">pip3 install keras_preprocessing==1.0.5 --no-deps</code>
</pre>

The dependencies are listed in the
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/pip_package/setup.py" class="external"><code>setup.py</code></a>
file under `REQUIRED_PACKAGES`.

### Install Bazel

[Install Bazel](./source.md#install-bazel), the build tool used to compile
TensorFlow. For Bazel version, see the
[tested build configurations](#tested-build-configurations) for Windows.
Configure Bazel to
<a href="https://docs.bazel.build/versions/master/windows.html#build-c" class="external">build
C++</a>.

Add the location of the Bazel executable to your `%PATH%` environment variable.

### Install MSYS2

[Install MSYS2](https://www.msys2.org/){:.external} for the bin tools needed to
build TensorFlow. If MSYS2 is installed to `C:\msys64`, add
`C:\msys64\usr\bin` to your `%PATH%` environment variable. Then, using `cmd.exe`,
run:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
pacman -S git patch unzip
</pre>

### Install Visual C++ Build Tools 2019

Install the *Visual C++ build tools 2019*. This comes with *Visual Studio 2019*
but can be installed separately:

1.  Go to the
    [Visual Studio downloads](https://visualstudio.microsoft.com/downloads/){:.external},
2.  Select *Redistributables and Build Tools*,
3.  Download and install:
    -   *Microsoft Visual C++ 2019 Redistributable*
    -   *Microsoft Build Tools 2019*

Note: TensorFlow is tested against the *Visual Studio 2019*.

### Install GPU support (optional)

See the Windows [GPU support](./gpu.md) guide to install the drivers and
additional software required to run TensorFlow on a GPU.

### Download the TensorFlow source code

Use [Git](https://git-scm.com/){:.external} to clone the
[TensorFlow repository](https://github.com/tensorflow/tensorflow){:.external}
(`git` is installed with MSYS2):

<pre class="devsite-click-to-copy">
<code class="devsite-terminal tfo-terminal-windows">git clone https://github.com/tensorflow/tensorflow.git</code>
<code class="devsite-terminal tfo-terminal-windows">cd tensorflow</code>
</pre>

The repo defaults to the `master` development branch. You can also checkout a
[release branch](https://github.com/tensorflow/tensorflow/releases){:.external}
to build:

<pre class="devsite-terminal tfo-terminal-windows prettyprint lang-bsh">
git checkout <em>branch_name</em>  # r1.9, r1.10, etc.
</pre>

Key Point: If you're having build problems on the latest development branch, try
a release branch that is known to work.


## Configure the build

Configure your system build by running the following at the root of your
TensorFlow source tree:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
python ./configure.py
</pre>

This script prompts you for the location of TensorFlow dependencies and asks for
additional build configuration options (compiler flags, for example). The
following shows a sample run of `python ./configure.py` (your session may
differ):

<section class="expandable">
<h4 class="showalways">View sample configuration session</h4>
<pre class="devsite-terminal tfo-terminal-windows">
python ./configure.py
Starting local Bazel server and connecting to it...
................
You have bazel 0.15.0 installed.
Please specify the location of python. [Default is C:\python36\python.exe]:

Found possible Python library paths:
  C:\python36\lib\site-packages
Please input the desired Python library path to use.  Default is [C:\python36\lib\site-packages]

Do you wish to build TensorFlow with CUDA support? [y/N]: <b>Y</b>
CUDA support will be enabled for TensorFlow.

Please specify the CUDA SDK version you want to use. [Leave empty to default to CUDA 9.0]:

Please specify the location where CUDA 9.0 toolkit is installed. Refer to README.md for more details. [Default is C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0]:

Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 7.0]: <b>7.0</b>

Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. [Default is C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0]: <b>C:\tools\cuda</b>

Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size. [Default is: 3.5,7.0]: <b>3.7</b>

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is /arch:AVX]:

Would you like to override eigen strong inline for some C++ compilation to reduce the compilation time? [Y/n]:
Eigen strong inline overridden.

Configuration finished
</pre>
</section>

### Configuration options

For [GPU support](./gpu.md), specify the versions of CUDA and cuDNN. If your
system has multiple versions of CUDA or cuDNN installed, explicitly set the
version instead of relying on the default. `./configure.py` creates symbolic
links to your system's CUDA libraries—so if you update your CUDA library paths,
this configuration step must be run again before building.

Note: Starting with TensorFlow 1.6, binaries use AVX instructions which may not
run on older CPUs.


## Build the pip package

### TensorFlow 2.x

tensorflow:master repo has been updated to build 2.x by default.
[Install Bazel](https://docs.bazel.build/versions/master/install.html) and use
`bazel build ` to create the TensorFlow package.

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
bazel build //tensorflow/tools/pip_package:build_pip_package
</pre>


### TensorFlow 1.x

To build the 1.x version of TensorFlow from master, use
`bazel build --config=v1` to create a TensorFlow 1.x package.

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
bazel build --config=v1 //tensorflow/tools/pip_package:build_pip_package
</pre>

#### CPU-only

Use `bazel` to make the TensorFlow package builder with CPU-only support:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
</pre>

#### GPU support

To make the TensorFlow package builder with GPU support:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
bazel build --config=opt --config=cuda --define=no_tensorflow_py_deps=true //tensorflow/tools/pip_package:build_pip_package
</pre>

#### Bazel build options

Use this option when building to avoid issue with package creation:
[tensorflow:issue#22390](https://github.com/tensorflow/tensorflow/issues/22390)

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
--define=no_tensorflow_py_deps=true
</pre>

See the Bazel [command-line reference](https://docs.bazel.build/versions/master/command-line-reference.html)
for
[build options](https://docs.bazel.build/versions/master/command-line-reference.html#build-options).

Building TensorFlow from source can use a lot of RAM. If your system is
memory-constrained, limit Bazel's RAM usage with: `--local_ram_resources=2048`.

If building with GPU support, add `--copt=-nvcc_options=disable-warnings`
to suppress nvcc warning messages.

### Build the package

The `bazel build` command creates an executable named `build_pip_package`—this
is the program that builds the `pip` package. For example, the following builds
a `.whl` package in the `C:/tmp/tensorflow_pkg` directory:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
bazel-bin\tensorflow\tools\pip_package\build_pip_package C:/tmp/tensorflow_pkg
</pre>

Although it is possible to build both CUDA and non-CUDA configs under the
same source tree, we recommend running `bazel clean` when switching between
these two configurations in the same source tree.

### Install the package

The filename of the generated `.whl` file depends on the TensorFlow version and
your platform. Use `pip3 install` to install the package, for example:

<pre class="devsite-terminal tfo-terminal-windows prettyprint lang-bsh">
pip3 install C:/tmp/tensorflow_pkg/tensorflow-<var>version</var>-cp36-cp36m-win_amd64.whl
</pre>

Success: TensorFlow is now installed.


## Build using the MSYS shell

TensorFlow can also be built using the MSYS shell. Make the changes listed
below, then follow the previous instructions for the Windows native command line
(`cmd.exe`).

### Disable MSYS path conversion {:.hide-from-toc}

MSYS automatically converts arguments that look like Unix paths to Windows
paths, and this doesn't work with `bazel`. (The label `//path/to:bin` is
considered a Unix absolute path since it starts with a slash.)

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">export MSYS_NO_PATHCONV=1</code>
<code class="devsite-terminal">export MSYS2_ARG_CONV_EXCL="*"</code>
</pre>

### Set your PATH {:.hide-from-toc}

Add the Bazel and Python installation directories to your `$PATH` environmental
variable. If Bazel is installed to `C:\tools\bazel.exe`, and Python to
`C:\Python36\python.exe`, set your `PATH` with:

<pre class="prettyprint lang-bsh">
# Use Unix-style with ':' as separator
<code class="devsite-terminal">export PATH="/c/tools:$PATH"</code>
<code class="devsite-terminal">export PATH="/c/Python36:$PATH"</code>
</pre>

For GPU support, add the CUDA and cuDNN bin directories to your `$PATH`:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">export PATH="/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.0/bin:$PATH"</code>
<code class="devsite-terminal">export PATH="/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.0/extras/CUPTI/libx64:$PATH"</code>
<code class="devsite-terminal">export PATH="/c/tools/cuda/bin:$PATH"</code>
</pre>

<a name="tested_build_configurations"></a>
## Tested build configurations

### CPU

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th></tr>
<tr><td>tensorflow-2.5.0</td><td>3.6-3.9</td><td>MSVC 2019</td><td>Bazel 3.7.2</td></tr>
<tr><td>tensorflow-2.4.0</td><td>3.6-3.8</td><td>MSVC 2019</td><td>Bazel 3.1.0</td></tr>
<tr><td>tensorflow-2.3.0</td><td>3.5-3.8</td><td>MSVC 2019</td><td>Bazel 3.1.0</td></tr>
<tr><td>tensorflow-2.2.0</td><td>3.5-3.8</td><td>MSVC 2019</td><td>Bazel 2.0.0</td></tr>
<tr><td>tensorflow-2.1.0</td><td>3.5-3.7</td><td>MSVC 2019</td><td>Bazel 0.27.1-0.29.1</td></tr>
<tr><td>tensorflow-2.0.0</td><td>3.5-3.7</td><td>MSVC 2017</td><td>Bazel 0.26.1</td></tr>
<tr><td>tensorflow-1.15.0</td><td>3.5-3.7</td><td>MSVC 2017</td><td>Bazel 0.26.1</td></tr>
<tr><td>tensorflow-1.14.0</td><td>3.5-3.7</td><td>MSVC 2017</td><td>Bazel 0.24.1-0.25.2</td></tr>
<tr><td>tensorflow-1.13.0</td><td>3.5-3.7</td><td>MSVC 2015 update 3</td><td>Bazel 0.19.0-0.21.0</td></tr>
<tr><td>tensorflow-1.12.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.11.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.10.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.9.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.8.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.7.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.6.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.5.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.4.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.3.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.2.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.1.0</td><td>3.5</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.0.0</td><td>3.5</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
</table>

### GPU

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow_gpu-2.5.0</td><td>3.6-3.9</td><td>MSVC 2019</td><td>Bazel 3.7.2</td><td>8.1</td><td>11.2</td></tr>
<tr><td>tensorflow_gpu-2.4.0</td><td>3.6-3.8</td><td>MSVC 2019</td><td>Bazel 3.1.0</td><td>8.0</td><td>11.0</td></tr>
<tr><td>tensorflow_gpu-2.3.0</td><td>3.5-3.8</td><td>MSVC 2019</td><td>Bazel 3.1.0</td><td>7.6</td><td>10.1</td></tr>
<tr><td>tensorflow_gpu-2.2.0</td><td>3.5-3.8</td><td>MSVC 2019</td><td>Bazel 2.0.0</td><td>7.6</td><td>10.1</td></tr>
<tr><td>tensorflow_gpu-2.1.0</td><td>3.5-3.7</td><td>MSVC 2019</td><td>Bazel 0.27.1-0.29.1</td><td>7.6</td><td>10.1</td></tr>
<tr><td>tensorflow_gpu-2.0.0</td><td>3.5-3.7</td><td>MSVC 2017</td><td>Bazel 0.26.1</td><td>7.4</td><td>10</td></tr>
<tr><td>tensorflow_gpu-1.15.0</td><td>3.5-3.7</td><td>MSVC 2017</td><td>Bazel 0.26.1</td><td>7.4</td><td>10</td></tr>
<tr><td>tensorflow_gpu-1.14.0</td><td>3.5-3.7</td><td>MSVC 2017</td><td>Bazel 0.24.1-0.25.2</td><td>7.4</td><td>10</td></tr>
<tr><td>tensorflow_gpu-1.13.0</td><td>3.5-3.7</td><td>MSVC 2015 update 3</td><td>Bazel 0.19.0-0.21.0</td><td>7.4</td><td>10</td></tr>
<tr><td>tensorflow_gpu-1.12.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Bazel 0.15.0</td><td>7.2</td><td>9.0</td></tr>
<tr><td>tensorflow_gpu-1.11.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.10.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.9.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.8.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.7.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.6.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.5.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.4.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>6</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.3.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>6</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.2.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.1.0</td><td>3.5</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.0.0</td><td>3.5</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>5.1</td><td>8</td></tr>
</table>
