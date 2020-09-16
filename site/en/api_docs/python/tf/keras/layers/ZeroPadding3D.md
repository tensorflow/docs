description: Zero-padding layer for 3D data (spatial or spatio-temporal).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.ZeroPadding3D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.ZeroPadding3D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/convolutional.py#L2859-L2981">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Zero-padding layer for 3D data (spatial or spatio-temporal).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.ZeroPadding3D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.ZeroPadding3D(
    padding=(1, 1, 1), data_format=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Examples:



```
>>> input_shape = (1, 1, 2, 2, 3)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> y = tf.keras.layers.ZeroPadding3D(padding=2)(x)
>>> print(y.shape)
(1, 5, 6, 6, 3)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`padding`
</td>
<td>
Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints.
- If int: the same symmetric padding
is applied to height and width.
- If tuple of 3 ints:
interpreted as two different
symmetric padding values for height and width:
`(symmetric_dim1_pad, symmetric_dim2_pad, symmetric_dim3_pad)`.
- If tuple of 3 tuples of 2 ints:
interpreted as
`((left_dim1_pad, right_dim1_pad), (left_dim2_pad,
right_dim2_pad), (left_dim3_pad, right_dim3_pad))`
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
    `(batch_size, first_axis_to_pad, second_axis_to_pad, third_axis_to_pad,
      depth)`
- If `data_format` is `"channels_first"`:
    `(batch_size, depth, first_axis_to_pad, second_axis_to_pad,
      third_axis_to_pad)`



#### Output shape:

5D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch_size, first_padded_axis, second_padded_axis, third_axis_to_pad,
      depth)`
- If `data_format` is `"channels_first"`:
    `(batch_size, depth, first_padded_axis, second_padded_axis,
      third_axis_to_pad)`


