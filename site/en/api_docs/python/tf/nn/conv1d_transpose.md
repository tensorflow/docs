description: The transpose of conv1d.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.conv1d_transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.conv1d_transpose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_ops.py#L1732-L1817">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The transpose of `conv1d`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.conv1d_transpose`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.conv1d_transpose(
    input, filters, output_shape, strides, padding='SAME', data_format='NWC',
    dilations=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation is sometimes called "deconvolution" after
(Zeiler et al., 2010), but is actually the transpose (gradient) of `conv1d`
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
A 3-D `Tensor` of type `float` and shape
`[batch, in_width, in_channels]` for `NWC` data format or
`[batch, in_channels, in_width]` for `NCW` data format.
</td>
</tr><tr>
<td>
`filters`
</td>
<td>
A 3-D `Tensor` with the same type as `value` and shape
`[filter_width, output_channels, in_channels]`.  `filter`'s
`in_channels` dimension must match that of `value`.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A 1-D `Tensor`, containing three elements, representing the
output shape of the deconvolution op.
</td>
</tr><tr>
<td>
`strides`
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
A string, either `'VALID'` or `'SAME'`. The padding algorithm.
See the "returns" section of <a href="../../tf/nn/convolution.md"><code>tf.nn.convolution</code></a> for details.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string. `'NWC'` and `'NCW'` are supported.
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
Optional name for the returned tensor.
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
If input/output depth does not match `filter`'s shape, if
`output_shape` is not at 3-element vector, if `padding` is other than
`'VALID'` or `'SAME'`, or if `data_format` is invalid.
</td>
</tr>
</table>



#### References:

Deconvolutional Networks:
  [Zeiler et al., 2010]
  (https://ieeexplore.ieee.org/abstract/document/5539957)
  ([pdf]
  (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
