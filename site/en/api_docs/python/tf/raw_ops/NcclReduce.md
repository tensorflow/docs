description: Reduces input from num_devices using reduction to a single device.

robots: noindex

# tf.raw_ops.NcclReduce

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Reduces `input` from `num_devices` using `reduction` to a single device.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.NcclReduce`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.NcclReduce(
    input, reduction, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reduces `input` from `num_devices` using `reduction` to a single device.

The graph should be constructed so that all inputs have a valid device
assignment, and the op itself is assigned one of these devices.

input: The input to the reduction.
data: the value of the reduction across all `num_devices` devices.
reduction: the reduction operation to perform.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type in: `half`, `float32`, `float64`, `int32`, `int64`.
</td>
</tr><tr>
<td>
`reduction`
</td>
<td>
A `string` from: `"min", "max", "prod", "sum"`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

