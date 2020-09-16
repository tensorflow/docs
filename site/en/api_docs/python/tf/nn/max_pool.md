description: Performs the max pooling on the input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.max_pool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.max_pool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_ops.py#L3824-L3880">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Performs the max pooling on the input.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.max_pool_v2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.max_pool(
    input, ksize, strides, padding, data_format=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape +
[num_channels]` if `data_format` does not start with "NC" (default), or
`[batch_size, num_channels] + input_spatial_shape` if data_format starts
with "NC". Pooling happens over the spatial dimensions only.
</td>
</tr><tr>
<td>
`ksize`
</td>
<td>
An int or list of `ints` that has length `1`, `N` or `N+2`. The size
of the window for each dimension of the input tensor.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An int or list of `ints` that has length `1`, `N` or `N+2`. The
stride of the sliding window for each dimension of the input tensor.
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
A string. Specifies the channel dimension. For N=1 it can be
either "NWC" (default) or "NCW", for N=2 it can be either "NHWC" (default)
or "NCHW" and for N=3 either "NDHWC" (default) or "NCDHW".
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of format specified by `data_format`.
The max pooled output tensor.
</td>
</tr>

</table>

