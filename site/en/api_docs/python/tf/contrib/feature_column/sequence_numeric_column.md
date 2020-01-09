page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.feature_column.sequence_numeric_column


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py#L392-L449">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a feature column that represents sequences of numeric data.

``` python
tf.contrib.feature_column.sequence_numeric_column(
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
input_layer, sequence_length = sequence_input_layer(features, columns)

rnn_cell = tf.compat.v1.nn.rnn_cell.BasicRNNCell(hidden_size)
outputs, state = tf.compat.v1.nn.dynamic_rnn(
    rnn_cell, inputs=input_layer, sequence_length=sequence_length)
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

A `_SequenceNumericColumn`.



#### Raises:


* <b>`TypeError`</b>: if any dimension in shape is not an int.
* <b>`ValueError`</b>: if any dimension in shape is not a positive integer.
* <b>`ValueError`</b>: if `dtype` is not convertible to <a href="../../../tf#float32"><code>tf.float32</code></a>.
