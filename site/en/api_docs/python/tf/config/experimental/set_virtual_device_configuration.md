page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.set_virtual_device_configuration

Set the virtual device configuration for a PhysicalDevice.

### Aliases:

* `tf.compat.v1.config.experimental.set_virtual_device_configuration`
* `tf.compat.v2.config.experimental.set_virtual_device_configuration`
* `tf.config.experimental.set_virtual_device_configuration`

``` python
tf.config.experimental.set_virtual_device_configuration(
    device,
    virtual_devices
)
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

A PhysicalDevice marked as visible will by default have a single LogicalDevice
allocated to it once the runtime is configured. Specifying a list of
tf.config.experimental.VirtualDeviceConfiguration objects allows multiple
devices to be configured that utilize the same PhysicalDevice.

The following example splits the CPU into 2 virtual devices:

```python
physical_devices = tf.config.experimental.list_physical_devices('CPU')
assert len(physical_devices) == 1, "No CPUs found"
# Specify 2 virtual CPUs. Note currently memory limit is not supported.
tf.config.experimental.set_virtual_device_configuration(
  physical_devices[0],
  [tf.config.experimental.VirtualDeviceConfiguration(),
   tf.config.experimental.VirtualDeviceConfiguration()])
logical_devices = tf.config.experimental.list_logical_devices('CPU')
assert len(logical_devices) == 2

try:
  tf.config.experimental.set_virtual_device_configuration(
    physical_devices[0],
    [tf.config.experimental.VirtualDeviceConfiguration(),
     tf.config.experimental.VirtualDeviceConfiguration(),
     tf.config.experimental.VirtualDeviceConfiguration(),
     tf.config.experimental.VirtualDeviceConfiguration()])
except:
  print('Cannot modify the virtual devices once they have been initialized.')
```

The following example splits the GPU into 2 virtual devices with 100 MB each:

```python
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "No GPUs found"
tf.config.experimental.set_virtual_device_configuration(
  physical_devices[0],
  [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=100),
   tf.config.experimental.VirtualDeviceConfiguration(memory_limit=100)])

try:
  tf.config.experimental.set_memory_growth(physical_devices[0], True)
except:
  print('Cannot set memory growth when virtual devices configured')

logical_devices = tf.config.experimental.list_logical_devices('GPU')
assert len(logical_devices) == len(physical_devices) + 1

try:
  tf.config.experimental.set_virtual_device_configuration(
    physical_devices[0],
    [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=10),
     tf.config.experimental.VirtualDeviceConfiguration(memory_limit=10)])
except:
  print('Cannot modify the virtual devices once they have been initialized.')
```

#### Args:


* <b>`device`</b>: (optional) Need to update
* <b>`virtual_devices`</b>: (optional) Need to update