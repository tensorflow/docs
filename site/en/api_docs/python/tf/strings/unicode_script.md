description: Determine the script codes of a given tensor of Unicode integer code points.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.unicode_script" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.unicode_script

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Determine the script codes of a given tensor of Unicode integer code points.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.strings.unicode_script`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.unicode_script(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation converts Unicode code points to script codes corresponding to
each code point. Script codes correspond to International Components for
Unicode (ICU) UScriptCode values.

See
[ICU project docs](http://icu-project.org/apiref/icu4c/uscript_8h.html)
for more details on script codes.

For an example, see the unicode strings guide on [unicode scripts]
(https://www.tensorflow.org/tutorials/load_data/unicode#representing_unicode).

Returns -1 (USCRIPT_INVALID_CODE) for invalid codepoints. Output shape will
match input shape.

#### Examples:



```
>>> tf.strings.unicode_script([1, 31, 38])
<tf.Tensor: shape=(3,), dtype=int32, numpy=array([0, 0, 0], dtype=int32)>
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
A `Tensor` of type `int32`. A Tensor of int32 Unicode code points.
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
A `Tensor` of type `int32`.
</td>
</tr>

</table>

