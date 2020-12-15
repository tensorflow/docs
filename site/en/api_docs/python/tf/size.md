description: Returns the size of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.size" />
<meta itemprop="path" content="Stable" />
</div>

# tf.size

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L700-L731">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the size of a tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.size(
    input, out_type=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/shape.md"><code>tf.shape</code></a>.

Returns a 0-D `Tensor` representing the number of elements in `input`
of type `out_type`. Defaults to tf.int32.

#### For example:



```
>>> t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
>>> tf.size(t)
<tf.Tensor: shape=(), dtype=int32, numpy=12>
```

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
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
(Optional) The specified non-quantized numeric output type of the
operation. Defaults to <a href="../tf.md#int32"><code>tf.int32</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `out_type`. Defaults to <a href="../tf.md#int32"><code>tf.int32</code></a>.
</td>
</tr>

</table>




#### Numpy Compatibility
Equivalent to np.size()

