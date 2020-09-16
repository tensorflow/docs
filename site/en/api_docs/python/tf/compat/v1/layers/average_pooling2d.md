description: Average pooling layer for 2D inputs (e.g. images). (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.average_pooling2d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.layers.average_pooling2d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/legacy_tf_layers/pooling.py#L201-L238">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Average pooling layer for 2D inputs (e.g. images). (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.average_pooling2d(
    inputs, pool_size, strides, padding='valid', data_format='channels_last',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use keras.layers.AveragePooling2D instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
The tensor over which to pool. Must have rank 4.
</td>
</tr><tr>
<td>
`pool_size`
</td>
<td>
An integer or tuple/list of 2 integers: (pool_height, pool_width)
specifying the size of the pooling window.
Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of 2 integers,
specifying the strides of the pooling operation.
Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A string. The padding method, either 'valid' or 'same'.
Case-insensitive.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string. The ordering of the dimensions in the inputs.
`channels_last` (default) and `channels_first` are supported.
`channels_last` corresponds to inputs with shape
`(batch, height, width, channels)` while `channels_first` corresponds to
inputs with shape `(batch, channels, height, width)`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string, the name of the layer.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Output tensor.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if eager execution is enabled.
</td>
</tr>
</table>

