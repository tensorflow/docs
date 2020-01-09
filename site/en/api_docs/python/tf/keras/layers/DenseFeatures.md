page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.DenseFeatures


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/feature_column/dense_features_v2.py#L28-L93">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `DenseFeatures`

A layer that produces a dense `Tensor` based on given `feature_columns`.

Inherits From: [`DenseFeatures`](../../../tf/compat/v1/keras/layers/DenseFeatures)

### Aliases:

* Class `tf.compat.v2.keras.layers.DenseFeatures`


### Used in the tutorials:

* [Boosted trees using Estimators](https://www.tensorflow.org/tutorials/estimator/boosted_trees)
* [Build a linear model with Estimators](https://www.tensorflow.org/tutorials/estimator/linear)
* [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)
* [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)



Generally a single example in training data is described with FeatureColumns.
At the first layer of the model, this column oriented data should be converted
to a single `Tensor`.

This layer can be called multiple times with different features.

This is the V2 version of this layer that uses name_scopes to create
variables instead of variable_scopes. But this approach currently lacks
support for partitioned variables. In that case, use the V1 version instead.

#### Example:



```python
price = numeric_column('price')
keywords_embedded = embedding_column(
    categorical_column_with_hash_bucket("keywords", 10K), dimensions=16)
columns = [price, keywords_embedded, ...]
feature_layer = DenseFeatures(columns)

features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = feature_layer(features)
for units in [128, 64, 32]:
  dense_tensor = tf.keras.layers.Dense(units, activation='relu')(dense_tensor)
prediction = tf.keras.layers.Dense(1)(dense_tensor)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/feature_column/dense_features_v2.py#L58-L85">View source</a>

``` python
__init__(
    feature_columns,
    trainable=True,
    name=None,
    **kwargs
)
```

Creates a DenseFeatures object.


#### Args:


* <b>`feature_columns`</b>: An iterable containing the FeatureColumns to use as
  inputs to your model. All items should be instances of classes derived
  from `DenseColumn` such as `numeric_column`, `embedding_column`,
  `bucketized_column`, `indicator_column`. If you have categorical
  features, you can wrap them with an `embedding_column` or
  `indicator_column`.
* <b>`trainable`</b>:  Boolean, whether the layer's variables will be updated via
  gradient descent during training.
* <b>`name`</b>: Name to give to the DenseFeatures.
* <b>`**kwargs`</b>: Keyword arguments to construct a layer.


#### Raises:


* <b>`ValueError`</b>: if an item in `feature_columns` is not a `DenseColumn`.
