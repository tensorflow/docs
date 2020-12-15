description: Replaces the match of pattern in input with rewrite.

robots: noindex

# tf.raw_ops.StaticRegexReplace

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Replaces the match of pattern in input with rewrite.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StaticRegexReplace`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StaticRegexReplace(
    input, pattern, rewrite, replace_global=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` of type `string`. The text to be processed.
</td>
</tr><tr>
<td>
`pattern`
</td>
<td>
A `string`. The regular expression to match the input.
</td>
</tr><tr>
<td>
`rewrite`
</td>
<td>
A `string`. The rewrite to be applied to the matched expression.
</td>
</tr><tr>
<td>
`replace_global`
</td>
<td>
An optional `bool`. Defaults to `True`.
If True, the replacement is global, otherwise the replacement
is done only on the first match.
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

