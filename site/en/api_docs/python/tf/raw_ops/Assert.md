description: Asserts that the given condition is true.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Assert" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Assert

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Asserts that the given condition is true.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Assert`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Assert(
    condition, data, summarize=3, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `condition` evaluates to false, print the list of tensors in `data`.
`summarize` determines how many entries of the tensors to print.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`condition`
</td>
<td>
A `Tensor` of type `bool`. The condition to evaluate.
</td>
</tr><tr>
<td>
`data`
</td>
<td>
A list of `Tensor` objects.
The tensors to print out when condition is false.
</td>
</tr><tr>
<td>
`summarize`
</td>
<td>
An optional `int`. Defaults to `3`.
Print this many entries of each tensor.
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

