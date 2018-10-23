


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.losses.hinge_loss

### `tf.losses.hinge_loss`

```
tf.losses.hinge_loss(labels, logits, weights=1.0, scope=None, loss_collection=tf.GraphKeys.LOSSES)
```


Adds a hinge loss to the training procedure.

#### Args:

* <b>`labels`</b>: The ground truth output tensor. Its shape should match the shape of
    logits. The values of the tensor are expected to be 0.0 or 1.0.
* <b>`logits`</b>: The logits, a float tensor.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `losses` dimension).
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which the loss will be added.


#### Returns:

  A scalar `Tensor` of the loss value.


#### Raises:

* <b>`ValueError`</b>: If the shapes of `logits` and `labels` don't match.

Defined in [`tensorflow/python/ops/losses/losses_impl.py`](https://www.tensorflow.org/code/tensorflow/python/ops/losses/losses_impl.py).

