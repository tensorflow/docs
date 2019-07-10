page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.dimension_value

Compatibility utility required to allow for both V1 and V2 behavior in TF.

### Aliases:

* `tf.compat.dimension_value`
* `tf.compat.v1.compat.dimension_value`
* `tf.compat.v1.dimension_value`
* `tf.compat.v2.compat.dimension_value`
* `tf.dimension_value`

``` python
tf.compat.dimension_value(dimension)
```



Defined in [`python/framework/tensor_shape.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/tensor_shape.py).

<!-- Placeholder for "Used in" -->

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
