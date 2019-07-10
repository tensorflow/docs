page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.get_losses

Gets the list of losses from the loss_collection.

### Aliases:

* `tf.compat.v1.losses.get_losses`
* `tf.losses.get_losses`

``` python
tf.losses.get_losses(
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES
)
```



Defined in [`python/ops/losses/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/losses/util.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`scope`</b>: An optional scope name for filtering the losses to return.
* <b>`loss_collection`</b>: Optional losses collection.


#### Returns:

a list of loss tensors.
