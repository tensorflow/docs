description: Configuration data for one embedding feature.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.embedding.FeatureConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.tpu.experimental.embedding.FeatureConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L547-L618">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration data for one embedding feature.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.embedding.FeatureConfig`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.embedding.FeatureConfig(
    table, max_sequence_length=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class holds the configuration data for a single embedding feature. The
main use is to assign features to <a href="../../../../tf/tpu/experimental/embedding/TableConfig.md"><code>tf.tpu.experimental.embedding.TableConfig</code></a>s
via the table parameter:

```python
table_config_one = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...)
table_config_two = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...)
feature_config = {
    'feature_one': tf.tpu.experimental.embedding.FeatureConfig(
        table=table_config_one),
    'feature_two': tf.tpu.experimental.embedding.FeatureConfig(
        table=table_config_one),
    'feature_three': tf.tpu.experimental.embedding.FeatureConfig(
        table=table_config_two)}
embedding = tf.tpu.experimental.embedding.TPUEmbedding(
    feature_config=feature_config,
    batch_size=...
    optimizer=tf.tpu.experimental.embedding.Adam(0.1))
```

The above configuration has 2 tables, and three features. The first two
features will be looked up in the first table and the third feature will be
looked up in the second table.

When feeding features into `embedding.enqueue` they can be <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a>s,
<a href="../../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>s or <a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s. When the argument
`max_sequence_length` is 0, the default, you should expect a output of
`embedding.dequeue` for this feature of shape `(batch_size, dim)`. If
`max_sequence_length` is greater than 0, the feature is embedded as a sequence
and padded up to the given length. The shape of the output for this feature
will be `(batch_size, max_sequence_length, dim)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`table`
</td>
<td>
An instance of <a href="../../../../tf/tpu/experimental/embedding/TableConfig.md"><code>tf.tpu.experimental.embedding.TableConfig</code></a>,
describing the table in which this feature should be looked up.
</td>
</tr><tr>
<td>
`max_sequence_length`
</td>
<td>
If positive, the feature is a sequence feature with
the corresponding maximum sequence length. If the sequence is longer
than this, it will be truncated. If 0, the feature is not a sequence
feature.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
An optional name for the feature, useful for debugging.
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
if `table` is not an instance of
<a href="../../../../tf/tpu/experimental/embedding/TableConfig.md"><code>tf.tpu.experimental.embedding.TableConfig</code></a>.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `max_sequence_length` not an integer or is negative.
</td>
</tr>
</table>



