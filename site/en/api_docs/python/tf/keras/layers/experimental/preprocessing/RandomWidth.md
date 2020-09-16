description: Randomly vary the width of a batch of images during training.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.RandomWidth" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.experimental.preprocessing.RandomWidth

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/preprocessing/image_preprocessing.py#L1175-L1266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Randomly vary the width of a batch of images during training.

Inherits From: [`Layer`](../../../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.preprocessing.RandomWidth`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.RandomWidth(
    factor, interpolation='bilinear', seed=None, name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Adjusts the width of a batch of images by a random factor. The input
should be a 4-D tensor in the "channels_last" image data format.

By default, this layer is inactive during inference.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`factor`
</td>
<td>
A positive float (fraction of original width), or a tuple of
size 2 representing lower and upper bound for resizing horizontally. When
represented as a single float, this value is used for both the upper and
lower bound. For instance, `factor=(0.2, 0.3)` results in an output width
varying in the range `[original + 20%, original + 30%]`. `factor=(-0.2,
0.3)` results in an output width varying in the range `[original - 20%,
original + 30%]`. `factor=0.2` results in an output width varying in the
range `[original - 20%, original + 20%]`.
</td>
</tr><tr>
<td>
`interpolation`
</td>
<td>
String, the interpolation method. Defaults to `bilinear`.
Supports `bilinear`, `nearest`, `bicubic`, `area`, `lanczos3`, `lanczos5`,
`gaussian`, `mitchellcubic`
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Integer. Used to create a random seed.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string, the name of the layer.
</td>
</tr>
</table>



#### Input shape:

4D tensor with shape:
`(samples, height, width, channels)` (data_format='channels_last').



#### Output shape:

4D tensor with shape:
`(samples, random_height, width, channels)`.


