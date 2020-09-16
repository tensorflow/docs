description: Configuration data for one embedding table.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.embedding.TableConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.tpu.experimental.embedding.TableConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L454-L543">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration data for one embedding table.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.embedding.TableConfig`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size, dim, initializer, optimizer=None, combiner='mean', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class holds the configuration data for a single embedding table. It is
used as the `table` parameter of a
<a href="../../../../tf/tpu/experimental/embedding/FeatureConfig.md"><code>tf.tpu.experimental.embedding.FeatureConfig</code></a>. Multiple
<a href="../../../../tf/tpu/experimental/embedding/FeatureConfig.md"><code>tf.tpu.experimental.embedding.FeatureConfig</code></a> objects can use the same
<a href="../../../../tf/tpu/experimental/embedding/TableConfig.md"><code>tf.tpu.experimental.embedding.TableConfig</code></a> object. In this case a shared
table will be created for those feature lookups.

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`vocabulary_size`
</td>
<td>
Size of the table's vocabulary (number of rows).
</td>
</tr><tr>
<td>
`dim`
</td>
<td>
The embedding dimension (width) of the table.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
A callable initializer taking one parameter, the shape of the
variable that will be initialized. Will be called once per task, to
initialize that task's shard of the embedding table. If not specified,
defaults to `truncated_normal_initializer` with mean `0.0` and standard
deviation `1/sqrt(dim)`.
</td>
</tr><tr>
<td>
`optimizer`
</td>
<td>
An optional instance of an optimizer parameters class, instance
of one of <a href="../../../../tf/tpu/experimental/embedding/SGD.md"><code>tf.tpu.experimental.embedding.SGD</code></a>,
<a href="../../../../tf/tpu/experimental/embedding/Adagrad.md"><code>tf.tpu.experimental.embedding.Adagrad</code></a> or
<a href="../../../../tf/tpu/experimental/embedding/Adam.md"><code>tf.tpu.experimental.embedding.Adam</code></a>. It set will override the global
optimizer passed to <a href="../../../../tf/tpu/experimental/embedding/TPUEmbedding.md"><code>tf.tpu.experimental.embedding.TPUEmbedding</code></a>.
</td>
</tr><tr>
<td>
`combiner`
</td>
<td>
A string specifying how to reduce if there are multiple entries
in a single row. Currently 'mean', 'sqrtn', 'sum' are
supported, with 'mean' the default. 'sqrtn' often achieves good
accuracy, in particular with bag-of-words columns. For more information,
see <a href="../../../../tf/nn/embedding_lookup_sparse.md"><code>tf.nn.embedding_lookup_sparse</code></a>.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
An optional string used to name the table. Useful for debugging.
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
if `vocabulary_size` is not a positive integer.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `dim` is not a positive integer.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `initializer` is specified and is not callable.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `combiner` is not supported.
</td>
</tr>
</table>



