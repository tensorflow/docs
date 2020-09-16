description: Closes the given barrier.

robots: noindex

# tf.raw_ops.BarrierClose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Closes the given barrier.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BarrierClose`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BarrierClose(
    handle, cancel_pending_enqueues=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation signals that no more new elements will be inserted in the
given barrier. Subsequent InsertMany that try to introduce a new key will fail.
Subsequent InsertMany operations that just add missing components to already
existing elements will continue to succeed. Subsequent TakeMany operations will
continue to succeed if sufficient completed elements remain in the barrier.
Subsequent TakeMany operations that would block will fail immediately.

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
`cancel_pending_enqueues`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, all pending enqueue requests that are
blocked on the barrier's queue will be canceled. InsertMany will fail, even
if no new key is introduced.
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

