description: Outputs deterministic pseudorandom random numbers from a binomial distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.StatelessRandomBinomial" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.StatelessRandomBinomial

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs deterministic pseudorandom random numbers from a binomial distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatelessRandomBinomial`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatelessRandomBinomial(
    shape, seed, counts, probs, dtype=tf.dtypes.int64, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Outputs random values from a binomial distribution.

The outputs are a deterministic function of `shape`, `seed`, `counts`, and `probs`.

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
The shape of the output tensor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
2 seeds (shape [2]).
</td>
</tr><tr>
<td>
`counts`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`.
The counts of the binomial distribution. Must be broadcastable with `probs`,
and broadcastable with the rightmost dimensions of `shape`.
</td>
</tr><tr>
<td>
`probs`
</td>
<td>
A `Tensor`. Must have the same type as `counts`.
The probability of success for the binomial distribution. Must be broadcastable
with `counts` and broadcastable with the rightmost dimensions of `shape`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.half, tf.float32, tf.float64, tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int64"><code>tf.int64</code></a>.
The type of the output.
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
A `Tensor` of type `dtype`.
</td>
</tr>

</table>

