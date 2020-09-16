description: Adds bias to value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.bias_add" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.bias_add

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_ops.py#L2738-L2797">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adds `bias` to `value`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.bias_add`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.bias_add(
    value, bias, data_format=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is (mostly) a special case of <a href="../../tf/math/add.md"><code>tf.add</code></a> where `bias` is restricted to 1-D.
Broadcasting is supported, so `value` may have any number of dimensions.
Unlike <a href="../../tf/math/add.md"><code>tf.add</code></a>, the type of `bias` is allowed to differ from `value` in the
case where both types are quantized.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A `Tensor` with type `float`, `double`, `int64`, `int32`, `uint8`,
`int16`, `int8`, `complex64`, or `complex128`.
</td>
</tr><tr>
<td>
`bias`
</td>
<td>
A 1-D `Tensor` with size matching the channel dimension of `value`.
Must be the same type as `value` unless `value` is a quantized type,
in which case a different quantized type may be used.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string. 'N...C' and 'NC...' are supported. If `None` (the
default) is specified then 'N..C' is assumed.
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
A `Tensor` with the same type as `value`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
ValueError if data format is unrecognized, if `value` has less than two
dimensions when `data_format` is 'N..C'/`None` or `value` has less
then three dimensions when `data_format` is `NC..`, if `bias` does not
have exactly one dimension (is a vector), or if the size of `bias`
does not match the size of the channel dimension of `value`.
</td>
</tr>

</table>

