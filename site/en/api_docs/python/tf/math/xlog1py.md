description: Compute x * log1p(y).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.xlog1py" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.xlog1py

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L4742-L4776">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compute x * log1p(y).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.xlog1py`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.xlog1py(
    x, y, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given `x` and `y`, compute `x * log1p(y)`. This function safely returns
zero when `x = 0`, no matter what the value of `y` is.

#### Example:



```
>>> tf.math.xlog1py(0., 1.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.>
>>> tf.math.xlog1py(1., 1.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.6931472>
>>> tf.math.xlog1py(2., 2.)
<tf.Tensor: shape=(), dtype=float32, numpy=2.1972246>
>>> tf.math.xlog1py(0., -1.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.>
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bfloat16`, `half`, `float32`, `float64`,
`complex64`, `complex128`
</td>
</tr><tr>
<td>
`y`
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
`x * log1p(y)`.
</td>
</tr>

</table>




#### Scipy Compatibility
Equivalent to scipy.special.xlog1py

