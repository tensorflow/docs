

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.count_nonzero

``` python
tf.count_nonzero(
    input_tensor,
    axis=None,
    keepdims=None,
    dtype=tf.int64,
    name=None,
    reduction_indices=None,
    keep_dims=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Reduction](../../../api_guides/python/math_ops#Reduction)

Computes number of nonzero elements across dimensions of a tensor. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` has no entries, all dimensions are reduced, and a
tensor with a single element is returned.

**NOTE** Floating point comparison to zero is done by exact floating point
equality check.  Small values are **not** rounded to zero for purposes of
the nonzero check.

For example:

```python
x = tf.constant([[0, 1, 0], [1, 1, 0]])
tf.count_nonzero(x)  # 3
tf.count_nonzero(x, 0)  # [1, 2, 0]
tf.count_nonzero(x, 1)  # [1, 2]
tf.count_nonzero(x, 1, keepdims=True)  # [[1], [2]]
tf.count_nonzero(x, [0, 1])  # 3
```

#### Args:

* <b>`input_tensor`</b>: The tensor to reduce. Should be of numeric type, or `bool`.
* <b>`axis`</b>: The dimensions to reduce. If `None` (the default),
    reduces all dimensions. Must be in the range
    `[-rank(input_tensor), rank(input_tensor))`.
* <b>`keepdims`</b>: If true, retains reduced dimensions with length 1.
* <b>`dtype`</b>: The output dtype; defaults to `tf.int64`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`reduction_indices`</b>: The old (deprecated) name for axis.
* <b>`keep_dims`</b>: Deprecated alias for `keepdims`.


#### Returns:

The reduced tensor (number of nonzero values).