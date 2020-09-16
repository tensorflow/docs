description: 2D deconvolution (i.e.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.conv2d_transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.conv2d_transpose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L4980-L5050">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



2D deconvolution (i.e.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.conv2d_transpose`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.conv2d_transpose(
    x, kernel, output_shape, strides=(1, 1), padding='valid', data_format=None,
    dilation_rate=(1, 1)
)
</code></pre>



<!-- Placeholder for "Used in" -->

transposed convolution).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Tensor or variable.
</td>
</tr><tr>
<td>
`kernel`
</td>
<td>
kernel tensor.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
1D int tensor for the output shape.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
strides tuple.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
string, `"same"` or `"valid"`.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
string, `"channels_last"` or `"channels_first"`.
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
Tuple of 2 integers.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor, result of transposed 2D convolution.
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
if `data_format` is neither `channels_last` or
`channels_first`.
</td>
</tr>
</table>

