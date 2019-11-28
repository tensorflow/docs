# GPU support

Note: GPU support is available for Ubuntu and Windows with CUDA®-enabled cards.

TensorFlow GPU support requires an assortment of drivers and libraries. To
simplify installation and avoid library conflicts, we recommend using a
[TensorFlow Docker image with GPU support](./docker.md) (Linux only). This setup
only requires the [NVIDIA® GPU drivers](https://www.nvidia.com/drivers){:.external}.

These install instructions are for the latest release of TensorFlow. See the
[tested build configurations](./source.md#linux) for CUDA and cuDNN versions to use
with older TensorFlow releases.

## Pip package

See the [pip install guide](./pip) for available packages, systems
requirements, and instructions. To `pip` install a TensorFlow package with
GPU support, choose a stable or development package:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install tensorflow-gpu  # stable</code>

<code class="devsite-terminal">pip install tf-nightly      # preview</code>
</pre>

### Older versions of TensorFlow

For the 1.15 release, CPU and GPU support are included in a single package:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install --pre "tensorflow==1.15.*"</code>
</pre>

For releases 1.14 and older, CPU and GPU packages are separate:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install tensorflow==1.14      # CPU</code>
<code class="devsite-terminal">pip install tensorflow-gpu==1.14  # GPU</code>
</pre>

## Hardware requirements

The following GPU-enabled devices are supported:

* NVIDIA® GPU card with CUDA® Compute Capability 3.5 or higher. See the list of
  [CUDA-enabled GPU cards](https://developer.nvidia.com/cuda-gpus){:.external}.


## Software requirements

The following NVIDIA® software must be installed on your system:

* [NVIDIA® GPU drivers](https://www.nvidia.com/drivers){:.external} —CUDA 10.0 requires 410.x or higher.
* [CUDA® Toolkit](https://developer.nvidia.com/cuda-toolkit-archive){:.external}
  —TensorFlow supports CUDA 10.0 (TensorFlow >= 1.13.0)
* [CUPTI](http://docs.nvidia.com/cuda/cupti/){:.external} ships with the CUDA Toolkit.
* [cuDNN SDK](https://developer.nvidia.com/cudnn){:.external} (>= 7.4.1)
* *(Optional)* [TensorRT 5.0](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html){:.external}
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

For a GPU with CUDA Compute Capability 3.0, or different versions of the
NVIDIA libraries, see the [Linux build from source](./source.md) guide.

### Install CUDA with apt

This section shows how to install CUDA 10 (TensorFlow >= 1.13.0) and CUDA 9
for Ubuntu 16.04 and 18.04. These instructions may work for other Debian-based
distros.

Caution: [Secure Boot](https://wiki.ubuntu.com/UEFI/SecureBoot){:.external}
complicates installation of the NVIDIA driver and is beyond the scope of these instructions.


#### Ubuntu 18.04 (CUDA 10)

<pre class="prettyprint lang-bsh">
# Add NVIDIA package repositories
<code class="devsite-terminal">wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb</code>
<code class="devsite-terminal">sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">sudo apt-get update</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-get update</code>

# Install NVIDIA driver
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-driver-418</code>
# Reboot. Check that GPUs are visible using the command: nvidia-smi

# Install development and runtime libraries (~4GB)
<code class="devsite-terminal">sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.6.2.24-1+cuda10.0  \
    libcudnn7-dev=7.6.2.24-1+cuda10.0
</code>

# Install TensorRT. Requires that libcudnn7 is installed above.
<code class="devsite-terminal">sudo apt-get install -y --no-install-recommends libnvinfer5=5.1.5-1+cuda10.0 \
    libnvinfer-dev=5.1.5-1+cuda10.0
</code>
</pre>


#### Ubuntu 16.04 (CUDA 10)

<pre class="prettyprint lang-bsh">
# Add NVIDIA package repositories
# Add HTTPS support for apt-key
<code class="devsite-terminal">sudo apt-get install gnupg-curl</code>
<code class="devsite-terminal">wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_10.0.130-1_amd64.deb</code>
<code class="devsite-terminal">sudo dpkg -i cuda-repo-ubuntu1604_10.0.130-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">sudo apt-get update</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-get update</code>

# Install NVIDIA driver
# Issue with driver install requires creating /usr/lib/nvidia
<code class="devsite-terminal">sudo mkdir /usr/lib/nvidia</code>
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-418</code>
# Reboot. Check that GPUs are visible using the command: nvidia-smi

# Install development and runtime libraries (~4GB)
<code class="devsite-terminal">sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.6.2.24-1+cuda10.0  \
    libcudnn7-dev=7.6.2.24-1+cuda10.0
</code>

# Install TensorRT. Requires that libcudnn7 is installed above.
<code class="devsite-terminal">sudo apt-get install -y --no-install-recommends libnvinfer5=5.1.5-1+cuda10.0 \
    libnvinfer-dev=5.1.5-1+cuda10.0
</code>
</pre>


#### Ubuntu 16.04 (CUDA 9.0 for TensorFlow < 1.13.0)

<pre class="prettyprint lang-bsh">
# Add NVIDIA package repository
<code class="devsite-terminal">sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.1.85-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./cuda-repo-ubuntu1604_9.1.85-1_amd64.deb</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt update</code>

# Install the NVIDIA driver
# Issue with driver install requires creating /usr/lib/nvidia
<code class="devsite-terminal">sudo mkdir /usr/lib/nvidia</code>
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-410</code>
# Reboot. Check that GPUs are visible using the command: nvidia-smi

# Install CUDA and tools. Include optional NCCL 2.x
<code class="devsite-terminal">sudo apt install cuda9.0 cuda-cublas-9-0 cuda-cufft-9-0 cuda-curand-9-0 \
    cuda-cusolver-9-0 cuda-cusparse-9-0 libcudnn7=7.2.1.38-1+cuda9.0 \
    libnccl2=2.2.13-1+cuda9.0 cuda-command-line-tools-9-0</code>

# Optional: Install the TensorRT runtime (must be after CUDA install)
<code class="devsite-terminal">sudo apt update</code>
<code class="devsite-terminal">sudo apt install libnvinfer4=4.1.2-1+cuda9.0</code>
</pre>


## Windows setup

See the [hardware requirements](#hardware_requirements) and
[software requirements](#software_requirements) listed above. Read the
[CUDA® install guide for Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/){:.external}.

Make sure the installed NVIDIA software packages match the versions listed above. In
particular, TensorFlow will not load without the `cuDNN64_7.dll` file. To use a
different version, see the [Windows build from source](./source_windows.md) guide.

Add the CUDA, CUPTI, and cuDNN installation directories to the `%PATH%`
environmental variable. For example, if the CUDA Toolkit is installed to
`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0` and cuDNN to
`C:\tools\cuda`, update your `%PATH%` to match:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\extras\CUPTI\libx64;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\include;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\tools\cuda\bin;%PATH%</code>
</pre>
