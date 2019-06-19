page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.feature_column.sequence_numeric_column

``` python
tf.contrib.feature_column.sequence_numeric_column(
    key,
    shape=(1,),
    default_value=0.0,
    dtype=tf.float32
)
```



Defined in [`tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py).

Returns a feature column that represents sequences of numeric data.

Example:

```python
temperature = sequence_numeric_column('temperature')
columns = [temperature]

features = tf.parse_example(..., features=make_parse_example_spec(columns))
input_layer, sequence_length = sequence_input_layer(features, columns)

rnn_cell = tf.nn.rnn_cell.BasicRNNCell(hidden_size)
outputs, state = tf.nn.dynamic_rnn(
    rnn_cell, inputs=input_layer, sequence_length=sequence_length)
```

#### Args:

* <b>`key`</b>: A unique string identifying the input features.
* <b>`shape`</b>: The shape of the input data per sequence id. E.g. if `shape=(2,)`,
    each example must contain `2 * sequence_length` values.
* <b>`default_value`</b>: A single value compatible with `dtype` that is used for
    padding the sparse data into a dense `Tensor`.
* <b>`dtype`</b>: The type of values.


#### Returns:

A `_SequenceNumericColumn`.


#### Raises:

* <b>`TypeError`</b>: if any dimension in shape is not an int.
* <b>`ValueError`</b>: if any dimension in shape is not a positive integer.
* <b>`ValueError`</b>: if `dtype` is not convertible to <a href="../../../tf/float32"><code>tf.float32</code></a>.