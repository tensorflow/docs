description: Computes element-wise population count (a.k.a. popcount, bitsum, bitcount).

robots: noindex

# tf.raw_ops.PopulationCount

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes element-wise population count (a.k.a. popcount, bitsum, bitcount).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.PopulationCount`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.PopulationCount(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For each entry in `x`, calculates the number of `1` (on) bits in the binary
representation of that entry.

**NOTE**: It is more efficient to first <a href="../../tf/bitcast.md"><code>tf.bitcast</code></a> your tensors into
`int32` or `int64` and perform the bitcount on the result, than to feed in
8- or 16-bit inputs and then aggregate the resulting counts.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`.
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
A `Tensor` of type `uint8`.
</td>
</tr>

</table>

