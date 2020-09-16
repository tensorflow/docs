description: Replace elements of input matching regex pattern with rewrite.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.regex_replace" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.regex_replace

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/string_ops.py#L74-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Replace elements of `input` matching regex `pattern` with `rewrite`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.regex_replace`, `tf.compat.v1.strings.regex_replace`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.regex_replace(
    input, pattern, rewrite, replace_global=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

```
>>> tf.strings.regex_replace("Text with tags.<br /><b>contains html</b>",
...                          "<[^>]+>", " ")
<tf.Tensor: shape=(), dtype=string, numpy=b'Text with tags.  contains html '>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
string `Tensor`, the source strings to process.
</td>
</tr><tr>
<td>
`pattern`
</td>
<td>
string or scalar string `Tensor`, regular expression to use,
see more details at https://github.com/google/re2/wiki/Syntax
</td>
</tr><tr>
<td>
`rewrite`
</td>
<td>
string or scalar string `Tensor`, value to use in match
replacement, supports backslash-escaped digits (\1 to \9) can be to insert
text matching corresponding parenthesized group.
</td>
</tr><tr>
<td>
`replace_global`
</td>
<td>
`bool`, if `True` replace all non-overlapping matches,
else replace only the first match.
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
string `Tensor` of the same shape as `input` with specified replacements.
</td>
</tr>

</table>

