description: Computes reciprocal of square root of x element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.rsqrt" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.rsqrt

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L4984-L5006">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes reciprocal of square root of x element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.rsqrt`, `tf.compat.v1.rsqrt`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.rsqrt(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### For example:



```
>>> x = tf.constant([2., 0., -2.])
>>> tf.math.rsqrt(x)
<tf.Tensor: shape=(3,), dtype=float32,
numpy=array([0.707, inf, nan], dtype=float32)>
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>. Has the same type as `x`.
</td>
</tr>

</table>

