description: Retrieves the global generator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.get_global_generator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.get_global_generator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L913-L930">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Retrieves the global generator.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.random.experimental.get_global_generator`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.experimental.get_global_generator`, `tf.compat.v1.random.get_global_generator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.get_global_generator()
</code></pre>



<!-- Placeholder for "Used in" -->

This function will create the global generator the first time it is called,
and the generator will be placed at the default device at that time, so one
needs to be careful when this function is first called. Using a generator
placed on a less-ideal device will incur performance regression.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The global <a href="../../tf/random/Generator.md"><code>tf.random.Generator</code></a> object.
</td>
</tr>

</table>

