description: Computes the maximum of elements across dimensions of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.reduce_max" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.reduce_max

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L2701-L2746">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the maximum of elements across dimensions of a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.reduce_max`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.reduce_max(
    input_tensor, axis=None, keepdims=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
of the entries in `axis`, which must be unique. If `keepdims` is true, the
reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

#### Usage example:



```
>>> x = tf.constant([5, 1, 2, 4])
>>> print(tf.reduce_max(x))
tf.Tensor(5, shape=(), dtype=int32)
>>> x = tf.constant([-5, -1, -2, -4])
>>> print(tf.reduce_max(x))
tf.Tensor(-1, shape=(), dtype=int32)
>>> x = tf.constant([4, float('nan')])
>>> print(tf.reduce_max(x))
tf.Tensor(nan, shape=(), dtype=float32)
>>> x = tf.constant([float('nan'), float('nan')])
>>> print(tf.reduce_max(x))
tf.Tensor(nan, shape=(), dtype=float32)
>>> x = tf.constant([float('-inf'), float('inf')])
>>> print(tf.reduce_max(x))
tf.Tensor(inf, shape=(), dtype=float32)
```

See the numpy docs for `np.amax` and `np.nanmax` behavior.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_tensor`
</td>
<td>
The tensor to reduce. Should have real numeric type.
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

