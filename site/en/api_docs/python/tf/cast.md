description: Casts a tensor to a new type.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.cast" />
<meta itemprop="path" content="Stable" />
</div>

# tf.cast

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/math_ops.py#L732-L792">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Casts a tensor to a new type.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.dtypes.cast`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.cast`, `tf.compat.v1.dtypes.cast`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.cast(
    x, dtype, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The operation casts `x` (in case of `Tensor`) or `x.values`
(in case of `SparseTensor` or `IndexedSlices`) to `dtype`.

#### For example:



```
>>> x = tf.constant([1.8, 2.2], dtype=tf.float32)
>>> tf.dtypes.cast(x, tf.int32)
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 2], dtype=int32)>
```

The operation supports data types (for `x` and `dtype`) of
`uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`,
`float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`.
In case of casting from complex types (`complex64`, `complex128`) to real
types, only the real part of `x` is returned. In case of casting from real
types to complex types (`complex64`, `complex128`), the imaginary part of the
returned value is set to `0`. The handling of complex types here matches the
behavior of numpy.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor` or `SparseTensor` or `IndexedSlices` of numeric type. It could
be `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`,
`int64`, `float16`, `float32`, `float64`, `complex64`, `complex128`,
`bfloat16`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The destination type. The list of supported dtypes is the same as
`x`.
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
A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` and
same type as `dtype`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `x` cannot be cast to the `dtype`.
</td>
</tr>
</table>

