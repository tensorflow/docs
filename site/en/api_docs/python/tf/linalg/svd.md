page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.svd

### Aliases:

* `tf.linalg.svd`
* `tf.svd`

``` python
tf.linalg.svd(
    tensor,
    full_matrices=False,
    compute_uv=True,
    name=None
)
```



Defined in [`tensorflow/python/ops/linalg_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/linalg_ops.py).

Computes the singular value decompositions of one or more matrices.

Computes the SVD of each inner matrix in `tensor` such that
`tensor[..., :, :] = u[..., :, :] * diag(s[..., :, :]) *
 transpose(conj(v[..., :, :]))`

```python
# a is a tensor.
# s is a tensor of singular values.
# u is a tensor of left singular vectors.
# v is a tensor of right singular vectors.
s, u, v = svd(a)
s = svd(a, compute_uv=False)
```

#### Args:

* <b>`tensor`</b>: `Tensor` of shape `[..., M, N]`. Let `P` be the minimum of `M` and
    `N`.
* <b>`full_matrices`</b>: If true, compute full-sized `u` and `v`. If false
    (the default), compute only the leading `P` singular vectors.
    Ignored if `compute_uv` is `False`.
* <b>`compute_uv`</b>: If `True` then left and right singular vectors will be
    computed and returned in `u` and `v`, respectively. Otherwise, only the
    singular values will be computed, which can be significantly faster.
* <b>`name`</b>: string, optional name of the operation.


#### Returns:

* <b>`s`</b>: Singular values. Shape is `[..., P]`. The values are sorted in reverse
    order of magnitude, so s[..., 0] is the largest value, s[..., 1] is the
    second largest, etc.
* <b>`u`</b>: Left singular vectors. If `full_matrices` is `False` (default) then
    shape is `[..., M, P]`; if `full_matrices` is `True` then shape is
    `[..., M, M]`. Not returned if `compute_uv` is `False`.
* <b>`v`</b>: Right singular vectors. If `full_matrices` is `False` (default) then
    shape is `[..., N, P]`. If `full_matrices` is `True` then shape is
    `[..., N, N]`. Not returned if `compute_uv` is `False`.



#### Numpy Compatibility
Mostly equivalent to numpy.linalg.svd, except that
  * The order of output  arguments here is `s`, `u`, `v` when `compute_uv` is
    `True`, as opposed to `u`, `s`, `v` for numpy.linalg.svd.
  * full_matrices is `False` by default as opposed to `True` for
     numpy.linalg.svd.
  * tf.linalg.svd uses the standard definition of the SVD
    \\(A = U \Sigma V^H\\), such that the left singular vectors of `a` are
    the columns of `u`, while the right singular vectors of `a` are the
    columns of `v`. On the other hand, numpy.linalg.svd returns the adjoint
    \\(V^H\\) as the third output argument.

```python
import tensorflow as tf
import numpy as np
s, u, v = tf.linalg.svd(a)
tf_a_approx = tf.matmul(u, tf.matmul(tf.linalg.diag(s), v, adjoint_b=True))
u, s, v_adj = np.linalg.svd(a, full_matrices=False)
np_a_approx = np.dot(u, np.dot(np.diag(s), v_adj))
# tf_a_approx and np_a_approx should be numerically close.
```

