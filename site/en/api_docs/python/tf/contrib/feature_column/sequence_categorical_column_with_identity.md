page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.feature_column.sequence_categorical_column_with_identity

``` python
tf.contrib.feature_column.sequence_categorical_column_with_identity(
    key,
    num_buckets,
    default_value=None
)
```



Defined in [`tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py).

Returns a feature column that represents sequences of integers.

Pass this to `embedding_column` or `indicator_column` to convert sequence
categorical data into dense representation for input to sequence NN, such as
RNN.

Example:

```python
watches = sequence_categorical_column_with_identity(
    'watches', num_buckets=1000)
watches_embedding = embedding_column(watches, dimension=10)
columns = [watches_embedding]

features = tf.parse_example(..., features=make_parse_example_spec(columns))
input_layer, sequence_length = sequence_input_layer(features, columns)

rnn_cell = tf.nn.rnn_cell.BasicRNNCell(hidden_size)
outputs, state = tf.nn.dynamic_rnn(
    rnn_cell, inputs=input_layer, sequence_length=sequence_length)
```

#### Args:

* <b>`key`</b>: A unique string identifying the input feature.
* <b>`num_buckets`</b>: Range of inputs. Namely, inputs are expected to be in the
    range `[0, num_buckets)`.
* <b>`default_value`</b>: If `None`, this column's graph operations will fail for
    out-of-range inputs. Otherwise, this value must be in the range
    `[0, num_buckets)`, and will replace out-of-range inputs.


#### Returns:

A `_SequenceCategoricalColumn`.


#### Raises:

* <b>`ValueError`</b>: if `num_buckets` is less than one.
* <b>`ValueError`</b>: if `default_value` is not in range `[0, num_buckets)`.