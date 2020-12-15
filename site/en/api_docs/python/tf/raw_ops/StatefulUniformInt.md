description: Outputs random integers from a uniform distribution.

robots: noindex

# tf.raw_ops.StatefulUniformInt

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs random integers from a uniform distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatefulUniformInt`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatefulUniformInt(
    resource, algorithm, shape, minval, maxval, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values are uniform integers in the range `[minval, maxval)`.
The lower bound `minval` is included in the range, while the upper bound
`maxval` is excluded.

The random integers are slightly biased unless `maxval - minval` is an exact
power of two.  The bias is small for values of `maxval - minval` significantly
smaller than the range of the output (either `2^32` or `2^64`).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`resource`
</td>
<td>
A `Tensor` of type `resource`.
The handle of the resource variable that stores the state of the RNG.
</td>
</tr><tr>
<td>
`algorithm`
</td>
<td>
A `Tensor` of type `int64`. The RNG algorithm.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A `Tensor`. The shape of the output tensor.
</td>
</tr><tr>
<td>
`minval`
</td>
<td>
A `Tensor`. Minimum value (inclusive, scalar).
</td>
</tr><tr>
<td>
`maxval`
</td>
<td>
A `Tensor`. Must have the same type as `minval`.
Maximum value (exclusive, scalar).
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
A `Tensor`. Has the same type as `minval`.
</td>
</tr>

</table>

