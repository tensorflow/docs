description: Zero-padding layer for 2D input (e.g. picture).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.ZeroPadding2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.ZeroPadding2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/convolutional.py#L2405-L2526">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Zero-padding layer for 2D input (e.g. picture).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.ZeroPadding2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.ZeroPadding2D(
    padding=(1, 1), data_format=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer can add rows and columns of zeros
at the top, bottom, left and right side of an image tensor.

#### Examples:



```
>>> input_shape = (1, 1, 2, 2)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> print(x)
[[[[0 1]
   [2 3]]]]
>>> y = tf.keras.layers.ZeroPadding2D(padding=1)(x)
>>> print(y)
tf.Tensor(
  [[[[0 0]
     [0 0]
     [0 0]
     [0 0]]
    [[0 0]
     [0 1]
     [2 3]
     [0 0]]
    [[0 0]
     [0 0]
     [0 0]
     [0 0]]]], shape=(1, 3, 4, 2), dtype=int64)
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
Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints.
- If int: the same symmetric padding
is applied to height and width.
- If tuple of 2 ints:
interpreted as two different
symmetric padding values for height and width:
`(symmetric_height_pad, symmetric_width_pad)`.
- If tuple of 2 tuples of 2 ints:
interpreted as
`((top_pad, bottom_pad), (left_pad, right_pad))`
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
`(batch_size, height, width, channels)` while `channels_first`
corresponds to inputs with shape
`(batch_size, channels, height, width)`.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be "channels_last".
</td>
</tr>
</table>



#### Input shape:

4D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch_size, rows, cols, channels)`
- If `data_format` is `"channels_first"`:
    `(batch_size, channels, rows, cols)`



#### Output shape:

4D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch_size, padded_rows, padded_cols, channels)`
- If `data_format` is `"channels_first"`:
    `(batch_size, channels, padded_rows, padded_cols)`


