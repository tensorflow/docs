description: Computes the theoretical and numeric Jacobian of f.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.test.compute_gradient" />
<meta itemprop="path" content="Stable" />
</div>

# tf.test.compute_gradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/gradient_checker_v2.py#L294-L332">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the theoretical and numeric Jacobian of `f`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.test.compute_gradient(
    f, x, delta=0.001
)
</code></pre>



<!-- Placeholder for "Used in" -->

With y = f(x), computes the theoretical and numeric Jacobian dy/dx.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`f`
</td>
<td>
the function.
</td>
</tr><tr>
<td>
`x`
</td>
<td>
the arguments for the function as a list or tuple of values convertible
to a Tensor.
</td>
</tr><tr>
<td>
`delta`
</td>
<td>
(optional) perturbation used to compute numeric Jacobian.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A pair of lists, where the first is a list of 2-d numpy arrays representing
the theoretical Jacobians for each argument, and the second list is the
numerical ones. Each 2-d array has "y_size" rows
and "x_size" columns where "x_size" is the number of elements in the
corresponding argument and "y_size" is the number of elements in f(x).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If result is empty but the gradient is nonzero.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If x is not list, but any other type.
</td>
</tr>
</table>



#### Example:


```python
@tf.function
def test_func(x):
  return x*x

theoretical, numerical = tf.test.compute_gradient(test_func, [1.0])
theoretical, numerical
# ((array([[2.]], dtype=float32),), (array([[2.000004]], dtype=float32),))
```