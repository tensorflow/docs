description: Write a scalar summary.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.scalar" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.scalar

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/scalar/summary_v2.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Write a scalar summary.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.summary.scalar(
    name, data, step=None, description=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this summary. The summary tag used for TensorBoard will
be this name prefixed by any active name scopes.
</td>
</tr><tr>
<td>
`data`
</td>
<td>
A real numeric scalar value, convertible to a `float32` Tensor.
</td>
</tr><tr>
<td>
`step`
</td>
<td>
Explicit `int64`-castable monotonic step value for this summary. If
omitted, this defaults to <a href="../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a>, which must
not be None.
</td>
</tr><tr>
<td>
`description`
</td>
<td>
Optional long-form description for this summary, as a
constant `str`. Markdown is supported. Defaults to empty.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
True on success, or false if no summary was written because no default
summary writer was available.
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
if a default writer exists, but no step was provided and
<a href="../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a> is None.
</td>
</tr>
</table>

