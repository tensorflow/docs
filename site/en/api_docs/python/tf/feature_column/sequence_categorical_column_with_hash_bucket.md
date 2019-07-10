page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.feature_column.sequence_categorical_column_with_hash_bucket

A sequence of categorical terms where ids are set by hashing.

### Aliases:

* `tf.compat.v1.feature_column.sequence_categorical_column_with_hash_bucket`
* `tf.compat.v2.feature_column.sequence_categorical_column_with_hash_bucket`
* `tf.feature_column.sequence_categorical_column_with_hash_bucket`

``` python
tf.feature_column.sequence_categorical_column_with_hash_bucket(
    key,
    hash_bucket_size,
    dtype=tf.dtypes.string
)
```



Defined in [`python/feature_column/sequence_feature_column.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/feature_column/sequence_feature_column.py).

<!-- Placeholder for "Used in" -->

Pass this to `embedding_column` or `indicator_column` to convert sequence
categorical data into dense representation for input to sequence NN, such as
RNN.

#### Example:



```python
tokens = sequence_categorical_column_with_hash_bucket(
    'tokens', hash_bucket_size=1000)
tokens_embedding = embedding_column(tokens, dimension=10)
columns = [tokens_embedding]

features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
sequence_feature_layer = SequenceFeatures(columns)
sequence_input, sequence_length = sequence_feature_layer(features)
sequence_length_mask = tf.sequence_mask(sequence_length)

rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
rnn_layer = tf.keras.layers.RNN(rnn_cell)
outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)
```

#### Args:


* <b>`key`</b>: A unique string identifying the input feature.
* <b>`hash_bucket_size`</b>: An int > 1. The number of buckets.
* <b>`dtype`</b>: The type of features. Only string and integer types are supported.


#### Returns:

A `SequenceCategoricalColumn`.



#### Raises:


* <b>`ValueError`</b>: `hash_bucket_size` is not greater than 1.
* <b>`ValueError`</b>: `dtype` is neither string nor integer.