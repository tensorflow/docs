description: Applies softmax to a batched N-D SparseTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.softmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.softmax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/sparse_ops.py#L2542-L2595">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies softmax to a batched N-D `SparseTensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.softmax`, `tf.compat.v1.sparse_softmax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.softmax(
    sp_input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The inputs represent an N-D SparseTensor with logical shape `[..., B, C]`
(where `N >= 2`), and with indices sorted in the canonical lexicographic
order.

This op is equivalent to applying the normal <a href="../../tf/nn/softmax.md"><code>tf.nn.softmax()</code></a> to each
innermost logical submatrix with shape `[B, C]`, but with the catch that *the
implicitly zero elements do not participate*.  Specifically, the algorithm is
equivalent to:

  (1) Applies <a href="../../tf/nn/softmax.md"><code>tf.nn.softmax()</code></a> to a densified view of each innermost
      submatrix with shape `[B, C]`, along the size-C dimension;
  (2) Masks out the original implicitly-zero locations;
  (3) Renormalizes the remaining elements.

Hence, the `SparseTensor` result has exactly the same non-zero indices and
shape.

#### Example:



```python
# First batch:
# [?   e.]
# [1.  ? ]
# Second batch:
# [e   ? ]
# [e   e ]
shape = [2, 2, 2]  # 3-D SparseTensor
values = np.asarray([[[0., np.e], [1., 0.]], [[np.e, 0.], [np.e, np.e]]])
indices = np.vstack(np.where(values)).astype(np.int64).T

result = tf.sparse.softmax(tf.sparse.SparseTensor(indices, values, shape))
# ...returning a 3-D SparseTensor, equivalent to:
# [?   1.]     [1    ?]
# [1.  ? ] and [.5  .5]
# where ? means implicitly zero.
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
N-D `SparseTensor`, where `N >= 2`.
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
N-D `SparseTensor` representing the results.
</td>
</tr>
</table>

