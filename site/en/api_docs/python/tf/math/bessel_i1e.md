description: Computes the Bessel i1e function of x element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.bessel_i1e" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.bessel_i1e

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/special_math_ops.py#L335-L358">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the Bessel i1e function of `x` element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.math.special.bessel_i1e`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.bessel_i1e`, `tf.compat.v1.math.special.bessel_i1e`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.bessel_i1e(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Modified Bessel function of order 1.

```
>>> tf.math.special.bessel_i1e([-1., -0.5, 0.5, 1.]).numpy()
array([-0.20791042, -0.15642083,  0.15642083,  0.20791042], dtype=float32)
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
A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
`float32`, `float64`.
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
A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.



If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.bessel_i1e(x.values, ...), x.dense_shape)`
</td>
</tr>

</table>



#### Scipy Compatibility
Equivalent to scipy.special.i1e

