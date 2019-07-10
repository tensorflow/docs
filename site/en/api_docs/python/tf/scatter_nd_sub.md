page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.scatter_nd_sub

``` python
tf.scatter_nd_sub(
    ref,
    indices,
    updates,
    use_locking=False,
    name=None
)
```



Defined in [`tensorflow/python/ops/state_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/state_ops.py).

Applies sparse subtraction to individual values or slices in a Variable.

`ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `ref`.
It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to
indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
dimension of `ref`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

```
[d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].
```

For example, say we want to subtract 4 scattered elements from a rank-1 tensor
to 8 elements. In Python, that update would look like this:

```python
    ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
    indices = tf.constant([[4], [3], [1] ,[7]])
    updates = tf.constant([9, 10, 11, 12])
    op = tf.scatter_nd_sub(ref, indices, updates)
    with tf.Session() as sess:
      print sess.run(op)
```

The resulting update to ref would look like this:

    [1, -9, 3, -6, -6, 6, 7, -4]

See <a href="../tf/scatter_nd"><code>tf.scatter_nd</code></a> for more details about how to make updates to
slices.

#### Args:

* <b>`ref`</b>: A mutable `Tensor`. Must be one of the following types: `float32`,
    `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
    `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
    `uint32`, `uint64`. A mutable Tensor. Should be from a Variable node.
* <b>`indices`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    A tensor of indices into ref.
* <b>`updates`</b>: A `Tensor`. Must have the same type as `ref`.
    A tensor of updated values to add to ref.
* <b>`use_locking`</b>: An optional `bool`. Defaults to `False`.
    An optional bool. Defaults to True. If True, the assignment will
    be protected by a lock; otherwise the behavior is undefined,
    but may exhibit less contention.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A mutable `Tensor`. Has the same type as `ref`.