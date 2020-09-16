description: Apply 1D conv with un-shared weights.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.local_conv1d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.local_conv1d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L5662-L5695">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Apply 1D conv with un-shared weights.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.local_conv1d`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.local_conv1d(
    inputs, kernel, kernel_size, strides, data_format=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
3D tensor with shape:
(batch_size, steps, input_dim)
if data_format is "channels_last" or
(batch_size, input_dim, steps)
if data_format is "channels_first".
</td>
</tr><tr>
<td>
`kernel`
</td>
<td>
the unshared weight for convolution,
with shape (output_length, feature_dim, filters).
</td>
</tr><tr>
<td>
`kernel_size`
</td>
<td>
a tuple of a single integer,
specifying the length of the 1D convolution window.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
a tuple of a single integer,
specifying the stride length of the convolution.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
the data format, channels_first or channels_last.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A 3d tensor with shape:
(batch_size, output_length, filters)
if data_format='channels_first'
or 3D tensor with shape:
(batch_size, filters, output_length)
if data_format='channels_last'.
</td>
</tr>

</table>

