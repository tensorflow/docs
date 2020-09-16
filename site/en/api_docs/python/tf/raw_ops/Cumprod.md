description: Compute the cumulative product of the tensor x along axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Cumprod" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Cumprod

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Compute the cumulative product of the tensor `x` along `axis`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Cumprod`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Cumprod(
    x, axis, exclusive=(False), reverse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

By default, this op performs an inclusive cumprod, which means that the first
element of the input is identical to the first element of the output:

```python
tf.cumprod([a, b, c])  # => [a, a * b, a * b * c]
```

By setting the `exclusive` kwarg to `True`, an exclusive cumprod is
performed instead:

```python
tf.cumprod([a, b, c], exclusive=True)  # => [1, a, a * b]
```

By setting the `reverse` kwarg to `True`, the cumprod is performed in the
opposite direction:

```python
tf.cumprod([a, b, c], reverse=True)  # => [a * b * c, b * c, c]
```

This is more efficient than using separate <a href="../../tf/reverse.md"><code>tf.reverse</code></a> ops.

The `reverse` and `exclusive` kwargs can also be combined:

```python
tf.cumprod([a, b, c], exclusive=True, reverse=True)  # => [b * c, c, 1]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
A `Tensor`. Must be one of the following types: `float32`, `float64`,
`int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`,
`complex128`, `qint8`, `quint8`, `qint32`, `half`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A `Tensor` of type `int32` (default: 0). Must be in the range
`[-rank(x), rank(x))`.
</td>
</tr><tr>
<td>
`exclusive`
</td>
<td>
An optional `bool`. Defaults to `False`.
If `True`, perform exclusive cumprod.
</td>
</tr><tr>
<td>
`reverse`
</td>
<td>
An optional `bool`. Defaults to `False`.
A `bool` (default: False).
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
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>

