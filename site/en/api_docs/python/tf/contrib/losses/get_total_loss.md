


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.losses.get_total_loss

### `tf.contrib.losses.get_total_loss`

```
tf.contrib.losses.get_total_loss(*args, **kwargs)
```


See the guide: [Losses (contrib) > Loss operations for use in neural networks.](../../../../../api_guides/python/contrib.losses#Loss_operations_for_use_in_neural_networks_)

Returns a tensor whose value represents the total loss. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.get_total_loss instead.

Notice that the function adds the given losses to the regularization losses.

#### Args:

* <b>`add_regularization_losses`</b>: A boolean indicating whether or not to use the
    regularization losses in the sum.
* <b>`name`</b>: The name of the returned tensor.


#### Returns:

  A `Tensor` whose value represents the total loss.


#### Raises:

* <b>`ValueError`</b>: if `losses` is not iterable.

Defined in [`tensorflow/python/util/deprecation.py`](https://www.tensorflow.org/code/tensorflow/python/util/deprecation.py).

