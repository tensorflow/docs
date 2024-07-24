# GPU device plugins

Note: This page is for non-NVIDIA® GPU devices. For NVIDIA® GPU support, go to
the [Install TensorFlow with pip](./pip.md) guide.

TensorFlow's
[pluggable device](https://github.com/tensorflow/community/blob/master/rfcs/20200624-pluggable-device-for-tensorflow.md)
architecture adds new device support as separate plug-in packages that are
installed alongside the official TensorFlow package.

The mechanism requires no device-specific changes in the TensorFlow code. It
relies on C APIs to communicate with the TensorFlow binary in a stable manner.
Plug-in developers maintain separate code repositories and distribution packages
for their plugins and are responsible for testing their devices.

## Use device plugins

To use a particular device, like one would a native device in TensorFlow, users
only have to install the device plug-in package for that device. The following
code snippet shows how the plugin for a new demonstration device, *Awesome
Processing Unit (APU)*, is installed and used. For simplicity, this sample APU
plug-in only has one custom kernel for ReLU:

```sh
# Install the APU example plug-in package
$ pip install tensorflow-apu-0.0.1-cp36-cp36m-linux_x86_64.whl
...
Successfully installed tensorflow-apu-0.0.1
```

With the plug-in installed, test that the device is visible and run an operation
on the new APU device:

```python
import tensorflow as tf   # TensorFlow registers PluggableDevices here.
tf.config.list_physical_devices()  # APU device is visible to TensorFlow.
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'), PhysicalDevice(name='/physical_device:APU:0', device_type='APU')]

a = tf.random.normal(shape=[5], dtype=tf.float32)  # Runs on CPU.
b =  tf.nn.relu(a)         # Runs on APU.

with tf.device("/APU:0"):  # Users can also use 'with tf.device' syntax.
  c = tf.nn.relu(a)        # Runs on APU.

with tf.device("/CPU:0"):
  c = tf.nn.relu(a)        # Runs on CPU.

@tf.function  # Defining a tf.function
def run():
  d = tf.random.uniform(shape=[100], dtype=tf.float32)  # Runs on CPU.
  e = tf.nn.relu(d)        # Runs on APU.

run()  # PluggableDevices also work with tf.function and graph mode.
```

## Available devices

Metal `PluggableDevice` for macOS GPUs:

*   Works with TF 2.5 or later.
*   [Getting started guide](https://developer.apple.com/metal/tensorflow-plugin/).
*   For questions and feedback, please visit the
    [Apple Developer Forum](https://developer.apple.com/forums/tags/tensorflow-metal).

DirectML `PluggableDevice` for Windows and WSL (preview):

*   Works with `tensorflow-cpu` package, version 2.10 or later.
*   [PyPI wheel](https://pypi.org/project/tensorflow-directml-plugin/).
*   [GitHub repo](https://github.com/microsoft/tensorflow-directml-plugin).
*   For questions, feedback or to raise issues, please visit the
    [Issues page of `tensorflow-directml-plugin` on GitHub](https://github.com/microsoft/tensorflow-directml-plugin/issues).

Intel® Extension for TensorFlow `PluggableDevice` for Linux and WSL:

*   Works with TF 2.10 or later.
*   [Getting started guide](https://intel.github.io/intel-extension-for-tensorflow/latest/get_started.html)
*   [PyPI wheel](https://pypi.org/project/intel-extension-for-tensorflow/).
*   [GitHub repo](https://github.com/intel/intel-extension-for-tensorflow).
*   For questions, feedback, or to raise issues, please visit the
    [Issues page of `intel-extension-for-tensorflow` on GitHub](https://github.com/intel/intel-extension-for-tensorflow/issues).
