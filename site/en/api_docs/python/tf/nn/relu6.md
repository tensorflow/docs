


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.nn.relu6

### `tf.nn.relu6`

```
tf.nn.relu6(features, name=None)
```


See the guides: [Layers (contrib) > Higher level ops for building neural network layers](../../../../api_guides/python/contrib.layers#Higher_level_ops_for_building_neural_network_layers), [Neural Network > Activation Functions](../../../../api_guides/python/nn#Activation_Functions)

Computes Rectified Linear 6: `min(max(features, 0), 6)`.

#### Args:

* <b>`features`</b>: A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
    `int16`, or `int8`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` with the same type as `features`.

Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/nn_ops.py).

