page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.add_loss

``` python
tf.contrib.losses.add_loss(
    loss,
    loss_collection=tf.GraphKeys.LOSSES
)
```



Defined in [`tensorflow/contrib/losses/python/losses/loss_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/losses/python/losses/loss_ops.py).

Adds a externally defined loss to the collection of losses. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.add_loss instead.

#### Args:

* <b>`loss`</b>: A loss `Tensor`.
* <b>`loss_collection`</b>: Optional collection to add the loss to.