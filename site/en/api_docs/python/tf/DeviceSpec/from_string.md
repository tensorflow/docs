


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.DeviceSpec.from_string

### `tf.DeviceSpec.from_string`

```
tf.DeviceSpec.from_string(spec)
```


Construct a `DeviceSpec` from a string.

#### Args:

* <b>`spec`</b>: a string of the form
   /job:<name>/replica:<id>/task:<id>/device:CPU:<id>
  or
   /job:<name>/replica:<id>/task:<id>/device:GPU:<id>
  as cpu and gpu are mutually exclusive.
  All entries are optional.


#### Returns:

  A DeviceSpec.

Defined in [`tensorflow/python/framework/device.py`](https://www.tensorflow.org/code/tensorflow/python/framework/device.py).

