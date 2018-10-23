


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.losses.get_total_loss

### `tf.losses.get_total_loss`

```
tf.losses.get_total_loss(add_regularization_losses=True, name='total_loss')
```


Returns a tensor whose value represents the total loss.

Notice that the function adds the given losses to the regularization losses.

#### Args:

* <b>`add_regularization_losses`</b>: A boolean indicating whether or not to use the
    regularization losses in the sum.
* <b>`name`</b>: The name of the returned tensor.


#### Returns:

  A `Tensor` whose value represents the total loss.


#### Raises:

* <b>`ValueError`</b>: if `losses` is not iterable.

Defined in [`tensorflow/python/ops/losses/util.py`](https://www.tensorflow.org/code/tensorflow/python/ops/losses/util.py).

