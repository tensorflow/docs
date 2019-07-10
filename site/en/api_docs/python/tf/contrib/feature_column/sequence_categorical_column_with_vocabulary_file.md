page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.feature_column.sequence_categorical_column_with_vocabulary_file

A sequence of categorical terms where ids use a vocabulary file.

``` python
tf.contrib.feature_column.sequence_categorical_column_with_vocabulary_file(
    key,
    vocabulary_file,
    vocabulary_size=None,
    num_oov_buckets=0,
    default_value=None,
    dtype=tf.dtypes.string
)
```



Defined in [`contrib/feature_column/python/feature_column/sequence_feature_column.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py).

<!-- Placeholder for "Used in" -->

Pass this to `embedding_column` or `indicator_column` to convert sequence
categorical data into dense representation for input to sequence NN, such as
RNN.

#### Example:



```python
states = sequence_categorical_column_with_vocabulary_file(
    key='states', vocabulary_file='/us/states.txt', vocabulary_size=50,
    num_oov_buckets=5)
states_embedding = embedding_column(states, dimension=10)
columns = [states_embedding]

features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
input_layer, sequence_length = sequence_input_layer(features, columns)

rnn_cell = tf.compat.v1.nn.rnn_cell.BasicRNNCell(hidden_size)
outputs, state = tf.compat.v1.nn.dynamic_rnn(
    rnn_cell, inputs=input_layer, sequence_length=sequence_length)
```

#### Args:


* <b>`key`</b>: A unique string identifying the input feature.
* <b>`vocabulary_file`</b>: The vocabulary file name.
* <b>`vocabulary_size`</b>: Number of the elements in the vocabulary. This must be no
  greater than length of `vocabulary_file`, if less than length, later
  values are ignored. If None, it is set to the length of `vocabulary_file`.
* <b>`num_oov_buckets`</b>: Non-negative integer, the number of out-of-vocabulary
  buckets. All out-of-vocabulary inputs will be assigned IDs in the range
  `[vocabulary_size, vocabulary_size+num_oov_buckets)` based on a hash of
  the input value. A positive `num_oov_buckets` can not be specified with
  `default_value`.
* <b>`default_value`</b>: The integer ID value to return for out-of-vocabulary feature
  values, defaults to `-1`. This can not be specified with a positive
  `num_oov_buckets`.
* <b>`dtype`</b>: The type of features. Only string and integer types are supported.


#### Returns:

A `_SequenceCategoricalColumn`.



#### Raises:


* <b>`ValueError`</b>: `vocabulary_file` is missing or cannot be opened.
* <b>`ValueError`</b>: `vocabulary_size` is missing or < 1.
* <b>`ValueError`</b>: `num_oov_buckets` is a negative integer.
* <b>`ValueError`</b>: `num_oov_buckets` and `default_value` are both specified.
* <b>`ValueError`</b>: `dtype` is neither string nor integer.