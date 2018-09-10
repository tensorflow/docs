# Anaconda

<aside class="caution"><code>conda</code> provides a community supported package
that is <em>not</em> an official release from the TensorFlow team.</aside>

Within an [Anaconda environment](https://www.anaconda.com/download){:.external},
we recommend installing the TensorFlow [pip package](./pip.md) (and *not* using `conda install`).

## Set up a virtual environment

Create a `conda` virtual environment to run Python:

<pre class="devsite-terminal prettyprint lang-bsh">
conda create -n <var>venv</var> pip python=2.7  # or python=3.3, etc.
</pre>

Activate the virtual environment:

<pre class="devsite-terminal devsite-click-to-copy">
source activate <var>venv</var>
</pre>

## Install the pip package

Within the virtual environment, install the TensorFlow *pip* package using its
complete URL:

<pre class="devsite-terminal tfo-terminal-venv">
pip install --ignore-installed --upgrade <var>packageURL</var>
</pre>

See the [pip package location](./pip.md#package-location) section for a list of
available packages and their URLs.

Success: TensorFlow is now installed. Read the [tutorials](../tutorials) to get started.
