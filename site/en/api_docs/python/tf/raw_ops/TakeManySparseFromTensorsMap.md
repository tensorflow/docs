description: Read SparseTensors from a SparseTensorsMap and concatenate them.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TakeManySparseFromTensorsMap" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TakeManySparseFromTensorsMap

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Read `SparseTensors` from a `SparseTensorsMap` and concatenate them.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TakeManySparseFromTensorsMap`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TakeManySparseFromTensorsMap(
    sparse_handles, dtype, container='', shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input `sparse_handles` must be an `int64` matrix of shape `[N, 1]` where
`N` is the minibatch size and the rows correspond to the output handles of
`AddSparseToTensorsMap` or `AddManySparseToTensorsMap`.  The ranks of the
original `SparseTensor` objects that went into the given input ops must all
match.  When the final `SparseTensor` is created, it has rank one
higher than the ranks of the incoming `SparseTensor` objects
(they have been concatenated along a new row dimension on the left).

The output `SparseTensor` object's shape values for all dimensions but the
first are the max across the input `SparseTensor` objects' shape values
for the corresponding dimensions.  Its first shape value is `N`, the minibatch
size.

The input `SparseTensor` objects' indices are assumed ordered in
standard lexicographic order.  If this is not the case, after this
step run `SparseReorder` to restore index ordering.

For example, if the handles represent an input, which is a `[2, 3]` matrix
representing two original `SparseTensor` objects:

```
    index = [ 0]
            [10]
            [20]
    values = [1, 2, 3]
    shape = [50]
```

and

```
    index = [ 2]
            [10]
    values = [4, 5]
    shape = [30]
```

then the final `SparseTensor` will be:

```
    index = [0  0]
            [0 10]
            [0 20]
            [1  2]
            [1 10]
    values = [1, 2, 3, 4, 5]
    shape = [2 50]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sparse_handles`
</td>
<td>
A `Tensor` of type `int64`.
1-D, The `N` serialized `SparseTensor` objects.
Shape: `[N]`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
The `dtype` of the `SparseTensor` objects stored in the
`SparseTensorsMap`.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
The container name for the `SparseTensorsMap` read by this op.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
The shared name for the `SparseTensorsMap` read by this op.
It should not be blank; rather the `shared_name` or unique Operation name
of the Op that created the original `SparseTensorsMap` should be used.
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
A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_shape).
</td>
</tr>
<tr>
<td>
`sparse_indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`sparse_values`
</td>
<td>
A `Tensor` of type `dtype`.
</td>
</tr><tr>
<td>
`sparse_shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

