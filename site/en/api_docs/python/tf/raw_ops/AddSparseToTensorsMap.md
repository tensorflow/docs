description: Add a SparseTensor to a SparseTensorsMap return its handle.

robots: noindex

# tf.raw_ops.AddSparseToTensorsMap

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Add a `SparseTensor` to a `SparseTensorsMap` return its handle.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AddSparseToTensorsMap`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AddSparseToTensorsMap(
    sparse_indices, sparse_values, sparse_shape, container='', shared_name='',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A `SparseTensor` is represented by three tensors: `sparse_indices`,
`sparse_values`, and `sparse_shape`.

This operator takes the given `SparseTensor` and adds it to a container
object (a `SparseTensorsMap`).  A unique key within this container is generated
in the form of an `int64`, and this is the value that is returned.

The `SparseTensor` can then be read out as part of a minibatch by passing
the key as a vector element to `TakeManySparseFromTensorsMap`.  To ensure
the correct `SparseTensorsMap` is accessed, ensure that the same
`container` and `shared_name` are passed to that Op.  If no `shared_name`
is provided here, instead use the *name* of the Operation created by calling
`AddSparseToTensorsMap` as the `shared_name` passed to
`TakeManySparseFromTensorsMap`.  Ensure the Operations are colocated.

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
2-D.  The `indices` of the `SparseTensor`.
</td>
</tr><tr>
<td>
`sparse_values`
</td>
<td>
A `Tensor`. 1-D.  The `values` of the `SparseTensor`.
</td>
</tr><tr>
<td>
`sparse_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  The `shape` of the `SparseTensor`.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
The container name for the `SparseTensorsMap` created by this op.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
The shared name for the `SparseTensorsMap` created by this op.
If blank, the new Operation's unique name is used.
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
A `Tensor` of type `int64`.
</td>
</tr>

</table>

