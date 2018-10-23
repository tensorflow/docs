


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.matrix_transpose

### `tf.matrix_transpose`

```
tf.matrix_transpose(a, name='matrix_transpose')
```


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
# tf.matrix_transpose is shape [1, 2, 4, 3]
```

#### Args:

* <b>`a`</b>: A `Tensor` with `rank >= 2`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A transposed batch matrix `Tensor`.


#### Raises:

* <b>`ValueError`</b>:  If `a` is determined statically to have `rank < 2`.

Defined in [`tensorflow/python/ops/array_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/array_ops.py).

