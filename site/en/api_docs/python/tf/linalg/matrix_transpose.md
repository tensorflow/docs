page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.matrix_transpose


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/matrix_transpose">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L1864-L1941">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Transposes last two dimensions of tensor `a`.

### Aliases:

* <a href="/api_docs/python/tf/linalg/matrix_transpose"><code>tf.compat.v1.linalg.matrix_transpose</code></a>
* <a href="/api_docs/python/tf/linalg/matrix_transpose"><code>tf.compat.v1.linalg.transpose</code></a>
* <a href="/api_docs/python/tf/linalg/matrix_transpose"><code>tf.compat.v1.matrix_transpose</code></a>
* <a href="/api_docs/python/tf/linalg/matrix_transpose"><code>tf.compat.v2.linalg.matrix_transpose</code></a>
* <a href="/api_docs/python/tf/linalg/matrix_transpose"><code>tf.linalg.transpose</code></a>
* <a href="/api_docs/python/tf/linalg/matrix_transpose"><code>tf.matrix_transpose</code></a>


``` python
tf.linalg.matrix_transpose(
    a,
    name='matrix_transpose',
    conjugate=False
)
```



<!-- Placeholder for "Used in" -->


#### For example:



```python
x = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.linalg.matrix_transpose(x)  # [[1, 4],
                               #  [2, 5],
                               #  [3, 6]]

x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                 [4 + 4j, 5 + 5j, 6 + 6j]])
tf.linalg.matrix_transpose(x, conjugate=True)  # [[1 - 1j, 4 - 4j],
                                               #  [2 - 2j, 5 - 5j],
                                               #  [3 - 3j, 6 - 6j]]

# Matrix with two batch dimensions.
# x.shape is [1, 2, 3, 4]
# tf.linalg.matrix_transpose(x) is shape [1, 2, 4, 3]
```

Note that <a href="../../tf/linalg/matmul"><code>tf.matmul</code></a> provides kwargs allowing for transpose of arguments.
This is done with minimal cost, and is preferable to using this function. E.g.

```python
# Good!  Transpose is taken at minimal additional cost.
tf.matmul(matrix, b, transpose_b=True)

# Inefficient!
tf.matmul(matrix, tf.linalg.matrix_transpose(b))
```



#### Args:


* <b>`a`</b>: A `Tensor` with `rank >= 2`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`conjugate`</b>: Optional bool. Setting it to `True` is mathematically equivalent
  to tf.math.conj(tf.linalg.matrix_transpose(input)).


#### Returns:

A transposed batch matrix `Tensor`.



#### Raises:


* <b>`ValueError`</b>:  If `a` is determined statically to have `rank < 2`.

#### Numpy Compatibility
In `numpy` transposes are memory-efficient constant time operations as they
simply return a new view of the same data with adjusted `strides`.

TensorFlow does not support strides, <a href="../../tf/linalg/matrix_transpose"><code>linalg.matrix_transpose</code></a> returns a new
tensor with the items permuted.
