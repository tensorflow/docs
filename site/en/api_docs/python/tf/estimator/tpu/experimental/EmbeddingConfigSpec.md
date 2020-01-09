page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.tpu.experimental.EmbeddingConfigSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/_tpu_estimator_embedding.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `EmbeddingConfigSpec`

Class to keep track of the specification for TPU embeddings.



### Aliases:

* Class <a href="/api_docs/python/tf/estimator/tpu/experimental/EmbeddingConfigSpec"><code>tf.compat.v1.estimator.tpu.experimental.EmbeddingConfigSpec</code></a>


<!-- Placeholder for "Used in" -->

Pass this class to <a href="../../../../tf/estimator/tpu/TPUEstimator"><code>tf.estimator.tpu.TPUEstimator</code></a> via the
`embedding_config_spec` parameter. At minimum you need to specify
`feature_columns` and `optimization_parameters`. The feature columns passed
should be created with some combination of
<a href="../../../../tf/tpu/experimental/embedding_column"><code>tf.tpu.experimental.embedding_column</code></a> and
<a href="../../../../tf/tpu/experimental/shared_embedding_columns"><code>tf.tpu.experimental.shared_embedding_columns</code></a>.

TPU embeddings do not support arbitrary Tensorflow optimizers and the
main optimizer you use for your model will be ignored for the embedding table
variables. Instead TPU embeddigns support a fixed set of predefined optimizers
that you can select from and set the parameters of. These include adagrad,
adam and stochastic gradient descent. Each supported optimizer has a
`Parameters` class in the <a href="../../../../tf/tpu/experimental"><code>tf.tpu.experimental</code></a> namespace.

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

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/_tpu_estimator_embedding.py">View source</a>

``` python
@staticmethod
__new__(
    cls,
    feature_columns=None,
    optimization_parameters=None,
    clipping_limit=None,
    pipeline_execution_with_tensor_core=False,
    experimental_gradient_multiplier_fn=None,
    feature_to_config_dict=None,
    table_to_config_dict=None,
    partition_strategy='div'
)
```

Creates an `EmbeddingConfigSpec` instance.


#### Args:


* <b>`feature_columns`</b>: All embedding `FeatureColumn`s used by model.
* <b>`optimization_parameters`</b>: An instance of `AdagradParameters`,
  `AdamParameters` or `StochasticGradientDescentParameters`. This
  optimizer will be applied to all embedding variables specified by
  `feature_columns`.
* <b>`clipping_limit`</b>: (Optional) Clipping limit (absolute value).
* <b>`pipeline_execution_with_tensor_core`</b>: setting this to `True` makes training
  faster, but trained model will be different if step N and step N+1
  involve the same set of embedding IDs. Please see
  `tpu_embedding_configuration.proto` for details.
* <b>`experimental_gradient_multiplier_fn`</b>: (Optional) A Fn taking global step as
  input returning the current multiplier for all embedding gradients.
* <b>`feature_to_config_dict`</b>: A dictionary mapping features names to instances
  of the class `FeatureConfig`. Either features_columns or the pair of
  `feature_to_config_dict` and `table_to_config_dict` must be specified.
* <b>`table_to_config_dict`</b>: A dictionary mapping features names to instances of
  the class `TableConfig`. Either features_columns or the pair of
  `feature_to_config_dict` and `table_to_config_dict` must be specified.
* <b>`partition_strategy`</b>: A string, determining how tensors are sharded to the
  tpu hosts. See <a href="../../../../tf/nn/safe_embedding_lookup_sparse"><code>tf.nn.safe_embedding_lookup_sparse</code></a> for more details.
  Allowed value are `"div"` and `"mod"'. If `"mod"` is used, evaluation
  and exporting the model to CPU will not work as expected.


#### Returns:

An `EmbeddingConfigSpec` instance.



#### Raises:


* <b>`ValueError`</b>: If the feature_columns are not specified.
* <b>`TypeError`</b>: If the feature columns are not of ths correct type (one of
  _SUPPORTED_FEATURE_COLUMNS, _TPU_EMBEDDING_COLUMN_CLASSES OR
  _EMBEDDING_COLUMN_CLASSES).
* <b>`ValueError`</b>: If `optimization_parameters` is not one of the required types.



## Properties

<h3 id="feature_columns"><code>feature_columns</code></h3>




<h3 id="optimization_parameters"><code>optimization_parameters</code></h3>




<h3 id="clipping_limit"><code>clipping_limit</code></h3>




<h3 id="pipeline_execution_with_tensor_core"><code>pipeline_execution_with_tensor_core</code></h3>




<h3 id="experimental_gradient_multiplier_fn"><code>experimental_gradient_multiplier_fn</code></h3>




<h3 id="feature_to_config_dict"><code>feature_to_config_dict</code></h3>




<h3 id="table_to_config_dict"><code>table_to_config_dict</code></h3>




<h3 id="partition_strategy"><code>partition_strategy</code></h3>
