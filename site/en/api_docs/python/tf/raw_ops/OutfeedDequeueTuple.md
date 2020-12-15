description: Retrieve multiple values from the computation outfeed.

robots: noindex

# tf.raw_ops.OutfeedDequeueTuple

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Retrieve multiple values from the computation outfeed.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.OutfeedDequeueTuple`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.OutfeedDequeueTuple(
    dtypes, shapes, device_ordinal=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation will block indefinitely until data is available. Output `i`
corresponds to XLA tuple element `i`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dtypes`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
The element types of each element in `outputs`.
</td>
</tr><tr>
<td>
`shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`).
The shapes of each tensor in `outputs`.
</td>
</tr><tr>
<td>
`device_ordinal`
</td>
<td>
An optional `int`. Defaults to `-1`.
The TPU device to use. This should be -1 when the Op
is running on a TPU device, and >= 0 when the Op is running on the CPU
device.
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
A list of `Tensor` objects of type `dtypes`.
</td>
</tr>

</table>

