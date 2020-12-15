description: Check if the input matches the regex pattern.

robots: noindex

# tf.raw_ops.RegexFullMatch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Check if the input matches the regex pattern.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RegexFullMatch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RegexFullMatch(
    input, pattern, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input is a string tensor of any shape. The pattern is a scalar
string tensor which is applied to every element of the input tensor.
The boolean values (True or False) of the output tensor indicate
if the input matches the regex pattern provided.

The pattern follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

#### Examples:



```
>>> tf.strings.regex_full_match(["TF lib", "lib TF"], ".*lib$")
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])>
>>> tf.strings.regex_full_match(["TF lib", "lib TF"], ".*TF$")
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>
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
A `Tensor` of type `string`.
A string tensor of the text to be processed.
</td>
</tr><tr>
<td>
`pattern`
</td>
<td>
A `Tensor` of type `string`.
A scalar string tensor containing the regular expression to match the input.
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
A `Tensor` of type `bool`.
</td>
</tr>

</table>

