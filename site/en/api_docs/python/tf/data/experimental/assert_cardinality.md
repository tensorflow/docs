description: Asserts the cardinality of the input dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.assert_cardinality" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.assert_cardinality

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/cardinality.py#L71-L100">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Asserts the cardinality of the input dataset.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.assert_cardinality`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.assert_cardinality(
    expected_cardinality
)
</code></pre>



<!-- Placeholder for "Used in" -->

NOTE: The following assumes that "examples.tfrecord" contains 42 records.

```
>>> dataset = tf.data.TFRecordDataset("examples.tfrecord")
>>> cardinality = tf.data.experimental.cardinality(dataset)
>>> print((cardinality == tf.data.experimental.UNKNOWN_CARDINALITY).numpy())
True
>>> dataset = dataset.apply(tf.data.experimental.assert_cardinality(42))
>>> print(tf.data.experimental.cardinality(dataset).numpy())
42
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`expected_cardinality`
</td>
<td>
The expected cardinality of the input dataset.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`FailedPreconditionError`
</td>
<td>
The assertion is checked at runtime (when iterating
the dataset) and an error is raised if the actual and expected cardinality
differ.
</td>
</tr>
</table>

