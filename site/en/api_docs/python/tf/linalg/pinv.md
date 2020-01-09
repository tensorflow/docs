page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.pinv


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linalg_impl.py#L697-L823">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute the Moore-Penrose pseudo-inverse of one or more matrices.

### Aliases:

* <a href="/api_docs/python/tf/linalg/pinv"><code>tf.compat.v1.linalg.pinv</code></a>
* <a href="/api_docs/python/tf/linalg/pinv"><code>tf.compat.v2.linalg.pinv</code></a>


``` python
tf.linalg.pinv(
    a,
    rcond=None,
    validate_args=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Calculate the [generalized inverse of a matrix](
https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse) using its
singular-value decomposition (SVD) and including all large singular values.

The pseudo-inverse of a matrix `A`, is defined as: 'the matrix that 'solves'
[the least-squares problem] `A @ x = b`,' i.e., if `x_hat` is a solution, then
`A_pinv` is the matrix such that `x_hat = A_pinv @ b`. It can be shown that if
`U @ Sigma @ V.T = A` is the singular value decomposition of `A`, then
`A_pinv = V @ inv(Sigma) U^T`. [(Strang, 1980)][1]

This function is analogous to [`numpy.linalg.pinv`](
https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.pinv.html).
It differs only in default value of `rcond`. In `numpy.linalg.pinv`, the
default `rcond` is `1e-15`. Here the default is
`10. * max(num_rows, num_cols) * np.finfo(dtype).eps`.

#### Args:


* <b>`a`</b>: (Batch of) `float`-like matrix-shaped `Tensor`(s) which are to be
  pseudo-inverted.
* <b>`rcond`</b>: `Tensor` of small singular value cutoffs.  Singular values smaller
  (in modulus) than `rcond` * largest_singular_value (again, in modulus) are
  set to zero. Must broadcast against `tf.shape(a)[:-2]`.
  Default value: `10. * max(num_rows, num_cols) * np.finfo(a.dtype).eps`.
* <b>`validate_args`</b>: When `True`, additional assertions might be embedded in the
  graph.
  Default value: `False` (i.e., no graph assertions are added).
* <b>`name`</b>: Python `str` prefixed to ops created by this function.
  Default value: 'pinv'.


#### Returns:


* <b>`a_pinv`</b>: (Batch of) pseudo-inverse of input `a`. Has same shape as `a` except
  rightmost two dimensions are transposed.


#### Raises:


* <b>`TypeError`</b>: if input `a` does not have `float`-like `dtype`.
* <b>`ValueError`</b>: if input `a` has fewer than 2 dimensions.

#### Examples

```python
import tensorflow as tf
import tensorflow_probability as tfp

a = tf.constant([[1.,  0.4,  0.5],
                 [0.4, 0.2,  0.25],
                 [0.5, 0.25, 0.35]])
tf.matmul(tf.linalg..pinv(a), a)
# ==> array([[1., 0., 0.],
             [0., 1., 0.],
             [0., 0., 1.]], dtype=float32)

a = tf.constant([[1.,  0.4,  0.5,  1.],
                 [0.4, 0.2,  0.25, 2.],
                 [0.5, 0.25, 0.35, 3.]])
tf.matmul(tf.linalg..pinv(a), a)
# ==> array([[ 0.76,  0.37,  0.21, -0.02],
             [ 0.37,  0.43, -0.33,  0.02],
             [ 0.21, -0.33,  0.81,  0.01],
             [-0.02,  0.02,  0.01,  1.  ]], dtype=float32)
```

#### References

[1]: G. Strang. 'Linear Algebra and Its Applications, 2nd Ed.' Academic Press,
     Inc., 1980, pp. 139-142.
