description: Crop the central portion of the images to target height and width.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.CenterCrop" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
</div>

# tf.keras.layers.experimental.preprocessing.CenterCrop

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/image_preprocessing.py#L125-L189">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Crop the central portion of the images to target height and width.

Inherits From: [`PreprocessingLayer`](../../../../../tf/keras/layers/experimental/preprocessing/PreprocessingLayer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.preprocessing.CenterCrop`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.CenterCrop(
    height, width, name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Input shape:

4D tensor with shape:
`(samples, height, width, channels)`, data_format='channels_last'.



#### Output shape:

4D tensor with shape:
`(samples, target_height, target_width, channels)`.


If the input height/width is even and the target height/width is odd (or
inversely), the input image is left-padded by 1 pixel.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`height`
</td>
<td>
Integer, the height of the output shape.
</td>
</tr><tr>
<td>
`width`
</td>
<td>
Integer, the width of the output shape.
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



## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/engine/base_preprocessing_layer.py#L53-L66">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>adapt(
    data, reset_state=(True)
)
</code></pre>

Fits the state of the preprocessing layer to the data being passed.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`data`
</td>
<td>
The data to train on. It can be passed either as a tf.data
Dataset, or as a numpy array.
</td>
</tr><tr>
<td>
`reset_state`
</td>
<td>
Optional argument specifying whether to clear the state of
the layer at the start of the call to `adapt`, or whether to start
from the existing state. This argument may not be relevant to all
preprocessing layers: a subclass of PreprocessingLayer may choose to
throw if 'reset_state' is set to False.
</td>
</tr>
</table>





