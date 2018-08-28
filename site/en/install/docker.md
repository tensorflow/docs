# Docker

Docker uses a *container* to create a virtual environment that isolates a
TensorFlow installation from the rest of the system. TensorFlow programs are run
*within* this virtual environment that can share resources with its host machine
(access directories, use the GPU, connect to the Internet, etc.).

We provide a number of
[tested Docker images](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
for each release. Docker is the easiest way to run TensorFlow on a GPU since the
*host* machine only requires the
[NVIDIA® driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external},
the *NVIDIA® CUDA® Toolkit* doesn't have to be installed.


## Install

1. [Install Docker](https://docs.docker.com/install/){:.external} on
   your local *host* machine.
2. For GPU support on Linux, [install nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external}.

Note: To run the `docker` command without `sudo`, create the `docker` group and
add your user. For details, the
[post-installation steps for Linux](https://docs.docker.com/install/linux/linux-postinstall/){:.external}.


## CPU-only

The official TensorFlow Docker images are located in the 
[tensorflow/tensorflow](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
Docker Hub repository. To start a TensorFlow-configured container with
*CPU-only* support, use the following command form:

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it [-p <em>hostPort</em>:<em>containerPort</em>] tensorflow/tensorflow[:<em>tag</em>] [<em>command</em>]
</pre>

Docker image releases are tagged. The complete
[list of tags](https://hub.docker.com/r/tensorflow/tensorflow/tags/){:.external}
is formatted as:

<table>
  <tr><th>Tag</th><th>Description</th></tr>
  <tr><td><code>latest</code></td><td>The latest release of TensorFlow CPU binary image. Default.</td></tr>
  <tr><td><code>nightly</code></td><td>Nightly builds of the TensorFlow image. (unstable)</td></tr>
  <tr><td><code><em>version</em></code></td><td>Specify the <em>version</em> of the TensorFlow binary image, for example: <em>1.10.1</em>.</td></tr>
  <tr class="alt"><td colspan="2">Tag variant</td></tr>
  <tr><td><code><em>tag</em>-devel<code></td><td>The specified <em>tag</em> release and the source code.</td></tr>
  <tr><td><code><em>tag</em>-gpu<code></td><td>The specified <em>tag</em> release with GPU support. (See below.)</td></tr>
  <tr><td><code><em>tag</em>-py3<code></td><td>The specified <em>tag</em> release with Python 3 support.</td></tr>
  <tr><td><code><em>tag</em>-gpu-py3<code></td><td>The specified <em>tag</em> release with GPU and Python 3 support.</td></tr>
  <tr><td><code><em>tag</em>-devel-py3<code></td><td>The specified <em>tag</em> release with Python 3 support and the source code.</td></tr>
  <tr><td><code><em>tag</em>-devel-gpu-py3<code></td><td>The specified <em>tag</em> release with GPU and Python 3 support, and the source code.</td></tr>
</table>

### Examples

Verify the Docker install using the `latest` TensorFlow image. Docker downloads
the TensorFlow image the first time you launch it:

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it tensorflow/tensorflow python -c "import tensorflow as tf; print(tf.__version__)"
</pre>

Execute a `bash` shell within the TensorFlow-configured container (run `python` inside):

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it tensorflow/tensorflow bash
</pre>

Run the host script `./script.py` within the container by mounting
the current directory and changing the working directory
(`-v hostDir:containerDir -w workDir`):

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it -v $PWD:/tmp -w /tmp tensorflow/tensorflow python script.py
</pre>


Start a [Jupyter Notebook](https://jupyter.org/){:.external} server using the nightly build with Python 3 support:

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-py3
</pre>

In your host web browser, open `http://localhost:8888/`.

TODO: Start [TensorBoard](../guide/summaries_and_tensorboard):

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it -p 6006:6006 tensorflow/tensorflow
</pre>


## GPU support

Docker is the easiest way to run TensorFlow on a GPU since the *host* machine
only requires the [NVIDIA® driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external};
the *NVIDIA® CUDA® Toolkit* doesn't have to be installed.

[Install nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external} to
launch a Docker container with NVIDIA® GPU support. `nvidia-docker` is only
available for Linux, see the
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

### Examples

Download and run a GPU-enabled TensorFlow image:

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
nvidia-docker run -it tensorflow/tensorflow:latest-gpu \
    python -c "import tensorflow as tf; print(tf.contrib.eager.num_gpus())"
</pre>

Use the latest TensorFlow GPU image to execute a `bash` shell in the container
(run `python` inside):

<pre class="devsite-terminal devsite-click-to-copy">
nvidia-docker run -it tensorflow/tensorflow:latest-gpu bash
</pre>
