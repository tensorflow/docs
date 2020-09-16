description: An op which feeds a single Tensor value into the computation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.InfeedEnqueue" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.InfeedEnqueue

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An op which feeds a single Tensor value into the computation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.InfeedEnqueue`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.InfeedEnqueue(
    input, shape=[], layout=[], device_ordinal=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`.
A tensor that will be provided using the infeed mechanism.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
An optional <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`. Defaults to `[]`.
The shape of the tensor.
</td>
</tr><tr>
<td>
`layout`
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
A vector holding the requested layout in minor-to-major sequence.
If a layout attribute is passed, but its values are all -1, the layout will
be computed by the infeed operation.
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
The created Operation.
</td>
</tr>

</table>

