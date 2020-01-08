page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gather

``` python
tf.gather(
    params,
    indices,
    validate_indices=None,
    name=None,
    axis=0
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/array_ops.py).

Gather slices from `params` axis `axis` according to `indices`.

`indices` must be an integer tensor of any dimension (usually 0-D or 1-D).
Produces an output tensor with shape `params.shape[:axis] + indices.shape +
params.shape[axis + 1:]` where:

```python
    # Scalar indices (output is rank(params) - 1).
    output[a_0, ..., a_n, b_0, ..., b_n] =
      params[a_0, ..., a_n, indices, b_0, ..., b_n]

    # Vector indices (output is rank(params)).
    output[a_0, ..., a_n, i, b_0, ..., b_n] =
      params[a_0, ..., a_n, indices[i], b_0, ..., b_n]

    # Higher rank indices (output is rank(params) + rank(indices) - 1).
    output[a_0, ..., a_n, i, ..., j, b_0, ... b_n] =
      params[a_0, ..., a_n, indices[i, ..., j], b_0, ..., b_n]
```

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/Gather.png" alt>
</div>

Note that on CPU, if an out of bound index is found, an error is returned.
On GPU, if an out of bound index is found, a 0 is stored in the
corresponding output value.

See also <a href="../tf/batch_gather"><code>tf.batch_gather</code></a> and <a href="../tf/gather_nd"><code>tf.gather_nd</code></a>.

#### Args:

* <b>`params`</b>: A `Tensor`.
    The tensor from which to gather values. Must be at least rank
    `axis + 1`.
* <b>`indices`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    Index tensor. Must be in range `[0, params.shape[axis])`.
* <b>`axis`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    The axis in `params` to gather `indices` from. Defaults to the first
    dimension. Supports negative indexes.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `params`.