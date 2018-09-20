# Docker

[Docker](https://docs.docker.com/install/){:.external} uses *containers* to
create virtual environments that isolate a TensorFlow installation from the rest
of the system. TensorFlow programs are run *within* this virtual environment that
can share resources with its host machine (access directories, use the GPU,
connect to the Internet, etc.). The
[TensorFlow Docker images](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
are tested for each release.

Docker is the easiest way to enable TensorFlow [GPU support](./gpu.md) on Linux since only the
[NVIDIA® GPU driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}
is required on the *host* machine (the *NVIDIA® CUDA® Toolkit* does not need to
be installed).


## TensorFlow Docker requirements

1. [Install Docker](https://docs.docker.com/install/){:.external} on
   your local *host* machine.
2. For GPU support on Linux, [install nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external}.

Note: To run the `docker` command without `sudo`, create the `docker` group and
add your user. For details, the
[post-installation steps for Linux](https://docs.docker.com/install/linux/linux-postinstall/){:.external}.


## Download a TensorFlow Docker image

The official TensorFlow Docker images are located in the 
[tensorflow/tensorflow](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
Docker Hub repository. Image releases [are tagged](https://hub.docker.com/r/tensorflow/tensorflow/tags/){:.external}
using the following format:

<table>
  <tr><th>Tag</th><th>Description</th></tr>
  <tr><td><code>latest</code></td><td>The latest release of TensorFlow CPU binary image. Default.</td></tr>
  <tr><td><code>nightly</code></td><td>Nightly builds of the TensorFlow image. (unstable)</td></tr>
  <tr><td><code><em>version</em></code></td><td>Specify the <em>version</em> of the TensorFlow binary image, for example: <em>1.11</em></td></tr>
  <tr class="alt"><td colspan="2">Tag variant</td></tr>
  <tr><td><code><em>tag</em>-devel<code></td><td>The specified <em>tag</em> release and the source code.</td></tr>
  <tr><td><code><em>tag</em>-gpu<code></td><td>The specified <em>tag</em> release with GPU support. (<a href="#gpu_support">See below</a>)</td></tr>
  <tr><td><code><em>tag</em>-py3<code></td><td>The specified <em>tag</em> release with Python 3 support.</td></tr>
  <tr><td><code><em>tag</em>-gpu-py3<code></td><td>The specified <em>tag</em> release with GPU and Python 3 support.</td></tr>
  <tr><td><code><em>tag</em>-devel-py3<code></td><td>The specified <em>tag</em> release with Python 3 support and the source code.</td></tr>
  <tr><td><code><em>tag</em>-devel-gpu<code></td><td>The specified <em>tag</em> release with GPU support and the source code.</td></tr>
  <tr><td><code><em>tag</em>-devel-gpu-py3<code></td><td>The specified <em>tag</em> release with GPU and Python 3 support, and the source code.</td></tr>
</table>

For example, the following downloads TensorFlow release images to your machine:

<pre class="devsite-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow                    # latest stable release</code>
<code class="devsite-terminal">docker pull tensorflow/tensorflow:nightly-devel-gpu  # nightly dev release w/ GPU support</code>
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
docker run --rm tensorflow/tensorflow python -c "import tensorflow as tf; print(tf.__version__)"
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
docker run --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./script.py
</pre>

Permission issues can arise when files created within a container are exposed to
the host. It's usually best to edit files on the host system.

Start a [Jupyter Notebook](https://jupyter.org/){:.external} server using
TensorFlow's nightly build with Python 3 support:

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-py3
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
docker run --runtime=nvidia --rm tensorflow/tensorflow:latest-gpu \
    python -c "import tensorflow as tf; print(tf.contrib.eager.num_gpus())"
</pre>

It can take a while to set up the GPU-enabled image. If repeatably running
GPU-based scripts, you can use `docker exec` to reuse a container.

Use the latest TensorFlow GPU image to start a `bash` shell session in the container:

<pre class="devsite-terminal devsite-click-to-copy">
docker run --runtime=nvidia -it tensorflow/tensorflow:latest-gpu bash
</pre>

Success: TensorFlow is now installed. Read the [tutorials](../tutorials) to get started.
