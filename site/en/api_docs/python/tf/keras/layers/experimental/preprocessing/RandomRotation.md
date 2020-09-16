description: Randomly rotate each image.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.RandomRotation" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.experimental.preprocessing.RandomRotation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/preprocessing/image_preprocessing.py#L718-L829">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Randomly rotate each image.

Inherits From: [`Layer`](../../../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.preprocessing.RandomRotation`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.RandomRotation(
    factor, fill_mode='constant', interpolation='bilinear', seed=None, name=None,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

By default, random rotations are only applied during training.
At inference time, the layer does nothing. If you need to apply random
rotations at inference time, set `training` to True when calling the layer.

#### Input shape:

4D tensor with shape:
`(samples, height, width, channels)`, data_format='channels_last'.



#### Output shape:

4D tensor with shape:
`(samples, height, width, channels)`, data_format='channels_last'.



#### Input shape:

4D tensor with shape: `(samples, height, width, channels)`,
  data_format='channels_last'.


#### Output shape:

4D tensor with shape: `(samples, height, width, channels)`,
  data_format='channels_last'.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raise</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if lower bound is not between [0, 1], or upper bound is
negative.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`factor`
</td>
<td>
a positive float represented as fraction of 2pi, or a tuple of size
2 representing lower and upper bound for rotating clockwise and
counter-clockwise. When represented as a single float, lower = upper.
</td>
</tr><tr>
<td>
`fill_mode`
</td>
<td>
Points outside the boundaries of the input are filled according
to the given mode (one of `{'constant', 'reflect', 'wrap'}`).
- *reflect*: `(d c b a | a b c d | d c b a)`
The input is extended by reflecting about the edge of the last pixel.
- *constant*: `(k k k k | a b c d | k k k k)`
The input is extended by filling all values beyond the edge with the
same constant value k = 0.
- *wrap*: `(a b c d | a b c d | a b c d)`
</td>
</tr><tr>
<td>
`interpolation`
</td>
<td>
Interpolation mode. Supported values: "nearest", "bilinear".
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



