description: Represents options for collecting dataset stats using StatsAggregator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.StatsOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__ne__"/>
</div>

# tf.data.experimental.StatsOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/stats_options.py#L28-L70">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents options for collecting dataset stats using `StatsAggregator`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.StatsOptions`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.StatsOptions()
</code></pre>



<!-- Placeholder for "Used in" -->

You can set the stats options of a dataset through the `experimental_stats`
property of <a href="../../../tf/data/Options.md"><code>tf.data.Options</code></a>; the property is an instance of
<a href="../../../tf/data/experimental/StatsOptions.md"><code>tf.data.experimental.StatsOptions</code></a>. For example, to collect latency stats
on all dataset edges, use the following pattern:

```python
aggregator = tf.data.experimental.StatsAggregator()

options = tf.data.Options()
options.experimental_stats.aggregator = aggregator
options.experimental_stats.latency_all_edges = True
dataset = dataset.with_options(options)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`aggregator`
</td>
<td>
Associates the given statistics aggregator with the dataset pipeline.
</td>
</tr><tr>
<td>
`counter_prefix`
</td>
<td>
Prefix for the statistics recorded as counter.
</td>
</tr><tr>
<td>
`latency_all_edges`
</td>
<td>
Whether to add latency measurements on all edges. Defaults to False.
</td>
</tr><tr>
<td>
`prefix`
</td>
<td>
Prefix to prepend all statistics recorded for the input `dataset` with.
</td>
</tr>
</table>



## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/util/options.py#L41-L47">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/util/options.py#L49-L53">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.




