description: The transpose of convolution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.conv_transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.conv_transpose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L3221-L3303">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The transpose of `convolution`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.conv_transpose`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.conv_transpose(
    input, filters, output_shape, strides, padding='SAME', data_format=None,
    dilations=None, name=None
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
`input`
</td>
<td>
An N+2 dimensional `Tensor` of shape
`[batch_size] + input_spatial_shape + [in_channels]` if data_format does
not start with "NC" (default), or
`[batch_size, in_channels] + input_spatial_shape` if data_format starts
with "NC". It must be one of the following types:
`half`, `bfloat16`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`filters`
</td>
<td>
An N+2 dimensional `Tensor` with the same type as `input` and
shape `spatial_filter_shape + [in_channels, out_channels]`.
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
An int or list of `ints` that has length `1`, `N` or `N+2`.  The
stride of the sliding window for each dimension of `input`. If a single
value is given it is replicated in the spatial dimensions. By default
the `N` and `C` dimensions are set to 0. The dimension order is determined
by the value of `data_format`, see below for details.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
the "returns" section of <a href="../../tf/nn/convolution.md"><code>tf.nn.convolution</code></a> for details.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string or None.  Specifies whether the channel dimension of
the `input` and output is the last dimension (default, or if `data_format`
does not start with "NC"), or the second dimension (if `data_format`
starts with "NC").  For N=1, the valid values are "NWC" (default) and
"NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
For N=3, the valid values are "NDHWC" (default) and "NCDHW".
</td>
</tr><tr>
<td>
`dilations`
</td>
<td>
An int or list of `ints` that has length `1`, `N` or `N+2`,
defaults to 1. The dilation factor for each dimension of`input`. If a
single value is given it is replicated in the spatial dimensions. By
default the `N` and `C` dimensions are set to 1. If set to k > 1, there
will be k-1 skipped cells between each filter element on that dimension.
The dimension order is determined by the value of `data_format`, see above
for details.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional). If not specified "conv_transpose"
is used.
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



#### References:

Deconvolutional Networks:
  [Zeiler et al., 2010]
  (https://ieeexplore.ieee.org/abstract/document/5539957)
  ([pdf]
  (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
