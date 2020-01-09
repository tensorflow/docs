page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.get_virtual_device_configuration


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/experimental/get_virtual_device_configuration">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L457-L489">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get the virtual device configuration for a PhysicalDevice.

### Aliases:

* <a href="/api_docs/python/tf/config/experimental/get_virtual_device_configuration"><code>tf.compat.v1.config.experimental.get_virtual_device_configuration</code></a>
* <a href="/api_docs/python/tf/config/experimental/get_virtual_device_configuration"><code>tf.compat.v2.config.experimental.get_virtual_device_configuration</code></a>


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
