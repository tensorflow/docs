description: Randomly zoom each image during training.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.RandomZoom" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
</div>

# tf.keras.layers.experimental.preprocessing.RandomZoom

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/image_preprocessing.py#L887-L1041">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Randomly zoom each image during training.

Inherits From: [`PreprocessingLayer`](../../../../../tf/keras/layers/experimental/preprocessing/PreprocessingLayer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.preprocessing.RandomZoom`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.RandomZoom(
    height_factor, width_factor=None, fill_mode='reflect', interpolation='bilinear',
    seed=None, name=None, fill_value=0.0, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`height_factor`
</td>
<td>
a float represented as fraction of value, or a tuple
of size 2 representing lower and upper bound for zooming vertically.
When represented as a single float, this value is used for both the
upper and lower bound. A positive value means zooming out, while a
negative value means zooming in.
For instance, `height_factor=(0.2, 0.3)` result in an output zoomed out
by a random amount in the range [+20%, +30%].
`height_factor=(-0.3, -0.2)` result in an output zoomed in by a random
amount in the range [+20%, +30%].
</td>
</tr><tr>
<td>
`width_factor`
</td>
<td>
a float represented as fraction of value, or a tuple
of size 2 representing lower and upper bound for zooming horizontally.
When represented as a single float, this value is used for both the
upper and lower bound.
For instance, `width_factor=(0.2, 0.3)` result in an output zooming out
between 20% to 30%.
`width_factor=(-0.3, -0.2)` result in an output zooming in between 20%
to 30%. Defaults to `None`, i.e., zooming vertical and horizontal
directions by preserving the aspect ratio.
</td>
</tr><tr>
<td>
`fill_mode`
</td>
<td>
Points outside the boundaries of the input are filled according
to the given mode (one of `{'constant', 'reflect', 'wrap', 'nearest'}`).
- *reflect*: `(d c b a | a b c d | d c b a)`
The input is extended by reflecting about the edge of the last pixel.
- *constant*: `(k k k k | a b c d | k k k k)`
The input is extended by filling all values beyond the edge with the
same constant value k = 0.
- *wrap*: `(a b c d | a b c d | a b c d)`
The input is extended by wrapping around to the opposite edge.
- *nearest*: `(a a a a | a b c d | d d d d)`
The input is extended by the nearest pixel.
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
</tr><tr>
<td>
`fill_value`
</td>
<td>
a float represents the value to be filled outside the
boundaries when `fill_mode` is "constant".
</td>
</tr>
</table>



#### Example:



```
>>> input_img = np.random.random((32, 224, 224, 3))
>>> layer = tf.keras.layers.experimental.preprocessing.RandomZoom(.5, .2)
>>> out_img = layer(input_img)
>>> out_img.shape
TensorShape([32, 224, 224, 3])
```

#### Input shape:

4D tensor with shape:
`(samples, height, width, channels)`, data_format='channels_last'.



#### Output shape:

4D tensor with shape:
`(samples, height, width, channels)`, data_format='channels_last'.



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





