description: Replaces matches of the pattern regular expression in input with the

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RegexReplace" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RegexReplace

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Replaces matches of the `pattern` regular expression in `input` with the

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RegexReplace`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RegexReplace(
    input, pattern, rewrite, replace_global=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->
replacement string provided in `rewrite`.

  It follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

  Args:
    input: A `Tensor` of type `string`. The text to be processed.
    pattern: A `Tensor` of type `string`.
      The regular expression to be matched in the `input` strings.
    rewrite: A `Tensor` of type `string`.
      The rewrite string to be substituted for the `pattern` expression where it is
      matched in the `input` strings.
    replace_global: An optional `bool`. Defaults to `True`.
      If True, the replacement is global (that is, all matches of the `pattern` regular
      expression in each input string are rewritten), otherwise the `rewrite`
      substitution is only made for the first `pattern` match.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  