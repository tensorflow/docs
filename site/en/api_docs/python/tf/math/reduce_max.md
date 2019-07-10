page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.reduce_max

Computes the maximum of elements across dimensions of a tensor. (deprecated arguments)

### Aliases:

* `tf.compat.v1.math.reduce_max`
* `tf.compat.v1.reduce_max`
* `tf.math.reduce_max`
* `tf.reduce_max`

``` python
tf.math.reduce_max(
    input_tensor,
    axis=None,
    keepdims=None,
    name=None,
    reduction_indices=None,
    keep_dims=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(keep_dims)`. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

#### Args:


* <b>`input_tensor`</b>: The tensor to reduce. Should have real numeric type.
* <b>`axis`</b>: The dimensions to reduce. If `None` (the default), reduces all
  dimensions. Must be in the range `[-rank(input_tensor),
  rank(input_tensor))`.
* <b>`keepdims`</b>: If true, retains reduced dimensions with length 1.
* <b>`name`</b>: A name for the operation (optional).
* <b>`reduction_indices`</b>: The old (deprecated) name for axis.
* <b>`keep_dims`</b>: Deprecated alias for `keepdims`.


#### Returns:

The reduced tensor.




#### Numpy Compatibility
Equivalent to np.max

