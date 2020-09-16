description: Shuts down the TPU devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.shutdown_tpu_system" />
<meta itemprop="path" content="Stable" />
</div>

# tf.tpu.experimental.shutdown_tpu_system

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/tpu/tpu_strategy_util.py#L130-L206">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Shuts down the TPU devices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.shutdown_tpu_system`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.shutdown_tpu_system(
    cluster_resolver=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This will clear all caches, even those that are maintained through sequential
calls to tf.tpu.experimental.initialize_tpu_system, such as the compilation
cache.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cluster_resolver`
</td>
<td>
A tf.distribute.cluster_resolver.TPUClusterResolver,
which provides information about the TPU cluster.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If no TPU devices found for eager execution or if run in a
tf.function.
</td>
</tr>
</table>

