description: Max pooling operation for 1D temporal data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.MaxPool1D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.MaxPool1D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/pooling.py#L112-L200">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Max pooling operation for 1D temporal data.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.MaxPooling1D`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.MaxPool1D`, `tf.compat.v1.keras.layers.MaxPooling1D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.MaxPool1D(
    pool_size=2, strides=None, padding='valid', data_format='channels_last',
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Downsamples the input representation by taking the maximum value over the
window defined by `pool_size`. The window is shifted by `strides`.  The
resulting output when using "valid" padding option has a shape of:
`output_shape = (input_shape - pool_size + 1) / strides)`

The resulting output shape when using the "same" padding option is:
`output_shape = input_shape / strides`

For example, for strides=1 and padding="valid":

```
>>> x = tf.constant([1., 2., 3., 4., 5.])
>>> x = tf.reshape(x, [1, 5, 1])
>>> max_pool_1d = tf.keras.layers.MaxPooling1D(pool_size=2,
...    strides=1, padding='valid')
>>> max_pool_1d(x)
<tf.Tensor: shape=(1, 4, 1), dtype=float32, numpy=
array([[[2.],
        [3.],
        [4.],
        [5.]]], dtype=float32)>
```

For example, for strides=2 and padding="valid":

```
>>> x = tf.constant([1., 2., 3., 4., 5.])
>>> x = tf.reshape(x, [1, 5, 1])
>>> max_pool_1d = tf.keras.layers.MaxPooling1D(pool_size=2,
...    strides=2, padding='valid')
>>> max_pool_1d(x)
<tf.Tensor: shape=(1, 2, 1), dtype=float32, numpy=
array([[[2.],
        [4.]]], dtype=float32)>
```

For example, for strides=1 and padding="same":

```
>>> x = tf.constant([1., 2., 3., 4., 5.])
>>> x = tf.reshape(x, [1, 5, 1])
>>> max_pool_1d = tf.keras.layers.MaxPooling1D(pool_size=2,
...    strides=1, padding='same')
>>> max_pool_1d(x)
<tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=
array([[[2.],
        [3.],
        [4.],
        [5.],
        [5.]]], dtype=float32)>
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
Integer, size of the max pooling window.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
Integer, or None. Specifies how much the pooling window moves
for each pooling step.
If None, it will default to `pool_size`.
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
`(batch, steps, features)` while `channels_first`
corresponds to inputs with shape
`(batch, features, steps)`.
</td>
</tr>
</table>



#### Input shape:

- If `data_format='channels_last'`:
  3D tensor with shape `(batch_size, steps, features)`.
- If `data_format='channels_first'`:
  3D tensor with shape `(batch_size, features, steps)`.



#### Output shape:

- If `data_format='channels_last'`:
  3D tensor with shape `(batch_size, downsampled_steps, features)`.
- If `data_format='channels_first'`:
  3D tensor with shape `(batch_size, features, downsampled_steps)`.


