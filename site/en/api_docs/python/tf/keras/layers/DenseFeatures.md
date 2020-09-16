description: A layer that produces a dense Tensor based on given feature_columns.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.DenseFeatures" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.DenseFeatures

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/feature_column/dense_features_v2.py#L28-L95">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A layer that produces a dense `Tensor` based on given `feature_columns`.

Inherits From: [`DenseFeatures`](../../../tf/compat/v1/keras/layers/DenseFeatures.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.DenseFeatures(
    feature_columns, trainable=(True), name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Generally a single example in training data is described with FeatureColumns.
At the first layer of the model, this column oriented data should be converted
to a single `Tensor`.

This layer can be called multiple times with different features.

This is the V2 version of this layer that uses name_scopes to create
variables instead of variable_scopes. But this approach currently lacks
support for partitioned variables. In that case, use the V1 version instead.

#### Example:



```python
price = tf.feature_column.numeric_column('price')
keywords_embedded = tf.feature_column.embedding_column(
    tf.feature_column.categorical_column_with_hash_bucket("keywords", 10K),
    dimensions=16)
columns = [price, keywords_embedded, ...]
feature_layer = tf.keras.layers.DenseFeatures(columns)

features = tf.io.parse_example(
    ..., features=tf.feature_column.make_parse_example_spec(columns))
dense_tensor = feature_layer(features)
for units in [128, 64, 32]:
  dense_tensor = tf.keras.layers.Dense(units, activation='relu')(dense_tensor)
prediction = tf.keras.layers.Dense(1)(dense_tensor)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`feature_columns`
</td>
<td>
An iterable containing the FeatureColumns to use as
inputs to your model. All items should be instances of classes derived
from `DenseColumn` such as `numeric_column`, `embedding_column`,
`bucketized_column`, `indicator_column`. If you have categorical
features, you can wrap them with an `embedding_column` or
`indicator_column`.
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, whether the layer's variables will be updated via
gradient descent during training.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name to give to the DenseFeatures.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments to construct a layer.
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
if an item in `feature_columns` is not a `DenseColumn`.
</td>
</tr>
</table>



