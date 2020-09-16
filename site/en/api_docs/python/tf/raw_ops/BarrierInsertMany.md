description: For each key, assigns the respective value to the specified component.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BarrierInsertMany" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BarrierInsertMany

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



For each key, assigns the respective value to the specified component.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BarrierInsertMany`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BarrierInsertMany(
    handle, keys, values, component_index, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If a key is not found in the barrier, this operation will create a new
incomplete element. If a key is found in the barrier, and the element
already has a value at component_index, this operation will fail with
INVALID_ARGUMENT, and leave the barrier in an undefined state.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`handle`
</td>
<td>
A `Tensor` of type mutable `string`. The handle to a barrier.
</td>
</tr><tr>
<td>
`keys`
</td>
<td>
A `Tensor` of type `string`.
A one-dimensional tensor of keys, with length n.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor`.
An any-dimensional tensor of values, which are associated with the
respective keys. The 0th dimension must have length n.
</td>
</tr><tr>
<td>
`component_index`
</td>
<td>
An `int`.
The component of the barrier elements that is being assigned.
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

