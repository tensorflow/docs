description: TPU version of <a href="../../../../../tf/feature_column/embedding_column.md"><code>tf.compat.v1.feature_column.embedding_column</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.experimental.embedding_column" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.experimental.embedding_column

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/feature_column_v2.py#L54-L207">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



TPU version of <a href="../../../../../tf/feature_column/embedding_column.md"><code>tf.compat.v1.feature_column.embedding_column</code></a>.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.experimental.embedding_column(
    categorical_column, dimension, combiner='mean', initializer=None,
    max_sequence_length=0, learning_rate_fn=None, embedding_lookup_device=None,
    tensor_core_shape=None, use_safe_embedding_lookup=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that the interface for `tf.tpu.experimental.embedding_column` is
different from that of <a href="../../../../../tf/feature_column/embedding_column.md"><code>tf.compat.v1.feature_column.embedding_column</code></a>: The
following arguments are NOT supported: `ckpt_to_load_from`,
`tensor_name_in_ckpt`, `max_norm` and `trainable`.

Use this function in place of <a href="../../../../../tf/feature_column/embedding_column.md"><code>tf.compat.v1.feature_column.embedding_column</code></a>
when you want to use the TPU to accelerate your embedding lookups via TPU
embeddings.

```
column = tf.feature_column.categorical_column_with_identity(...)
tpu_column = tf.tpu.experimental.embedding_column(column, 10)
...
def model_fn(features):
  dense_feature = tf.keras.layers.DenseFeature(tpu_column)
  embedded_feature = dense_feature(features)
  ...

estimator = tf.estimator.tpu.TPUEstimator(
    model_fn=model_fn,
    ...
    embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
      column=[tpu_column],
      ...))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`categorical_column`
</td>
<td>
A categorical column returned from
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
A string specifying how to reduce if there are multiple entries
in a single row for a non-sequence column. For more information, see
<a href="../../../../../tf/feature_column/embedding_column.md"><code>tf.feature_column.embedding_column</code></a>.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
A variable initializer function to be used in embedding
variable initialization. If not specified, defaults to
<a href="../../../../../tf/compat/v1/truncated_normal_initializer.md"><code>tf.compat.v1.truncated_normal_initializer</code></a> with mean `0.0` and
standard deviation `1/sqrt(dimension)`.
</td>
</tr><tr>
<td>
`max_sequence_length`
</td>
<td>
An non-negative integer specifying the max sequence
length. Any sequence shorter then this will be padded with 0 embeddings
and any sequence longer will be truncated. This must be positive for
sequence features and 0 for non-sequence features.
</td>
</tr><tr>
<td>
`learning_rate_fn`
</td>
<td>
A function that takes global step and returns learning
rate for the embedding table. If you intend to use the same learning rate
for multiple embedding tables, please ensure that you pass the exact same
python function to all calls of embedding_column, otherwise performence
may suffer.
</td>
</tr><tr>
<td>
`embedding_lookup_device`
</td>
<td>
The device on which to run the embedding lookup.
Valid options are "cpu", "tpu_tensor_core", and "tpu_embedding_core".
If specifying "tpu_tensor_core", a tensor_core_shape must be supplied.
If not specified, the default behavior is embedding lookup on
"tpu_embedding_core" for training and "cpu" for inference.
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
If supplied, a list of integers which specifies
the intended dense shape to run embedding lookup for this feature on
TensorCore. The batch dimension can be left None or -1 to indicate
a dynamic shape. Only rank 2 shapes currently supported.
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
A  `_TPUEmbeddingColumnV2`.
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
</tr>
</table>

