description: Transforms a scalar brain.SequenceExample proto (as strings) into typed tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ParseSingleSequenceExample" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ParseSingleSequenceExample

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transforms a scalar brain.SequenceExample proto (as strings) into typed tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParseSingleSequenceExample`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParseSingleSequenceExample(
    serialized, feature_list_dense_missing_assumed_empty, context_sparse_keys,
    context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys,
    context_dense_defaults, debug_name, context_sparse_types=[],
    feature_list_dense_types=[], context_dense_shapes=[],
    feature_list_sparse_types=[], feature_list_dense_shapes=[], name=None
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
A scalar containing a binary serialized SequenceExample proto.
</td>
</tr><tr>
<td>
`feature_list_dense_missing_assumed_empty`
</td>
<td>
A `Tensor` of type `string`.
A vector listing the
FeatureList keys which may be missing from the SequenceExample.  If the
associated FeatureList is missing, it is treated as empty.  By default,
any FeatureList not listed in this vector must exist in the SequenceExample.
</td>
</tr><tr>
<td>
`context_sparse_keys`
</td>
<td>
A list of `Tensor` objects with type `string`.
A list of Ncontext_sparse string Tensors (scalars).
The keys expected in the Examples' features associated with context_sparse
values.
</td>
</tr><tr>
<td>
`context_dense_keys`
</td>
<td>
A list of `Tensor` objects with type `string`.
A list of Ncontext_dense string Tensors (scalars).
The keys expected in the SequenceExamples' context features associated with
dense values.
</td>
</tr><tr>
<td>
`feature_list_sparse_keys`
</td>
<td>
A list of `Tensor` objects with type `string`.
A list of Nfeature_list_sparse string Tensors
(scalars).  The keys expected in the FeatureLists associated with sparse
values.
</td>
</tr><tr>
<td>
`feature_list_dense_keys`
</td>
<td>
A list of `Tensor` objects with type `string`.
A list of Nfeature_list_dense string Tensors (scalars).
The keys expected in the SequenceExamples' feature_lists associated
with lists of dense values.
</td>
</tr><tr>
<td>
`context_dense_defaults`
</td>
<td>
A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
A list of Ncontext_dense Tensors (some may be empty).
context_dense_defaults[j] provides default values
when the SequenceExample's context map lacks context_dense_key[j].
If an empty Tensor is provided for context_dense_defaults[j],
then the Feature context_dense_keys[j] is required.
The input type is inferred from context_dense_defaults[j], even when it's
empty.  If context_dense_defaults[j] is not empty, its shape must match
context_dense_shapes[j].
</td>
</tr><tr>
<td>
`debug_name`
</td>
<td>
A `Tensor` of type `string`.
A scalar containing the name of the serialized proto.
May contain, for example, table key (descriptive) name for the
corresponding serialized proto.  This is purely useful for debugging
purposes, and the presence of values here has no effect on the output.
May also be an empty scalar if no name is available.
</td>
</tr><tr>
<td>
`context_sparse_types`
</td>
<td>
An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
A list of Ncontext_sparse types; the data types of data in
each context Feature given in context_sparse_keys.
Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
DT_INT64 (Int64List), and DT_STRING (BytesList).
</td>
</tr><tr>
<td>
`feature_list_dense_types`
</td>
<td>
An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
</td>
</tr><tr>
<td>
`context_dense_shapes`
</td>
<td>
An optional list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`). Defaults to `[]`.
A list of Ncontext_dense shapes; the shapes of data in
each context Feature given in context_dense_keys.
The number of elements in the Feature corresponding to context_dense_key[j]
must always equal context_dense_shapes[j].NumEntries().
The shape of context_dense_values[j] will match context_dense_shapes[j].
</td>
</tr><tr>
<td>
`feature_list_sparse_types`
</td>
<td>
An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
A list of Nfeature_list_sparse types; the data types
of data in each FeatureList given in feature_list_sparse_keys.
Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
DT_INT64 (Int64List), and DT_STRING (BytesList).
</td>
</tr><tr>
<td>
`feature_list_dense_shapes`
</td>
<td>
An optional list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`). Defaults to `[]`.
A list of Nfeature_list_dense shapes; the shapes of
data in each FeatureList given in feature_list_dense_keys.
The shape of each Feature in the FeatureList corresponding to
feature_list_dense_key[j] must always equal
feature_list_dense_shapes[j].NumEntries().
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
A tuple of `Tensor` objects (context_sparse_indices, context_sparse_values, context_sparse_shapes, context_dense_values, feature_list_sparse_indices, feature_list_sparse_values, feature_list_sparse_shapes, feature_list_dense_values).
</td>
</tr>
<tr>
<td>
`context_sparse_indices`
</td>
<td>
A list with the same length as `context_sparse_keys` of `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`context_sparse_values`
</td>
<td>
A list of `Tensor` objects of type `context_sparse_types`.
</td>
</tr><tr>
<td>
`context_sparse_shapes`
</td>
<td>
A list with the same length as `context_sparse_keys` of `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`context_dense_values`
</td>
<td>
A list of `Tensor` objects. Has the same type as `context_dense_defaults`.
</td>
</tr><tr>
<td>
`feature_list_sparse_indices`
</td>
<td>
A list with the same length as `feature_list_sparse_keys` of `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`feature_list_sparse_values`
</td>
<td>
A list of `Tensor` objects of type `feature_list_sparse_types`.
</td>
</tr><tr>
<td>
`feature_list_sparse_shapes`
</td>
<td>
A list with the same length as `feature_list_sparse_keys` of `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`feature_list_dense_values`
</td>
<td>
A list of `Tensor` objects of type `feature_list_dense_types`.
</td>
</tr>
</table>

