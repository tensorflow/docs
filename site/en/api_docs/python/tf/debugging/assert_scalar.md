page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_scalar

### Aliases:

* `tf.assert_scalar`
* `tf.contrib.framework.assert_scalar`
* `tf.debugging.assert_scalar`

``` python
tf.debugging.assert_scalar(
    tensor,
    name=None,
    message=None
)
```



Defined in [`tensorflow/python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/check_ops.py).

Asserts that the given `tensor` is a scalar.

This function raises `ValueError` unless it can be certain that the given
`tensor` is a scalar. `ValueError` is also raised if the shape of `tensor` is
unknown.

#### Args:

* <b>`tensor`</b>: A `Tensor`.
* <b>`name`</b>:  A name for this operation. Defaults to "assert_scalar"
* <b>`message`</b>: A string to prefix to the default message.


#### Returns:

The input tensor (potentially converted to a `Tensor`).


#### Raises:

* <b>`ValueError`</b>: If the tensor is not scalar (rank 0), or if its shape is
    unknown.