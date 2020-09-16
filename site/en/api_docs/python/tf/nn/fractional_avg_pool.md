description: Performs fractional average pooling on the input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.fractional_avg_pool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.fractional_avg_pool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_ops.py#L4763-L4822">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Performs fractional average pooling on the input.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.fractional_avg_pool(
    value, pooling_ratio, pseudo_random=(False), overlapping=(False), seed=0,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Fractional average pooling is similar to Fractional max pooling in the pooling
region generation step. The only difference is that after pooling regions are
generated, a mean operation is performed instead of a max operation in each
pooling region.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A `Tensor`. 4-D with shape `[batch, height, width, channels]`.
</td>
</tr><tr>
<td>
`pooling_ratio`
</td>
<td>
A list of `floats` that has length >= 4.  Pooling ratio for
each dimension of `value`, currently only supports row and col dimension
and should be >= 1.0. For example, a valid pooling ratio looks like [1.0,
1.44, 1.73, 1.0]. The first and last elements must be 1.0 because we don't
allow pooling on batch and channels dimensions.  1.44 and 1.73 are pooling
ratio on height and width dimensions respectively.
</td>
</tr><tr>
<td>
`pseudo_random`
</td>
<td>
An optional `bool`.  Defaults to `False`. When set to `True`,
generates the pooling sequence in a pseudorandom fashion, otherwise, in a
random fashion. Check paper (Graham, 2015) for difference between
pseudorandom and random.
</td>
</tr><tr>
<td>
`overlapping`
</td>
<td>
An optional `bool`.  Defaults to `False`.  When set to `True`,
it means when pooling, the values at the boundary of adjacent pooling
cells are used by both cells. For example:
`index  0  1  2  3  4`
`value  20 5  16 3  7`
If the pooling sequence is [0, 2, 4], then 16, at index 2 will be used
twice.  The result would be [20, 16] for fractional avg pooling.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An optional `int`.  Defaults to `0`.  If set to be non-zero, the
random number generator is seeded by the given seed.  Otherwise it is
seeded by a random seed.
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


</table>


A tuple of `Tensor` objects (`output`, `row_pooling_sequence`,
`col_pooling_sequence`).
  output: Output `Tensor` after fractional avg pooling.  Has the same type as
    `value`.
  row_pooling_sequence: A `Tensor` of type `int64`.
  col_pooling_sequence: A `Tensor` of type `int64`.

#### References:

Fractional Max-Pooling:
  [Graham, 2015](https://arxiv.org/abs/1412.6071)
  ([pdf](https://arxiv.org/pdf/1412.6071.pdf))
