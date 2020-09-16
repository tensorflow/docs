description: Transforms a vector of tf.io.SequenceExample protos (as strings) into

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ParseSequenceExampleV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ParseSequenceExampleV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transforms a vector of tf.io.SequenceExample protos (as strings) into

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParseSequenceExampleV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParseSequenceExampleV2(
    serialized, debug_name, context_sparse_keys, context_dense_keys,
    context_ragged_keys, feature_list_sparse_keys, feature_list_dense_keys,
    feature_list_ragged_keys, feature_list_dense_missing_assumed_empty,
    context_dense_defaults, Ncontext_sparse=0, context_sparse_types=[],
    context_ragged_value_types=[], context_ragged_split_types=[],
    context_dense_shapes=[], Nfeature_list_sparse=0, Nfeature_list_dense=0,
    feature_list_dense_types=[], feature_list_sparse_types=[],
    feature_list_ragged_value_types=[], feature_list_ragged_split_types=[],
    feature_list_dense_shapes=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->
typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A scalar or vector containing binary serialized SequenceExample protos.
    debug_name: A `Tensor` of type `string`.
      A scalar or vector containing the names of the serialized protos.
      May contain, for example, table key (descriptive) name for the
      corresponding serialized proto.  This is purely useful for debugging
      purposes, and the presence of values here has no effect on the output.
      May also be an empty vector if no name is available.
    context_sparse_keys: A `Tensor` of type `string`.
      The keys expected in the Examples' features associated with context_sparse
      values.
    context_dense_keys: A `Tensor` of type `string`.
      The keys expected in the SequenceExamples' context features associated with
      dense values.
    context_ragged_keys: A `Tensor` of type `string`.
      The keys expected in the Examples' features associated with context_ragged
      values.
    feature_list_sparse_keys: A `Tensor` of type `string`.
      The keys expected in the FeatureLists associated with sparse values.
    feature_list_dense_keys: A `Tensor` of type `string`.
      The keys expected in the SequenceExamples' feature_lists associated
      with lists of dense values.
    feature_list_ragged_keys: A `Tensor` of type `string`.
      The keys expected in the FeatureLists associated with ragged values.
    feature_list_dense_missing_assumed_empty: A `Tensor` of type `bool`.
      A vector corresponding 1:1 with featue_list_dense_keys, indicating which
      features may be missing from the SequenceExamples.  If the associated
      FeatureList is missing, it is treated as empty.
    context_dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Ncontext_dense Tensors (some may be empty).
      context_dense_defaults[j] provides default values
      when the SequenceExample's context map lacks context_dense_key[j].
      If an empty Tensor is provided for context_dense_defaults[j],
      then the Feature context_dense_keys[j] is required.
      The input type is inferred from context_dense_defaults[j], even when it's
      empty.  If context_dense_defaults[j] is not empty, its shape must match
      context_dense_shapes[j].
    Ncontext_sparse: An optional `int` that is `>= 0`. Defaults to `0`.
    context_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Ncontext_sparse types; the data types of data in
      each context Feature given in context_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    context_ragged_value_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      RaggedTensor.value dtypes for the ragged context features.
    context_ragged_split_types: An optional list of `tf.DTypes` from: `tf.int32, tf.int64`. Defaults to `[]`.
      RaggedTensor.row_split dtypes for the ragged context features.
    context_dense_shapes: An optional list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`). Defaults to `[]`.
      A list of Ncontext_dense shapes; the shapes of data in
      each context Feature given in context_dense_keys.
      The number of elements in the Feature corresponding to context_dense_key[j]
      must always equal context_dense_shapes[j].NumEntries().
      The shape of context_dense_values[j] will match context_dense_shapes[j].
    Nfeature_list_sparse: An optional `int` that is `>= 0`. Defaults to `0`.
    Nfeature_list_dense: An optional `int` that is `>= 0`. Defaults to `0`.
    feature_list_dense_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
    feature_list_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Nfeature_list_sparse types; the data types
      of data in each FeatureList given in feature_list_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    feature_list_ragged_value_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      RaggedTensor.value dtypes for the ragged FeatureList features.
    feature_list_ragged_split_types: An optional list of `tf.DTypes` from: `tf.int32, tf.int64`. Defaults to `[]`.
      RaggedTensor.row_split dtypes for the ragged FeatureList features.
    feature_list_dense_shapes: An optional list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`). Defaults to `[]`.
      A list of Nfeature_list_dense shapes; the shapes of
      data in each FeatureList given in feature_list_dense_keys.
      The shape of each Feature in the FeatureList corresponding to
      feature_list_dense_key[j] must always equal
      feature_list_dense_shapes[j].NumEntries().
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (context_sparse_indices, context_sparse_values, context_sparse_shapes, context_dense_values, context_ragged_values, context_ragged_row_splits, feature_list_sparse_indices, feature_list_sparse_values, feature_list_sparse_shapes, feature_list_dense_values, feature_list_dense_lengths, feature_list_ragged_values, feature_list_ragged_outer_splits, feature_list_ragged_inner_splits).

    context_sparse_indices: A list of `Ncontext_sparse` `Tensor` objects with type `int64`.
    context_sparse_values: A list of `Tensor` objects of type `context_sparse_types`.
    context_sparse_shapes: A list of `Ncontext_sparse` `Tensor` objects with type `int64`.
    context_dense_values: A list of `Tensor` objects. Has the same type as `context_dense_defaults`.
    context_ragged_values: A list of `Tensor` objects of type `context_ragged_value_types`.
    context_ragged_row_splits: A list of `Tensor` objects of type `context_ragged_split_types`.
    feature_list_sparse_indices: A list of `Nfeature_list_sparse` `Tensor` objects with type `int64`.
    feature_list_sparse_values: A list of `Tensor` objects of type `feature_list_sparse_types`.
    feature_list_sparse_shapes: A list of `Nfeature_list_sparse` `Tensor` objects with type `int64`.
    feature_list_dense_values: A list of `Tensor` objects of type `feature_list_dense_types`.
    feature_list_dense_lengths: A list of `Nfeature_list_dense` `Tensor` objects with type `int64`.
    feature_list_ragged_values: A list of `Tensor` objects of type `feature_list_ragged_value_types`.
    feature_list_ragged_outer_splits: A list of `Tensor` objects of type `feature_list_ragged_split_types`.
    feature_list_ragged_inner_splits: A list of `Tensor` objects of type `feature_list_ragged_split_types`.
  