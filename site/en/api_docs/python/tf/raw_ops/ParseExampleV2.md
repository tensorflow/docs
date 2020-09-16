description: Transforms a vector of tf.Example protos (as strings) into typed tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ParseExampleV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ParseExampleV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transforms a vector of tf.Example protos (as strings) into typed tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParseExampleV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParseExampleV2(
    serialized, names, sparse_keys, dense_keys, ragged_keys, dense_defaults,
    num_sparse, sparse_types, ragged_value_types, ragged_split_types, dense_shapes,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`serialized`
</td>
<td>
A `Tensor` of type `string`.
A scalar or vector containing binary serialized Example protos.
</td>
</tr><tr>
<td>
`names`
</td>
<td>
A `Tensor` of type `string`.
A tensor containing the names of the serialized protos.
Corresponds 1:1 with the `serialized` tensor.
May contain, for example, table key (descriptive) names for the
corresponding serialized protos.  These are purely useful for debugging
purposes, and the presence of values here has no effect on the output.
May also be an empty vector if no names are available.
If non-empty, this tensor must have the same shape as "serialized".
</td>
</tr><tr>
<td>
`sparse_keys`
</td>
<td>
A `Tensor` of type `string`. Vector of strings.
The keys expected in the Examples' features associated with sparse values.
</td>
</tr><tr>
<td>
`dense_keys`
</td>
<td>
A `Tensor` of type `string`. Vector of strings.
The keys expected in the Examples' features associated with dense values.
</td>
</tr><tr>
<td>
`ragged_keys`
</td>
<td>
A `Tensor` of type `string`. Vector of strings.
The keys expected in the Examples' features associated with ragged values.
</td>
</tr><tr>
<td>
`dense_defaults`
</td>
<td>
A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
A list of Tensors (some may be empty).  Corresponds 1:1 with `dense_keys`.
dense_defaults[j] provides default values
when the example's feature_map lacks dense_key[j].  If an empty Tensor is
provided for dense_defaults[j], then the Feature dense_keys[j] is required.
The input type is inferred from dense_defaults[j], even when it's empty.
If dense_defaults[j] is not empty, and dense_shapes[j] is fully defined,
then the shape of dense_defaults[j] must match that of dense_shapes[j].
If dense_shapes[j] has an undefined major dimension (variable strides dense
feature), dense_defaults[j] must contain a single element:
the padding element.
</td>
</tr><tr>
<td>
`num_sparse`
</td>
<td>
An `int` that is `>= 0`. The number of sparse keys.
</td>
</tr><tr>
<td>
`sparse_types`
</td>
<td>
A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
A list of `num_sparse` types; the data types of data in each Feature
given in sparse_keys.
Currently the ParseExample supports DT_FLOAT (FloatList),
DT_INT64 (Int64List), and DT_STRING (BytesList).
</td>
</tr><tr>
<td>
`ragged_value_types`
</td>
<td>
A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
A list of `num_ragged` types; the data types of data in each Feature
given in ragged_keys (where `num_ragged = sparse_keys.size()`).
Currently the ParseExample supports DT_FLOAT (FloatList),
DT_INT64 (Int64List), and DT_STRING (BytesList).
</td>
</tr><tr>
<td>
`ragged_split_types`
</td>
<td>
A list of `tf.DTypes` from: `tf.int32, tf.int64`.
A list of `num_ragged` types; the data types of row_splits in each Feature
given in ragged_keys (where `num_ragged = sparse_keys.size()`).
May be DT_INT32 or DT_INT64.
</td>
</tr><tr>
<td>
`dense_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`).
A list of `num_dense` shapes; the shapes of data in each Feature
given in dense_keys (where `num_dense = dense_keys.size()`).
The number of elements in the Feature corresponding to dense_key[j]
must always equal dense_shapes[j].NumEntries().
If dense_shapes[j] == (D0, D1, ..., DN) then the shape of output
Tensor dense_values[j] will be (|serialized|, D0, D1, ..., DN):
The dense outputs are just the inputs row-stacked by batch.
This works for dense_shapes[j] = (-1, D1, ..., DN).  In this case
the shape of the output Tensor dense_values[j] will be
(|serialized|, M, D1, .., DN), where M is the maximum number of blocks
of elements of length D1 * .... * DN, across all minibatch entries
in the input.  Any minibatch entry with less than M blocks of elements of
length D1 * ... * DN will be padded with the corresponding default_value
scalar element along the second dimension.
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
A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_shapes, dense_values, ragged_values, ragged_row_splits).
</td>
</tr>
<tr>
<td>
`sparse_indices`
</td>
<td>
A list of `num_sparse` `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`sparse_values`
</td>
<td>
A list of `Tensor` objects of type `sparse_types`.
</td>
</tr><tr>
<td>
`sparse_shapes`
</td>
<td>
A list of `num_sparse` `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`dense_values`
</td>
<td>
A list of `Tensor` objects. Has the same type as `dense_defaults`.
</td>
</tr><tr>
<td>
`ragged_values`
</td>
<td>
A list of `Tensor` objects of type `ragged_value_types`.
</td>
</tr><tr>
<td>
`ragged_row_splits`
</td>
<td>
A list of `Tensor` objects of type `ragged_split_types`.
</td>
</tr>
</table>

