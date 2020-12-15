description: Forwards the ref tensor data to the output port determined by pred.

robots: noindex

# tf.raw_ops.RefSwitch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Forwards the ref tensor `data` to the output port determined by `pred`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RefSwitch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RefSwitch(
    data, pred, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `pred` is true, the `data` input is forwarded to `output_true`. Otherwise,
the data goes to `output_false`.

See also `Switch` and `Merge`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A mutable `Tensor`.
The ref tensor to be forwarded to the appropriate output.
</td>
</tr><tr>
<td>
`pred`
</td>
<td>
A `Tensor` of type `bool`.
A scalar that specifies which output port will receive data.
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
A tuple of `Tensor` objects (output_false, output_true).
</td>
</tr>
<tr>
<td>
`output_false`
</td>
<td>
A mutable `Tensor`. Has the same type as `data`.
</td>
</tr><tr>
<td>
`output_true`
</td>
<td>
A mutable `Tensor`. Has the same type as `data`.
</td>
</tr>
</table>

