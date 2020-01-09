# 在树莓派设备上编译 tensorflow 源代码

本指南基于运行在 [Raspbian 9.0](https://www.raspberrypi.org/downloads/raspbian/){:.external} 系统的[树莓派设备](https://www.raspberrypi.org/){:.external}中编译 tensorflow 源代码。
尽管本指南可能适用于其他 Raspberry Pi 系统，但仅对此配置进行了测试和支持。

我们建议对 TensorFlow Raspbian package 进行*交叉编译 (cross-compiling)*。
交叉编译使用的平台与部署平台不同。 相较于在 Raspberry Pi 使用有限的 RAM 和相对较慢的处理器，我们更加建议在 Linux ，macOS 或 Windows 等功能更强大的主机上构建TensorFlow。

注意: 我们已经提供了适用于 Raspbian 系统的，预编译 [TensorFlow packages](./pip.md)。

## 宿主机 （host） 设置

### 安装 Docker
为了简化依赖关系管理，构建脚本使用 [Docker](https://docs.docker.com/install/){:.external} 来创建虚拟 Linux 开发环境进行编译。通过执行以下操作来验证您的 Docker 是否安装成功：
`docker run --rm hello-world`

### 下载 Tensorflow 源代码

使用 [Git](https://git-scm.com/){:.external} 去克隆 (clone)
[TensorFlow repository](https://github.com/tensorflow/tensorflow){:.external}:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow.git</code>
<code class="devsite-terminal">cd tensorflow</code>
</pre>

此 repo 默认使用 master 开发分支，你可以切换到 [release](https://github.com/tensorflow/tensorflow/releases){:.external} 分支去编译。

<pre class="devsite-terminal prettyprint lang-bsh">
git checkout <em>branch_name</em>  # r1.9, r1.10, etc.
</pre>

注意：如果您在最新的开发分支上遇到构建问题，请尝试一个已知有效的 release 分支。

## 编译源代码

交叉编译TensorFlow源代码，用ARMv7 [NEON 指令]（https://developer.arm.com/technologies/neon）{：.external}构建 Python *pip* 程序包，该程序可在 Raspberry Pi 2和3设备上运行。 构建脚本启动 Docker 容器进行编译。 在Python 3和Python 2.7之间选择目标软件包：

<div class="ds-selector-tabs">
  <section>
    <h3>Python 3</h3>
<pre class="devsite-terminal prettyprint lang-bsh">
CI_DOCKER_EXTRA_PARAMS="-e CI_BUILD_PYTHON=python3 -e CROSSTOOL_PYTHON_INCLUDE_PATH=/usr/include/python3.4" \\
    tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 \\
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
</pre>
  </section>
  <section>
    <h3>Python 2.7</h3>
<pre class="devsite-terminal prettyprint lang-bsh">
tensorflow/tools/ci_build/ci_build.sh PI \\
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
</pre>
  </section>
</div><!--/ds-selector-tabs-->

要构建一个支持所有Raspberry Pi设备的软件包，包括Pi 1和 Zero - 请传递`PI_ONE`参数，例如：

<pre class="devsite-terminal prettyprint lang-bsh">
tensorflow/tools/ci_build/ci_build.sh PI \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh PI_ONE
</pre>

构建完成（约30分钟）后，将在 host 源代码树的 output-artifacts 目录中创建一个 `.whl` 软件包文件。将 wheel 文件复制到 Raspberry Pi 并使用 `pip` 安装：

<pre class="devsite-terminal devsite-click-to-copy">
pip install tensorflow-<var>version</var>-cp34-none-linux_armv7l.whl
</pre>

现在 TensorFlow 已安装在 Raspbian 上。