page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.list_physical_devices

Return a list of physical devices visible to the runtime.

### Aliases:

* `tf.compat.v1.config.experimental.list_physical_devices`
* `tf.compat.v2.config.experimental.list_physical_devices`
* `tf.config.experimental.list_physical_devices`

``` python
tf.config.experimental.list_physical_devices(device_type=None)
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

Physical devices are hardware devices locally present on the current machine.
By default all discovered CPU and GPU devices are considered visible. The
`list_physical_devices` allows querying the hardware prior to runtime
initialization.

The following example ensures the machine can see at least 1 GPU.

```python
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "No GPUs found."
```

#### Args:


* <b>`device_type`</b>: (optional) Device type to filter by such as "CPU" or "GPU"


#### Returns:

List of PhysicalDevice objects
