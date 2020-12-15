description: Average pooling operation for 3D data (spatial or spatio-temporal).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.AveragePooling3D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.AveragePooling3D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/pooling.py#L672-L721">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Average pooling operation for 3D data (spatial or spatio-temporal).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.AvgPool3D`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.AveragePooling3D`, `tf.compat.v1.keras.layers.AvgPool3D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.AveragePooling3D(
    pool_size=(2, 2, 2), strides=None, padding='valid', data_format=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`pool_size`
</td>
<td>
tuple of 3 integers,
factors by which to downscale (dim1, dim2, dim3).
`(2, 2, 2)` will halve the size of the 3D input in each dimension.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
tuple of 3 integers, or None. Strides values.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
One of `"valid"` or `"same"` (case-insensitive).
`"valid"` means no padding. `"same"` results in padding evenly to 
the left/right or up/down of the input such that output has the same 
height/width dimension as the input.
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
`(batch, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
while `channels_first` corresponds to inputs with shape
`(batch, channels, spatial_dim1, spatial_dim2, spatial_dim3)`.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be "channels_last".
</td>
</tr>
</table>



#### Input shape:

- If `data_format='channels_last'`:
  5D tensor with shape:
  `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
- If `data_format='channels_first'`:
  5D tensor with shape:
  `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`



#### Output shape:

- If `data_format='channels_last'`:
  5D tensor with shape:
  `(batch_size, pooled_dim1, pooled_dim2, pooled_dim3, channels)`
- If `data_format='channels_first'`:
  5D tensor with shape:
  `(batch_size, channels, pooled_dim1, pooled_dim2, pooled_dim3)`


