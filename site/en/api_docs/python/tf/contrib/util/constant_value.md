page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.util.constant_value

``` python
tf.contrib.util.constant_value(
    tensor,
    partial=False
)
```



Defined in [`tensorflow/python/framework/tensor_util.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/framework/tensor_util.py).

Returns the constant value of the given tensor, if efficiently calculable.

This function attempts to partially evaluate the given tensor, and
returns its value as a numpy ndarray if this succeeds.

TODO(mrry): Consider whether this function should use a registration
mechanism like gradients and ShapeFunctions, so that it is easily
extensible.

NOTE: If `constant_value(tensor)` returns a non-`None` result, it will no
longer be possible to feed a different value for `tensor`. This allows the
result of this function to influence the graph that is constructed, and
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