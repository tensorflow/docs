description: Performs fractional max pooling on the input. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.fractional_max_pool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.fractional_max_pool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_ops.py#L4527-L4610">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Performs fractional max pooling on the input. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.fractional_max_pool(
    value, pooling_ratio, pseudo_random=(False), overlapping=(False),
    deterministic=(False), seed=0, seed2=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
`seed2` and `deterministic` args are deprecated.  Use fractional_max_pool_v2.

This is a deprecated version of `fractional_max_pool`.

Fractional max pooling is slightly different than regular max pooling.  In
regular max pooling, you downsize an input set by taking the maximum value of
smaller N x N subsections of the set (often 2x2), and try to reduce the set by
a factor of N, where N is an integer.  Fractional max pooling, as you might
expect from the word "fractional", means that the overall reduction ratio N
does not have to be an integer.

The sizes of the pooling regions are generated randomly but are fairly
uniform.  For example, let's look at the height dimension, and the constraints
on the list of rows that will be pool boundaries.

First we define the following:

1.  input_row_length : the number of rows from the input set
2.  output_row_length : which will be smaller than the input
3.  alpha = input_row_length / output_row_length : our reduction ratio
4.  K = floor(alpha)
5.  row_pooling_sequence : this is the result list of pool boundary rows

Then, row_pooling_sequence should satisfy:

1.  a[0] = 0 : the first value of the sequence is 0
2.  a[end] = input_row_length : the last value of the sequence is the size
3.  K <= (a[i+1] - a[i]) <= K+1 : all intervals are K or K+1 size
4.  length(row_pooling_sequence) = output_row_length+1

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
random fashion. Check (Graham, 2015) for difference between
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
twice.  The result would be [20, 16] for fractional max pooling.
</td>
</tr><tr>
<td>
`deterministic`
</td>
<td>
An optional `bool`.  Deprecated; use `fractional_max_pool_v2`
instead.
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
`seed2`
</td>
<td>
An optional `int`.  Deprecated; use `fractional_max_pool_v2` instead.
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
  output: Output `Tensor` after fractional max pooling.  Has the same type as
    `value`.
  row_pooling_sequence: A `Tensor` of type `int64`.
  col_pooling_sequence: A `Tensor` of type `int64`.

#### References:

Fractional Max-Pooling:
  [Graham, 2015](https://arxiv.org/abs/1412.6071)
  ([pdf](https://arxiv.org/pdf/1412.6071.pdf))
