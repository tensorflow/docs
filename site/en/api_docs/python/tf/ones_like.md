page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ones_like

``` python
tf.ones_like(
    tensor,
    dtype=None,
    name=None,
    optimize=True
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/array_ops.py).

See the guide: [Constants, Sequences, and Random Values > Constant Value Tensors](../../../api_guides/python/constant_op#Constant_Value_Tensors)

Creates a tensor with all elements set to 1.

Given a single tensor (`tensor`), this operation returns a tensor of the same
type and shape as `tensor` with all elements set to 1. Optionally, you can
specify a new type (`dtype`) for the returned tensor.

For example:

```python
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.ones_like(tensor)  # [[1, 1, 1], [1, 1, 1]]
```

#### Args:

* <b>`tensor`</b>: A `Tensor`.
* <b>`dtype`</b>: A type for the returned `Tensor`. Must be `float32`, `float64`,
    `int8`, `uint8`, `int16`, `uint16`, int32`, `int64`,
    `complex64`, `complex128` or `bool`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`optimize`</b>: if true, attempt to statically determine the shape of 'tensor'
  and encode it as a constant.


#### Returns:

A `Tensor` with all elements set to 1.