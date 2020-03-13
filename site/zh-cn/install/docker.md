# Docker

[Docker](https://docs.docker.com/install/){:.external} 使用 *容器* 创建虚拟环境，改环境将 TensorFlow 的安装和系统其他部分隔离开来。TensorFlow 程序运行于虚拟环境 *之内* 并和宿主机分享资源（文件的访问、GPU的使用、Internet连接等）。
[TensorFlow Docker 镜像](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
已经为每个发行版做了相关测试。

Docker 是在Linux上启用 TensorFlow [GPU 支持](./gpu.md) 最简单的方式，仅需。on Linux since only the
[NVIDIA® GPU driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}
is required on the *host* machine (无需安装 *NVIDIA® CUDA® Toolkit* ).


## TensorFlow Docker 环境需求

1. 在你的宿主机上[安装 Docker ](https://docs.docker.com/install/){:.external} 。
2. 在Linux上开启支持, [安装 nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external}.

注: 如需不通过 `sudo` 运行命令 `docker` , 请创建 `docker` 用户组并将您的用户添加进改组。详情请查看：
[Linux下安装后续步骤](https://docs.docker.com/install/linux/linux-postinstall/){:.external}.


## 下载 TensorFlow Docker 镜像

官方 TensorFlow Docker 镜像位于 
[tensorflow/tensorflow](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
Docker Hub 仓库. 镜像发行版本的 [标签](https://hub.docker.com/r/tensorflow/tensorflow/tags/){:.external}
格式如下:

| 标记        | 描述                                                                   |
| ---         | ---                                                                    |
| `latest`    | 最新 TensorFlow CPU 二进制发行版镜像。默认。                           |
| `nightly`   | TensorFlow 每日版的镜像。（不稳定）                                    |
| *`version`* | 指定版本的 TensorFlow 二进制镜像，例如：  *1.14.0*                     |
| `devel`     | TensorFlow `master` 分支开发环境的每日版。包含了 TensorFlow 源码。     |

每个基础 *tag* 含有多个新增或变更的功能：

| 其他标签          | 描述                                                                       |
| ---               | ---                                                                               |
| *`tag`*`-gpu`     | The specified *tag* release with GPU support. ([See below](#gpu_support))         |
| *`tag`*`-py3`     | The specified *tag* release with Python 3 support.                                |
| *`tag`*`-jupyter` | The specified *tag* release with Jupyter (includes TensorFlow tutorial notebooks) |

You can use multiple variants at once. For example, the following downloads
TensorFlow release images to your machine:

<pre class="devsite-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow                     # 最新稳定发行版</code>
<code class="devsite-terminal">docker pull tensorflow/tensorflow:devel-gpu           # 每日开发版，包含GPU 致辞</code>
<code class="devsite-terminal">docker pull tensorflow/tensorflow:latest-gpu-jupyter  # latest release w/ GPU support and Jupyter</code>
</pre>


## Start a TensorFlow Docker container

To start a TensorFlow-configured container, use the following command form:

<pre class="devsite-terminal devsite-click-to-copy">
docker run [-it] [--rm] [-p <em>hostPort</em>:<em>containerPort</em>] tensorflow/tensorflow[:<em>tag</em>] [<em>command</em>]
</pre>

For details, see the [docker run reference](https://docs.docker.com/engine/reference/run/){:.external}.

### Examples using CPU-only images

Let's verify the TensorFlow installation using the `latest` tagged image. Docker
downloads a new TensorFlow image the first time it is run:

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it --rm tensorflow/tensorflow \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
</pre>

Success: TensorFlow is now installed. Read the [tutorials](../tutorials) to get started.

Let's demonstrate some more TensorFlow Docker recipes. Start a `bash` shell
session within a TensorFlow-configured container:

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it tensorflow/tensorflow bash
</pre>

Within the container, you can start a `python` session and import TensorFlow.

To run a TensorFlow program developed on the *host* machine within a container,
mount the host directory and change the container's working directory
(`-v hostDir:containerDir -w workDir`):

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./script.py
</pre>

Permission issues can arise when files created within a container are exposed to
the host. It's usually best to edit files on the host system.

Start a [Jupyter Notebook](https://jupyter.org/){:.external} server using
TensorFlow's nightly build with Python 3 support:

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-py3-jupyter
</pre>

Follow the instructions and open the URL in your host web browser:
`http://127.0.0.1:8888/?token=...`


## GPU support

Docker is the easiest way to run TensorFlow on a GPU since the *host* machine
only requires the [NVIDIA® driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}
(the *NVIDIA® CUDA® Toolkit* is not required).

Install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external} to
launch a Docker container with NVIDIA® GPU support. `nvidia-docker` is only
available for Linux, see their
[platform support FAQ](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#platform-support){:.external}
for details.

Check if a GPU is available:

<pre class="devsite-terminal devsite-click-to-copy">
lspci | grep -i nvidia
</pre>

Verify your `nvidia-docker` installation:

<pre class="devsite-terminal devsite-click-to-copy">
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
</pre>

Note: `nvidia-docker` v1 uses the `nvidia-docker` alias, where v2 uses `docker --runtime=nvidia`.

### Examples using GPU-enabled images

Download and run a GPU-enabled TensorFlow image (may take a few minutes):

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run --runtime=nvidia -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
</pre>

It can take a while to set up the GPU-enabled image. If repeatably running
GPU-based scripts, you can use `docker exec` to reuse a container.

Use the latest TensorFlow GPU image to start a `bash` shell session in the container:

<pre class="devsite-terminal devsite-click-to-copy">
docker run --runtime=nvidia -it tensorflow/tensorflow:latest-gpu bash
</pre>

Success: TensorFlow is now installed. Read the [tutorials](../tutorials) to get started.
