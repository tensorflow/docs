description: Serialize an N-minibatch SparseTensor into an [N, 3] Tensor object.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SerializeManySparse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SerializeManySparse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Serialize an `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor` object.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SerializeManySparse`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SerializeManySparse(
    sparse_indices, sparse_values, sparse_shape, out_type=tf.dtypes.string,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `SparseTensor` must have rank `R` greater than 1, and the first dimension
is treated as the minibatch dimension.  Elements of the `SparseTensor`
must be sorted in increasing order of this first dimension.  The serialized
`SparseTensor` objects going into each row of `serialized_sparse` will have
rank `R-1`.

The minibatch size `N` is extracted from `sparse_shape[0]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sparse_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  The `indices` of the minibatch `SparseTensor`.
</td>
</tr><tr>
<td>
`sparse_values`
</td>
<td>
A `Tensor`.
1-D.  The `values` of the minibatch `SparseTensor`.
</td>
</tr><tr>
<td>
`sparse_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  The `shape` of the minibatch `SparseTensor`.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.string, tf.variant`. Defaults to <a href="../../tf.md#string"><code>tf.string</code></a>.
The `dtype` to use for serialization; the supported types are `string`
(default) and `variant`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `out_type`.
</td>
</tr>

</table>

