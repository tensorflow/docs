


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.layers.flatten

### `tf.contrib.layers.flatten`

```
tf.contrib.layers.flatten(*args, **kwargs)
```


See the guide: [Layers (contrib) > Higher level ops for building neural network layers](../../../../../api_guides/python/contrib.layers#Higher_level_ops_for_building_neural_network_layers)

Flattens the input while maintaining the batch_size.

  Assumes that the first dimension represents the batch.

#### Args:

* <b>`inputs`</b>: a tensor of size [batch_size, ...].
* <b>`outputs_collections`</b>: collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

  a flattened tensor with shape [batch_size, k].
Raises:
* <b>`ValueError`</b>: if inputs.dense_shape is wrong.

Defined in [`tensorflow/contrib/framework/python/ops/arg_scope.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/python/ops/arg_scope.py).

