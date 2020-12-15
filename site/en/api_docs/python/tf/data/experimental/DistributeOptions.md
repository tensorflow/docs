description: Represents options for distributed data processing.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.DistributeOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__ne__"/>
</div>

# tf.data.experimental.DistributeOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/distribute_options.py#L46-L85">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents options for distributed data processing.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.DistributeOptions`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.DistributeOptions()
</code></pre>



<!-- Placeholder for "Used in" -->

You can set the distribution options of a dataset through the
`experimental_distribute` property of <a href="../../../tf/data/Options.md"><code>tf.data.Options</code></a>; the property is
an instance of <a href="../../../tf/data/experimental/DistributeOptions.md"><code>tf.data.experimental.DistributeOptions</code></a>.

```python
options = tf.data.Options()
options.experimental_distribute.auto_shard_policy = AutoShardPolicy.OFF
dataset = dataset.with_options(options)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`auto_shard_policy`
</td>
<td>
The type of sharding that auto-shard should attempt. If this is set to FILE, then we will attempt to shard by files (each worker will get a set of files to process). If we cannot find a set of files to shard for at least one file per worker, we will error out. When this option is selected, make sure that you have enough files so that each worker gets at least one file. There will be a runtime error thrown if there are insufficient files. If this is set to DATA, then we will shard by elements produced by the dataset, and each worker will process the whole dataset and discard the portion that is not for itself. If this is set to OFF, then we will not autoshard, and each worker will receive a copy of the full dataset. This option is set to AUTO by default, AUTO will attempt to first shard by FILE, and fall back to sharding by DATA if we cannot find a set of files to shard.
</td>
</tr><tr>
<td>
`num_devices`
</td>
<td>
The number of devices attached to this input pipeline. This will be automatically set by MultiDeviceIterator.
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




