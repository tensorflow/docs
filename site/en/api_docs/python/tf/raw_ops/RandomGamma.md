description: Outputs random values from the Gamma distribution(s) described by alpha.

robots: noindex

# tf.raw_ops.RandomGamma

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs random values from the Gamma distribution(s) described by alpha.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RandomGamma`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RandomGamma(
    shape, alpha, seed=0, seed2=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op uses the algorithm by Marsaglia et al. to acquire samples via
transformation-rejection from pairs of uniform and normal random variables.
See http://dl.acm.org/citation.cfm?id=358414

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
1-D integer tensor. Shape of independent samples to draw from each
distribution described by the shape parameters given in alpha.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
A tensor in which each scalar is a "shape" parameter describing the
associated gamma distribution.
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
A `Tensor`. Has the same type as `alpha`.
</td>
</tr>

</table>

