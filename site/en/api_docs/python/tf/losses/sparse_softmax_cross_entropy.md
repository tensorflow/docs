

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.losses.sparse_softmax_cross_entropy

### `tf.losses.sparse_softmax_cross_entropy`

``` python
sparse_softmax_cross_entropy(
    labels,
    logits,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES
)
```



Defined in [`tensorflow/python/ops/losses/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/losses/losses_impl.py).

Cross-entropy loss using `tf.nn.sparse_softmax_cross_entropy_with_logits`.

`weights` acts as a coefficient for the loss. If a scalar is provided,
then the loss is simply scaled by the given value. If `weights` is a
tensor of shape [`batch_size`], then the loss weights apply to each
corresponding sample.

#### Args:

* <b>`labels`</b>: `Tensor` of shape `[d_0, d_1, ..., d_{r-1}]` (where `r` is rank of
    `labels` and result) and dtype `int32` or `int64`. Each entry in `labels`
    must be an index in `[0, num_classes)`. Other values will raise an
    exception when this op is run on CPU, and return `NaN` for corresponding
    loss and gradient rows on GPU.
* <b>`logits`</b>: Unscaled log probabilities of shape
    `[d_0, d_1, ..., d_{r-1}, num_classes]` and dtype `float32` or `float64`.
* <b>`weights`</b>: Coefficients for the loss. This must be scalar or of same rank as
    `labels`
* <b>`scope`</b>: the scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which the loss will be added.


#### Returns:

  A scalar `Tensor` representing the mean loss value.


#### Raises:

* <b>`ValueError`</b>: If the shapes of logits, labels, and weight are incompatible, or
    if `weights` is None.