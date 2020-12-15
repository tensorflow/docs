description: Compute set difference of elements in last dimension of a and b.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sets.difference" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sets.difference

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/sets_impl.py#L209-L288">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compute set difference of elements in last dimension of `a` and `b`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sets.difference`, `tf.compat.v1.sets.set_difference`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sets.difference(
    a, b, aminusb=(True), validate_indices=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

All but the last dimension of `a` and `b` must match.

#### Example:



```python
  import tensorflow as tf
  import collections

  # Represent the following array of sets as a sparse tensor:
  # a = np.array([[{1, 2}, {3}], [{4}, {5, 6}]])
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

  # np.array([[{1, 3}, {2}], [{4, 5}, {5, 6, 7, 8}]])
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

  # `set_difference` is applied to each aligned pair of sets.
  tf.sets.difference(a, b)

  # The result will be equivalent to either of:
  #
  # np.array([[{2}, {3}], [{}, {}]])
  #
  # collections.OrderedDict([
  #     ((0, 0, 0), 2),
  #     ((0, 1, 0), 3),
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
`aminusb`
</td>
<td>
Whether to subtract `b` from `a`, vs vice versa.
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
differences.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If inputs are invalid types, or if `a` and `b` have
different types.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `a` is sparse and `b` is dense.
</td>
</tr><tr>
<td>
`errors_impl.InvalidArgumentError`
</td>
<td>
If the shapes of `a` and `b` do not
match in any dimension other than the last dimension.
</td>
</tr>
</table>

