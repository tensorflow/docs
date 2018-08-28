# Anaconda

Note: `conda` is a community supported package and not officially
maintained by the TensorFlow team. Use this package at your own risk since it is
not tested on new TensorFlow releases.

Anaconda provides the `conda` utility to create a virtual environment. However,
within Anaconda, we recommend installing TensorFlow using the `pip install`
command and *not* with the `conda install` command.

To install TensorFlow in an Anaconda environment:

1. Follow the [Anaconda instructions](https://www.continuum.io/downloads) to
   download and install Anaconda.
2. Create a `conda` environment named `tensorflow` to run a Python:
   `$ conda create -n tensorflow pip python=2.7  # or python=3.3, etc.`
3. Activate the `conda` environment:
   `$ source activate tensorflow`. The prompt will change.
4. Install TensorFlow inside the conda environment:
   `(tensorflow)$ pip install --ignore-installed --upgrade <var>tfBinaryURL</var>`
   Where <var>tfBinaryURL</var> is the URL location of the [pip package](./pip.md).
   For example, the following command installs the CPU-only version of
   TensorFlow for Python 3.4:
   `(tensorflow)$ pip install --ignore-installed --upgrade \
     https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.10.1-cp34-cp34m-linux_x86_64.whl`
