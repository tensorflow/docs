description: Computes the mean of elements across dimensions of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.reduce_mean" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.reduce_mean

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/math_ops.py#L1943-L2006">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the mean of elements across dimensions of a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.reduce_mean`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.reduce_mean(
    input_tensor, axis=None, keepdims=None, name=None, reduction_indices=None,
    keep_dims=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reduces `input_tensor` along the dimensions given in `axis` by computing the
mean of elements across the dimensions in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single
element is returned.

#### For example:



```
>>> x = tf.constant([[1., 1.], [2., 2.]])
>>> tf.reduce_mean(x)
<tf.Tensor: shape=(), dtype=float32, numpy=1.5>
>>> tf.reduce_mean(x, 0)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([1.5, 1.5], dtype=float32)>
>>> tf.reduce_mean(x, 1)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([1., 2.], dtype=float32)>
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
The tensor to reduce. Should have numeric type.
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
A name for the operation (optional).
</td>
</tr><tr>
<td>
`reduction_indices`
</td>
<td>
The old (deprecated) name for axis.
</td>
</tr><tr>
<td>
`keep_dims`
</td>
<td>
Deprecated alias for `keepdims`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The reduced tensor.
</td>
</tr>

</table>




#### Numpy Compatibility
Equivalent to np.mean

Please note that `np.mean` has a `dtype` parameter that could be used to
specify the output type. By default this is `dtype=float64`. On the other
hand, <a href="../../../tf/math/reduce_mean.md"><code>tf.reduce_mean</code></a> has an aggressive type inference from `input_tensor`,
for example:

```
>>> x = tf.constant([1, 0, 1, 0])
>>> tf.reduce_mean(x)
<tf.Tensor: shape=(), dtype=int32, numpy=0>
>>> y = tf.constant([1., 0., 1., 0.])
>>> tf.reduce_mean(y)
<tf.Tensor: shape=(), dtype=float32, numpy=0.5>
```


