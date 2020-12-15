description: Global average pooling operation for spatial data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.GlobalAveragePooling2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.GlobalAveragePooling2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/pooling.py#L884-L921">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Global average pooling operation for spatial data.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.GlobalAvgPool2D`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.GlobalAveragePooling2D`, `tf.compat.v1.keras.layers.GlobalAvgPool2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.GlobalAveragePooling2D(
    data_format=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Examples:



```
>>> input_shape = (2, 4, 5, 3)
>>> x = tf.random.normal(input_shape)
>>> y = tf.keras.layers.GlobalAveragePooling2D()(x)
>>> print(y.shape)
(2, 3)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
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

2D tensor with shape `(batch_size, channels)`.


