description: Adds bias to value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BiasAddV1" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BiasAddV1

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Adds `bias` to `value`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BiasAddV1`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BiasAddV1(
    value, bias, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a deprecated version of BiasAdd and will be soon removed.

This is a special case of <a href="../../tf/math/add.md"><code>tf.add</code></a> where `bias` is restricted to be 1-D.
Broadcasting is supported, so `value` may have any number of dimensions.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
Any number of dimensions.
</td>
</tr><tr>
<td>
`bias`
</td>
<td>
A `Tensor`. Must have the same type as `value`.
1-D with size the last dimension of `value`.
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
A `Tensor`. Has the same type as `value`.
</td>
</tr>

</table>

