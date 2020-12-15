description: Returns the element-wise min of two SparseTensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.minimum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.minimum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L2676-L2711">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the element-wise min of two SparseTensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.minimum`, `tf.compat.v1.sparse_minimum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.minimum(
    sp_a, sp_b, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Assumes the two SparseTensors have the same shape, i.e., no broadcasting.
Example:

```python
sp_zero = sparse_tensor.SparseTensor([[0]], [0], [7])
sp_one = sparse_tensor.SparseTensor([[1]], [1], [7])
res = tf.sparse.minimum(sp_zero, sp_one).eval()
# "res" should be equal to SparseTensor([[0], [1]], [0, 0], [7]).
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_a`
</td>
<td>
a `SparseTensor` operand whose dtype is real, and indices
lexicographically ordered.
</td>
</tr><tr>
<td>
`sp_b`
</td>
<td>
the other `SparseTensor` operand with the same requirements (and the
same shape).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
optional name of the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`output`
</td>
<td>
the output SparseTensor.
</td>
</tr>
</table>

