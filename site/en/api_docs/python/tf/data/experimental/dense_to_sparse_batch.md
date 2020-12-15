description: A transformation that batches ragged elements into <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>s.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.dense_to_sparse_batch" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.dense_to_sparse_batch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/batching.py#L101-L148">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that batches ragged elements into <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>s.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.dense_to_sparse_batch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.dense_to_sparse_batch(
    batch_size, row_shape
)
</code></pre>



<!-- Placeholder for "Used in" -->

Like <a href="../../../tf/data/Dataset.md#padded_batch"><code>Dataset.padded_batch()</code></a>, this transformation combines multiple
consecutive elements of the dataset, which might have different
shapes, into a single element. The resulting element has three
components (`indices`, `values`, and `dense_shape`), which
comprise a <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> that represents the same data. The
`row_shape` represents the dense shape of each row in the
resulting <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>, to which the effective batch size is
prepended. For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }

a.apply(tf.data.experimental.dense_to_sparse_batch(
    batch_size=2, row_shape=[6])) ==
{
    ([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]],  # indices
     ['a', 'b', 'c', 'a', 'b'],                 # values
     [2, 6]),                                   # dense_shape
    ([[0, 0], [0, 1], [0, 2], [0, 3]],
     ['a', 'b', 'c', 'd'],
     [1, 6])
}
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`batch_size`
</td>
<td>
A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the number of
consecutive elements of this dataset to combine in a single batch.
</td>
</tr><tr>
<td>
`row_shape`
</td>
<td>
A <a href="../../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or <a href="../../../tf.md#int64"><code>tf.int64</code></a> vector tensor-like object
representing the equivalent dense shape of a row in the resulting
<a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>. Each element of this dataset must have the same
rank as `row_shape`, and must have size less than or equal to `row_shape`
in each dimension.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
</td>
</tr>

</table>

