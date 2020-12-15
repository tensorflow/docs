description: Computes the inverse given the LU decomposition(s) of one or more matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.lu_matrix_inverse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.lu_matrix_inverse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/linalg/linalg_impl.py#L1006-L1068">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the inverse given the LU decomposition(s) of one or more matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.lu_matrix_inverse`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.lu_matrix_inverse(
    lower_upper, perm, validate_args=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op is conceptually identical to,

```python
inv_X = tf.lu_matrix_inverse(*tf.linalg.lu(X))
tf.assert_near(tf.matrix_inverse(X), inv_X)
# ==> True
```

Note: this function does not verify the implied matrix is actually invertible
nor is this condition checked even when `validate_args=True`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`lower_upper`
</td>
<td>
`lu` as returned by <a href="../../tf/linalg/lu.md"><code>tf.linalg.lu</code></a>, i.e., if `matmul(P,
matmul(L, U)) = X` then `lower_upper = L + U - eye`.
</td>
</tr><tr>
<td>
`perm`
</td>
<td>
`p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) =
X` then `perm = argmax(P)`.
</td>
</tr><tr>
<td>
`validate_args`
</td>
<td>
Python `bool` indicating whether arguments should be checked
for correctness. Note: this function does not verify the implied matrix is
actually invertible, even when `validate_args=True`.
Default value: `False` (i.e., don't validate arguments).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` name given to ops managed by this object.
Default value: `None` (i.e., 'lu_matrix_inverse').
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`inv_x`
</td>
<td>
The matrix_inv, i.e.,
`tf.matrix_inverse(tf.linalg.lu_reconstruct(lu, perm))`.
</td>
</tr>
</table>


#### Examples

```python
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp

x = [[[3., 4], [1, 2]],
     [[7., 8], [3, 4]]]
inv_x = tf.linalg.lu_matrix_inverse(*tf.linalg.lu(x))
tf.assert_near(tf.matrix_inverse(x), inv_x)
# ==> True
```