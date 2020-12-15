description: Calculate padding required to make block_shape divide input_shape.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.required_space_to_batch_paddings" />
<meta itemprop="path" content="Stable" />
</div>

# tf.required_space_to_batch_paddings

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L3778-L3854">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calculate padding required to make block_shape divide input_shape.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.required_space_to_batch_paddings`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.required_space_to_batch_paddings(
    input_shape, block_shape, base_paddings=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function can be used to calculate a suitable paddings argument for use
with space_to_batch_nd and batch_to_space_nd.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_shape`
</td>
<td>
int32 Tensor of shape [N].
</td>
</tr><tr>
<td>
`block_shape`
</td>
<td>
int32 Tensor of shape [N].
</td>
</tr><tr>
<td>
`base_paddings`
</td>
<td>
Optional int32 Tensor of shape [N, 2].  Specifies the minimum
amount of padding to use.  All elements must be >= 0.  If not specified,
defaults to 0.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
string.  Optional name prefix.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
(paddings, crops), where:

`paddings` and `crops` are int32 Tensors of rank 2 and shape [N, 2]
</td>
</tr>
<tr>
<td>
`satisfying`
</td>
<td>
paddings[i, 0] = base_paddings[i, 0].
0 <= paddings[i, 1] - base_paddings[i, 1] < block_shape[i]
(input_shape[i] + paddings[i, 0] + paddings[i, 1]) % block_shape[i] == 0

crops[i, 0] = 0
crops[i, 1] = paddings[i, 1] - base_paddings[i, 1]
</td>
</tr>
</table>


Raises: ValueError if called with incompatible shapes.