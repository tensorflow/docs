description: Preprocesses a tensor or Numpy array encoding a batch of images.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.applications.imagenet_utils.preprocess_input" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.applications.imagenet_utils.preprocess_input

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/applications/imagenet_utils.py#L103-L119">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Preprocesses a tensor or Numpy array encoding a batch of images.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.applications.imagenet_utils.preprocess_input`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.applications.imagenet_utils.preprocess_input(
    x, data_format=None, mode='caffe'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Usage example with <a href="../../../../tf/keras/applications/MobileNet.md"><code>applications.MobileNet</code></a>:

```python
i = tf.keras.layers.Input([None, None, 3], dtype = tf.uint8)
x = tf.cast(i, tf.float32)
x = tf.keras.applications.mobilenet.preprocess_input(x)
core = tf.keras.applications.MobileNet()
x = core(x)
model = tf.keras.Model(inputs=[i], outputs=[x])

image = tf.image.decode_png(tf.io.read_file('file.png'))
result = model(image)
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
A floating point `numpy.array` or a <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a>, 3D or 4D with 3 color
channels, with values in the range [0, 255].
The preprocessed data are written over the input data
if the data types are compatible. To avoid this
behaviour, `numpy.copy(x)` can be used.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
Optional data format of the image tensor/array. Defaults to
None, in which case the global setting
<a href="../../../../tf/keras/backend/image_data_format.md"><code>tf.keras.backend.image_data_format()</code></a> is used (unless you changed it,
it defaults to "channels_last").
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
One of "caffe", "tf" or "torch". Defaults to "caffe".
- caffe: will convert the images from RGB to BGR,
then will zero-center each color channel with
respect to the ImageNet dataset,
without scaling.
- tf: will scale pixels between -1 and 1,
sample-wise.
- torch: will scale pixels between 0 and 1 and then
will normalize each channel with respect to the
ImageNet dataset.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Preprocessed `numpy.array` or a <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> with type `float32`.
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
In case of unknown `mode` or `data_format` argument.
</td>
</tr>
</table>

