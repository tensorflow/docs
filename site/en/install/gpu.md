# GPU support

Note: GPU support is available for Ubuntu and Windows with CUDA®-enabled cards.

TensorFlow GPU support requires an assortment of drivers and libraries. To
simplify installation and avoid library conflicts, we recommend using a
[TensorFlow Docker image with GPU support](./docker.md) (Linux only). This setup
only requires the [NVIDIA® GPU drivers](https://www.nvidia.com/drivers){:.external}.

These install instructions are for the latest release of TensorFlow. See the
[tested build configurations](./source.md#gpu) for CUDA® and cuDNN versions to
use with older TensorFlow releases.

## Pip package

See the [pip install guide](./pip) for available packages, systems requirements,
and instructions. The TensorFlow `pip` package includes GPU support for
CUDA®-enabled cards:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install tensorflow</code>
</pre>

This guide covers GPU support and installation steps for the latest *stable*
TensorFlow release.

### Older versions of TensorFlow

For releases 1.15 and older, CPU and GPU packages are separate:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install tensorflow==1.15      # CPU</code>
<code class="devsite-terminal">pip install tensorflow-gpu==1.15  # GPU</code>
</pre>

## Hardware requirements

The following GPU-enabled devices are supported:

*   NVIDIA® GPU card with CUDA® architectures 3.5, 5.0, 6.0, 7.0, 7.5, 8.0 and
    higher than 8.0. See the list of
    <a href="https://developer.nvidia.com/cuda-gpus" class="external">CUDA®-enabled
    GPU cards</a>.
*   For GPUs with unsupported CUDA® architectures, or to avoid JIT compilation
    from PTX, or to use different versions of the NVIDIA® libraries, see the
    [Linux build from source](./source.md) guide.
*   Packages do not contain PTX code except for the latest supported CUDA®
    architecture; therefore, TensorFlow fails to load on older GPUs when
    `CUDA_FORCE_PTX_JIT=1` is set. (See
    <a href="http://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#application-compatibility" class="external">Application
    Compatibility</a> for details.)

Note: The error message "Status: device kernel image is invalid" indicates that
the TensorFlow package does not contain PTX for your architecture. You can
enable compute capabilities by [building TensorFlow from source](./source.md).

## Software requirements

The following NVIDIA® software must be installed on your system:

*   [NVIDIA® GPU drivers](https://www.nvidia.com/drivers){:.external} —CUDA®
    11.2 requires 450.80.02 or higher.
*   [CUDA® Toolkit](https://developer.nvidia.com/cuda-toolkit-archive){:.external}
    —TensorFlow supports CUDA® 11.2 (TensorFlow >= 2.5.0)
*   [CUPTI](http://docs.nvidia.com/cuda/cupti/){:.external} ships with the CUDA®
    Toolkit.
*   [cuDNN SDK 8.1.0](https://developer.nvidia.com/cudnn){:.external}
    [cuDNN versions](https://developer.nvidia.com/rdp/cudnn-archive){:.external}).
*   *(Optional)*
    [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/archives/index.html#trt_7){:.external}
    to improve latency and throughput for inference on some models.

## Linux setup

The `apt` instructions below are the easiest way to install the required NVIDIA
software on Ubuntu. However, if [building TensorFlow from source](./source.md),
manually install the software requirements listed above, and consider using a
`-devel` [TensorFlow Docker image](./docker.md) as a base.

Install [CUPTI](http://docs.nvidia.com/cuda/cupti/){:.external} which ships with
the CUDA® Toolkit. Append its installation directory to the `$LD_LIBRARY_PATH`
environmental variable:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64</code>
</pre>

### Install CUDA with apt

This section shows how to install CUDA® 11 (TensorFlow >= 2.4.0) on Ubuntu
16.04 and 18.04. These instructions may work for other Debian-based distros.

Caution: [Secure Boot](https://wiki.ubuntu.com/UEFI/SecureBoot){:.external}
complicates installation of the NVIDIA driver and is beyond the scope of these instructions.

#### Ubuntu 18.04 (CUDA 11.2)

<pre class="prettyprint lang-bsh">
# Add NVIDIA package repositories
# Note: For the Ubuntu version other than 18.04 or CPU architecture other than x86,
# replace `ubuntu1804` and/or `x86_64` as needed in the following URL.
<code class="devsite-terminal">wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb</code>
<code class="devsite-terminal">sudo dpkg -i cuda-keyring_1.0-1_all.deb</code>
<code class="devsite-terminal">sudo apt-get update</code>

# Install development and runtime libraries (~4GB)
# libnvinfer packages are optional, needed to support TensorRT inference.
<code class="devsite-terminal">sudo apt-get install --no-install-recommends \
    cuda-11-2 \
    libcudnn8=8.1.0.77-1+cuda11.2  \
    libcudnn8-dev=8.1.0.77-1+cuda11.2 \
    libnvinfer8=8.2.4-1+cuda11.4 \
    libnvinfer-dev=8.2.4-1+cuda11.4 \
    libnvinfer-plugin8=8.2.4-1+cuda11.4 \
    libnvinfer-plugin-dev=8.2.4-1+cuda11.4
</code>

# Reboot. Check that GPUs are visible using the command: nvidia-smi
</pre>

#### Ubuntu 16.04 (CUDA 11.2)

<pre class="prettyprint lang-bsh">
# Add NVIDIA package repositories
<code class="devsite-terminal">sudo apt-get update</code>
<code class="devsite-terminal">sudo apt-get install -y apt-transport-https</code>
<code class="devsite-terminal">wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-keyring_1.0-1_all.deb</code>
<code class="devsite-terminal">sudo dpkg -i cuda-keyring_1.0-1_all.deb</code>
<code class="devsite-terminal">sudo apt-get update</code>

# Install development and runtime libraries (~4GB)
# libnvinfer packages are optional, needed to support TensorRT inference.
<code class="devsite-terminal">sudo apt-get install --no-install-recommends \
    cuda-11-2 \
    libcudnn8=8.1.0.77-1+cuda11.2  \
    libcudnn8-dev=8.1.0.77-1+cuda11.2 \
    libnvinfer8=8.0.1-1+cuda11.3 \
    libnvinfer-dev=8.0.1-1+cuda11.3 \
    libnvinfer-plugin8=8.0.1-1+cuda11.3 \
    libnvinfer-plugin-dev=8.0.1-1+cuda11.3
</code>

# Reboot. Check that GPUs are visible using the command: nvidia-smi
</pre>


## Windows setup

See the [hardware requirements](#hardware_requirements) and
[software requirements](#software_requirements) listed above. Read the
[CUDA® install guide for Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/){:.external}.

Make sure the installed NVIDIA software packages match the versions listed above. In
particular, TensorFlow will not load without the `cuDNN64_8.dll` file. To use a
different version, see the [Windows build from source](./source_windows.md) guide.

Add the CUDA®, CUPTI, and cuDNN installation directories to the `%PATH%`
environmental variable. For example, if the CUDA® Toolkit is installed to
`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0` and cuDNN to
`C:\tools\cuda`, update your `%PATH%` to match:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\bin;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\extras\CUPTI\lib64;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\include;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\tools\cuda\bin;%PATH%</code>
</pre>

## WSL2 setup

Experimental support for WSL2 on Windows 10 19044 or higher with GPU access is now available. This corresponds to the most recent update of Windows 10 (aka version 21H2/November 2021 Update). You can get the latest update from here: [Download Windows 10](https://www.microsoft.com/en-us/software-download/windows10).

For instructions, please see [NVIDIA’s setup docs](https://docs.nvidia.com/cuda/wsl-user-guide/index.html) for CUDA in WSL.



