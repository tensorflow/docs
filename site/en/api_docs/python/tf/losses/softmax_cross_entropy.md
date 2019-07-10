page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.softmax_cross_entropy

``` python
tf.losses.softmax_cross_entropy(
    onehot_labels,
    logits,
    weights=1.0,
    label_smoothing=0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
```



Defined in [`tensorflow/python/ops/losses/losses_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/losses/losses_impl.py).

Creates a cross-entropy loss using tf.nn.softmax_cross_entropy_with_logits_v2.

`weights` acts as a coefficient for the loss. If a scalar is provided,
then the loss is simply scaled by the given value. If `weights` is a
tensor of shape `[batch_size]`, then the loss weights apply to each
corresponding sample.

If `label_smoothing` is nonzero, smooth the labels towards 1/num_classes:
    new_onehot_labels = onehot_labels * (1 - label_smoothing)
                        + label_smoothing / num_classes

Note that `onehot_labels` and `logits` must have the same shape,
e.g. `[batch_size, num_classes]`. The shape of `weights` must be
broadcastable to loss, whose shape is decided by the shape of `logits`.
In case the shape of `logits` is `[batch_size, num_classes]`, loss is
a `Tensor` of shape `[batch_size]`.

#### Args:

* <b>`onehot_labels`</b>: One-hot-encoded labels.
* <b>`logits`</b>: Logits outputs of the network.
* <b>`weights`</b>: Optional `Tensor` that is broadcastable to loss.
* <b>`label_smoothing`</b>: If greater than 0 then smooth the labels.
* <b>`scope`</b>: the scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which the loss will be added.
* <b>`reduction`</b>: Type of reduction to apply to loss.


#### Returns:

Weighted loss `Tensor` of the same type as `logits`. If `reduction` is
`NONE`, this has shape `[batch_size]`; otherwise, it is scalar.


#### Raises:

* <b>`ValueError`</b>: If the shape of `logits` doesn't match that of `onehot_labels`
    or if the shape of `weights` is invalid or if `weights` is None.  Also if
    `onehot_labels` or `logits` is None.



#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../tf/keras/models/Model"><code>tf.keras.Model</code></a>.

