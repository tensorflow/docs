description: Formats a string template using a list of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.StringFormat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.StringFormat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Formats a string template using a list of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StringFormat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StringFormat(
    inputs, template='%s', placeholder='%s', summarize=3, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Formats a string template using a list of tensors, pretty-printing tensor summaries.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of `Tensor` objects.
The list of tensors to format into the placeholder string.
</td>
</tr><tr>
<td>
`template`
</td>
<td>
An optional `string`. Defaults to `"%s"`.
A string, the template to format tensor summaries into.
</td>
</tr><tr>
<td>
`placeholder`
</td>
<td>
An optional `string`. Defaults to `"%s"`.
A string, at each placeholder in the template a subsequent tensor summary will be inserted.
</td>
</tr><tr>
<td>
`summarize`
</td>
<td>
An optional `int`. Defaults to `3`.
When formatting the tensor summaries print the first and last summarize entries of each tensor dimension.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

