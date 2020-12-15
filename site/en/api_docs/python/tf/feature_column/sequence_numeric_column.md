description: Returns a feature column that represents sequences of numeric data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column.sequence_numeric_column" />
<meta itemprop="path" content="Stable" />
</div>

# tf.feature_column.sequence_numeric_column

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/feature_column/sequence_feature_column.py#L312-L372">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a feature column that represents sequences of numeric data.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.feature_column.sequence_numeric_column`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.feature_column.sequence_numeric_column(
    key, shape=(1,), default_value=0.0, dtype=tf.dtypes.float32, normalizer_fn=None
)
</code></pre>



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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`key`
</td>
<td>
A unique string identifying the input features.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
The shape of the input data per sequence id. E.g. if `shape=(2,)`,
each example must contain `2 * sequence_length` values.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
A single value compatible with `dtype` that is used for
padding the sparse data into a dense `Tensor`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of values.
</td>
</tr><tr>
<td>
`normalizer_fn`
</td>
<td>
If not `None`, a function that can be used to normalize the
value of the tensor after `default_value` is applied for parsing.
Normalizer function takes the input `Tensor` as its argument, and returns
the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that
even though the most common use case of this function is normalization, it
can be used for any kind of Tensorflow transformations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SequenceNumericColumn`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if any dimension in shape is not an int.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if any dimension in shape is not a positive integer.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `dtype` is not convertible to <a href="../../tf.md#float32"><code>tf.float32</code></a>.
</td>
</tr>
</table>

