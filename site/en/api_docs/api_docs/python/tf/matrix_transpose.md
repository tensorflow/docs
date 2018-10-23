

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.matrix_transpose

``` python
matrix_transpose(
    a,
    name='matrix_transpose'
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/array_ops.py).

See the guide: [Math > Matrix Math Functions](../../../api_guides/python/math_ops#Matrix_Math_Functions)

Transposes last two dimensions of tensor `a`.

For example:

```python
# Matrix with no batch dimension.
# 'x' is [[1 2 3]
#         [4 5 6]]
tf.matrix_transpose(x) ==> [[1 4]
                                 [2 5]
                                 [3 6]]

# Matrix with two batch dimensions.
# x.shape is [1, 2, 3, 4]
# tf.matrix_transpose(x) is shape [1, 2, 4, 3]
```

Note that `tf.matmul` provides kwargs allowing for transpose of arguments.
This is done with minimal cost, and is preferable to using this function. E.g.

```
# Good!  Transpose is taken at minimal additional cost.
tf.matmul(matrix, b, transpose_b=True)

# Inefficient!
tf.matmul(matrix, tf.matrix_transpose(b))
```

#### Args:

* <b>`a`</b>: A `Tensor` with `rank >= 2`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A transposed batch matrix `Tensor`.


#### Raises:

* <b>`ValueError`</b>:  If `a` is determined statically to have `rank < 2`.