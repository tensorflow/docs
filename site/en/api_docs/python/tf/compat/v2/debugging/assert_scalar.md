page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.debugging.assert_scalar

Asserts that the given `tensor` is a scalar.

``` python
tf.compat.v2.debugging.assert_scalar(
    tensor,
    message=None,
    name=None
)
```



Defined in [`python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/check_ops.py).

<!-- Placeholder for "Used in" -->

This function raises `ValueError` unless it can be certain that the given
`tensor` is a scalar. `ValueError` is also raised if the shape of `tensor` is
unknown.

This is always checked statically, so this method returns nothing.

#### Args:


* <b>`tensor`</b>: A `Tensor`.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>:  A name for this operation. Defaults to "assert_scalar"


#### Raises:


* <b>`ValueError`</b>: If the tensor is not scalar (rank 0), or if its shape is
  unknown.