description: Computes sigmoid of x element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.sigmoid" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.sigmoid

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L3594-L3643">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes sigmoid of `x` element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.nn.sigmoid`, `tf.sigmoid`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.sigmoid`, `tf.compat.v1.nn.sigmoid`, `tf.compat.v1.sigmoid`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.sigmoid(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Formula for calculating sigmoid(x): `y = 1 / (1 + exp(-x))`.

For x \in (-inf, inf) => sigmoid(x) \in (0, 1)

#### Example Usage:



If a positive number is large, then its sigmoid will approach to 1 since the
formula will be `y = <large_num> / (1 + <large_num>)`

```
>>> x = tf.constant([0.0, 1.0, 50.0, 100.0])
>>> tf.math.sigmoid(x)
<tf.Tensor: shape=(4,), dtype=float32,
numpy=array([0.5      , 0.7310586, 1.       , 1.       ], dtype=float32)>
```

If a negative number is large, its sigmoid will approach to 0 since the
formula will be `y = 1 / (1 + <large_num>)`

```
>>> x = tf.constant([-100.0, -50.0, -1.0, 0.0])
>>> tf.math.sigmoid(x)
<tf.Tensor: shape=(4,), dtype=float32, numpy=
array([0.0000000e+00, 1.9287499e-22, 2.6894143e-01, 0.5],
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
A Tensor with type `float16`, `float32`, `float64`, `complex64`, or
`complex128`.
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
A Tensor with the same type as `x`.
</td>
</tr>

</table>



#### Usage Example:



```
>>> x = tf.constant([-128.0, 0.0, 128.0], dtype=tf.float32)
>>> tf.sigmoid(x)
<tf.Tensor: shape=(3,), dtype=float32,
numpy=array([0. , 0.5, 1. ], dtype=float32)>
```



#### Scipy Compatibility
Equivalent to scipy.special.expit

