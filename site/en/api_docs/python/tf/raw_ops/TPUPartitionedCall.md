description: Calls a function placed on a specified TPU device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TPUPartitionedCall" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TPUPartitionedCall

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Calls a function placed on a specified TPU device.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TPUPartitionedCall`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TPUPartitionedCall(
    args, device_ordinal, Tout, f, autotuner_thresh=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`args`
</td>
<td>
A list of `Tensor` objects. The arguments to the function.
</td>
</tr><tr>
<td>
`device_ordinal`
</td>
<td>
A `Tensor` of type `int32`.
The TPU device ordinal to run the function on.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list of `tf.DTypes`. The types of the outputs of the function.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun. The function to call.
</td>
</tr><tr>
<td>
`autotuner_thresh`
</td>
<td>
An optional `int`. Defaults to `0`.
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
A list of `Tensor` objects of type `Tout`.
</td>
</tr>

</table>

