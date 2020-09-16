description: Converts a PIL Image instance to a Numpy array.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image.img_to_array" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.image.img_to_array

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/preprocessing/image.py#L90-L128">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a PIL Image instance to a Numpy array.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.image.img_to_array`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image.img_to_array(
    img, data_format=None, dtype=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Usage:



```python
from PIL import Image
img_data = np.random.random(size=(100, 100, 3))
img = tf.keras.preprocessing.image.array_to_img(img_data)
array = tf.keras.preprocessing.image.img_to_array(img)
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`img`
</td>
<td>
Input PIL Image instance.
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
A 3D Numpy array.
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
if invalid `img` or `data_format` is passed.
</td>
</tr>
</table>

