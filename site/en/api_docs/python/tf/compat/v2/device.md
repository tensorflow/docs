page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.device

Specifies the device for ops created/executed in this context.

``` python
tf.compat.v2.device(device_name)
```



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->

`device_name` can be fully specified, as in "/job:worker/task:1/device:cpu:0",
or partially specified, containing only a subset of the "/"-separated
fields. Any fields which are specified override device annotations from outer
scopes. For example:

```python
with tf.device('/job:foo'):
  # ops created here have devices with /job:foo
  with tf.device('/job:bar/task:0/device:gpu:2'):
    # ops created here have the fully specified device above
  with tf.device('/device:gpu:1'):
    # ops created here have the device '/job:foo/device:gpu:1'
```

#### Args:


* <b>`device_name`</b>: The device name to use in the context.


#### Returns:

A context manager that specifies the default device to use for newly
created ops.



#### Raises:


* <b>`RuntimeError`</b>: If a function is passed in.