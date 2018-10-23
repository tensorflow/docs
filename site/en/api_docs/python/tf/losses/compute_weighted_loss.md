


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.losses.compute_weighted_loss

### `tf.losses.compute_weighted_loss`

```
tf.losses.compute_weighted_loss(losses, weights=1.0, scope=None, loss_collection=tf.GraphKeys.LOSSES)
```


Computes the weighted loss.

#### Args:

* <b>`losses`</b>: `Tensor` of shape `[batch_size, d1, ... dN]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `losses`, and must be broadcastable to `losses` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `losses` dimension).
* <b>`scope`</b>: the scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: the loss will be added to these collections.


#### Returns:

  A scalar `Tensor` that returns the weighted loss.


#### Raises:

* <b>`ValueError`</b>: If `weights` is `None` or the shape is not compatible with
    `losses`, or if the number of dimensions (rank) of either `losses` or
    `weights` is missing.

Defined in [`tensorflow/python/ops/losses/losses_impl.py`](https://www.tensorflow.org/code/tensorflow/python/ops/losses/losses_impl.py).

