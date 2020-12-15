description: Class to keep track of the specification for TPU embeddings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.tpu.experimental.EmbeddingConfigSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="clipping_limit"/>
<meta itemprop="property" content="experimental_gradient_multiplier_fn"/>
<meta itemprop="property" content="feature_columns"/>
<meta itemprop="property" content="feature_to_config_dict"/>
<meta itemprop="property" content="optimization_parameters"/>
<meta itemprop="property" content="partition_strategy"/>
<meta itemprop="property" content="pipeline_execution_with_tensor_core"/>
<meta itemprop="property" content="table_to_config_dict"/>
<meta itemprop="property" content="tensor_core_feature_columns"/>
</div>

# tf.compat.v1.estimator.tpu.experimental.EmbeddingConfigSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/_tpu_estimator_embedding.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Class to keep track of the specification for TPU embeddings.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.tpu.experimental.EmbeddingConfigSpec(
    feature_columns=None, optimization_parameters=None, clipping_limit=None,
    pipeline_execution_with_tensor_core=(False),
    experimental_gradient_multiplier_fn=None, feature_to_config_dict=None,
    table_to_config_dict=None, partition_strategy='div'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Pass this class to `tf.estimator.tpu.TPUEstimator` via the
`embedding_config_spec` parameter. At minimum you need to specify
`feature_columns` and `optimization_parameters`. The feature columns passed
should be created with some combination of
`tf.tpu.experimental.embedding_column` and
`tf.tpu.experimental.shared_embedding_columns`.

TPU embeddings do not support arbitrary Tensorflow optimizers and the
main optimizer you use for your model will be ignored for the embedding table
variables. Instead TPU embeddigns support a fixed set of predefined optimizers
that you can select from and set the parameters of. These include adagrad,
adam and stochastic gradient descent. Each supported optimizer has a
`Parameters` class in the <a href="../../../../../../tf/tpu/experimental.md"><code>tf.tpu.experimental</code></a> namespace.

```
column_a = tf.feature_column.categorical_column_with_identity(...)
column_b = tf.feature_column.categorical_column_with_identity(...)
column_c = tf.feature_column.categorical_column_with_identity(...)
tpu_shared_columns = tf.tpu.experimental.shared_embedding_columns(
    [column_a, column_b], 10)
tpu_non_shared_column = tf.tpu.experimental.embedding_column(
    column_c, 10)
tpu_columns = [tpu_non_shared_column] + tpu_shared_columns
...
def model_fn(features):
  dense_features = tf.keras.layers.DenseFeature(tpu_columns)
  embedded_feature = dense_features(features)
  ...

estimator = tf.estimator.tpu.TPUEstimator(
    model_fn=model_fn,
    ...
    embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
        column=tpu_columns,
        optimization_parameters=(
            tf.estimator.tpu.experimental.AdagradParameters(0.1))))

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`feature_columns`
</td>
<td>
All embedding `FeatureColumn`s used by model.
</td>
</tr><tr>
<td>
`optimization_parameters`
</td>
<td>
An instance of `AdagradParameters`,
`AdamParameters` or `StochasticGradientDescentParameters`. This
optimizer will be applied to all embedding variables specified by
`feature_columns`.
</td>
</tr><tr>
<td>
`clipping_limit`
</td>
<td>
(Optional) Clipping limit (absolute value).
</td>
</tr><tr>
<td>
`pipeline_execution_with_tensor_core`
</td>
<td>
setting this to `True` makes training
faster, but trained model will be different if step N and step N+1
involve the same set of embedding IDs. Please see
`tpu_embedding_configuration.proto` for details.
</td>
</tr><tr>
<td>
`experimental_gradient_multiplier_fn`
</td>
<td>
(Optional) A Fn taking global step as
input returning the current multiplier for all embedding gradients.
</td>
</tr><tr>
<td>
`feature_to_config_dict`
</td>
<td>
A dictionary mapping features names to instances
of the class `FeatureConfig`. Either features_columns or the pair of
`feature_to_config_dict` and `table_to_config_dict` must be specified.
</td>
</tr><tr>
<td>
`table_to_config_dict`
</td>
<td>
A dictionary mapping features names to instances of
the class `TableConfig`. Either features_columns or the pair of
`feature_to_config_dict` and `table_to_config_dict` must be specified.
</td>
</tr><tr>
<td>
`partition_strategy`
</td>
<td>
A string, determining how tensors are sharded to the
tpu hosts. See <a href="../../../../../../tf/nn/safe_embedding_lookup_sparse.md"><code>tf.nn.safe_embedding_lookup_sparse</code></a> for more details.
Allowed value are `"div"` and `"mod"'. If `"mod"` is used, evaluation
and exporting the model to CPU will not work as expected.
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
If the feature_columns are not specified.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If the feature columns are not of ths correct type (one of
_SUPPORTED_FEATURE_COLUMNS, _TPU_EMBEDDING_COLUMN_CLASSES OR
_EMBEDDING_COLUMN_CLASSES).
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `optimization_parameters` is not one of the required types.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`feature_columns`
</td>
<td>

</td>
</tr><tr>
<td>
`tensor_core_feature_columns`
</td>
<td>

</td>
</tr><tr>
<td>
`optimization_parameters`
</td>
<td>

</td>
</tr><tr>
<td>
`clipping_limit`
</td>
<td>

</td>
</tr><tr>
<td>
`pipeline_execution_with_tensor_core`
</td>
<td>

</td>
</tr><tr>
<td>
`experimental_gradient_multiplier_fn`
</td>
<td>

</td>
</tr><tr>
<td>
`feature_to_config_dict`
</td>
<td>

</td>
</tr><tr>
<td>
`table_to_config_dict`
</td>
<td>

</td>
</tr><tr>
<td>
`partition_strategy`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `clipping_limit` <a id="clipping_limit"></a>
* `experimental_gradient_multiplier_fn` <a id="experimental_gradient_multiplier_fn"></a>
* `feature_columns` <a id="feature_columns"></a>
* `feature_to_config_dict` <a id="feature_to_config_dict"></a>
* `optimization_parameters` <a id="optimization_parameters"></a>
* `partition_strategy` <a id="partition_strategy"></a>
* `pipeline_execution_with_tensor_core` <a id="pipeline_execution_with_tensor_core"></a>
* `table_to_config_dict` <a id="table_to_config_dict"></a>
* `tensor_core_feature_columns` <a id="tensor_core_feature_columns"></a>
