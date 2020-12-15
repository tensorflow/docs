description: Returns the element-wise sum of a list of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.accumulate_n" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.accumulate_n

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L3515-L3584">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the element-wise sum of a list of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.accumulate_n`, `tf.compat.v1.math.accumulate_n`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.accumulate_n(
    inputs, shape=None, tensor_dtype=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Optionally, pass `shape` and `tensor_dtype` for shape and type checking,
otherwise, these are inferred.

`accumulate_n` performs the same operation as <a href="../../tf/math/add_n.md"><code>tf.math.add_n</code></a>.

#### For example:



```python
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 0], [0, 6]])
tf.math.accumulate_n([a, b, a])  # [[7, 4], [6, 14]]

# Explicitly pass shape and type
tf.math.accumulate_n([a, b, a], shape=[2, 2], tensor_dtype=tf.int32)
                                                               # [[7,  4],
                                                               #  [6, 14]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of `Tensor` objects, each with same shape and type.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Expected shape of elements of `inputs` (optional). Also controls the
output shape of this op, which may affect type inference in other ops. A
value of `None` means "infer the input shape from the shapes in `inputs`".
</td>
</tr><tr>
<td>
`tensor_dtype`
</td>
<td>
Expected data type of `inputs` (optional). A value of `None`
means "infer the input dtype from `inputs[0]`".
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
A `Tensor` of same shape and type as the elements of `inputs`.
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
If `inputs` don't all have same shape and dtype or the shape
cannot be inferred.
</td>
</tr>
</table>

