page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sets.intersection


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/sets/intersection">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sets_impl.py#L136-L201">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute set intersection of elements in last dimension of `a` and `b`.

### Aliases:

* <a href="/api_docs/python/tf/sets/intersection"><code>tf.compat.v1.sets.intersection</code></a>
* <a href="/api_docs/python/tf/sets/intersection"><code>tf.compat.v1.sets.set_intersection</code></a>
* <a href="/api_docs/python/tf/sets/intersection"><code>tf.compat.v2.sets.intersection</code></a>
* <a href="/api_docs/python/tf/sets/intersection"><code>tf.contrib.metrics.set_intersection</code></a>
* <a href="/api_docs/python/tf/sets/intersection"><code>tf.sets.set_intersection</code></a>


``` python
tf.sets.intersection(
    a,
    b,
    validate_indices=True
)
```



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
  a = tf.SparseTensor(list(a.keys()), list(a.values()), dense_shape=[2,2,2])

  # b = np.array([[{1}, {}], [{4}, {5, 6, 7, 8}]])
  b = collections.OrderedDict([
      ((0, 0, 0), 1),
      ((1, 0, 0), 4),
      ((1, 1, 0), 5),
      ((1, 1, 1), 6),
      ((1, 1, 2), 7),
      ((1, 1, 3), 8),
  ])
  b = tf.SparseTensor(list(b.keys()), list(b.values()), dense_shape=[2, 2, 4])

  # `tf.sets.intersection` is applied to each aligned pair of sets.
  tf.sets.intersection(a, b)

  # The result will be equivalent to either of:
  #
  # np.array([[{1}, {}], [{4}, {5, 6}]])
  #
  # collections.OrderedDict([
  #     ((0, 0, 0), 1),
  #     ((1, 0, 0), 4),
  #     ((1, 1, 0), 5),
  #     ((1, 1, 1), 6),
  # ])
```

#### Args:


* <b>`a`</b>: `Tensor` or `SparseTensor` of the same type as `b`. If sparse, indices
    must be sorted in row-major order.
* <b>`b`</b>: `Tensor` or `SparseTensor` of the same type as `a`. If sparse, indices
    must be sorted in row-major order.
* <b>`validate_indices`</b>: Whether to validate the order and range of sparse indices
   in `a` and `b`.


#### Returns:

A `SparseTensor` whose shape is the same rank as `a` and `b`, and all but
the last dimension the same. Elements along the last dimension contain the
intersections.
