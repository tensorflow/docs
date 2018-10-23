

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.gather

``` python
gather(
    params,
    indices,
    validate_indices=None,
    name=None,
    axis=0
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/array_ops.py).

See the guides: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining), [Variables > Sparse Variable Updates](../../../api_guides/python/state_ops#Sparse_Variable_Updates)

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
  Values from `params` gathered from indices given by `indices`, with
  shape `params.shape[:axis] + indices.shape + params.shape[axis + 1:]`.