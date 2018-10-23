


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.layers.one_hot_encoding

### `tf.contrib.layers.one_hot_encoding`

```
tf.contrib.layers.one_hot_encoding(*args, **kwargs)
```


See the guide: [Layers (contrib) > Higher level ops for building neural network layers](../../../../../api_guides/python/contrib.layers#Higher_level_ops_for_building_neural_network_layers)

Transform numeric labels into onehot_labels using `tf.one_hot`.

#### Args:

* <b>`labels`</b>: [batch_size] target labels.
* <b>`num_classes`</b>: total number of classes.
* <b>`on_value`</b>: A scalar defining the on-value.
* <b>`off_value`</b>: A scalar defining the off-value.
* <b>`outputs_collections`</b>: collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

  one hot encoding of the labels.

Defined in [`tensorflow/contrib/framework/python/ops/arg_scope.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/python/ops/arg_scope.py).

