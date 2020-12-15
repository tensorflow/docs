description: Returns a feature column that represents sequences of integers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column.sequence_categorical_column_with_identity" />
<meta itemprop="path" content="Stable" />
</div>

# tf.feature_column.sequence_categorical_column_with_identity

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/feature_column/sequence_feature_column.py#L90-L136">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a feature column that represents sequences of integers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.feature_column.sequence_categorical_column_with_identity`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.feature_column.sequence_categorical_column_with_identity(
    key, num_buckets, default_value=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Pass this to `embedding_column` or `indicator_column` to convert sequence
categorical data into dense representation for input to sequence NN, such as
RNN.

#### Example:



```python
watches = sequence_categorical_column_with_identity(
    'watches', num_buckets=1000)
watches_embedding = embedding_column(watches, dimension=10)
columns = [watches_embedding]

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
`num_buckets`
</td>
<td>
Range of inputs. Namely, inputs are expected to be in the
range `[0, num_buckets)`.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
If `None`, this column's graph operations will fail for
out-of-range inputs. Otherwise, this value must be in the range
`[0, num_buckets)`, and will replace out-of-range inputs.
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
if `num_buckets` is less than one.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `default_value` is not in range `[0, num_buckets)`.
</td>
</tr>
</table>

