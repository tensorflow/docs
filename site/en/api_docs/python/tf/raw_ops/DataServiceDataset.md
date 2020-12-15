description: Creates a dataset that reads data from the tf.data service.

robots: noindex

# tf.raw_ops.DataServiceDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that reads data from the tf.data service.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DataServiceDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DataServiceDataset(
    dataset_id, processing_mode, address, protocol, job_name,
    max_outstanding_requests, iteration_counter, output_types, output_shapes,
    task_refresh_interval_hint_ms=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dataset_id`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`processing_mode`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`address`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`protocol`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`job_name`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`max_outstanding_requests`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`iteration_counter`
</td>
<td>
A `Tensor` of type `resource`.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
</td>
</tr><tr>
<td>
`task_refresh_interval_hint_ms`
</td>
<td>
An optional `int`. Defaults to `-1`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

