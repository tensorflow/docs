page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.get_losses

Gets the list of losses from the loss_collection. (deprecated)

``` python
tf.contrib.losses.get_losses(
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES
)
```



Defined in [`contrib/losses/python/losses/loss_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/losses/python/losses/loss_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.get_losses instead.

#### Args:


* <b>`scope`</b>: an optional scope for filtering the losses to return.
* <b>`loss_collection`</b>: Optional losses collection.


#### Returns:

a list of loss tensors.
