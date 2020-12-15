description: The transpose of conv3d.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.conv3d_transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.conv3d_transpose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/nn_ops.py#L3057-L3126">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The transpose of `conv3d`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.conv3d_transpose(
    value, filter=None, output_shape=None, strides=None, padding='SAME',
    data_format='NDHWC', name=None, input=None, filters=None, dilations=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation is sometimes called "deconvolution" after
(Zeiler et al., 2010), but is really the transpose (gradient) of `conv3d`
rather than an actual deconvolution.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A 5-D `Tensor` of type `float` and shape
`[batch, depth, height, width, in_channels]`.
</td>
</tr><tr>
<td>
`filter`
</td>
<td>
A 5-D `Tensor` with the same type as `value` and shape
`[depth, height, width, output_channels, in_channels]`.  `filter`'s
`in_channels` dimension must match that of `value`.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A 1-D `Tensor` representing the output shape of the
deconvolution op.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of ints. The stride of the sliding window for each
dimension of the input tensor.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A string, either `'VALID'` or `'SAME'`. The padding algorithm.
See the "returns" section of <a href="../../../../tf/nn/convolution.md"><code>tf.nn.convolution</code></a> for details.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string, either `'NDHWC'` or `'NCDHW`' specifying the layout
of the input and output tensors. Defaults to `'NDHWC'`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned tensor.
</td>
</tr><tr>
<td>
`input`
</td>
<td>
Alias of value.
</td>
</tr><tr>
<td>
`filters`
</td>
<td>
Alias of filter.
</td>
</tr><tr>
<td>
`dilations`
</td>
<td>
An int or list of `ints` that has length `1`, `3` or `5`,
defaults to 1. The dilation factor for each dimension of`input`. If a
single value is given it is replicated in the `D`, `H` and `W` dimension.
By default the `N` and `C` dimensions are set to 1. If set to k > 1, there
will be k-1 skipped cells between each filter element on that dimension.
The dimension order is determined by the value of `data_format`, see above
for details. Dilations in the batch and depth dimensions if a 5-d tensor
must be 1.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with the same type as `value`.
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
If input/output depth does not match `filter`'s shape, or if
padding is other than `'VALID'` or `'SAME'`.
</td>
</tr>
</table>



#### References:

Deconvolutional Networks:
  [Zeiler et al., 2010]
  (https://ieeexplore.ieee.org/abstract/document/5539957)
  ([pdf]
  (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
