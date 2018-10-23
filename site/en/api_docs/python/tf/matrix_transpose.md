

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.matrix_transpose

### Aliases:

* `tf.linalg.transpose`
* `tf.matrix_transpose`

``` python
matrix_transpose(
    a,
    name='matrix_transpose',
    conjugate=False
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/array_ops.py).

See the guide: [Math > Matrix Math Functions](../../../api_guides/python/math_ops#Matrix_Math_Functions)

Transposes last two dimensions of tensor `a`.

For example:

```python
x = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.matrix_transpose(x)  # [[1, 4],
                        #  [2, 5],
                        #  [3, 6]]

x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                 [4 + 4j, 5 + 5j, 6 + 6j]])
tf.matrix_transpose(x, conjugate=True)  # [[1 - 1j, 4 - 4j],
                                        #  [2 - 2j, 5 - 5j],
                                        #  [3 - 3j, 6 - 6j]]

# Matrix with two batch dimensions.
# x.shape is [1, 2, 3, 4]
# tf.matrix_transpose(x) is shape [1, 2, 4, 3]
```

Note that `tf.matmul` provides kwargs allowing for transpose of arguments.
This is done with minimal cost, and is preferable to using this function. E.g.

```python
# Good!  Transpose is taken at minimal additional cost.
tf.matmul(matrix, b, transpose_b=True)

# Inefficient!
tf.matmul(matrix, tf.matrix_transpose(b))
```

#### Args:

* <b>`a`</b>: A `Tensor` with `rank >= 2`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`conjugate`</b>: Optional bool. Setting it to `True` is mathematically equivalent
    to tf.conj(tf.matrix_transpose(input)).


#### Returns:

A transposed batch matrix `Tensor`.


#### Raises:

* <b>`ValueError`</b>:  If `a` is determined statically to have `rank < 2`.