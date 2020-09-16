description: Outputs a tensor containing the reduction across all input tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.NcclAllReduce" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.NcclAllReduce

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs a tensor containing the reduction across all input tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.NcclAllReduce`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.NcclAllReduce(
    input, reduction, num_devices, shared_name, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Outputs a tensor containing the reduction across all input tensors passed to ops
within the same `shared_name.

The graph should be constructed so if one op runs with shared_name value `c`,
then `num_devices` ops will run with shared_name value `c`.  Failure to do so
will cause the graph execution to fail to complete.

input: the input to the reduction
data: the value of the reduction across all `num_devices` devices.
reduction: the reduction operation to perform.
num_devices: The number of devices participating in this reduction.
shared_name: Identifier that shared between ops of the same reduction.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`.
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
`num_devices`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
A `string`.
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

