description: Sets the value of the image data format convention.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.set_image_data_format" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.set_image_data_format

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/backend_config.py#L129-L150">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets the value of the image data format convention.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.set_image_data_format`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.set_image_data_format(
    data_format
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`data_format`
</td>
<td>
string. `'channels_first'` or `'channels_last'`.
</td>
</tr>
</table>



#### Example:


>>> tf.keras.backend.image_data_format()
'channels_last'
>>> tf.keras.backend.set_image_data_format('channels_first')
>>> tf.keras.backend.image_data_format()
'channels_first'
>>> tf.keras.backend.set_image_data_format('channels_last')

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
In case of invalid `data_format` value.
</td>
</tr>
</table>

