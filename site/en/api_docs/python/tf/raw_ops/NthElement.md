description: Finds values of the n-th order statistic for the last dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.NthElement" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.NthElement

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Finds values of the `n`-th order statistic for the last dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.NthElement`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.NthElement(
    input, n, reverse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If the input is a vector (rank-1), finds the entries which is the nth-smallest
value in the vector and outputs their values as scalar tensor.

For matrices (resp. higher rank input), computes the entries which is the
nth-smallest value in each row (resp. vector along the last dimension). Thus,

    values.shape = input.shape[:-1]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
1-D or higher with last dimension at least `n+1`.
</td>
</tr><tr>
<td>
`n`
</td>
<td>
A `Tensor` of type `int32`.
0-D. Position of sorted vector to select along the last dimension (along
each row for matrices). Valid range of n is `[0, input.shape[:-1])`
</td>
</tr><tr>
<td>
`reverse`
</td>
<td>
An optional `bool`. Defaults to `False`.
When set to True, find the nth-largest value in the vector and vice
versa.
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

