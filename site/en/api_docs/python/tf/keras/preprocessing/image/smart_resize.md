description: Resize images to a target size without aspect ratio distortion.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image.smart_resize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.image.smart_resize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/preprocessing/image.py#L54-L148">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Resize images to a target size without aspect ratio distortion.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image.smart_resize(
    x, size, interpolation='bilinear'
)
</code></pre>



<!-- Placeholder for "Used in" -->

TensorFlow image datasets typically yield images that have each a different
size. However, these images need to be batched before they can be
processed by Keras layers. To be batched, images need to share the same height
and width.

#### You could simply do:



````python
size = (200, 200)
ds = ds.map(lambda img: tf.image.resize(img, size))
```

However, if you do this, you distort the aspect ratio of your images, since
in general they do not all have the same aspect ratio as `size`. This is
fine in many cases, but not always (e.g. for GANs this can be a problem).

Note that passing the argument `preserve_aspect_ratio=True` to `resize`
will preserve the aspect ratio, but at the cost of no longer respecting the
provided target size. Because <a href="../../../../tf/image/resize.md"><code>tf.image.resize</code></a> doesn't crop images,
your output images will still have different sizes.

#### This calls for:



```python
size = (200, 200)
ds = ds.map(lambda img: smart_resize(img, size))
```

Your output images will actually be `(200, 200)`, and will not be distorted.
Instead, the parts of the image that do not fit within the target size
get cropped out.

The resizing process is:

1. Take the largest centered crop of the image that has the same aspect ratio
as the target size. For instance, if `size=(200, 200)` and the input image has
size `(340, 500)`, we take a crop of `(340, 340)` centered along the width.
2. Resize the cropped image to the target size. In the example above,
we resize the `(340, 340)` crop to `(200, 200)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Input image (as a tensor or NumPy array). Must be in format
`(height, width, channels)`.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
Tuple of `(height, width)` integer. Target size.
</td>
</tr><tr>
<td>
`interpolation`
</td>
<td>
String, interpolation to use for resizing.
Defaults to `'bilinear'`. Supports `bilinear`, `nearest`, `bicubic`,
`area`, `lanczos3`, `lanczos5`, `gaussian`, `mitchellcubic`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Array with shape `(size[0], size[1], channels)`. If the input image was a
NumPy array, the output is a NumPy array, and if it was a TF tensor,
the output is a TF tensor.
</td>
</tr>

</table>

