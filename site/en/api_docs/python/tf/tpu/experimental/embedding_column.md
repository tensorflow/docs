page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.experimental.embedding_column


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/feature_column_v2.py#L35-L125">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



TPU version of <a href="../../../tf/feature_column/embedding_column"><code>tf.compat.v1.feature_column.embedding_column</code></a>.

### Aliases:

* <a href="/api_docs/python/tf/tpu/experimental/embedding_column"><code>tf.compat.v1.tpu.experimental.embedding_column</code></a>


``` python
tf.tpu.experimental.embedding_column(
    categorical_column,
    dimension,
    combiner='mean',
    initializer=None,
    max_sequence_length=0,
    learning_rate_fn=None
)
```



<!-- Placeholder for "Used in" -->

Note that the interface for <a href="../../../tf/tpu/experimental/embedding_column"><code>tf.tpu.experimental.embedding_column</code></a> is
different from that of <a href="../../../tf/feature_column/embedding_column"><code>tf.compat.v1.feature_column.embedding_column</code></a>: The
following arguments are NOT supported: `ckpt_to_load_from`,
`tensor_name_in_ckpt`, `max_norm` and `trainable`.

Use this function in place of <a href="../../../tf/feature_column/embedding_column"><code>tf.compat.v1.feature_column.embedding_column</code></a>
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

#### Args:


* <b>`categorical_column`</b>: A categorical column returned from
    `categorical_column_with_identity`, `weighted_categorical_column`,
    `categorical_column_with_vocabulary_file`,
    `categorical_column_with_vocabulary_list`,
    `sequence_categorical_column_with_identity`,
    `sequence_categorical_column_with_vocabulary_file`,
    `sequence_categorical_column_with_vocabulary_list`
* <b>`dimension`</b>: An integer specifying dimension of the embedding, must be > 0.
* <b>`combiner`</b>: A string specifying how to reduce if there are multiple entries
  in a single row for a non-sequence column. For more information, see
  <a href="../../../tf/feature_column/embedding_column"><code>tf.feature_column.embedding_column</code></a>.
* <b>`initializer`</b>: A variable initializer function to be used in embedding
  variable initialization. If not specified, defaults to
  <a href="../../../tf/initializers/truncated_normal"><code>tf.compat.v1.truncated_normal_initializer</code></a> with mean `0.0` and
  standard deviation `1/sqrt(dimension)`.
* <b>`max_sequence_length`</b>: An non-negative integer specifying the max sequence
  length. Any sequence shorter then this will be padded with 0 embeddings
  and any sequence longer will be truncated. This must be positive for
  sequence features and 0 for non-sequence features.
* <b>`learning_rate_fn`</b>: A function that takes global step and returns learning
  rate for the embedding table.


#### Returns:

A  `_TPUEmbeddingColumnV2`.



#### Raises:


* <b>`ValueError`</b>: if `dimension` not > 0.
* <b>`ValueError`</b>: if `initializer` is specified but not callable.
