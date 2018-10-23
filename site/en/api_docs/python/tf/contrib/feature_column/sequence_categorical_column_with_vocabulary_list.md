

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.feature_column.sequence_categorical_column_with_vocabulary_list

``` python
tf.contrib.feature_column.sequence_categorical_column_with_vocabulary_list(
    key,
    vocabulary_list,
    dtype=None,
    default_value=-1,
    num_oov_buckets=0
)
```



Defined in [`tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py).

A sequence of categorical terms where ids use an in-memory list.

Pass this to `embedding_column` or `indicator_column` to convert sequence
categorical data into dense representation for input to sequence NN, such as
RNN.

Example:

```python
colors = sequence_categorical_column_with_vocabulary_list(
    key='colors', vocabulary_list=('R', 'G', 'B', 'Y'),
    num_oov_buckets=2)
colors_embedding = embedding_column(colors, dimension=3)
columns = [colors_embedding]

features = tf.parse_example(..., features=make_parse_example_spec(columns))
input_layer, sequence_length = sequence_input_layer(features, columns)

rnn_cell = tf.nn.rnn_cell.BasicRNNCell(hidden_size)
outputs, state = tf.nn.dynamic_rnn(
    rnn_cell, inputs=input_layer, sequence_length=sequence_length)
```

#### Args:

* <b>`key`</b>: A unique string identifying the input feature.
* <b>`vocabulary_list`</b>: An ordered iterable defining the vocabulary. Each feature
    is mapped to the index of its value (if present) in `vocabulary_list`.
    Must be castable to `dtype`.
* <b>`dtype`</b>: The type of features. Only string and integer types are supported.
    If `None`, it will be inferred from `vocabulary_list`.
* <b>`default_value`</b>: The integer ID value to return for out-of-vocabulary feature
    values, defaults to `-1`. This can not be specified with a positive
    `num_oov_buckets`.
* <b>`num_oov_buckets`</b>: Non-negative integer, the number of out-of-vocabulary
    buckets. All out-of-vocabulary inputs will be assigned IDs in the range
    `[len(vocabulary_list), len(vocabulary_list)+num_oov_buckets)` based on a
    hash of the input value. A positive `num_oov_buckets` can not be specified
    with `default_value`.


#### Returns:

A `_SequenceCategoricalColumn`.


#### Raises:

* <b>`ValueError`</b>: if `vocabulary_list` is empty, or contains duplicate keys.
* <b>`ValueError`</b>: `num_oov_buckets` is a negative integer.
* <b>`ValueError`</b>: `num_oov_buckets` and `default_value` are both specified.
* <b>`ValueError`</b>: if `dtype` is not integer or string.