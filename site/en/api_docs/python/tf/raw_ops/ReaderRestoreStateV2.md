description: Restore a reader to a previously saved state.

robots: noindex

# tf.raw_ops.ReaderRestoreStateV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Restore a reader to a previously saved state.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ReaderRestoreStateV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ReaderRestoreStateV2(
    reader_handle, state, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Not all Readers support being restored, so this can produce an
Unimplemented error.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`reader_handle`
</td>
<td>
A `Tensor` of type `resource`. Handle to a Reader.
</td>
</tr><tr>
<td>
`state`
</td>
<td>
A `Tensor` of type `string`.
Result of a ReaderSerializeState of a Reader with type
matching reader_handle.
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

