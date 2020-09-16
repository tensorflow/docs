description: Creates a two-dimensional sparse tensor with ones along the diagonal.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.eye" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.eye

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/sparse_ops.py#L183-L214">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a two-dimensional sparse tensor with ones along the diagonal.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.eye`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.eye(
    num_rows, num_columns=None, dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_rows`
</td>
<td>
Non-negative integer or `int32` scalar `tensor` giving the number
of rows in the resulting matrix.
</td>
</tr><tr>
<td>
`num_columns`
</td>
<td>
Optional non-negative integer or `int32` scalar `tensor` giving
the number of columns in the resulting matrix. Defaults to `num_rows`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of element in the resulting `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this `Op`. Defaults to "eye".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` of shape [num_rows, num_columns] with ones along the
diagonal.
</td>
</tr>

</table>

