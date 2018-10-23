

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.relu

``` python
relu(
    features,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_nn_ops.py`.

See the guides: [Layers (contrib) > Higher level ops for building neural network layers](../../../../api_guides/python/contrib.layers#Higher_level_ops_for_building_neural_network_layers), [Neural Network > Activation Functions](../../../../api_guides/python/nn#Activation_Functions)

Computes rectified linear: `max(features, 0)`.

#### Args:

* <b>`features`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `int64`, `uint8`, `int16`, `int8`, `uint16`, `half`, `uint32`, `uint64`, `bfloat16`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `features`.