description: Local Response Normalization.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.local_response_normalization" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.local_response_normalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Local Response Normalization.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.nn.lrn`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.local_response_normalization`, `tf.compat.v1.nn.lrn`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.local_response_normalization(
    input, depth_radius=5, bias=1, alpha=1, beta=0.5, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The 4-D `input` tensor is treated as a 3-D array of 1-D vectors (along the last
dimension), and each vector is normalized independently.  Within a given vector,
each component is divided by the weighted, squared sum of inputs within
`depth_radius`.  In detail,

    sqr_sum[a, b, c, d] =
        sum(input[a, b, c, d - depth_radius : d + depth_radius + 1] ** 2)
    output = input / (bias + alpha * sqr_sum) ** beta

For details, see [Krizhevsky et al., ImageNet classification with deep
convolutional neural networks (NIPS 2012)](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`.
4-D.
</td>
</tr><tr>
<td>
`depth_radius`
</td>
<td>
An optional `int`. Defaults to `5`.
0-D.  Half-width of the 1-D normalization window.
</td>
</tr><tr>
<td>
`bias`
</td>
<td>
An optional `float`. Defaults to `1`.
An offset (usually positive to avoid dividing by 0).
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
An optional `float`. Defaults to `1`.
A scale factor, usually positive.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
An optional `float`. Defaults to `0.5`. An exponent.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

