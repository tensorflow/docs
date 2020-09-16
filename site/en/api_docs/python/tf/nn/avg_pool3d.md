description: Performs the average pooling on the input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.avg_pool3d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.avg_pool3d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_ops.py#L3784-L3820">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Performs the average pooling on the input.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.avg_pool3d`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.avg_pool3d(
    input, ksize, strides, padding, data_format='NDHWC', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A 5-D `Tensor` of shape `[batch, height, width, channels]` and type
`float32`, `float64`, `qint8`, `quint8`, or `qint32`.
</td>
</tr><tr>
<td>
`ksize`
</td>
<td>
An int or list of `ints` that has length `1`, `3` or `5`. The size of
the window for each dimension of the input tensor.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An int or list of `ints` that has length `1`, `3` or `5`. The
stride of the sliding window for each dimension of the input tensor.
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
A string. 'NDHWC' and 'NCDHW' are supported.
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
A `Tensor` with the same type as `value`.  The average pooled output tensor.
</td>
</tr>

</table>

