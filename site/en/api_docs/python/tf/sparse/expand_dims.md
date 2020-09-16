description: Inserts a dimension of 1 into a tensor's shape.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.expand_dims" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.expand_dims

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/sparse_ops.py#L127-L180">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Inserts a dimension of 1 into a tensor's shape.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.expand_dims`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.expand_dims(
    sp_input, axis=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a tensor `sp_input`, this operation inserts a dimension of 1 at the
dimension index `axis` of `sp_input`'s shape. The dimension index `axis`
starts at zero; if you specify a negative number for `axis` it is counted
backwards from the end.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
A `SparseTensor`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
0-D (scalar). Specifies the dimension index at which to expand the
shape of `input`. Must be in the range `[-rank(sp_input) - 1,
rank(sp_input)]`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the output `SparseTensor`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` with the same data as `sp_input`, but its shape has an
additional dimension of size 1 added.
</td>
</tr>

</table>

