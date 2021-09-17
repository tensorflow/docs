# GPU device plugins

Note: This page is for non-NVIDIA® GPU devices. For NVIDIA® GPU support, click
[here](./gpu.md).

TensorFlow's
<a href="https://github.com/tensorflow/community/blob/master/rfcs/20200624-pluggable-device-for-tensorflow.md" class="external">pluggable
device</a> architecture adds new device support as separate plug-in packages
that are installed alongside the official TensorFlow package.

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

*   [Getting started guide](https://developer.apple.com/metal/tensorflow-plugin/){:.external}.
*   For questions and feedback, please visit the
    [Apple Developer Forum](https://developer.apple.com/forums/tags/tensorflow-metal){:.external}.
