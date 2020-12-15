description: Computes element-wise square root of the input tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.sqrt" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.sqrt

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L4739-L4773">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes element-wise square root of the input tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.sqrt`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.sqrt`, `tf.compat.v1.sqrt`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.sqrt(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: This operation does not support integer types.

```
>>> x = tf.constant([[4.0], [16.0]])
>>> tf.sqrt(x)
<tf.Tensor: shape=(2, 1), dtype=float32, numpy=
  array([[2.],
         [4.]], dtype=float32)>
>>> y = tf.constant([[-4.0], [16.0]])
>>> tf.sqrt(y)
<tf.Tensor: shape=(2, 1), dtype=float32, numpy=
  array([[nan],
         [ 4.]], dtype=float32)>
>>> z = tf.constant([[-1.0], [16.0]], dtype=tf.complex128)
>>> tf.sqrt(z)
<tf.Tensor: shape=(2, 1), dtype=complex128, numpy=
  array([[0.0+1.j],
         [4.0+0.j]])>
```

Note: In order to support complex complex, please provide an input tensor
of `complex64` or `complex128`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bfloat16`, `half`, `float32`, `float64`,
`complex64`, `complex128`
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of same size, type and sparsity as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.sqrt(x.values, ...), x.dense_shape)`
</td>
</tr>

</table>

