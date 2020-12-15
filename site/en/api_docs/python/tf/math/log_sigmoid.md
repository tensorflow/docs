description: Computes log sigmoid of x element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.log_sigmoid" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.log_sigmoid

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L3706-L3747">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes log sigmoid of `x` element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.log_sigmoid`, `tf.compat.v1.math.log_sigmoid`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.log_sigmoid(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Specifically, `y = log(1 / (1 + exp(-x)))`.  For numerical stability,
we use `y = -tf.nn.softplus(-x)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A Tensor with type `float32` or `float64`.
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



If a positive number is large, then its log_sigmoid will approach to 0 since
the formula will be `y = log( <large_num> / (1 + <large_num>) )` which
approximates to `log (1)` which is 0.

```
>>> x = tf.constant([0.0, 1.0, 50.0, 100.0])
>>> tf.math.log_sigmoid(x)
<tf.Tensor: shape=(4,), dtype=float32, numpy=
array([-6.9314718e-01, -3.1326169e-01, -1.9287499e-22, -0.0000000e+00],
      dtype=float32)>
```

If a negative number is large, its log_sigmoid will approach to the number
itself since the formula will be `y = log( 1 / (1 + <large_num>) )` which is
`log (1) - log ( (1 + <large_num>) )` which approximates to `- <large_num>`
that is the number itself.

```
>>> x = tf.constant([-100.0, -50.0, -1.0, 0.0])
>>> tf.math.log_sigmoid(x)
<tf.Tensor: shape=(4,), dtype=float32, numpy=
array([-100.       ,  -50.       ,   -1.3132616,   -0.6931472],
      dtype=float32)>
```