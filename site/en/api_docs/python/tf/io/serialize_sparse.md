description: Serialize a SparseTensor into a 3-vector (1-D Tensor) object.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.serialize_sparse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.serialize_sparse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L2111-L2135">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.serialize_sparse(
    sp_input, out_type=tf.dtypes.string, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
`out_type`
</td>
<td>
The `dtype` to use for serialization.
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
A 3-vector (1-D `Tensor`), with each column representing the serialized
`SparseTensor`'s indices, values, and shape (respectively).
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

