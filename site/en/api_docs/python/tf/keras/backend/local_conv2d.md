description: Apply 2D conv with un-shared weights.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.local_conv2d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.local_conv2d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L5698-L5737">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Apply 2D conv with un-shared weights.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.local_conv2d`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.local_conv2d(
    inputs, kernel, kernel_size, strides, output_shape, data_format=None
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
4D tensor with shape:
(batch_size, filters, new_rows, new_cols)
if data_format='channels_first'
or 4D tensor with shape:
(batch_size, new_rows, new_cols, filters)
if data_format='channels_last'.
</td>
</tr><tr>
<td>
`kernel`
</td>
<td>
the unshared weight for convolution,
with shape (output_items, feature_dim, filters).
</td>
</tr><tr>
<td>
`kernel_size`
</td>
<td>
a tuple of 2 integers, specifying the
width and height of the 2D convolution window.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
a tuple of 2 integers, specifying the strides
of the convolution along the width and height.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
a tuple with (output_row, output_col).
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
A 4D tensor with shape:
(batch_size, filters, new_rows, new_cols)
if data_format='channels_first'
or 4D tensor with shape:
(batch_size, new_rows, new_cols, filters)
if data_format='channels_last'.
</td>
</tr>

</table>

