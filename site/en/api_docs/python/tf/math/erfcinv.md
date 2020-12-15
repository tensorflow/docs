description: Computes the inverse of complementary error function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.erfcinv" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.erfcinv

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L4812-L4838">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the inverse of complementary error function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.erfcinv`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.erfcinv(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given `x`, compute the inverse complementary error function of `x`.
This function is the inverse of <a href="../../tf/math/erfc.md"><code>tf.math.erfc</code></a>, and is defined on
`[0, 2]`.

```
>>> tf.math.erfcinv([0., 0.2, 1., 1.5, 2.])
<tf.Tensor: shape=(5,), dtype=float32, numpy=
array([       inf,  0.9061935, -0.       , -0.4769363,       -inf],
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
`Tensor` with type `float` or `double`.
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
Inverse complementary error function of `x`.
</td>
</tr>

</table>




#### Numpy Compatibility
Equivalent to scipy.special.erfcinv

