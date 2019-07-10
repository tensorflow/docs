page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.add_loss

Adds a externally defined loss to the collection of losses.

### Aliases:

* `tf.compat.v1.losses.add_loss`
* `tf.losses.add_loss`

``` python
tf.losses.add_loss(
    loss,
    loss_collection=tf.GraphKeys.LOSSES
)
```



Defined in [`python/ops/losses/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/losses/util.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`loss`</b>: A loss `Tensor`.
* <b>`loss_collection`</b>: Optional collection to add the loss to.