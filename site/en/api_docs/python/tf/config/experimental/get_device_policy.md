page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.get_device_policy

Gets the current device policy.

### Aliases:

* `tf.compat.v1.config.experimental.get_device_policy`
* `tf.compat.v2.config.experimental.get_device_policy`
* `tf.config.experimental.get_device_policy`

``` python
tf.config.experimental.get_device_policy()
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

The device policy controls how operations requiring inputs on a specific
device (e.g., on GPU:0) handle inputs on a different device (e.g. GPU:1).

This function only gets the device policy for the current thread. Any
subsequently started thread will again use the default policy.

#### Returns:

Current thread device policy
