description: Computes acos of x element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.acos" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.acos

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L5009-L5037">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes acos of x element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.acos`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.acos`, `tf.compat.v1.math.acos`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.acos(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Provided an input tensor, the <a href="../../tf/math/acos.md"><code>tf.math.acos</code></a> operation
returns the inverse cosine of each element of the tensor.
If `y = tf.math.cos(x)` then, `x = tf.math.acos(y)`.

Input range is `[-1, 1]` and the output has a range of `[0, pi]`.

#### For example:



```
>>> x = tf.constant([1.0, -0.5, 3.4, 0.2, 0.0, -2], dtype = tf.float32)
>>> tf.math.acos(x)
<tf.Tensor: shape=(6,), dtype=float32,
numpy= array([0. , 2.0943952, nan, 1.3694383, 1.5707964, nan],
dtype=float32)>
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
A `Tensor`. Must be one of the following types: `bfloat16`, `half`,
`float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`,
`complex64`, `complex128`, `string`.
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
A `Tensor`. Has the same type as x.
</td>
</tr>

</table>

