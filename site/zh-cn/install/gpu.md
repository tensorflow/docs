# GPU 支持

注：当使用支持CUDA®的计算卡时，Ubuntu 与 Windows 系统可得到 GPU 支持。

Tensorflow GPU 支持需要各种驱动程序和库。为简化安装以及避免库冲突，我们建议使用[带有 GPU 支持的 Tensorflow Docker 镜像](./docker.md)（仅针对 Linux）。该配置仅需要 [NVIDIA® GPU 驱动](https://www.nvidia.com/drivers){:.external}。

这些安装说明适用于最新版 Tensorflow。参阅[经过测试的构建配置](./source.md#linux)，以获取与较早版本 Tensorflow 一起使用的 CUDA 和 CuDNN 版本。


## Pip 软件包

See the [pip install guide](./pip) for available packages, systems
requirements, and instructions. To `pip` install a TensorFlow package with
GPU support, choose a stable or development package:

有关可用软件包，系统，要求与说明，请参阅 [pip 安装指导](./pip)。使用 `pip` 安装具有 GPU 支持的 Tensorflow 包，可选择稳定版或者预览版：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install tensorflow  # 稳定版</code>

<code class="devsite-terminal">pip install tf-nightly  # 预览版</code>
</pre>


### 较早版本 Tensorflow

对于 1.15 版本，CPU 与 GPU 支持包含在一个单独的包中：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install --pre "tensorflow==1.15.*"</code>
</pre>

对于 1.14 或更早的版本，CPU 和 GPU 包是分开的：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install tensorflow==1.14      # CPU</code>
<code class="devsite-terminal">pip install tensorflow-gpu==1.14  # GPU</code>
</pre>


## 硬件要求

支持以下启用 GPU 的设备：

具有 3.5 或更高 CUDA® 计算能力的 NVIDIA® GPU。参阅清单[启用 CUDA 的 GPU 卡](https://developer.nvidia.com/cuda-gpus){:.external}。


## 软件要求

以下 NVIDIA® 软件必须安装到您的系统中：

* [NVIDIA® GPU 驱动](https://www.nvidia.com/drivers){: .external} —CUDA 10.1
  要求 418.x 或更高版本。
* [CUDA® 工具包](https://developer.nvidia.com/cuda-toolkit-archive){: .external}
  —TensorFlow 支持 CUDA 10.1 (TensorFlow >= 2.1.0)
* [CUPTI](http://docs.nvidia.com/cuda/cupti/){: .external} 附带 CUDA 工具包。
* [cuDNN SDK](https://developer.nvidia.com/cudnn){: .external} (>= 7.6)
* *(可选)* [TensorRT 6.0](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html){: .external} 提高某些模型推理的速度和吞吐量。


## Linux 设置

下方的 `apt` 说明是在 Ubuntu 上安装所需英伟达软件最简单的方法。但若要[从源码构建 Tensorflow](./source.md)，请手动安装上方的软件需求列表，并考虑使用 `-devel` [TensorFlow Docker 镜像](./docker.md) 作为基础。

请安装附带 CUDA® 工具包的 [CUPTI](http://docs.nvidia.com/cuda/cupti/){: .external}。将其安装目录追加到环境变量 `$LD_LIBRARY_PATH` 中：

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64</code>
</pre>

关于 CUDA 计算能力为 3.0 的 GPU 或不同版本的英伟达库，请参阅[在 Linux 上从源码构建](./source.md)指南。

### 使用 apt 安装 CUDA

此部分说明了如何在 Ubuntu 16.04 与 18.04 上安装 CUDA 10 (TensorFlow >= 1.13.0) 和 CUDA 9。这些说明可能适用于其他基于 Debian 的发行版。

警告：[安全启动](https://wiki.ubuntu.com/UEFI/SecureBoot){: .external}使英伟达驱动的安装复杂化，并超出了这些说明的范围。


#### Ubuntu 18.04 (CUDA 10.1)

<pre class="prettyprint lang-bsh">
# 添加英伟达软件包存储库
<code class="devsite-terminal">wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.1.243-1_amd64.deb</code>
<code class="devsite-terminal">sudo dpkg -i cuda-repo-ubuntu1804_10.1.243-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">sudo apt-get update</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-get update</code>

# 安装英伟达驱动
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-driver-418</code>
# 重启。使用命令 nvidia-smi 检查 GPU 是否可见。

# 安装开发和运行时库 (~4GB)
<code class="devsite-terminal">sudo apt-get install --no-install-recommends \
    cuda-10-1 \
    libcudnn7=7.6.4.38-1+cuda10.1  \
    libcudnn7-dev=7.6.4.38-1+cuda10.1
</code>

# 安装 TensorRT。需要在其上安装 libcudnn7。
<code class="devsite-terminal">sudo apt-get install -y --no-install-recommends libnvinfer6=6.0.1-1+cuda10.1 \
    libnvinfer-dev=6.0.1-1+cuda10.1 \
    libnvinfer-plugin6=6.0.1-1+cuda10.1
</code>
</pre>


#### Ubuntu 16.04 (CUDA 10.1)

<pre class="prettyprint lang-bsh">
# 添加英伟达软件包存储库
# Add HTTPS support for apt-key
<code class="devsite-terminal">sudo apt-get install gnupg-curl</code>
<code class="devsite-terminal">wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_10.1.243-1_amd64.deb</code>
<code class="devsite-terminal">sudo dpkg -i cuda-repo-ubuntu1604_10.1.243-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">sudo apt-get update</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-get update</code>

# 安装英伟达驱动
# 驱动安装出现问题则需要创建 /usr/lib/nvidia
<code class="devsite-terminal">sudo mkdir /usr/lib/nvidia</code>
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-418</code>
# 重启。使用命令 nvidia-smi 检查 GPU 是否可见。

# 安装开发和运行时库 (~4GB)
<code class="devsite-terminal">sudo apt-get install --no-install-recommends \
    cuda-10-1 \
    libcudnn7=7.6.4.38-1+cuda10.1  \
    libcudnn7-dev=7.6.4.38-1+cuda10.1
</code>

# 安装 TensorRT。需要在其上安装 libcudnn7。
<code class="devsite-terminal">sudo apt-get install -y --no-install-recommends \
    libnvinfer6=6.0.1-1+cuda10.1 \
    libnvinfer-dev=6.0.1-1+cuda10.1 \
    libnvinfer-plugin6=6.0.1-1+cuda10.1
</code>
</pre>


#### Ubuntu 16.04 (针对 TensorFlow < 1.13.0 的 CUDA 9.0)

<pre class="prettyprint lang-bsh">
# 添加英伟达软件包存储库
<code class="devsite-terminal">sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.1.85-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./cuda-repo-ubuntu1604_9.1.85-1_amd64.deb</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt update</code>

# 安装英伟达驱动
# 驱动安装出现问题则需要创建/usr/lib/nvidia
<code class="devsite-terminal">sudo mkdir /usr/lib/nvidia</code>
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-410</code>
# 重启。使用命令 nvidia-smi 检查 GPU 是否可见。

# 安装 CUDA 与工具。包含可选的 NCCL 2.x
<code class="devsite-terminal">sudo apt install cuda9.0 cuda-cublas-9-0 cuda-cufft-9-0 cuda-curand-9-0 \
    cuda-cusolver-9-0 cuda-cusparse-9-0 libcudnn7=7.2.1.38-1+cuda9.0 \
    libnccl2=2.2.13-1+cuda9.0 cuda-command-line-tools-9-0</code>

# 可选项：安装 TensorRT 运行时（需在 CUDA 安装后）
<code class="devsite-terminal">sudo apt update</code>
<code class="devsite-terminal">sudo apt install libnvinfer4=4.1.2-1+cuda9.0</code>
</pre>


## Windows 设置

请参阅上方所列出的 [硬件要求](#hardware_requirements) 与
[软件要求](#software_requirements)，并阅读
[CUDA® Windows 安装指南](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/){:.external}.

确保安装的英伟达软件包与上方所列出的版本所匹配。特别是，若没有 `cuDNN64_7.dll` 文件 Tensorflow 将不会加载。若要使用不同的版本，请参阅[在 Windows 上从源码构建](./source_windows.md)指南。

请将 CUDA，CUPTI，与 cuDNN 的安装目录添加到 `%PATH%` 环境变量中。例如，如果 CUDA 工具包安装到 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1` 且 cuDNN 安装到 `C:\tools\cuda` 中，更新您的 `%PATH%` 以适配：

<pre class="devsite-click-to-copy">
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\bin;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\extras\CUPTI\libx64;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\include;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\tools\cuda\bin;%PATH%</code>
</pre>
