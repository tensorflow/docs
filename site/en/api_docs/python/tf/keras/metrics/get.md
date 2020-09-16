description: Retrieves a Keras metric as a function/Metric class instance.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.get" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.metrics.get

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/metrics.py#L3446-L3488">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Retrieves a Keras metric as a `function`/`Metric` class instance.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.metrics.get`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.metrics.get`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.metrics.get(
    identifier
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `identifier` may be the string name of a metric function or class.

```
>>> metric = tf.keras.metrics.get("categorical_crossentropy")
>>> type(metric)
<class 'function'>
>>> metric = tf.keras.metrics.get("CategoricalCrossentropy")
>>> type(metric)
<class '...tensorflow.python.keras.metrics.CategoricalCrossentropy'>
```

You can also specify `config` of the metric to this function by passing dict
containing `class_name` and `config` as an identifier. Also note that the
`class_name` must map to a `Metric` class

```
>>> identifier = {"class_name": "CategoricalCrossentropy",
...               "config": {"from_logits": True}}
>>> metric = tf.keras.metrics.get(identifier)
>>> type(metric)
<class '...tensorflow.python.keras.metrics.CategoricalCrossentropy'>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`identifier`
</td>
<td>
A metric identifier. One of None or string name of a metric
function/class or metric configuration dictionary or a metric function or
a metric class instance
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras metric as a `function`/ `Metric` class instance.
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
If `identifier` cannot be interpreted.
</td>
</tr>
</table>

