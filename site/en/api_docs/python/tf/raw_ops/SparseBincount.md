description: Counts the number of occurrences of each value in an integer array.

robots: noindex

# tf.raw_ops.SparseBincount

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Counts the number of occurrences of each value in an integer array.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseBincount`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseBincount(
    indices, values, dense_shape, size, weights, binary_output=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Outputs a vector with length `size` and the same dtype as `weights`. If
`weights` are empty, then index `i` stores the number of times the value `i` is
counted in `arr`. If `weights` are non-empty, then index `i` stores the sum of
the value in `weights` at each index where the corresponding value in `arr` is
`i`.

Values in `arr` outside of the range [0, size) are ignored.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int64`. 2D int64 `Tensor`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
1D int `Tensor`.
</td>
</tr><tr>
<td>
`dense_shape`
</td>
<td>
A `Tensor` of type `int64`. 1D int64 `Tensor`.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A `Tensor`. Must have the same type as `values`.
non-negative int scalar `Tensor`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
is an int32, int64, float32, or float64 `Tensor` with the same
shape as `input`, or a length-0 `Tensor`, in which case it acts as all weights
equal to 1.
</td>
</tr><tr>
<td>
`binary_output`
</td>
<td>
An optional `bool`. Defaults to `False`.
bool; Whether the kernel should count the appearance or number of occurrences.
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
A `Tensor`. Has the same type as `weights`.
</td>
</tr>

</table>

