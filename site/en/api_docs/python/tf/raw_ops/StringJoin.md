description: Joins the strings in the given list of string tensors into one tensor;

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.StringJoin" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.StringJoin

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Joins the strings in the given list of string tensors into one tensor;

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StringJoin`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StringJoin(
    inputs, separator='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

with the given separator (default is an empty separator).

#### Examples:



```
>>> s = ["hello", "world", "tensorflow"]
>>> tf.strings.join(s, " ")
<tf.Tensor: shape=(), dtype=string, numpy=b'hello world tensorflow'>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of at least 1 `Tensor` objects with type `string`.
A list of string tensors.  The tensors must all have the same shape,
or be scalars.  Scalars may be mixed in; these will be broadcast to the shape
of non-scalar inputs.
</td>
</tr><tr>
<td>
`separator`
</td>
<td>
An optional `string`. Defaults to `""`.
string, an optional join separator.
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

