description: Computes exponential of x element-wise.  \\(y = e^x\\).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.exp" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.exp

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L4907-L4953">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes exponential of x element-wise.  \\(y = e^x\\).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.exp`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.exp`, `tf.compat.v1.math.exp`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.exp(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function computes the exponential of the input tensor element-wise.
i.e. <a href="../../tf/math/exp.md"><code>math.exp(x)</code></a> or \\(e^x\\), where `x` is the input tensor.
\\(e\\) denotes Euler's number and is approximately equal to 2.718281.
Output is positive for any real input.

```
>>> x = tf.constant(2.0)
>>> tf.math.exp(x)
<tf.Tensor: shape=(), dtype=float32, numpy=7.389056>
```

```
>>> x = tf.constant([2.0, 8.0])
>>> tf.math.exp(x)
<tf.Tensor: shape=(2,), dtype=float32,
numpy=array([   7.389056, 2980.958   ], dtype=float32)>
```

For complex numbers, the exponential value is calculated as
$$
e^{x+iy} = {e^x} {e^{iy}} = {e^x} ({\cos (y) + i \sin (y)})
$$

For `1+1j` the value would be computed as:
$$
e^1 (\cos (1) + i \sin (1)) = 2.7182817 \times (0.5403023+0.84147096j)
$$

```
>>> x = tf.constant(1 + 1j)
>>> tf.math.exp(x)
<tf.Tensor: shape=(), dtype=complex128,
numpy=(1.4686939399158851+2.2873552871788423j)>
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>. Must be one of the following types: `bfloat16`, `half`,
`float32`, `float64`, `complex64`, `complex128`.
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>. Has the same type as `x`.
</td>
</tr>

</table>




#### Numpy Compatibility
Equivalent to np.exp

