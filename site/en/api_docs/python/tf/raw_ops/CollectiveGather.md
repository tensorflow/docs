description: Mutually accumulates multiple tensors of identical type and shape.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CollectiveGather" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CollectiveGather

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Mutually accumulates multiple tensors of identical type and shape.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CollectiveGather`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CollectiveGather(
    input, group_size, group_key, instance_key, shape, communication_hint='auto',
    name=None
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
A `Tensor`. Must be one of the following types: `float32`, `half`, `float64`, `int32`, `int64`.
</td>
</tr><tr>
<td>
`group_size`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`group_key`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`instance_key`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`.
</td>
</tr><tr>
<td>
`communication_hint`
</td>
<td>
An optional `string`. Defaults to `"auto"`.
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

