description: Max pooling operation for 2D spatial data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.MaxPool2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.MaxPool2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/pooling.py#L330-L461">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Max pooling operation for 2D spatial data.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.MaxPooling2D`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.MaxPool2D`, `tf.compat.v1.keras.layers.MaxPooling2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.MaxPool2D(
    pool_size=(2, 2), strides=None, padding='valid', data_format=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Downsamples the input representation by taking the maximum value over the
window defined by `pool_size` for each dimension along the features axis.
The window is shifted by `strides` in each dimension.  The resulting output
when using "valid" padding option has a shape(number of rows or columns) of:
`output_shape = (input_shape - pool_size + 1) / strides)`

The resulting output shape when using the "same" padding option is:
`output_shape = input_shape / strides`

For example, for stride=(1,1) and padding="valid":

```
>>> x = tf.constant([[1., 2., 3.],
...                  [4., 5., 6.],
...                  [7., 8., 9.]])
>>> x = tf.reshape(x, [1, 3, 3, 1])
>>> max_pool_2d = tf.keras.layers.MaxPooling2D(pool_size=(2, 2),
...    strides=(1, 1), padding='valid')
>>> max_pool_2d(x)
<tf.Tensor: shape=(1, 2, 2, 1), dtype=float32, numpy=
  array([[[[5.],
           [6.]],
          [[8.],
           [9.]]]], dtype=float32)>
```

For example, for stride=(2,2) and padding="valid":

```
>>> x = tf.constant([[1., 2., 3., 4.],
...                  [5., 6., 7., 8.],
...                  [9., 10., 11., 12.]])
>>> x = tf.reshape(x, [1, 3, 4, 1])
>>> max_pool_2d = tf.keras.layers.MaxPooling2D(pool_size=(2, 2),
...    strides=(1, 1), padding='valid')
>>> max_pool_2d(x)
<tf.Tensor: shape=(1, 2, 3, 1), dtype=float32, numpy=
  array([[[[ 6.],
           [ 7.],
           [ 8.]],
          [[10.],
           [11.],
           [12.]]]], dtype=float32)>
```

#### Usage Example:



```
>>> input_image = tf.constant([[[[1.], [1.], [2.], [4.]],
...                            [[2.], [2.], [3.], [2.]],
...                            [[4.], [1.], [1.], [1.]],
...                            [[2.], [2.], [1.], [4.]]]]) 
>>> output = tf.constant([[[[1], [0]],
...                       [[0], [1]]]]) 
>>> model = tf.keras.models.Sequential()
>>> model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), 
...    input_shape=(4,4,1)))
>>> model.compile('adam', 'mean_squared_error')
>>> model.predict(input_image, steps=1)
array([[[[2.],
         [4.]],
        [[4.],
         [4.]]]], dtype=float32)
```

For example, for stride=(1,1) and padding="same":

```
>>> x = tf.constant([[1., 2., 3.],
...                  [4., 5., 6.],
...                  [7., 8., 9.]])
>>> x = tf.reshape(x, [1, 3, 3, 1])
>>> max_pool_2d = tf.keras.layers.MaxPooling2D(pool_size=(2, 2),
...    strides=(1, 1), padding='same')
>>> max_pool_2d(x)
<tf.Tensor: shape=(1, 3, 3, 1), dtype=float32, numpy=
  array([[[[5.],
           [6.],
           [6.]],
          [[8.],
           [9.],
           [9.]],
          [[8.],
           [9.],
           [9.]]]], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`pool_size`
</td>
<td>
integer or tuple of 2 integers,
window size over which to take the maximum.
`(2, 2)` will take the max value over a 2x2 pooling window.
If only one integer is specified, the same window length
will be used for both dimensions.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
Integer, tuple of 2 integers, or None.
Strides values.  Specifies how far the pooling window moves
for each pooling step. If None, it will default to `pool_size`.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
One of `"valid"` or `"same"` (case-insensitive).
"valid" adds no zero padding.  "same" adds padding such that if the stride
is 1, the output shape is the same as input shape.
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
`(batch, height, width, channels)` while `channels_first`
corresponds to inputs with shape
`(batch, channels, height, width)`.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be "channels_last".
</td>
</tr>
</table>



#### Input shape:

- If `data_format='channels_last'`:
  4D tensor with shape `(batch_size, rows, cols, channels)`.
- If `data_format='channels_first'`:
  4D tensor with shape `(batch_size, channels, rows, cols)`.



#### Output shape:

- If `data_format='channels_last'`:
  4D tensor with shape `(batch_size, pooled_rows, pooled_cols, channels)`.
- If `data_format='channels_first'`:
  4D tensor with shape `(batch_size, channels, pooled_rows, pooled_cols)`.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of rank 4 representing the maximum pooled values.  See above for
output shape.
</td>
</tr>

</table>



