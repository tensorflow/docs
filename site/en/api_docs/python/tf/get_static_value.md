page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_static_value

Returns the constant value of the given tensor, if efficiently calculable.

### Aliases:

* `tf.compat.v1.get_static_value`
* `tf.compat.v2.get_static_value`
* `tf.contrib.util.constant_value`
* `tf.get_static_value`

``` python
tf.get_static_value(
    tensor,
    partial=False
)
```



Defined in [`python/framework/tensor_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/tensor_util.py).

<!-- Placeholder for "Used in" -->

This function attempts to partially evaluate the given tensor, and
returns its value as a numpy ndarray if this succeeds.

Compatibility(V1): If `constant_value(tensor)` returns a non-`None` result, it
will no longer be possible to feed a different value for `tensor`. This allows
the result of this function to influence the graph that is constructed, and
permits static shape optimizations.

#### Args:


* <b>`tensor`</b>: The Tensor to be evaluated.
* <b>`partial`</b>: If True, the returned numpy array is allowed to have partially
  evaluated values. Values that can't be evaluated will be None.


#### Returns:

A numpy ndarray containing the constant value of the given `tensor`,
or None if it cannot be calculated.



#### Raises:


* <b>`TypeError`</b>: if tensor is not an ops.Tensor.