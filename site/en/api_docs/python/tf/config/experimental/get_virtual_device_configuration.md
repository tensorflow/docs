page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.get_virtual_device_configuration


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L457-L489">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get the virtual device configuration for a PhysicalDevice.

### Aliases:

* `tf.compat.v1.config.experimental.get_virtual_device_configuration`
* `tf.compat.v2.config.experimental.get_virtual_device_configuration`


``` python
tf.config.experimental.get_virtual_device_configuration(device)
```



<!-- Placeholder for "Used in" -->

Returns the list of VirtualDeviceConfiguration objects previously configured
by a call to <a href="../../../tf/config/experimental/set_virtual_device_configuration"><code>tf.config.experimental.set_virtual_device_configuration()</code></a>.

#### For example:



```python
physical_devices = tf.config.experimental.list_physical_devices('CPU')
assert len(physical_devices) == 1, "No CPUs found"
configs = tf.config.experimental.get_virtual_device_configuration(
    physical_devices[0])
assert configs is None
tf.config.experimental.set_virtual_device_configuration(
    physical_devices[0],
    [tf.config.experimental.VirtualDeviceConfiguration(),
     tf.config.experimental.VirtualDeviceConfiguration()])
configs = tf.config.experimental.get_virtual_device_configuration(
    physical_devices[0])
assert len(configs) == 2
```

#### Args:


* <b>`device`</b>: PhysicalDevice to query


#### Returns:

List of <a href="../../../tf/config/experimental/VirtualDeviceConfiguration"><code>tf.config.experimental.VirtualDeviceConfiguration</code></a> objects or
`None` if no virtual device configuration has been set for this physical
device.
