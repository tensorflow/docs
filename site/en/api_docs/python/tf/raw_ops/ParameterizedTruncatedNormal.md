description: Outputs random values from a normal distribution. The parameters may each be a

robots: noindex

# tf.raw_ops.ParameterizedTruncatedNormal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs random values from a normal distribution. The parameters may each be a

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParameterizedTruncatedNormal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParameterizedTruncatedNormal(
    shape, means, stdevs, minvals, maxvals, seed=0, seed2=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

scalar which applies to the entire output, or a vector of length shape[0] which
stores the parameters for each batch.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
The shape of the output tensor. Batches are indexed by the 0th dimension.
</td>
</tr><tr>
<td>
`means`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
The mean parameter of each batch.
</td>
</tr><tr>
<td>
`stdevs`
</td>
<td>
A `Tensor`. Must have the same type as `means`.
The standard deviation parameter of each batch. Must be greater than 0.
</td>
</tr><tr>
<td>
`minvals`
</td>
<td>
A `Tensor`. Must have the same type as `means`.
The minimum cutoff. May be -infinity.
</td>
</tr><tr>
<td>
`maxvals`
</td>
<td>
A `Tensor`. Must have the same type as `means`.
The maximum cutoff. May be +infinity, and must be more than the minval
for each batch.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An optional `int`. Defaults to `0`.
If either `seed` or `seed2` are set to be non-zero, the random number
generator is seeded by the given seed.  Otherwise, it is seeded by a
random seed.
</td>
</tr><tr>
<td>
`seed2`
</td>
<td>
An optional `int`. Defaults to `0`.
A second seed to avoid seed collision.
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
A `Tensor`. Has the same type as `means`.
</td>
</tr>

</table>

