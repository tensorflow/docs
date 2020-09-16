description: Wraps a given text to a maximum line length and returns it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.text_wrap" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.text_wrap

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Wraps a given text to a maximum line length and returns it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.text_wrap`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.text_wrap(
    text, length=None, indent='', firstline_indent=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It turns lines that only contain whitespace into empty lines, keeps new lines,
and expands tabs using 4 spaces.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`text`
</td>
<td>
str, text to wrap.
</td>
</tr><tr>
<td>
`length`
</td>
<td>
int, maximum length of a line, includes indentation.
If this is None then use get_help_width()
</td>
</tr><tr>
<td>
`indent`
</td>
<td>
str, indent for all but first line.
</td>
</tr><tr>
<td>
`firstline_indent`
</td>
<td>
str, indent for first line; if None, fall back to indent.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
str, the wrapped text.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
Raised if indent or firstline_indent not shorter than length.
</td>
</tr>
</table>

