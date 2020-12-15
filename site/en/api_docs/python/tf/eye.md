description: Construct an identity matrix, or a batch of matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.eye" />
<meta itemprop="path" content="Stable" />
</div>

# tf.eye

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg_ops.py#L196-L241">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Construct an identity matrix, or a batch of matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.linalg.eye`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.eye`, `tf.compat.v1.linalg.eye`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.eye(
    num_rows, num_columns=None, batch_shape=None, dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/ones.md"><code>tf.ones</code></a>, <a href="../tf/zeros.md"><code>tf.zeros</code></a>, <a href="../tf/fill.md"><code>tf.fill</code></a>, <a href="../tf/one_hot.md"><code>tf.one_hot</code></a>.

```python
# Construct one identity matrix.
tf.eye(2)
==> [[1., 0.],
     [0., 1.]]

# Construct a batch of 3 identity matrices, each 2 x 2.
# batch_identity[i, :, :] is a 2 x 2 identity matrix, i = 0, 1, 2.
batch_identity = tf.eye(2, batch_shape=[3])

# Construct one 2 x 3 "identity" matrix
tf.eye(2, num_columns=3)
==> [[ 1.,  0.,  0.],
     [ 0.,  1.,  0.]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_rows`
</td>
<td>
Non-negative `int32` scalar `Tensor` giving the number of rows
in each batch matrix.
</td>
</tr><tr>
<td>
`num_columns`
</td>
<td>
Optional non-negative `int32` scalar `Tensor` giving the number
of columns in each batch matrix.  Defaults to `num_rows`.
</td>
</tr><tr>
<td>
`batch_shape`
</td>
<td>
A list or tuple of Python integers or a 1-D `int32` `Tensor`.
If provided, the returned `Tensor` will have leading batch dimensions of
this shape.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of an element in the resulting `Tensor`
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this `Op`.  Defaults to "eye".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of shape `batch_shape + [num_rows, num_columns]`
</td>
</tr>

</table>

