

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.losses.compute_weighted_loss

``` python
compute_weighted_loss(
    losses,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
```



Defined in [`tensorflow/python/ops/losses/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/losses/losses_impl.py).

Computes the weighted loss.

#### Args:

* <b>`losses`</b>: `Tensor` of shape `[batch_size, d1, ... dN]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `losses`, and must be broadcastable to `losses` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `losses` dimension).
* <b>`scope`</b>: the scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: the loss will be added to these collections.
* <b>`reduction`</b>: Type of reduction to apply to loss.


#### Returns:

Weighted loss `Tensor` of the same type as `losses`. If `reduction` is
`NONE`, this has the same shape as `losses`; otherwise, it is scalar.


#### Raises:

* <b>`ValueError`</b>: If `weights` is `None` or the shape is not compatible with
    `losses`, or if the number of dimensions (rank) of either `losses` or
    `weights` is missing.