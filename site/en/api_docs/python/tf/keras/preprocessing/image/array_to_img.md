description: Converts a 3D Numpy array to a PIL Image instance.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image.array_to_img" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.image.array_to_img

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/preprocessing/image.py#L152-L192">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a 3D Numpy array to a PIL Image instance.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.image.array_to_img`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image.array_to_img(
    x, data_format=None, scale=(True), dtype=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Usage:



```python
from PIL import Image
img = np.random.random(size=(100, 100, 3))
pil_img = tf.keras.preprocessing.image.array_to_img(img)
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Input Numpy array.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
Image data format, can be either "channels_first" or
"channels_last". Defaults to `None`, in which case the global setting
<a href="../../../../tf/keras/backend/image_data_format.md"><code>tf.keras.backend.image_data_format()</code></a> is used (unless you changed it,
it defaults to "channels_last").
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
Whether to rescale image values to be within `[0, 255]`. Defaults
to `True`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Dtype to use. Default to `None`, in which case the global setting
<a href="../../../../tf/keras/backend/floatx.md"><code>tf.keras.backend.floatx()</code></a> is used (unless you changed it, it defaults
to "float32")
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A PIL Image instance.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ImportError`
</td>
<td>
if PIL is not available.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if invalid `x` or `data_format` is passed.
</td>
</tr>
</table>

