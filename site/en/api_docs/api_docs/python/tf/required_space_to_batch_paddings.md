

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.required_space_to_batch_paddings

``` python
required_space_to_batch_paddings(
    input_shape,
    block_shape,
    base_paddings=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/array_ops.py).

See the guide: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining)

Calculate padding required to make block_shape divide input_shape.

This function can be used to calculate a suitable paddings argument for use
with space_to_batch_nd and batch_to_space_nd.

#### Args:

* <b>`input_shape`</b>: int32 Tensor of shape [N].
* <b>`block_shape`</b>: int32 Tensor of shape [N].
* <b>`base_paddings`</b>: Optional int32 Tensor of shape [N, 2].  Specifies the minimum
    amount of padding to use.  All elements must be >= 0.  If not specified,
    defaults to 0.
* <b>`name`</b>: string.  Optional name prefix.


#### Returns:

  (paddings, crops), where:

  `paddings` and `crops` are int32 Tensors of rank 2 and shape [N, 2]
* <b>`satisfying`</b>:

      paddings[i, 0] = base_paddings[i, 0].
      0 <= paddings[i, 1] - base_paddings[i, 1] < block_shape[i]
      (input_shape[i] + paddings[i, 0] + paddings[i, 1]) % block_shape[i] == 0

      crops[i, 0] = 0
      crops[i, 1] = paddings[i, 1] - base_paddings[i, 1]

Raises: ValueError if called with incompatible shapes.