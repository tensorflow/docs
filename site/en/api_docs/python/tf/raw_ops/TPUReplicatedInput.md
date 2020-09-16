description: Connects N inputs to an N-way replicated TPU computation.

robots: noindex

# tf.raw_ops.TPUReplicatedInput

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Connects N inputs to an N-way replicated TPU computation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TPUReplicatedInput`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TPUReplicatedInput(
    inputs, is_mirrored_variable=(False), index=-1, is_packed=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation holds a replicated input to a `tpu.replicate()` computation subgraph.
Each replicated input has the same shape and type alongside the output.

#### For example:


```
%a = "tf.opA"()
%b = "tf.opB"()
%replicated_input = "tf.TPUReplicatedInput"(%a, %b)
%computation = "tf.Computation"(%replicated_input)
```
The above computation has a replicated input of two replicas.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type.
</td>
</tr><tr>
<td>
`is_mirrored_variable`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`index`
</td>
<td>
An optional `int`. Defaults to `-1`.
</td>
</tr><tr>
<td>
`is_packed`
</td>
<td>
An optional `bool`. Defaults to `False`.
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
A `Tensor`. Has the same type as `inputs`.
</td>
</tr>

</table>

