description: Spatial 2D version of Dropout.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.SpatialDropout2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.SpatialDropout2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/core.py#L290-L345">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Spatial 2D version of Dropout.

Inherits From: [`Dropout`](../../../tf/keras/layers/Dropout.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.SpatialDropout2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.SpatialDropout2D(
    rate, data_format=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This version performs the same function as Dropout, however, it drops
entire 2D feature maps instead of individual elements. If adjacent pixels
within feature maps are strongly correlated (as is normally the case in
early convolution layers) then regular dropout will not regularize the
activations and will otherwise just result in an effective learning rate
decrease. In this case, SpatialDropout2D will help promote independence
between feature maps and should be used instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`rate`
</td>
<td>
Float between 0 and 1. Fraction of the input units to drop.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
'channels_first' or 'channels_last'.
In 'channels_first' mode, the channels dimension
(the depth) is at index 1,
in 'channels_last' mode is it at index 3.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be "channels_last".
</td>
</tr>
</table>



#### Call arguments:


* <b>`inputs`</b>: A 4D tensor.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding dropout) or in inference mode (doing nothing).


#### Input shape:

4D tensor with shape:
`(samples, channels, rows, cols)` if data_format='channels_first'
or 4D tensor with shape:
`(samples, rows, cols, channels)` if data_format='channels_last'.



#### Output shape:

Same as input.



#### References:

- [Efficient Object Localization Using Convolutional
  Networks](https://arxiv.org/abs/1411.4280)


