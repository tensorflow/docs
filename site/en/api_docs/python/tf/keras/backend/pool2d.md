description: 2D Pooling.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.pool2d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.pool2d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L5471-L5528">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



2D Pooling.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.pool2d`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.pool2d(
    x, pool_size, strides=(1, 1), padding='valid', data_format=None, pool_mode='max'
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
Tensor or variable.
</td>
</tr><tr>
<td>
`pool_size`
</td>
<td>
tuple of 2 integers.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
tuple of 2 integers.
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
`pool_mode`
</td>
<td>
string, `"max"` or `"avg"`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor, result of 2D pooling.
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
if `data_format` is neither `"channels_last"` or
`"channels_first"`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `pool_size` is not a tuple of 2 integers.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `strides` is not a tuple of 2 integers.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `pool_mode` is neither `"max"` or `"avg"`.
</td>
</tr>
</table>

