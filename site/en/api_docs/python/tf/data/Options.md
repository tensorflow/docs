description: Represents options for tf.data.Dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.Options" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="merge"/>
</div>

# tf.data.Options

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/dataset_ops.py#L2814-L2943">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents options for tf.data.Dataset.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.Options`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.Options()
</code></pre>



<!-- Placeholder for "Used in" -->

An `Options` object can be, for instance, used to control which graph
optimizations to apply or whether to use performance modeling to dynamically
tune the parallelism of operations such as <a href="../../tf/data/Dataset.md#map"><code>tf.data.Dataset.map</code></a> or
<a href="../../tf/data/Dataset.md#interleave"><code>tf.data.Dataset.interleave</code></a>.

After constructing an `Options` object, use `dataset.with_options(options)` to
apply the options to a dataset.

```
>>> dataset = tf.data.Dataset.range(3)
>>> options = tf.data.Options()
>>> # Set options here.
>>> dataset = dataset.with_options(options)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`experimental_deterministic`
</td>
<td>
Whether the outputs need to be produced in deterministic order. If None, defaults to True.
</td>
</tr><tr>
<td>
`experimental_distribute`
</td>
<td>
The distribution strategy options associated with the dataset. See <a href="../../tf/data/experimental/DistributeOptions.md"><code>tf.data.experimental.DistributeOptions</code></a> for more details.
</td>
</tr><tr>
<td>
`experimental_external_state_policy`
</td>
<td>
This option can be used to override the default policy for how to handle external state when serializing a dataset or checkpointing its iterator. There are three settings available - IGNORE: in which we completely ignore any state; WARN: We warn the user that some state might be thrown away; FAIL: We fail if any state is being captured.
</td>
</tr><tr>
<td>
`experimental_optimization`
</td>
<td>
The optimization options associated with the dataset. See <a href="../../tf/data/experimental/OptimizationOptions.md"><code>tf.data.experimental.OptimizationOptions</code></a> for more details.
</td>
</tr><tr>
<td>
`experimental_slack`
</td>
<td>
Whether to introduce 'slack' in the last `prefetch` of the input pipeline, if it exists. This may reduce CPU contention with accelerator host-side activity at the start of a step. The slack frequency is determined by the number of devices attached to this input pipeline. If None, defaults to False.
</td>
</tr><tr>
<td>
`experimental_stats`
</td>
<td>
The statistics options associated with the dataset. See <a href="../../tf/data/experimental/StatsOptions.md"><code>tf.data.experimental.StatsOptions</code></a> for more details.
</td>
</tr><tr>
<td>
`experimental_threading`
</td>
<td>
The threading options associated with the dataset. See <a href="../../tf/data/experimental/ThreadingOptions.md"><code>tf.data.experimental.ThreadingOptions</code></a> for more details.
</td>
</tr>
</table>



## Methods

<h3 id="merge"><code>merge</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/dataset_ops.py#L2927-L2943">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>merge(
    options
)
</code></pre>

Merges itself with the given <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a>.

The given <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a> can be merged as long as there does not exist an
attribute that is set to different values in `self` and `options`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`options`
</td>
<td>
a <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a> to merge with
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the given <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a> cannot be merged
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
New <a href="../../tf/data/Options.md"><code>tf.data.Options()</code></a> object which is the result of merging self with
the input <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a>.
</td>
</tr>

</table>



<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/util/options.py#L37-L43">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/util/options.py#L45-L49">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.




