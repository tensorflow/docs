description: Computes the elementwise value of a polynomial.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.polyval" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.polyval

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L4537-L4605">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the elementwise value of a polynomial.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.polyval`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.polyval(
    coeffs, x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `x` is a tensor and `coeffs` is a list n + 1 tensors,
this function returns the value of the n-th order polynomial

   p(x) = coeffs[n-1] + coeffs[n-2] * x + ...  + coeffs[0] * x**(n-1)

evaluated using Horner's method, i.e.

   p(x) = coeffs[n-1] + x * (coeffs[n-2] + ... + x * (coeffs[1] +
          x * coeffs[0]))

#### Usage Example:



```
>>> coefficients = [1.0, 2.5, -4.2]
>>> x = 5.0
>>> y = tf.math.polyval(coefficients, x)
>>> y
<tf.Tensor: shape=(), dtype=float32, numpy=33.3>
```

#### Usage Example:



```
>>> tf.math.polyval([2, 1, 0], 3) # evaluates 2 * (3**2) + 1 * (3**1) + 0 * (3**0)
<tf.Tensor: shape=(), dtype=int32, numpy=21>
```

<a href="../../tf/math/polyval.md"><code>tf.math.polyval</code></a> can also be used in polynomial regression. Taking
advantage of this function can facilitate writing a polynomial equation
as compared to explicitly writing it out, especially for higher degree
polynomials.

```
>>> x = tf.constant(3)
>>> theta1 = tf.Variable(2)
>>> theta2 = tf.Variable(1)
>>> theta3 = tf.Variable(0)
>>> tf.math.polyval([theta1, theta2, theta3], x)
<tf.Tensor: shape=(), dtype=int32, numpy=21>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`coeffs`
</td>
<td>
A list of `Tensor` representing the coefficients of the polynomial.
</td>
</tr><tr>
<td>
`x`
</td>
<td>
A `Tensor` representing the variable of the polynomial.
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
A `tensor` of the shape as the expression p(x) with usual broadcasting
rules for element-wise addition and multiplication applied.
</td>
</tr>

</table>




#### Numpy Compatibility
Equivalent to numpy.polyval.

