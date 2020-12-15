description: Add an N-minibatch SparseTensor to a SparseTensorsMap, return N handles.

robots: noindex

# tf.raw_ops.AddManySparseToTensorsMap

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Add an `N`-minibatch `SparseTensor` to a `SparseTensorsMap`, return `N` handles.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AddManySparseToTensorsMap`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AddManySparseToTensorsMap(
    sparse_indices, sparse_values, sparse_shape, container='', shared_name='',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A `SparseTensor` of rank `R` is represented by three tensors: `sparse_indices`,
`sparse_values`, and `sparse_shape`, where

```sparse_indices.shape[1] == sparse_shape.shape[0] == R```

An `N`-minibatch of `SparseTensor` objects is represented as a `SparseTensor`
having a first `sparse_indices` column taking values between `[0, N)`, where
the minibatch size `N == sparse_shape[0]`.

The input `SparseTensor` must have rank `R` greater than 1, and the first
dimension is treated as the minibatch dimension.  Elements of the `SparseTensor`
must be sorted in increasing order of this first dimension.  The stored
`SparseTensor` objects pointed to by each row of the output `sparse_handles`
will have rank `R-1`.

The `SparseTensor` values can then be read out as part of a minibatch by passing
the given keys as vector elements to `TakeManySparseFromTensorsMap`.  To ensure
the correct `SparseTensorsMap` is accessed, ensure that the same
`container` and `shared_name` are passed to that Op.  If no `shared_name`
is provided here, instead use the *name* of the Operation created by calling
`AddManySparseToTensorsMap` as the `shared_name` passed to
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
2-D.  The `indices` of the minibatch `SparseTensor`.
`sparse_indices[:, 0]` must be ordered values in `[0, N)`.
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
The minibatch size `N == sparse_shape[0]`.
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

