description: Returns the shape of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.shape" />
<meta itemprop="path" content="Stable" />
</div>

# tf.shape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L557-L601">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the shape of a tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.shape(
    input, out_type=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/size.md"><code>tf.size</code></a>, <a href="../tf/rank.md"><code>tf.rank</code></a>.

<a href="../tf/shape.md"><code>tf.shape</code></a> returns a 1-D integer tensor representing the shape of `input`.

#### For example:



```
>>> t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
>>> tf.shape(t)
<tf.Tensor: shape=(3,), dtype=int32, numpy=array([2, 2, 3], dtype=int32)>
```

Note: When using symbolic tensors, such as when using the Keras API,
tf.shape() will return the shape of the symbolic tensor.

```
>>> a = tf.keras.layers.Input((None, 10))
>>> tf.shape(a)
<tf.Tensor ... shape=(3,) dtype=int32>
```

In these cases, using <a href="../tf/Tensor.md#shape"><code>tf.Tensor.shape</code></a> will return more informative results.

```
>>> a.shape
TensorShape([None, None, 10])
```

(The first `None` represents the as yet unknown batch size.)

<a href="../tf/shape.md"><code>tf.shape</code></a> and <a href="../tf/Tensor.md#shape"><code>Tensor.shape</code></a> should be identical in eager mode.  Within
<a href="../tf/function.md"><code>tf.function</code></a> or within a <a href="../tf/compat/v1.md"><code>compat.v1</code></a> context, not all dimensions may be
known until execution time. Hence when defining custom layers and models
for graph mode, prefer the dynamic <a href="../tf/shape.md"><code>tf.shape(x)</code></a> over the static `x.shape`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` or `SparseTensor`.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
(Optional) The specified output type of the operation (`int32` or
`int64`). Defaults to <a href="../tf.md#int32"><code>tf.int32</code></a>.
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
A `Tensor` of type `out_type`.
</td>
</tr>

</table>

