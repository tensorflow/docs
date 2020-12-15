description: Converts each entry in the given tensor to strings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.as_string" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.as_string

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts each entry in the given tensor to strings.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.as_string`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.as_string`, `tf.compat.v1.dtypes.as_string`, `tf.compat.v1.strings.as_string`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.as_string(
    input, precision=-1, scientific=(False), shortest=(False), width=-1, fill='',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Supports many numeric types and boolean.

For Unicode, see the
[https://www.tensorflow.org/tutorials/representation/unicode](Working with Unicode text)
tutorial.

#### Examples:



```
>>> tf.strings.as_string([3, 2])
<tf.Tensor: shape=(2,), dtype=string, numpy=array([b'3', b'2'], dtype=object)>
>>> tf.strings.as_string([3.1415926, 2.71828], precision=2).numpy()
array([b'3.14', b'2.72'], dtype=object)
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
A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `float32`, `float64`, `bool`.
</td>
</tr><tr>
<td>
`precision`
</td>
<td>
An optional `int`. Defaults to `-1`.
The post-decimal precision to use for floating point numbers.
Only used if precision > -1.
</td>
</tr><tr>
<td>
`scientific`
</td>
<td>
An optional `bool`. Defaults to `False`.
Use scientific notation for floating point numbers.
</td>
</tr><tr>
<td>
`shortest`
</td>
<td>
An optional `bool`. Defaults to `False`.
Use shortest representation (either scientific or standard) for
floating point numbers.
</td>
</tr><tr>
<td>
`width`
</td>
<td>
An optional `int`. Defaults to `-1`.
Pad pre-decimal numbers to this width.
Applies to both floating point and integer numbers.
Only used if width > -1.
</td>
</tr><tr>
<td>
`fill`
</td>
<td>
An optional `string`. Defaults to `""`.
The value to pad if width > -1.  If empty, pads with spaces.
Another typical value is '0'.  String cannot be longer than 1 character.
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

