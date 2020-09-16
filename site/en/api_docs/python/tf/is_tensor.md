description: Checks whether x is a TF-native type that can be passed to many TF ops.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.is_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.is_tensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/tensor_util.py#L986-L1014">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Checks whether `x` is a TF-native type that can be passed to many TF ops.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.is_tensor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.is_tensor(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->

Use is_tensor to differentiate types that can ingested by TensorFlow ops
without any conversion (e.g., <a href="../tf/Tensor.md"><code>tf.Tensor</code></a>, <a href="../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>, and
<a href="../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>) from types that need to be converted into tensors before
they are ingested (e.g., numpy `ndarray` and Python scalars).

For example, in the following code block:

```python
if not tf.is_tensor(t):
  t = tf.convert_to_tensor(t)
return t.dtype
```

we check to make sure that `t` is a tensor (and convert it if not) before
accessing its `shape` and `dtype`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A python object to check.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
`True` if `x` is a tensor or "tensor-like", `False` if not.
</td>
</tr>

</table>

