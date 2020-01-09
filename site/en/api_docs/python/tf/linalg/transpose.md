page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.transpose

### Aliases:

* `tf.linalg.transpose`
* `tf.matrix_transpose`

``` python
tf.linalg.transpose(
    a,
    name='matrix_transpose',
    conjugate=False
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/array_ops.py).

See the guide: [Upgrade to TensorFlow 1.0 > Upgrading your code manually](../../../../api_guides/python/upgrade#Upgrading_your_code_manually)

Transposes last two dimensions of tensor `a`.

For example:

```python
x = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.linalg.transpose(x)  # [[1, 4],
                        #  [2, 5],
                        #  [3, 6]]

x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                 [4 + 4j, 5 + 5j, 6 + 6j]])
tf.linalg.transpose(x, conjugate=True)  # [[1 - 1j, 4 - 4j],
                                        #  [2 - 2j, 5 - 5j],
                                        #  [3 - 3j, 6 - 6j]]

# Matrix with two batch dimensions.
# x.shape is [1, 2, 3, 4]
# tf.linalg.transpose(x) is shape [1, 2, 4, 3]
```

Note that <a href="../../tf/linalg/matmul"><code>tf.matmul</code></a> provides kwargs allowing for transpose of arguments.
This is done with minimal cost, and is preferable to using this function. E.g.

```python
# Good!  Transpose is taken at minimal additional cost.
tf.matmul(matrix, b, transpose_b=True)

# Inefficient!
tf.matmul(matrix, tf.linalg.transpose(b))
```



#### Args:

* <b>`a`</b>: A `Tensor` with `rank >= 2`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`conjugate`</b>: Optional bool. Setting it to `True` is mathematically equivalent
    to tf.conj(tf.linalg.transpose(input)).


#### Returns:

A transposed batch matrix `Tensor`.


#### Raises:

* <b>`ValueError`</b>:  If `a` is determined statically to have `rank < 2`.

#### Numpy Compatibility
In `numpy` transposes are memory-efficient constant time operations as they
simply return a new view of the same data with adjusted `strides`.

TensorFlow does not support strides, `linalg.transposes` return a new tensor
with the items permuted.

