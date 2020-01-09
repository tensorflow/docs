page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.feature_column.sequence_numeric_column


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/feature_column/sequence_feature_column.py#L424-L484">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a feature column that represents sequences of numeric data.

### Aliases:

* `tf.compat.v1.feature_column.sequence_numeric_column`
* `tf.compat.v2.feature_column.sequence_numeric_column`


``` python
tf.feature_column.sequence_numeric_column(
    key,
    shape=(1,),
    default_value=0.0,
    dtype=tf.dtypes.float32,
    normalizer_fn=None
)
```



<!-- Placeholder for "Used in" -->


#### Example:



```python
temperature = sequence_numeric_column('temperature')
columns = [temperature]

features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
sequence_feature_layer = SequenceFeatures(columns)
sequence_input, sequence_length = sequence_feature_layer(features)
sequence_length_mask = tf.sequence_mask(sequence_length)

rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
rnn_layer = tf.keras.layers.RNN(rnn_cell)
outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)
```

#### Args:


* <b>`key`</b>: A unique string identifying the input features.
* <b>`shape`</b>: The shape of the input data per sequence id. E.g. if `shape=(2,)`,
  each example must contain `2 * sequence_length` values.
* <b>`default_value`</b>: A single value compatible with `dtype` that is used for
  padding the sparse data into a dense `Tensor`.
* <b>`dtype`</b>: The type of values.
* <b>`normalizer_fn`</b>: If not `None`, a function that can be used to normalize the
  value of the tensor after `default_value` is applied for parsing.
  Normalizer function takes the input `Tensor` as its argument, and returns
  the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that
  even though the most common use case of this function is normalization, it
  can be used for any kind of Tensorflow transformations.


#### Returns:

A `SequenceNumericColumn`.



#### Raises:


* <b>`TypeError`</b>: if any dimension in shape is not an int.
* <b>`ValueError`</b>: if any dimension in shape is not a positive integer.
* <b>`ValueError`</b>: if `dtype` is not convertible to <a href="../../tf#float32"><code>tf.float32</code></a>.
