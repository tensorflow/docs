description: Generate a [Hamming][hamming] window.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.hamming_window" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.hamming_window

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/signal/window_ops.py#L175-L200">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generate a [Hamming][hamming] window.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.hamming_window`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.hamming_window(
    window_length, periodic=(True), dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`window_length`
</td>
<td>
A scalar `Tensor` indicating the window length to generate.
</td>
</tr><tr>
<td>
`periodic`
</td>
<td>
A bool `Tensor` indicating whether to generate a periodic or
symmetric window. Periodic windows are typically used for spectral
analysis while symmetric windows are typically used for digital
filter design.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The data type to produce. Must be a floating point type.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
An optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of shape `[window_length]` of type `dtype`.
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
If `dtype` is not a floating point type.
</td>
</tr>
</table>


[hamming]:
  https://en.wikipedia.org/wiki/Window_function#Hann_and_Hamming_windows