page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.batch_gather

``` python
tf.batch_gather(
    params,
    indices,
    name=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/array_ops.py).

Gather slices from `params` according to `indices` with leading batch dims.

This operation assumes that the leading dimensions of `indices` are dense,
and the gathers on the axis corresponding to the last dimension of `indices`.
More concretely it computes:

result[i1, ..., in] = params[i1, ..., in-1, indices[i1, ..., in]]

Therefore `params` should be a Tensor of shape [A1, ..., AN, B1, ..., BM],
`indices` should be a Tensor of shape [A1, ..., AN-1, C] and `result` will be
a Tensor of size `[A1, ..., AN-1, C, B1, ..., BM]`.

In the case in which indices is a 1D tensor, this operation is equivalent to
<a href="../tf/gather"><code>tf.gather</code></a>.

See also <a href="../tf/gather"><code>tf.gather</code></a> and <a href="../tf/gather_nd"><code>tf.gather_nd</code></a>.

#### Args:

* <b>`params`</b>: A Tensor. The tensor from which to gather values.
* <b>`indices`</b>: A Tensor. Must be one of the following types: int32, int64. Index
      tensor. Must be in range `[0, params.shape[axis]`, where `axis` is the
      last dimension of `indices` itself.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A Tensor. Has the same type as `params`.


#### Raises:

* <b>`ValueError`</b>: if `indices` has an unknown shape.