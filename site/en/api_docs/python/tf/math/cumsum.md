description: Compute the cumulative sum of the tensor x along axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.cumsum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.cumsum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L3750-L3819">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compute the cumulative sum of the tensor `x` along `axis`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.cumsum`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.cumsum`, `tf.compat.v1.math.cumsum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.cumsum(
    x, axis=0, exclusive=(False), reverse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

By default, this op performs an inclusive cumsum, which means that the first
element of the input is identical to the first element of the output:
For example:

```
>>> # tf.cumsum([a, b, c])   # [a, a + b, a + b + c]
>>> x = tf.constant([2, 4, 6, 8])
>>> tf.cumsum(x)
<tf.Tensor: shape=(4,), dtype=int32,
numpy=array([ 2,  6, 12, 20], dtype=int32)>
```

```
>>> # using varying `axis` values
>>> y = tf.constant([[2, 4, 6, 8], [1,3,5,7]])
>>> tf.cumsum(y, axis=0)
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[ 2,  4,  6,  8],
       [ 3,  7, 11, 15]], dtype=int32)>
>>> tf.cumsum(y, axis=1)
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[ 2,  6, 12, 20],
       [ 1,  4,  9, 16]], dtype=int32)>
```

By setting the `exclusive` kwarg to `True`, an exclusive cumsum is performed
instead:

```
>>> # tf.cumsum([a, b, c], exclusive=True)  => [0, a, a + b]
>>> x = tf.constant([2, 4, 6, 8])
>>> tf.cumsum(x, exclusive=True)
<tf.Tensor: shape=(4,), dtype=int32,
numpy=array([ 0,  2,  6, 12], dtype=int32)>
```

By setting the `reverse` kwarg to `True`, the cumsum is performed in the
opposite direction:

```
>>> # tf.cumsum([a, b, c], reverse=True)  # [a + b + c, b + c, c]
>>> x = tf.constant([2, 4, 6, 8])
>>> tf.cumsum(x, reverse=True)
<tf.Tensor: shape=(4,), dtype=int32,
numpy=array([20, 18, 14,  8], dtype=int32)>
```

This is more efficient than using separate <a href="../../tf/reverse.md"><code>tf.reverse</code></a> ops.
The `reverse` and `exclusive` kwargs can also be combined:

```
>>> # tf.cumsum([a, b, c], exclusive=True, reverse=True)  # [b + c, c, 0]
>>> x = tf.constant([2, 4, 6, 8])
>>> tf.cumsum(x, exclusive=True, reverse=True)
<tf.Tensor: shape=(4,), dtype=int32,
numpy=array([18, 14,  8,  0], dtype=int32)>
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
A `Tensor`. Must be one of the following types: `float32`, `float64`,
`int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`,
`complex128`, `qint8`, `quint8`, `qint32`, `half`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A `Tensor` of type `int32` (default: 0). Must be in the range
`[-rank(x), rank(x))`.
</td>
</tr><tr>
<td>
`exclusive`
</td>
<td>
If `True`, perform exclusive cumsum.
</td>
</tr><tr>
<td>
`reverse`
</td>
<td>
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

