page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.concat

``` python
tf.concat(
    values,
    axis,
    name='concat'
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/array_ops.py).

Concatenates tensors along one dimension.

Concatenates the list of tensors `values` along dimension `axis`.  If
`values[i].shape = [D0, D1, ... Daxis(i), ...Dn]`, the concatenated
result has shape

    [D0, D1, ... Raxis, ...Dn]

where

    Raxis = sum(Daxis(i))

That is, the data from the input tensors is joined along the `axis`
dimension.

The number of dimensions of the input tensors must match, and all dimensions
except `axis` must be equal.

For example:

```python
t1 = [[1, 2, 3], [4, 5, 6]]
t2 = [[7, 8, 9], [10, 11, 12]]
tf.concat([t1, t2], 0)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
tf.concat([t1, t2], 1)  # [[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]]

# tensor t3 with shape [2, 3]
# tensor t4 with shape [2, 3]
tf.shape(tf.concat([t3, t4], 0))  # [4, 3]
tf.shape(tf.concat([t3, t4], 1))  # [2, 6]
```
As in Python, the `axis` could also be negative numbers. Negative `axis`
are interpreted as counting from the end of the rank, i.e.,
 `axis + rank(values)`-th dimension.

For example:

```python
t1 = [[[1, 2], [2, 3]], [[4, 4], [5, 3]]]
t2 = [[[7, 4], [8, 4]], [[2, 10], [15, 11]]]
tf.concat([t1, t2], -1)
```

would produce:

```python
[[[ 1,  2,  7,  4],
  [ 2,  3,  8,  4]],

 [[ 4,  4,  2, 10],
  [ 5,  3, 15, 11]]]
```

Note: If you are concatenating along a new axis consider using stack.
E.g.

```python
tf.concat([tf.expand_dims(t, axis) for t in tensors], axis)
```

can be rewritten as

```python
tf.stack(tensors, axis=axis)
```

#### Args:

* <b>`values`</b>: A list of `Tensor` objects or a single `Tensor`.
* <b>`axis`</b>: 0-D `int32` `Tensor`.  Dimension along which to concatenate. Must be
    in the range `[-rank(values), rank(values))`. As in Python, indexing
    for axis is 0-based. Positive axis in the rage of
    `[0, rank(values))` refers to `axis`-th dimension. And negative axis
    refers to `axis + rank(values)`-th dimension.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` resulting from concatenation of the input tensors.