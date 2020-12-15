description: Global max pooling operation for 1D temporal data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.GlobalMaxPool1D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.GlobalMaxPool1D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/pooling.py#L809-L854">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Global max pooling operation for 1D temporal data.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.GlobalMaxPooling1D`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.GlobalMaxPool1D`, `tf.compat.v1.keras.layers.GlobalMaxPooling1D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.GlobalMaxPool1D(
    data_format='channels_last', **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Downsamples the input representation by taking the maximum value over
the time dimension.

#### For example:



```
>>> x = tf.constant([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
>>> x = tf.reshape(x, [3, 3, 1])
>>> x
<tf.Tensor: shape=(3, 3, 1), dtype=float32, numpy=
array([[[1.], [2.], [3.]],
       [[4.], [5.], [6.]],
       [[7.], [8.], [9.]]], dtype=float32)>
>>> max_pool_1d = tf.keras.layers.GlobalMaxPooling1D()
>>> max_pool_1d(x)
<tf.Tensor: shape=(3, 1), dtype=float32, numpy=
array([[3.],
       [6.],
       [9.], dtype=float32)>
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
`(batch, steps, features)` while `channels_first`
corresponds to inputs with shape
`(batch, features, steps)`.
</td>
</tr>
</table>



#### Input shape:

- If `data_format='channels_last'`:
  3D tensor with shape:
  `(batch_size, steps, features)`
- If `data_format='channels_first'`:
  3D tensor with shape:
  `(batch_size, features, steps)`



#### Output shape:

2D tensor with shape `(batch_size, features)`.


