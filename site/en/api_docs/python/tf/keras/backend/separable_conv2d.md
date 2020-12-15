description: 2D convolution with separable filters.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.separable_conv2d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.separable_conv2d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L5260-L5315">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



2D convolution with separable filters.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.separable_conv2d`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.separable_conv2d(
    x, depthwise_kernel, pointwise_kernel, strides=(1, 1), padding='valid',
    data_format=None, dilation_rate=(1, 1)
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
input tensor
</td>
</tr><tr>
<td>
`depthwise_kernel`
</td>
<td>
convolution kernel for the depthwise convolution.
</td>
</tr><tr>
<td>
`pointwise_kernel`
</td>
<td>
kernel for the 1x1 convolution.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
strides tuple (length 2).
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
tuple of integers,
dilation rates for the separable convolution.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Output tensor.
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
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `strides` is not a tuple of 2 integers.
</td>
</tr>
</table>

