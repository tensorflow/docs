description: Max pooling layer for 3D inputs (e.g. volumes).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.MaxPooling3D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.compat.v1.layers.MaxPooling3D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/layers/pooling.py#L392-L423">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Max pooling layer for 3D inputs (e.g. volumes).

Inherits From: [`MaxPool3D`](../../../../tf/keras/layers/MaxPool3D.md), [`Layer`](../../../../tf/compat/v1/layers/Layer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.MaxPooling3D(
    pool_size, strides, padding='valid', data_format='channels_last', name=None,
    **kwargs
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
An integer or tuple/list of 3 integers:
(pool_depth, pool_height, pool_width)
specifying the size of the pooling window.
Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of 3 integers,
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
`(batch, depth, height, width, channels)` while `channels_first`
corresponds to inputs with shape
`(batch, channels, depth, height, width)`.
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
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.
</td>
</tr><tr>
<td>
`scope_name`
</td>
<td>

</td>
</tr>
</table>



