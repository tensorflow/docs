page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.reduce_any

``` python
tf.reduce_any(
    input_tensor,
    axis=None,
    keepdims=None,
    name=None,
    reduction_indices=None,
    keep_dims=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Reduction](../../../api_guides/python/math_ops#Reduction)

Computes the "logical or" of elements across dimensions of a tensor. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` has no entries, all dimensions are reduced, and a
tensor with a single element is returned.

For example:

```python
x = tf.constant([[True,  True], [False, False]])
tf.reduce_any(x)  # True
tf.reduce_any(x, 0)  # [True, True]
tf.reduce_any(x, 1)  # [True, False]
```

#### Args:

* <b>`input_tensor`</b>: The boolean tensor to reduce.
* <b>`axis`</b>: The dimensions to reduce. If `None` (the default),
    reduces all dimensions. Must be in the range
    `[-rank(input_tensor), rank(input_tensor))`.
* <b>`keepdims`</b>: If true, retains reduced dimensions with length 1.
* <b>`name`</b>: A name for the operation (optional).
* <b>`reduction_indices`</b>: The old (deprecated) name for axis.
* <b>`keep_dims`</b>: Deprecated alias for `keepdims`.


#### Returns:

The reduced tensor.



#### Numpy Compatibility
Equivalent to np.any

