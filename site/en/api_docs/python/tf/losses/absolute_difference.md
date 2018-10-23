


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.losses.absolute_difference

### `tf.losses.absolute_difference`

```
tf.losses.absolute_difference(labels, predictions, weights=1.0, scope=None, loss_collection=tf.GraphKeys.LOSSES)
```


Adds an Absolute Difference loss to the training procedure.

`weights` acts as a coefficient for the loss. If a scalar is provided, then
the loss is simply scaled by the given value. If `weights` is a `Tensor` of
shape `[batch_size]`, then the total loss for each sample of the batch is
rescaled by the corresponding element in the `weights` vector. If the shape of
`weights` matches the shape of `predictions`, then the loss of each
measurable element of `predictions` is scaled by the corresponding value of
`weights`.

#### Args:

* <b>`labels`</b>: The ground truth output tensor, same dimensions as 'predictions'.
* <b>`predictions`</b>: The predicted outputs.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `losses` dimension).
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which this loss will be added.


#### Returns:

  A scalar `Tensor` representing the loss value.


#### Raises:

* <b>`ValueError`</b>: If the shape of `predictions` doesn't match that of `labels` or
    if the shape of `weights` is invalid.

Defined in [`tensorflow/python/ops/losses/losses_impl.py`](https://www.tensorflow.org/code/tensorflow/python/ops/losses/losses_impl.py).

