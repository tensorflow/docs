description: Prints a list of tensors.

robots: noindex

# tf.raw_ops.Print

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Prints a list of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Print`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Print(
    input, data, message='', first_n=-1, summarize=3, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Passes `input` through to `output` and prints `data` when evaluating.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. The tensor passed to `output`
</td>
</tr><tr>
<td>
`data`
</td>
<td>
A list of `Tensor` objects.
A list of tensors to print out when op is evaluated.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
An optional `string`. Defaults to `""`.
A string, prefix of the error message.
</td>
</tr><tr>
<td>
`first_n`
</td>
<td>
An optional `int`. Defaults to `-1`.
Only log `first_n` number of times. -1 disables logging.
</td>
</tr><tr>
<td>
`summarize`
</td>
<td>
An optional `int`. Defaults to `3`.
Only print this many entries of each tensor.
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

