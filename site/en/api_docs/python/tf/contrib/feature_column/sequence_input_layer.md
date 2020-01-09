page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.feature_column.sequence_input_layer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/feature_column/python/feature_column/sequence_feature_column.py#L39-L134">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



"Builds input layer for sequence input.

``` python
tf.contrib.feature_column.sequence_input_layer(
    features,
    feature_columns,
    weight_collections=None,
    trainable=True
)
```



<!-- Placeholder for "Used in" -->

All `feature_columns` must be sequence dense columns with the same
`sequence_length`. The output of this method can be fed into sequence
networks, such as RNN.

The output of this method is a 3D `Tensor` of shape `[batch_size, T, D]`.
`T` is the maximum sequence length for this batch, which could differ from
batch to batch.

If multiple `feature_columns` are given with `Di` `num_elements` each, their
outputs are concatenated. So, the final `Tensor` has shape
`[batch_size, T, D0 + D1 + ... + Dn]`.

#### Example:



```python
rating = sequence_numeric_column('rating')
watches = sequence_categorical_column_with_identity(
    'watches', num_buckets=1000)
watches_embedding = embedding_column(watches, dimension=10)
columns = [rating, watches]

features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
input_layer, sequence_length = sequence_input_layer(features, columns)

rnn_cell = tf.compat.v1.nn.rnn_cell.BasicRNNCell(hidden_size)
outputs, state = tf.compat.v1.nn.dynamic_rnn(
    rnn_cell, inputs=input_layer, sequence_length=sequence_length)
```

#### Args:


* <b>`features`</b>: A dict mapping keys to tensors.
* <b>`feature_columns`</b>: An iterable of dense sequence columns. Valid columns are
  - `embedding_column` that wraps a `sequence_categorical_column_with_*`
  - `sequence_numeric_column`.
* <b>`weight_collections`</b>: A list of collection names to which the Variable will be
  added. Note that variables will also be added to collections
  <a href="../../../tf/GraphKeys#GLOBAL_VARIABLES"><code>tf.GraphKeys.GLOBAL_VARIABLES</code></a> and `ops.GraphKeys.MODEL_VARIABLES`.
* <b>`trainable`</b>: If `True` also add the variable to the graph collection
  <a href="/api_docs/python/tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a>.


#### Returns:

An `(input_layer, sequence_length)` tuple where:
- input_layer: A float `Tensor` of shape `[batch_size, T, D]`.
    `T` is the maximum sequence length for this batch, which could differ
    from batch to batch. `D` is the sum of `num_elements` for all
    `feature_columns`.
- sequence_length: An int `Tensor` of shape `[batch_size]`. The sequence
    length for each example.



#### Raises:


* <b>`ValueError`</b>: If any of the `feature_columns` is the wrong type.
