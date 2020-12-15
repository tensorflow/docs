description: Returns an element-wise indication of the sign of a number.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.sign" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.sign

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L719-L762">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns an element-wise indication of the sign of a number.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.sign`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.sign`, `tf.compat.v1.sign`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.sign(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`y = sign(x) = -1 if x < 0; 0 if x == 0; 1 if x > 0`.

For complex numbers, `y = sign(x) = x / |x| if x != 0, otherwise y = 0`.

#### Example usage:



```
>>> # real number
>>> tf.math.sign([0., 2., -3.])
<tf.Tensor: shape=(3,), dtype=float32,
numpy=array([ 0.,  1., -1.], dtype=float32)>
```

```
>>> # complex number
>>> tf.math.sign([1 + 1j, 0 + 0j])
<tf.Tensor: shape=(2,), dtype=complex128,
numpy=array([0.70710678+0.70710678j, 0.        +0.j        ])>
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
A Tensor. Must be one of the following types: bfloat16, half, float32,
float64, int32, int64, complex64, complex128.
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
A Tensor. Has the same type as x.

If x is a SparseTensor, returns SparseTensor(x.indices,
tf.math.sign(x.values, ...), x.dense_shape).

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.sign(x.values, ...), x.dense_shape)`
</td>
</tr>

</table>

