page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sets.difference


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sets_impl.py#L204-L280">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute set difference of elements in last dimension of `a` and `b`.

### Aliases:

* `tf.compat.v1.sets.difference`
* `tf.compat.v1.sets.set_difference`
* `tf.compat.v2.sets.difference`


``` python
tf.sets.difference(
    a,
    b,
    aminusb=True,
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
  a = tf.SparseTensor(list(a.keys()), list(a.values()), dense_shape=[2, 2, 2])

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
  b = tf.SparseTensor(list(b.keys()), list(b.values()), dense_shape=[2, 2, 4])

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

#### Args:


* <b>`a`</b>: `Tensor` or `SparseTensor` of the same type as `b`. If sparse, indices
    must be sorted in row-major order.
* <b>`b`</b>: `Tensor` or `SparseTensor` of the same type as `a`. If sparse, indices
    must be sorted in row-major order.
* <b>`aminusb`</b>: Whether to subtract `b` from `a`, vs vice versa.
* <b>`validate_indices`</b>: Whether to validate the order and range of sparse indices
   in `a` and `b`.


#### Returns:

A `SparseTensor` whose shape is the same rank as `a` and `b`, and all but
the last dimension the same. Elements along the last dimension contain the
differences.



#### Raises:


* <b>`TypeError`</b>: If inputs are invalid types, or if `a` and `b` have
    different types.
* <b>`ValueError`</b>: If `a` is sparse and `b` is dense.
* <b>`errors_impl.InvalidArgumentError`</b>: If the shapes of `a` and `b` do not
    match in any dimension other than the last dimension.
