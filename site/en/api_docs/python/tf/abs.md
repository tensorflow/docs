


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.abs

### `tf.abs`

```
tf.abs(x, name=None)
```


See the guide: [Math > Basic Math Functions](../../../api_guides/python/math_ops#Basic_Math_Functions)

Computes the absolute value of a tensor.

Given a tensor of real numbers `x`, this operation returns a tensor
containing the absolute value of each element in `x`. For example, if x is
an input element and y is an output element, this operation computes
\\(y = |x|\\).

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor` of type `float32`, `float64`, `int32`, or
    `int64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` or `SparseTensor` the same size and type as `x` with absolute
    values.

Defined in [`tensorflow/python/ops/math_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/math_ops.py).

