description: Computes a 1-D convolution given 3-D input and filter tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.conv1d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.conv1d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L1911-L1976">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes a 1-D convolution given 3-D input and filter tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.conv1d(
    input, filters, stride, padding, data_format='NWC', dilations=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given an input tensor of shape
  `batch_shape + [in_width, in_channels]`
if `data_format` is `"NWC"`, or
  `batch_shape + [in_channels, in_width]`
if `data_format` is `"NCW"`,
and a filter / kernel tensor of shape
`[filter_width, in_channels, out_channels]`, this op reshapes
the arguments to pass them to `conv2d` to perform the equivalent
convolution operation.

Internally, this op reshapes the input tensors and invokes <a href="../../tf/nn/conv2d.md"><code>tf.nn.conv2d</code></a>.
For example, if `data_format` does not start with `"NC"`, a tensor of shape
  `batch_shape + [in_width, in_channels]`
is reshaped to
  `batch_shape + [1, in_width, in_channels]`,
and the filter is reshaped to
  `[1, filter_width, in_channels, out_channels]`.
The result is then reshaped back to
  `batch_shape + [out_width, out_channels]`
\(where out_width is a function of the stride and padding as in conv2d\) and
returned to the caller.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A Tensor of rank at least 3. Must be of type `float16`, `float32`, or
`float64`.
</td>
</tr><tr>
<td>
`filters`
</td>
<td>
A Tensor of rank at least 3.  Must have the same type as `input`.
</td>
</tr><tr>
<td>
`stride`
</td>
<td>
An int or list of `ints` that has length `1` or `3`.  The number of
entries by which the filter is moved right at each step.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
'SAME' or 'VALID'
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
An optional `string` from `"NWC", "NCW"`.  Defaults to `"NWC"`,
the data is stored in the order of
`batch_shape + [in_width, in_channels]`.  The `"NCW"` format stores data
as `batch_shape + [in_channels, in_width]`.
</td>
</tr><tr>
<td>
`dilations`
</td>
<td>
An int or list of `ints` that has length `1` or `3` which
defaults to 1. The dilation factor for each dimension of input. If set to
k > 1, there will be k-1 skipped cells between each filter element on that
dimension. Dilations in the batch and depth dimensions must be 1.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`.  Has the same type as input.
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
if `data_format` is invalid.
</td>
</tr>
</table>

