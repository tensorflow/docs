description: Upsampling layer for 3D inputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.UpSampling3D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.UpSampling3D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/convolutional.py#L2618-L2695">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Upsampling layer for 3D inputs.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.UpSampling3D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.UpSampling3D(
    size=(2, 2, 2), data_format=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Repeats the 1st, 2nd and 3rd dimensions
of the data by `size[0]`, `size[1]` and `size[2]` respectively.

#### Examples:



```
>>> input_shape = (2, 1, 2, 1, 3)
>>> x = tf.constant(1, shape=input_shape)
>>> y = tf.keras.layers.UpSampling3D(size=2)(x)
>>> print(y.shape)
(2, 2, 4, 2, 3)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`size`
</td>
<td>
Int, or tuple of 3 integers.
The upsampling factors for dim1, dim2 and dim3.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string,
one of `channels_last` (default) or `channels_first`.
The ordering of the dimensions in the inputs.
`channels_last` corresponds to inputs with shape
`(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
while `channels_first` corresponds to inputs with shape
`(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be "channels_last".
</td>
</tr>
</table>



#### Input shape:

5D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch_size, dim1, dim2, dim3, channels)`
- If `data_format` is `"channels_first"`:
    `(batch_size, channels, dim1, dim2, dim3)`



#### Output shape:

5D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch_size, upsampled_dim1, upsampled_dim2, upsampled_dim3, channels)`
- If `data_format` is `"channels_first"`:
    `(batch_size, channels, upsampled_dim1, upsampled_dim2, upsampled_dim3)`


