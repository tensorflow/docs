description: Computes the singular value decompositions of one or more matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.svd" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.svd

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/linalg_ops.py#L484-L552">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the singular value decompositions of one or more matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.svd`, `tf.compat.v1.svd`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.svd(
    tensor, full_matrices=(False), compute_uv=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
`Tensor` of shape `[..., M, N]`. Let `P` be the minimum of `M` and
`N`.
</td>
</tr><tr>
<td>
`full_matrices`
</td>
<td>
If true, compute full-sized `u` and `v`. If false
(the default), compute only the leading `P` singular vectors.
Ignored if `compute_uv` is `False`.
</td>
</tr><tr>
<td>
`compute_uv`
</td>
<td>
If `True` then left and right singular vectors will be
computed and returned in `u` and `v`, respectively. Otherwise, only the
singular values will be computed, which can be significantly faster.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
string, optional name of the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`s`
</td>
<td>
Singular values. Shape is `[..., P]`. The values are sorted in reverse
order of magnitude, so s[..., 0] is the largest value, s[..., 1] is the
second largest, etc.
</td>
</tr><tr>
<td>
`u`
</td>
<td>
Left singular vectors. If `full_matrices` is `False` (default) then
shape is `[..., M, P]`; if `full_matrices` is `True` then shape is
`[..., M, M]`. Not returned if `compute_uv` is `False`.
</td>
</tr><tr>
<td>
`v`
</td>
<td>
Right singular vectors. If `full_matrices` is `False` (default) then
shape is `[..., N, P]`. If `full_matrices` is `True` then shape is
`[..., N, N]`. Not returned if `compute_uv` is `False`.
</td>
</tr>
</table>




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

