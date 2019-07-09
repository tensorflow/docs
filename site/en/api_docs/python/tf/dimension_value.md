page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dimension_value

``` python
tf.dimension_value(dimension)
```



Defined in [`tensorflow/python/framework/tensor_shape.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/framework/tensor_shape.py).

Compatibility utility required to allow for both V1 and V2 behavior in TF.

Until the release of TF 2.0, we need the legacy behavior of `TensorShape` to
coexist with the new behavior. This utility is a bridge between the two.

When accessing the value of a TensorShape dimension,
use this utility, like this:

```
# If you had this in your V1 code:
value = tensor_shape[i].value

# Use `dimension_value` as direct replacement compatible with both V1 & V2:
value = dimension_value(tensor_shape[i])

# This would be the V2 equivalent:
value = tensor_shape[i]  # Warning: this will return the dim value in V2!
```

#### Arguments:

* <b>`dimension`</b>: Either a `Dimension` instance, an integer, or None.


#### Returns:

A plain value, i.e. an integer or None.