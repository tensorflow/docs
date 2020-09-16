description: Computes the variance of elements across dimensions of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.reduce_variance" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.reduce_variance

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L2315-L2373">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the variance of elements across dimensions of a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.reduce_variance`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.reduce_variance(
    input_tensor, axis=None, keepdims=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

#### For example:



```
>>> x = tf.constant([[1., 2.], [3., 4.]])
>>> tf.math.reduce_variance(x)
<tf.Tensor: shape=(), dtype=float32, numpy=1.25>
>>> tf.math.reduce_variance(x, 0)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([1., 1.], ...)>
>>> tf.math.reduce_variance(x, 1)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([0.25, 0.25], ...)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_tensor`
</td>
<td>
The tensor to reduce. Should have real or complex type.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The dimensions to reduce. If `None` (the default), reduces all
dimensions. Must be in the range `[-rank(input_tensor),
rank(input_tensor))`.
</td>
</tr><tr>
<td>
`keepdims`
</td>
<td>
If true, retains reduced dimensions with length 1.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name scope for the associated operations (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The reduced tensor, of the same dtype as the input_tensor. Note,  for
`complex64` or `complex128` input, the returned `Tensor` will be of type
`float32` or `float64`, respectively.
</td>
</tr>

</table>




#### Numpy Compatibility
Equivalent to np.var

Please note `np.var` has a `dtype` parameter that could be used to specify the
output type. By default this is `dtype=float64`. On the other hand,
<a href="../../tf/math/reduce_variance.md"><code>tf.math.reduce_variance</code></a> has aggressive type inference from `input_tensor`.

