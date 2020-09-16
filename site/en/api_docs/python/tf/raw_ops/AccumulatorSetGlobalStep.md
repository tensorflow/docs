description: Updates the accumulator with a new value for global_step.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.AccumulatorSetGlobalStep" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.AccumulatorSetGlobalStep

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Updates the accumulator with a new value for global_step.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AccumulatorSetGlobalStep`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AccumulatorSetGlobalStep(
    handle, new_global_step, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Logs warning if the accumulator's value is already higher than
new_global_step.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`handle`
</td>
<td>
A `Tensor` of type mutable `string`. The handle to an accumulator.
</td>
</tr><tr>
<td>
`new_global_step`
</td>
<td>
A `Tensor` of type `int64`.
The new global_step value to set.
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

