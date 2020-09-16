description: The reconstruct one or more matrices from their LU decomposition(s).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.lu_reconstruct" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.lu_reconstruct

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/linalg/linalg_impl.py#L1071-L1142">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The reconstruct one or more matrices from their LU decomposition(s).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.lu_reconstruct`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.lu_reconstruct(
    lower_upper, perm, validate_args=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
for correctness.
Default value: `False` (i.e., don't validate arguments).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` name given to ops managed by this object.
Default value: `None` (i.e., 'lu_reconstruct').
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
The original input to <a href="../../tf/linalg/lu.md"><code>tf.linalg.lu</code></a>, i.e., `x` as in,
`lu_reconstruct(*tf.linalg.lu(x))`.
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
x_reconstructed = tf.linalg.lu_reconstruct(*tf.linalg.lu(x))
tf.assert_near(x, x_reconstructed)
# ==> True
```