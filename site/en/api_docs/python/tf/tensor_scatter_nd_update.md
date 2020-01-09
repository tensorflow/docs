page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tensor_scatter_nd_update


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Scatter `updates` into an existing tensor according to `indices`.

### Aliases:

* `tf.compat.v1.tensor_scatter_nd_update`
* `tf.compat.v1.tensor_scatter_update`
* `tf.compat.v2.tensor_scatter_nd_update`


``` python
tf.tensor_scatter_nd_update(
    tensor,
    indices,
    updates,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation creates a new tensor by applying sparse `updates` to the passed
in `tensor`.
This operation is very similar to <a href="../tf/scatter_nd"><code>tf.scatter_nd</code></a>, except that the updates are
scattered onto an existing tensor (as opposed to a zero-tensor). If the memory
for the existing tensor cannot be re-used, a copy is made and updated.

If `indices` contains duplicates, then their updates are accumulated (summed).

**WARNING**: The order in which updates are applied is nondeterministic, so the
output will be nondeterministic if `indices` contains duplicates -- because
of some numerical approximation issues, numbers summed in different order
may yield different results.

`indices` is an integer tensor containing indices into a new tensor of shape
`shape`.  The last dimension of `indices` can be at most the rank of `shape`:

    indices.shape[-1] <= shape.rank

The last dimension of `indices` corresponds to indices into elements
(if `indices.shape[-1] = shape.rank`) or slices
(if `indices.shape[-1] < shape.rank`) along dimension `indices.shape[-1]` of
`shape`.  `updates` is a tensor with shape

    indices.shape[:-1] + shape[indices.shape[-1]:]

The simplest form of scatter is to insert individual elements in a tensor by
index. For example, say we want to insert 4 scattered elements in a rank-1
tensor with 8 elements.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/ScatterNd1.png" alt>
</div>

In Python, this scatter operation would look like this:

```python
    indices = tf.constant([[4], [3], [1], [7]])
    updates = tf.constant([9, 10, 11, 12])
    tensor = tf.ones([8], dtype=tf.int32)
    updated = tf.tensor_scatter_update(tensor, indices, updates)
    with tf.Session() as sess:
      print(sess.run(scatter))
```

The resulting tensor would look like this:

    [1, 11, 1, 10, 9, 1, 1, 12]

We can also, insert entire slices of a higher rank tensor all at once. For
example, if we wanted to insert two slices in the first dimension of a
rank-3 tensor with two matrices of new values.

In Python, this scatter operation would look like this:

```python
    indices = tf.constant([[0], [2]])
    updates = tf.constant([[[5, 5, 5, 5], [6, 6, 6, 6],
                            [7, 7, 7, 7], [8, 8, 8, 8]],
                           [[5, 5, 5, 5], [6, 6, 6, 6],
                            [7, 7, 7, 7], [8, 8, 8, 8]]])
    tensor = tf.ones([4, 4, 4])
    updated = tf.tensor_scatter_update(tensor, indices, updates)
    with tf.Session() as sess:
      print(sess.run(scatter))
```

The resulting tensor would look like this:

    [[[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]],
     [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
     [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]],
     [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]]

Note that on CPU, if an out of bound index is found, an error is returned.
On GPU, if an out of bound index is found, the index is ignored.

#### Args:


* <b>`tensor`</b>: A `Tensor`. Tensor to copy/update.
* <b>`indices`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  Index tensor.
* <b>`updates`</b>: A `Tensor`. Must have the same type as `tensor`.
  Updates to scatter into output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `tensor`.
