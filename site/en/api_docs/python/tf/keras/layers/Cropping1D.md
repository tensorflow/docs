description: Cropping layer for 1D input (e.g. temporal sequence).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Cropping1D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Cropping1D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/convolutional.py#L2656-L2713">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Cropping layer for 1D input (e.g. temporal sequence).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Cropping1D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Cropping1D(
    cropping=(1, 1), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

It crops along the time dimension (axis 1).

#### Examples:



```
>>> input_shape = (2, 3, 2)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> print(x)
[[[ 0  1]
  [ 2  3]
  [ 4  5]]
 [[ 6  7]
  [ 8  9]
  [10 11]]]
>>> y = tf.keras.layers.Cropping1D(cropping=1)(x)
>>> print(y)
tf.Tensor(
  [[[2 3]]
   [[8 9]]], shape=(2, 1, 2), dtype=int64)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`cropping`
</td>
<td>
Int or tuple of int (length 2)
How many units should be trimmed off at the beginning and end of
the cropping dimension (axis 1).
If a single int is provided, the same value will be used for both.
</td>
</tr>
</table>



#### Input shape:

3D tensor with shape `(batch_size, axis_to_crop, features)`



#### Output shape:

3D tensor with shape `(batch_size, cropped_axis, features)`


