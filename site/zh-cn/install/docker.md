# Docker

[Docker](https://docs.docker.com/install/){:.external} 使用 *容器* 创建虚拟环境，改环境将 TensorFlow 的安装和系统其他部分隔离开来。TensorFlow 程序运行于虚拟环境 *之内* 并和宿主机分享资源（文件的访问、GPU的使用、Internet连接等）。
[TensorFlow Docker 镜像](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
已经为每个发行版做了相关测试。

Docker 是在Linux上启用 TensorFlow [GPU 支持](./gpu.md) 最简单的方式，仅需在主机上安装
[NVIDIA® GPU 驱动](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}
 (无需安装 *NVIDIA® CUDA® Toolkit* ).


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

| 其他变量标签      | 描述                                                              |
| ---               | ---                                                               |
| *`tag`*`-gpu`     | 指定 GPU 支持的 *tag* 发行版本。([See below](#gpu_support))       |
| *`tag`*`-py3`     | 指定支持 Python 3 的 *tag* 发行版本。                             |
| *`tag`*`-jupyter` | 指定包含 Jupyter 的*tag* 发行版本。（包含 TensorFlow 教程笔记本） |

您可以同时使用多个变量标签。如下命令将下载TensorFlow发行版本的镜像：

<pre class="devsite-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow                     # 最新稳定发行版</code>
<code class="devsite-terminal">docker pull tensorflow/tensorflow:devel-gpu           # 每日开发版，包含GPU 致辞</code>
<code class="devsite-terminal">docker pull tensorflow/tensorflow:latest-gpu-jupyter  # 最新支持 GPU 并包含 Jupyter 的发行版l</code>
</pre>


## 启动 TensorFlow Docker 容器

使用如下命令，将启动预配置 TensorFlow容器：

<pre class="devsite-terminal devsite-click-to-copy">
docker run [-it] [--rm] [-p <em>hostPort</em>:<em>containerPort</em>] tensorflow/tensorflow[:<em>tag</em>] [<em>command</em>]
</pre>

更多详情，请查阅 [docker run 命令参考](https://docs.docker.com/engine/reference/run/){:.external}.

### 示例：使用 仅CPU 镜像

让我们来验证使用 `latest` 标签镜像的安装吧。Docker将在第一次运行时下载新的 TensorFlow 镜像：

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it --rm tensorflow/tensorflow \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
</pre>

成功：TensorFlow 已经安装完成。阅读 [教程](../tutorials) 开始使用。

让我们展示一些 TensorFlow Docker 方法。在配置了 TensorFlow 的容器中启动 `bash` shell 会话：

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it tensorflow/tensorflow bash
</pre>

在容器中，您可以启动 `python` 会话并导入 TensorFlow。

如需在容器中运行本机开发的 TensorFlow 程序，可以通过挂载本机目录并变更容器的工作目录
(`-v hostDir:containerDir -w workDir`):

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./script.py
</pre>

在容器中创建并暴露给主机的文件会存在权限问题。通常的做法是在主机上编辑文件。

使用支持 Python 3 的 TensorFlow 每日版构建，启动[Jupyter 笔记本](https://jupyter.org/){:.external} ：

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-py3-jupyter
</pre>

根据如下提示，在主机浏览器中打开该URL：
`http://127.0.0.1:8888/?token=...`


## GPU 支持

Docker 是在主机的GPU上运行 TensorFlow 最简易的方式，仅在主机上需要 [NVIDIA® 驱动](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}
（无需 *NVIDIA® CUDA® Toolkit* ）。

安装 [nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external} 并加载支持 NVIDIA® GPU 的容器。
`nvidia-docker` 仅可以在Linux上使用，查阅
[支持平台FAQ](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#platform-support){:.external}
获取更多信息。

检查 GPU 的状态是否可用：

<pre class="devsite-terminal devsite-click-to-copy">
lspci | grep -i nvidia
</pre>

验证 `nvidia-docker` 的安装：

<pre class="devsite-terminal devsite-click-to-copy">
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
</pre>

提示： `nvidia-docker` v1版使用 `nvidia-docker` 命令别名， v2 版使用 `docker --runtime=nvidia` 命令。

### 示范：使用启用GPU支持的镜像

下载和运行启用 GPU 支持的 TensorFlow 镜像 （可能需要几分钟）：

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run --runtime=nvidia -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
</pre>

需要花费数分钟设置启用GPU支持的镜像。 如需重复运行基于GPU的脚本，可以使用 `docker exec` 命令来重复使用容器。

使用最新 TensorFlow GPU 进行并在容器中启动 `bash` shell 会话:

<pre class="devsite-terminal devsite-click-to-copy">
docker run --runtime=nvidia -it tensorflow/tensorflow:latest-gpu bash
</pre>

成功：TensorFlow 已经安装完成。阅读 [教程](../tutorials) 开始使用。