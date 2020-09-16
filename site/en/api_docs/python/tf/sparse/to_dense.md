description: Converts a SparseTensor into a dense tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.to_dense" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.to_dense

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/sparse_ops.py#L1448-L1500">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a `SparseTensor` into a dense tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.to_dense`, `tf.compat.v1.sparse_tensor_to_dense`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.to_dense(
    sp_input, default_value=None, validate_indices=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op is a convenience wrapper around `sparse_to_dense` for `SparseTensor`s.

For example, if `sp_input` has shape `[3, 5]` and non-empty string values:

    [0, 1]: a
    [0, 3]: b
    [2, 0]: c

and `default_value` is `x`, then the output will be a dense `[3, 5]`
string tensor with values:

    [[x a x b x]
     [x x x x x]
     [c x x x x]]

Indices must be without repeats.  This is only
tested if `validate_indices` is `True`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
The input `SparseTensor`.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
Scalar value to set for indices not specified in
`sp_input`.  Defaults to zero.
</td>
</tr><tr>
<td>
`validate_indices`
</td>
<td>
A boolean value.  If `True`, indices are checked to make
sure they are sorted in lexicographic order and that there are no repeats.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dense tensor with shape `sp_input.dense_shape` and values specified by
the non-empty values in `sp_input`. Indices not in `sp_input` are assigned
`default_value`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `sp_input` is not a `SparseTensor`.
</td>
</tr>
</table>

