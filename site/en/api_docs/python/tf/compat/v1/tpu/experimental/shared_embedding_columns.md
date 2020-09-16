description: TPU version of <a href="../../../../../tf/compat/v1/feature_column/shared_embedding_columns.md"><code>tf.compat.v1.feature_column.shared_embedding_columns</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.experimental.shared_embedding_columns" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.experimental.shared_embedding_columns

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/tpu/feature_column_v2.py#L201-L401">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



TPU version of <a href="../../../../../tf/compat/v1/feature_column/shared_embedding_columns.md"><code>tf.compat.v1.feature_column.shared_embedding_columns</code></a>.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.experimental.shared_embedding_columns(
    categorical_columns, dimension, combiner='mean', initializer=None,
    shared_embedding_collection_name=None, max_sequence_lengths=None,
    learning_rate_fn=None, embedding_lookup_device=None, tensor_core_shape=None,
    use_safe_embedding_lookup=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that the interface for `tf.tpu.experimental.shared_embedding_columns` is
different from that of <a href="../../../../../tf/compat/v1/feature_column/shared_embedding_columns.md"><code>tf.compat.v1.feature_column.shared_embedding_columns</code></a>:
The following arguments are NOT supported: `ckpt_to_load_from`,
`tensor_name_in_ckpt`, `max_norm` and `trainable`.

Use this function in place of
tf.compat.v1.feature_column.shared_embedding_columns` when you want to use the
TPU to accelerate your embedding lookups via TPU embeddings.

```
column_a = tf.feature_column.categorical_column_with_identity(...)
column_b = tf.feature_column.categorical_column_with_identity(...)
tpu_columns = tf.tpu.experimental.shared_embedding_columns(
    [column_a, column_b], 10)
...
def model_fn(features):
  dense_feature = tf.keras.layers.DenseFeature(tpu_columns)
  embedded_feature = dense_feature(features)
  ...

estimator = tf.estimator.tpu.TPUEstimator(
    model_fn=model_fn,
    ...
    embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
        column=tpu_columns,
        ...))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`categorical_columns`
</td>
<td>
A list of categorical columns returned from
`categorical_column_with_identity`, `weighted_categorical_column`,
`categorical_column_with_vocabulary_file`,
`categorical_column_with_vocabulary_list`,
`sequence_categorical_column_with_identity`,
`sequence_categorical_column_with_vocabulary_file`,
`sequence_categorical_column_with_vocabulary_list`
</td>
</tr><tr>
<td>
`dimension`
</td>
<td>
An integer specifying dimension of the embedding, must be > 0.
</td>
</tr><tr>
<td>
`combiner`
</td>
<td>
A string specifying how to reduce if there are multiple entries in
a single row for a non-sequence column. For more information, see
<a href="../../../../../tf/feature_column/embedding_column.md"><code>tf.feature_column.embedding_column</code></a>.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
A variable initializer function to be used in embedding
variable initialization. If not specified, defaults to
`tf.truncated_normal_initializer` with mean `0.0` and standard deviation
`1/sqrt(dimension)`.
</td>
</tr><tr>
<td>
`shared_embedding_collection_name`
</td>
<td>
Optional name of the collection where
shared embedding weights are added. If not given, a reasonable name will
be chosen based on the names of `categorical_columns`. This is also used
in `variable_scope` when creating shared embedding weights.
</td>
</tr><tr>
<td>
`max_sequence_lengths`
</td>
<td>
An list of non-negative integers, either None or empty
or the same length as the argument categorical_columns. Entries
corresponding to non-sequence columns must be 0 and entries corresponding
to sequence columns specify the max sequence length for the column. Any
sequence shorter then this will be padded with 0 embeddings and any
sequence longer will be truncated.
</td>
</tr><tr>
<td>
`learning_rate_fn`
</td>
<td>
A function that takes global step and returns learning
rate for the embedding table.
</td>
</tr><tr>
<td>
`embedding_lookup_device`
</td>
<td>
The device on which to run the embedding lookup.
Valid options are "cpu", "tpu_tensor_core", and "tpu_embedding_core". If
specifying "tpu_tensor_core", a tensor_core_shape must be supplied.
Defaults to "cpu". If not specified, the default behavior is embedding
lookup on "tpu_embedding_core" for training and "cpu" for inference.
Valid options for training : ["tpu_embedding_core", "tpu_tensor_core"]
Valid options for serving :  ["cpu", "tpu_tensor_core"]
For training, tpu_embedding_core is good for large embedding vocab (>1M),
otherwise, tpu_tensor_core is often sufficient.
For serving, doing embedding lookup on tpu_tensor_core during serving is
a way to reduce host cpu usage in cases where that is a bottleneck.
</td>
</tr><tr>
<td>
`tensor_core_shape`
</td>
<td>
If supplied, a list of integers which specifies the
intended dense shape to run embedding lookup for this feature on
TensorCore. The batch dimension can be left None or -1 to indicate a
dynamic shape. Only rank 2 shapes currently supported.
</td>
</tr><tr>
<td>
`use_safe_embedding_lookup`
</td>
<td>
If true, uses safe_embedding_lookup_sparse
instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
there are no empty rows and all weights and ids are positive at the
expense of extra compute cost. This only applies to rank 2 (NxM) shaped
input tensors. Defaults to true, consider turning off if the above checks
are not needed. Note that having empty rows will not trigger any error
though the output result might be 0 or omitted.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A  list of `_TPUSharedEmbeddingColumnV2`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `dimension` not > 0.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `initializer` is specified but not callable.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `max_sequence_lengths` is specified and not the same length
as `categorical_columns`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `max_sequence_lengths` is positive for a non sequence column
or 0 for a sequence column.
</td>
</tr>
</table>

