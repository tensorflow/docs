description: Average Pooling layer for 1D inputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.average_pooling1d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.layers.average_pooling1d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/legacy_tf_layers/pooling.py#L62-L97">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Average Pooling layer for 1D inputs.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.average_pooling1d(
    inputs, pool_size, strides, padding='valid', data_format='channels_last',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
The tensor over which to pool. Must have rank 3.
</td>
</tr><tr>
<td>
`pool_size`
</td>
<td>
An integer or tuple/list of a single integer,
representing the size of the pooling window.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of a single integer, specifying the
strides of the pooling operation.
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
A string, one of `channels_last` (default) or `channels_first`.
The ordering of the dimensions in the inputs.
`channels_last` corresponds to inputs with shape
`(batch, length, channels)` while `channels_first` corresponds to
inputs with shape `(batch, channels, length)`.
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
The output tensor, of rank 3.
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

