description: Eagerly executes a python function to compute func(input)->output. The

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.EagerPyFunc" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.EagerPyFunc

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Eagerly executes a python function to compute func(input)->output. The

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.EagerPyFunc`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.EagerPyFunc(
    input, token, Tout, is_async=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

semantics of the input, output, and attributes are the same as those for
PyFunc.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`token`
</td>
<td>
A `string`.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list of `tf.DTypes`.
</td>
</tr><tr>
<td>
`is_async`
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
A list of `Tensor` objects of type `Tout`.
</td>
</tr>

</table>

