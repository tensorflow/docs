description: Counts the number of occurrences of each value in an integer array.

robots: noindex

# tf.raw_ops.Bincount

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
<p>`tf.compat.v1.raw_ops.Bincount`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Bincount(
    arr, size, weights, name=None
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
`arr`
</td>
<td>
A `Tensor` of type `int32`. int32 `Tensor`.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A `Tensor` of type `int32`. non-negative int32 scalar `Tensor`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
is an int32, int64, float32, or float64 `Tensor` with the same
shape as `arr`, or a length-0 `Tensor`, in which case it acts as all weights
equal to 1.
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

