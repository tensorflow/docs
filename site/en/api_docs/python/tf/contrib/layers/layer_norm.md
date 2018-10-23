

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.layers.layer_norm

### `tf.contrib.layers.layer_norm`

``` python
layer_norm(
    inputs,
    center=True,
    scale=True,
    activation_fn=None,
    reuse=None,
    variables_collections=None,
    outputs_collections=None,
    trainable=True,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/layers/python/layers/layers.py).

See the guide: [Layers (contrib) > Higher level ops for building neural network layers](../../../../../api_guides/python/contrib.layers#Higher_level_ops_for_building_neural_network_layers)

Adds a Layer Normalization layer from https://arxiv.org/abs/1607.06450.

  "Layer Normalization"

  Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton

Can be used as a normalizer function for conv2d and fully_connected.

#### Args:

* <b>`inputs`</b>: A tensor with 2 or more dimensions. The normalization
          occurs over all but the first dimension.
* <b>`center`</b>: If True, add offset of `beta` to normalized tensor. If False, `beta`
    is ignored.
* <b>`scale`</b>: If True, multiply by `gamma`. If False, `gamma` is
    not used. When the next layer is linear (also e.g. `nn.relu`), this can be
    disabled since the scaling can be done by the next layer.
* <b>`activation_fn`</b>: Activation function, default set to None to skip it and
    maintain a linear activation.
* <b>`reuse`</b>: Whether or not the layer and its variables should be reused. To be
    able to reuse the layer scope must be given.
* <b>`variables_collections`</b>: Optional collections for the variables.
* <b>`outputs_collections`</b>: Collections to add the outputs.
* <b>`trainable`</b>: If `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
* <b>`scope`</b>: Optional scope for `variable_scope`.


#### Returns:

  A `Tensor` representing the output of the operation.


#### Raises:

* <b>`ValueError`</b>: If rank or last dimension of `inputs` is undefined.