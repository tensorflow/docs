description: A sequence of categorical terms where ids use an in-memory list.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column.sequence_categorical_column_with_vocabulary_list" />
<meta itemprop="path" content="Stable" />
</div>

# tf.feature_column.sequence_categorical_column_with_vocabulary_list

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/feature_column/sequence_feature_column.py#L250-L309">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A sequence of categorical terms where ids use an in-memory list.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.feature_column.sequence_categorical_column_with_vocabulary_list`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.feature_column.sequence_categorical_column_with_vocabulary_list(
    key, vocabulary_list, dtype=None, default_value=-1, num_oov_buckets=0
)
</code></pre>



<!-- Placeholder for "Used in" -->

Pass this to `embedding_column` or `indicator_column` to convert sequence
categorical data into dense representation for input to sequence NN, such as
RNN.

#### Example:



```python
colors = sequence_categorical_column_with_vocabulary_list(
    key='colors', vocabulary_list=('R', 'G', 'B', 'Y'),
    num_oov_buckets=2)
colors_embedding = embedding_column(colors, dimension=3)
columns = [colors_embedding]

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
A unique string identifying the input feature.
</td>
</tr><tr>
<td>
`vocabulary_list`
</td>
<td>
An ordered iterable defining the vocabulary. Each feature
is mapped to the index of its value (if present) in `vocabulary_list`.
Must be castable to `dtype`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of features. Only string and integer types are supported.
If `None`, it will be inferred from `vocabulary_list`.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
The integer ID value to return for out-of-vocabulary feature
values, defaults to `-1`. This can not be specified with a positive
`num_oov_buckets`.
</td>
</tr><tr>
<td>
`num_oov_buckets`
</td>
<td>
Non-negative integer, the number of out-of-vocabulary
buckets. All out-of-vocabulary inputs will be assigned IDs in the range
`[len(vocabulary_list), len(vocabulary_list)+num_oov_buckets)` based on a
hash of the input value. A positive `num_oov_buckets` can not be specified
with `default_value`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SequenceCategoricalColumn`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `vocabulary_list` is empty, or contains duplicate keys.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
`num_oov_buckets` is a negative integer.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
`num_oov_buckets` and `default_value` are both specified.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `dtype` is not integer or string.
</td>
</tr>
</table>

