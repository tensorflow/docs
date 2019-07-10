page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.add_loss

Adds a externally defined loss to the collection of losses. (deprecated)

``` python
tf.contrib.losses.add_loss(
    loss,
    loss_collection=tf.GraphKeys.LOSSES
)
```



Defined in [`contrib/losses/python/losses/loss_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/losses/python/losses/loss_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.add_loss instead.

#### Args:


* <b>`loss`</b>: A loss `Tensor`.
* <b>`loss_collection`</b>: Optional collection to add the loss to.