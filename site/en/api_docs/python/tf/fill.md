description: Creates a tensor filled with a scalar value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.fill" />
<meta itemprop="path" content="Stable" />
</div>

# tf.fill

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L200-L241">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a tensor filled with a scalar value.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.fill`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.fill(
    dims, value, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/ones.md"><code>tf.ones</code></a>, <a href="../tf/zeros.md"><code>tf.zeros</code></a>, <a href="../tf/one_hot.md"><code>tf.one_hot</code></a>, <a href="../tf/eye.md"><code>tf.eye</code></a>.

This operation creates a tensor of shape `dims` and fills it with `value`.

#### For example:



```
>>> tf.fill([2, 3], 9)
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[9, 9, 9],
       [9, 9, 9]], dtype=int32)>
```

<a href="../tf/fill.md"><code>tf.fill</code></a> evaluates at graph runtime and supports dynamic shapes based on
other runtime `tf.Tensors`, unlike <a href="../tf/constant.md"><code>tf.constant(value, shape=dims)</code></a>, which
embeds the value as a `Const` node.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dims`
</td>
<td>
A 1-D sequence of non-negative numbers. Represents the shape of the
output <a href="../tf/Tensor.md"><code>tf.Tensor</code></a>. Entries should be of type: `int32`, `int64`.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A value to fill the returned <a href="../tf/Tensor.md"><code>tf.Tensor</code></a>.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional string. The name of the output <a href="../tf/Tensor.md"><code>tf.Tensor</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> with shape `dims` and the same dtype as `value`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`InvalidArgumentError`
</td>
<td>
`dims` contains negative entries.
</td>
</tr><tr>
<td>
`NotFoundError`
</td>
<td>
`dims` contains non-integer entries.
</td>
</tr>
</table>




#### Numpy Compatibility
Similar to `np.full`. In `numpy`, more parameters are supported. Passing a
number argument as the shape (`np.full(5, value)`) is valid in `numpy` for
specifying a 1-D shaped result, while TensorFlow does not support this syntax.

