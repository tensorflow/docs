description: Outputs deterministic pseudorandom random integers from a uniform distribution.

robots: noindex

# tf.raw_ops.StatelessRandomUniformFullIntV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs deterministic pseudorandom random integers from a uniform distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatelessRandomUniformFullIntV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatelessRandomUniformFullIntV2(
    shape, key, counter, alg, dtype=tf.dtypes.uint64, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values are uniform integers covering the whole range of `dtype`.

The outputs are a deterministic function of `shape`, `key`, `counter` and `alg`.

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
`key`
</td>
<td>
A `Tensor` of type `uint64`.
Key for the counter-based RNG algorithm (shape uint64[1]).
</td>
</tr><tr>
<td>
`counter`
</td>
<td>
A `Tensor` of type `uint64`.
Initial counter for the counter-based RNG algorithm (shape uint64[2] or uint64[1] depending on the algorithm). If a larger vector is given, only the needed portion on the left (i.e. [:N]) will be used.
</td>
</tr><tr>
<td>
`alg`
</td>
<td>
A `Tensor` of type `int32`. The RNG algorithm (shape int32[]).
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64, tf.uint32, tf.uint64`. Defaults to <a href="../../tf.md#uint64"><code>tf.uint64</code></a>.
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

