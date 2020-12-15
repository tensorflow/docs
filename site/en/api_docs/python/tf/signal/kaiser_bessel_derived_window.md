description: Generate a [Kaiser Bessel derived window][kbd].

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.kaiser_bessel_derived_window" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.kaiser_bessel_derived_window

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/signal/window_ops.py#L96-L121">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generate a [Kaiser Bessel derived window][kbd].

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.kaiser_bessel_derived_window`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.kaiser_bessel_derived_window(
    window_length, beta=12.0, dtype=tf.dtypes.float32, name=None
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
`beta`
</td>
<td>
Beta parameter for Kaiser window.
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


[kbd]:
  https://en.wikipedia.org/wiki/Kaiser_window#Kaiser%E2%80%93Bessel-derived_(KBD)_window