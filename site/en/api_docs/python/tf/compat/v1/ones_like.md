description: Creates a tensor with all elements set to 1.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.ones_like" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.ones_like

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/array_ops.py#L2853-L2883">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a tensor with all elements set to 1.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.ones_like(
    tensor, dtype=None, name=None, optimize=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../../../tf/ones.md"><code>tf.ones</code></a>.

Given a single tensor (`tensor`), this operation returns a tensor of the same
type and shape as `tensor` with all elements set to 1. Optionally, you can
specify a new type (`dtype`) for the returned tensor.

#### For example:



```python
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.ones_like(tensor)  # [[1, 1, 1], [1, 1, 1]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
A type for the returned `Tensor`. Must be `float32`, `float64`,
`int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `complex64`,
`complex128` or `bool`.
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
`optimize`
</td>
<td>
if true, attempt to statically determine the shape of 'tensor' and
encode it as a constant.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with all elements set to 1.
</td>
</tr>

</table>

