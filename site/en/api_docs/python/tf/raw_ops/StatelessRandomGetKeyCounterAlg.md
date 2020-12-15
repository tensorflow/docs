description: Picks the best algorithm based on device, and scrambles seed into key and counter.

robots: noindex

# tf.raw_ops.StatelessRandomGetKeyCounterAlg

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Picks the best algorithm based on device, and scrambles seed into key and counter.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatelessRandomGetKeyCounterAlg`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatelessRandomGetKeyCounterAlg(
    seed, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op picks the best counter-based RNG algorithm based on device, and scrambles a shape-[2] seed into a key and a counter, both needed by the counter-based algorithm. The scrambling is opaque but approximately satisfies the property that different seed results in different key/counter pair (which will in turn result in different random numbers).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`seed`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
2 seeds (shape [2]).
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
A tuple of `Tensor` objects (key, counter, alg).
</td>
</tr>
<tr>
<td>
`key`
</td>
<td>
A `Tensor` of type `uint64`.
</td>
</tr><tr>
<td>
`counter`
</td>
<td>
A `Tensor` of type `uint64`.
</td>
</tr><tr>
<td>
`alg`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr>
</table>

