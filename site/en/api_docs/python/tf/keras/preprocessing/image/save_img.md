description: Saves an image stored as a Numpy array to a path or file object.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image.save_img" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.image.save_img

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/preprocessing/image.py#L235-L262">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Saves an image stored as a Numpy array to a path or file object.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.image.save_img`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image.save_img(
    path, x, data_format=None, file_format=None, scale=(True), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`path`
</td>
<td>
Path or file object.
</td>
</tr><tr>
<td>
`x`
</td>
<td>
Numpy array.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
Image data format,
either "channels_first" or "channels_last".
</td>
</tr><tr>
<td>
`file_format`
</td>
<td>
Optional file format override. If omitted, the
format to use is determined from the filename extension.
If a file object was used instead of a filename, this
parameter should always be used.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
Whether to rescale image values to be within `[0, 255]`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Additional keyword arguments passed to `PIL.Image.save()`.
</td>
</tr>
</table>

