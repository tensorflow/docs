description: Creates a tensor with all elements set to zero.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.zeros" />
<meta itemprop="path" content="Stable" />
</div>

# tf.zeros

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L2754-L2808">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a tensor with all elements set to zero.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.zeros`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.zeros(
    shape, dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/zeros_like.md"><code>tf.zeros_like</code></a>, <a href="../tf/ones.md"><code>tf.ones</code></a>, <a href="../tf/fill.md"><code>tf.fill</code></a>, <a href="../tf/eye.md"><code>tf.eye</code></a>.

This operation returns a tensor of type `dtype` with shape `shape` and
all elements set to zero.

```
>>> tf.zeros([3, 4], tf.int32)
<tf.Tensor: shape=(3, 4), dtype=int32, numpy=
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]], dtype=int32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A `list` of integers, a `tuple` of integers, or
a 1-D `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The DType of an element in the resulting `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional string. A name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with all elements set to zero.
</td>
</tr>

</table>

