description: Returns the cardinality of dataset, if known.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.cardinality" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.cardinality

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/cardinality.py#L35-L66">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the cardinality of `dataset`, if known.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.cardinality`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.cardinality(
    dataset
)
</code></pre>



<!-- Placeholder for "Used in" -->

The operation returns the cardinality of `dataset`. The operation may return
<a href="../../../tf/data/experimental.md#INFINITE_CARDINALITY"><code>tf.data.experimental.INFINITE_CARDINALITY</code></a> if `dataset` contains an infinite
number of elements or <a href="../../../tf/data/experimental.md#UNKNOWN_CARDINALITY"><code>tf.data.experimental.UNKNOWN_CARDINALITY</code></a> if the
analysis fails to determine the number of elements in `dataset` (e.g. when the
dataset source is a file).

```
>>> dataset = tf.data.Dataset.range(42)
>>> print(tf.data.experimental.cardinality(dataset).numpy())
42
>>> dataset = dataset.repeat()
>>> cardinality = tf.data.experimental.cardinality(dataset)
>>> print((cardinality == tf.data.experimental.INFINITE_CARDINALITY).numpy())
True
>>> dataset = dataset.filter(lambda x: True)
>>> cardinality = tf.data.experimental.cardinality(dataset)
>>> print((cardinality == tf.data.experimental.UNKNOWN_CARDINALITY).numpy())
True
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dataset`
</td>
<td>
A <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> for which to determine cardinality.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A scalar <a href="../../../tf.md#int64"><code>tf.int64</code></a> `Tensor` representing the cardinality of `dataset`. If
the cardinality is infinite or unknown, the operation returns the named
constant `INFINITE_CARDINALITY` and `UNKNOWN_CARDINALITY` respectively.
</td>
</tr>

</table>

