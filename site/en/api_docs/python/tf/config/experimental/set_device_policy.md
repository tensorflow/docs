page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.set_device_policy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L215-L255">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the current thread device policy.

### Aliases:

* `tf.compat.v1.config.experimental.set_device_policy`
* `tf.compat.v2.config.experimental.set_device_policy`


``` python
tf.config.experimental.set_device_policy(device_policy)
```



<!-- Placeholder for "Used in" -->

The device policy controls how operations requiring inputs on a specific
device (e.g., on GPU:0) handle inputs on a different device (e.g. GPU:1).

When using the default, an appropriate policy will be picked automatically.
The default policy may change over time.

This function only sets the device policy for the current thread. Any
subsequently started thread will again use the default policy.

#### Args:


* <b>`device_policy`</b>: A device policy.
  Valid values:
  - None: Switch to a system default.
  - 'warn': Copies the tensors which are not on the right device and logs
      a warning.
  - 'explicit': Raises an error if the placement is not as required.
  - 'silent': Silently copies the tensors. Note that this may hide
      performance problems as there is no notification provided when
      operations are blocked on the tensor being copied between devices.
  - 'silent_for_int32': silently copies `int32` tensors, raising errors on
      the other ones.


#### Raises:


* <b>`ValueError`</b>: If an invalid `device_policy` is passed.
