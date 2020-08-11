# Build from source for the Raspberry Pi

This guide builds a TensorFlow package for a
[Raspberry Pi](https://www.raspberrypi.org/){:.external} device running
[Raspbian 9.0](https://www.raspberrypi.org/downloads/raspbian/){:.external}.
While the instructions might work for other Raspberry Pi variants, it is only
tested and supported for this configuration.

We recommend *cross-compiling* the TensorFlow Raspbian package. Cross-compilation
is using a different platform to build the package than deploy to. Instead of
using the Raspberry Pi's limited RAM and comparatively slow processor, it's
easier to build TensorFlow on a more powerful host machine running Linux, macOS,
or Windows.

Note: We already provide well-tested, pre-built [TensorFlow packages](./pip.md)
for Raspbian systems.


## Setup for host

### Install Docker

To simplify dependency management, the build script uses
[Docker](https://docs.docker.com/install/){:.external} to create a virtual Linux
development environment for compilation. Verify your Docker install by executing:
`docker run --rm hello-world`

### Download the TensorFlow source code

Use [Git](https://git-scm.com/){:.external} to clone the
[TensorFlow repository](https://github.com/tensorflow/tensorflow){:.external}:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow.git</code>
<code class="devsite-terminal">cd tensorflow</code>
</pre>

The repo defaults to the `master` development branch. You can also checkout a
[release branch](https://github.com/tensorflow/tensorflow/releases){:.external}
to build:

<pre class="devsite-terminal prettyprint lang-bsh">
git checkout <em>branch_name</em>  # r1.9, r1.10, etc.
</pre>

Key Point: If you're having build problems on the latest development branch, try
a release branch that is known to work.


## Build from source

Cross-compile the TensorFlow source code to build a Python *pip* package with
ARMv7
[NEON instructions](https://developer.arm.com/technologies/neon){:.external}
that works on Raspberry Pi 2, 3 and 4 devices. The build script launches a
Docker container for compilation. You can also build ARM 64-bit binary (aarch64)
by providing "AARCH64" parameter to the 'build_raspberry_pi.sh' script. Choose
among Python 3.8, Python 3.7, Python 3.5 and Python 2.7 for the target package:

<div class="ds-selector-tabs">
  <section>
    <h3>Python 3.5</h3>
<pre class="devsite-terminal prettyprint lang-bsh">
tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 \\
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
</pre>
  </section>
  <section>
    <h3>Python 3.7</h3>
<pre class="devsite-terminal prettyprint lang-bsh">
tensorflow/tools/ci_build/ci_build.sh PI-PYTHON37 \\
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
</pre>
  </section>
  <section>
    <h3>Python 3.8 (64bit)</h3>
<pre class="devsite-terminal prettyprint lang-bsh">
tensorflow/tools/ci_build/ci_build.sh PI-PYTHON38 \\
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh AARCH64
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

To build a package that supports all Raspberry Pi devices—including the Pi 1 and
Zero—pass the `PI_ONE` argument, for example:

<pre class="devsite-terminal prettyprint lang-bsh">
tensorflow/tools/ci_build/ci_build.sh PI \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh PI_ONE
</pre>

When the build finishes (~30 minutes), a `.whl` package file is created in the
output-artifacts directory of the host's source tree. Copy the wheel file to the
Raspberry Pi and install with `pip`:

<pre class="devsite-terminal devsite-click-to-copy">
pip install tensorflow-<var>version</var>-cp35-none-linux_armv7l.whl
</pre>

Success: TensorFlow is now installed on Raspbian.
