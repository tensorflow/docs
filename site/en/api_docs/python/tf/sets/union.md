description: Compute set union of elements in last dimension of a and b.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sets.union" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sets.union

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/sets_impl.py#L291-L368">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compute set union of elements in last dimension of `a` and `b`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sets.set_union`, `tf.compat.v1.sets.union`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sets.union(
    a, b, validate_indices=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

All but the last dimension of `a` and `b` must match.

#### Example:



```python
  import tensorflow as tf
  import collections

  # [[{1, 2}, {3}], [{4}, {5, 6}]]
  a = collections.OrderedDict([
      ((0, 0, 0), 1),
      ((0, 0, 1), 2),
      ((0, 1, 0), 3),
      ((1, 0, 0), 4),
      ((1, 1, 0), 5),
      ((1, 1, 1), 6),
  ])
  a = tf.sparse.SparseTensor(list(a.keys()), list(a.values()),
                             dense_shape=[2, 2, 2])

  # [[{1, 3}, {2}], [{4, 5}, {5, 6, 7, 8}]]
  b = collections.OrderedDict([
      ((0, 0, 0), 1),
      ((0, 0, 1), 3),
      ((0, 1, 0), 2),
      ((1, 0, 0), 4),
      ((1, 0, 1), 5),
      ((1, 1, 0), 5),
      ((1, 1, 1), 6),
      ((1, 1, 2), 7),
      ((1, 1, 3), 8),
  ])
  b = tf.sparse.SparseTensor(list(b.keys()), list(b.values()),
                             dense_shape=[2, 2, 4])

  # `set_union` is applied to each aligned pair of sets.
  tf.sets.union(a, b)

  # The result will be a equivalent to either of:
  #
  # np.array([[{1, 2, 3}, {2, 3}], [{4, 5}, {5, 6, 7, 8}]])
  #
  # collections.OrderedDict([
  #     ((0, 0, 0), 1),
  #     ((0, 0, 1), 2),
  #     ((0, 0, 2), 3),
  #     ((0, 1, 0), 2),
  #     ((0, 1, 1), 3),
  #     ((1, 0, 0), 4),
  #     ((1, 0, 1), 5),
  #     ((1, 1, 0), 5),
  #     ((1, 1, 1), 6),
  #     ((1, 1, 2), 7),
  #     ((1, 1, 3), 8),
  # ])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
`Tensor` or `SparseTensor` of the same type as `b`. If sparse, indices
must be sorted in row-major order.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
`Tensor` or `SparseTensor` of the same type as `a`. If sparse, indices
must be sorted in row-major order.
</td>
</tr><tr>
<td>
`validate_indices`
</td>
<td>
Whether to validate the order and range of sparse indices
in `a` and `b`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` whose shape is the same rank as `a` and `b`, and all but
the last dimension the same. Elements along the last dimension contain the
unions.
</td>
</tr>

</table>

