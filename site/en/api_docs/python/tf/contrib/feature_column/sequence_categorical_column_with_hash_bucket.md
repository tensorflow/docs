page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.feature_column.sequence_categorical_column_with_hash_bucket

``` python
tf.contrib.feature_column.sequence_categorical_column_with_hash_bucket(
    key,
    hash_bucket_size,
    dtype=tf.dtypes.string
)
```



Defined in [`tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py).

A sequence of categorical terms where ids are set by hashing.

Pass this to `embedding_column` or `indicator_column` to convert sequence
categorical data into dense representation for input to sequence NN, such as
RNN.

Example:

```python
tokens = sequence_categorical_column_with_hash_bucket(
    'tokens', hash_bucket_size=1000)
tokens_embedding = embedding_column(tokens, dimension=10)
columns = [tokens_embedding]

features = tf.parse_example(..., features=make_parse_example_spec(columns))
input_layer, sequence_length = sequence_input_layer(features, columns)

rnn_cell = tf.nn.rnn_cell.BasicRNNCell(hidden_size)
outputs, state = tf.nn.dynamic_rnn(
    rnn_cell, inputs=input_layer, sequence_length=sequence_length)
```

#### Args:

* <b>`key`</b>: A unique string identifying the input feature.
* <b>`hash_bucket_size`</b>: An int > 1. The number of buckets.
* <b>`dtype`</b>: The type of features. Only string and integer types are supported.


#### Returns:

A `_SequenceCategoricalColumn`.


#### Raises:

* <b>`ValueError`</b>: `hash_bucket_size` is not greater than 1.
* <b>`ValueError`</b>: `dtype` is neither string nor integer.