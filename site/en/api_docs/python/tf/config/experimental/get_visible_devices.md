page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.get_visible_devices


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L350-L376">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get the list of visible physical devices.

### Aliases:

* `tf.compat.v1.config.experimental.get_visible_devices`
* `tf.compat.v2.config.experimental.get_visible_devices`


``` python
tf.config.experimental.get_visible_devices(device_type=None)
```



<!-- Placeholder for "Used in" -->

Returns a list of PhysicalDevice objects that are current marked as visible to
the runtime. Any visible devices will have LogicalDevices assigned to them
once the runtime is initialized.

The following example verifies all visible GPUs have been disabled:

```python
physical_devices = config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
# Disable all GPUS
tf.config.experimental.set_visible_devices([], 'GPU')
visible_devices = tf.config.experimental.get_visible_devices()
for device in visible_devices:
  assert device.device_type != 'GPU'
```

#### Args:


* <b>`device_type`</b>: (optional) Device types to limit query to.


#### Returns:

List of PhysicalDevice objects
