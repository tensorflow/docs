description: Cropping layer for 3D data (e.g. spatial or spatio-temporal).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Cropping3D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Cropping3D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/convolutional.py#L3173-L3351">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Cropping layer for 3D data (e.g. spatial or spatio-temporal).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Cropping3D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Cropping3D(
    cropping=((1, 1), (1, 1), (1, 1)), data_format=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

  Examples:

```
>>> input_shape = (2, 28, 28, 10, 3)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> y = tf.keras.layers.Cropping3D(cropping=(2, 4, 2))(x)
>>> print(y.shape)
(2, 24, 20, 6, 3)
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
Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints.
- If int: the same symmetric cropping
is applied to depth, height, and width.
- If tuple of 3 ints: interpreted as two different
symmetric cropping values for depth, height, and width:
`(symmetric_dim1_crop, symmetric_dim2_crop, symmetric_dim3_crop)`.
- If tuple of 3 tuples of 2 ints: interpreted as
`((left_dim1_crop, right_dim1_crop), (left_dim2_crop,
right_dim2_crop), (left_dim3_crop, right_dim3_crop))`
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
  `(batch_size, first_axis_to_crop, second_axis_to_crop, third_axis_to_crop,
    depth)`
- If `data_format` is `"channels_first"`:
  `(batch_size, depth, first_axis_to_crop, second_axis_to_crop,
    third_axis_to_crop)`



#### Output shape:

5D tensor with shape:
- If `data_format` is `"channels_last"`:
  `(batch_size, first_cropped_axis, second_cropped_axis, third_cropped_axis,
    depth)`
- If `data_format` is `"channels_first"`:
  `(batch_size, depth, first_cropped_axis, second_cropped_axis,
    third_cropped_axis)`


