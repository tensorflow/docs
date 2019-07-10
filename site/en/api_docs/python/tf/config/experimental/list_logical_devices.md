page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.list_logical_devices

Return a list of logical devices created by runtime.

### Aliases:

* `tf.compat.v1.config.experimental.list_logical_devices`
* `tf.compat.v2.config.experimental.list_logical_devices`
* `tf.config.experimental.list_logical_devices`

``` python
tf.config.experimental.list_logical_devices(device_type=None)
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

Logical devices may correspond to physical devices or remote devices in the
cluster. Operations and tensors may be placed on these devices by using the
`name` of the LogicalDevice.

#### For example:



```python
logical_devices = tf.config.experimental.list_logical_devices('GPU')
# Allocate on GPU:0
with tf.device(logical_devices[0].name):
  one = tf.constant(1)
# Allocate on GPU:1
with tf.device(logical_devices[1].name):
  two = tf.constant(2)
```

#### Args:


* <b>`device_type`</b>: (optional) Device type to filter by such as "CPU" or "GPU"


#### Returns:

List of LogicalDevice objects
