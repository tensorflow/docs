description: The transpose of atrous_conv2d.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.atrous_conv2d_transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.atrous_conv2d_transpose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L2618-L2774">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The transpose of `atrous_conv2d`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.atrous_conv2d_transpose`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.atrous_conv2d_transpose(
    value, filters, output_shape, rate, padding, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation is sometimes called "deconvolution" after
(Zeiler et al., 2010), but is really the transpose (gradient) of
`atrous_conv2d` rather than an actual deconvolution.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A 4-D `Tensor` of type `float`. It needs to be in the default `NHWC`
format. Its shape is `[batch, in_height, in_width, in_channels]`.
</td>
</tr><tr>
<td>
`filters`
</td>
<td>
A 4-D `Tensor` with the same type as `value` and shape
`[filter_height, filter_width, out_channels, in_channels]`. `filters`'
`in_channels` dimension must match that of `value`. Atrous convolution is
equivalent to standard convolution with upsampled filters with effective
height `filter_height + (filter_height - 1) * (rate - 1)` and effective
width `filter_width + (filter_width - 1) * (rate - 1)`, produced by
inserting `rate - 1` zeros along consecutive elements across the
`filters`' spatial dimensions.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A 1-D `Tensor` of shape representing the output shape of the
deconvolution op.
</td>
</tr><tr>
<td>
`rate`
</td>
<td>
A positive int32. The stride with which we sample input values across
the `height` and `width` dimensions. Equivalently, the rate by which we
upsample the filter values by inserting zeros across the `height` and
`width` dimensions. In the literature, the same parameter is sometimes
called `input stride` or `dilation`.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A string, either `'VALID'` or `'SAME'`. The padding algorithm.
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
If input/output depth does not match `filters`' shape, or if
padding is other than `'VALID'` or `'SAME'`, or if the `rate` is less
than one, or if the output_shape is not a tensor with 4 elements.
</td>
</tr>
</table>



#### References:

Deconvolutional Networks:
  [Zeiler et al., 2010]
  (https://ieeexplore.ieee.org/abstract/document/5539957)
  ([pdf]
  (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
