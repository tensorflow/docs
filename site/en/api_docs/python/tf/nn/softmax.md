

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.softmax

### `tf.nn.softmax`

``` python
softmax(
    logits,
    dim=-1,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/nn_ops.py).

See the guides: [Layers (contrib) > Higher level ops for building neural network layers](../../../../api_guides/python/contrib.layers#Higher_level_ops_for_building_neural_network_layers), [Neural Network > Classification](../../../../api_guides/python/nn#Classification)

Computes softmax activations.

For each batch `i` and class `j` we have

    softmax = exp(logits) / reduce_sum(exp(logits), dim)

#### Args:

* <b>`logits`</b>: A non-empty `Tensor`. Must be one of the following types: `half`,
    `float32`, `float64`.
* <b>`dim`</b>: The dimension softmax would be performed on. The default is -1 which
    indicates the last dimension.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor`. Has the same type as `logits`. Same shape as `logits`.

#### Raises:

* <b>`InvalidArgumentError`</b>: if `logits` is empty or `dim` is beyond the last
    dimension of `logits`.