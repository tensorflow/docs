

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.losses.add_loss

### `tf.losses.add_loss`

``` python
add_loss(
    loss,
    loss_collection=tf.GraphKeys.LOSSES
)
```



Defined in [`tensorflow/python/ops/losses/util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/losses/util.py).

Adds a externally defined loss to the collection of losses.

#### Args:

* <b>`loss`</b>: A loss `Tensor`.
* <b>`loss_collection`</b>: Optional collection to add the loss to.