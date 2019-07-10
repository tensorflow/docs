page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.compute_weighted_loss

Computes the weighted loss. (deprecated)

``` python
tf.contrib.losses.compute_weighted_loss(
    losses,
    weights=1.0,
    scope=None
)
```



Defined in [`contrib/losses/python/losses/loss_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/losses/python/losses/loss_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.compute_weighted_loss instead.

#### Args:


* <b>`losses`</b>: A tensor of size [batch_size, d1, ... dN].
* <b>`weights`</b>: A tensor of size [1] or [batch_size, d1, ... dK] where K < N.
* <b>`scope`</b>: the scope for the operations performed in computing the loss.


#### Returns:

A scalar `Tensor` that returns the weighted loss.



#### Raises:


* <b>`ValueError`</b>: If `weights` is `None` or the shape is not compatible with
  `losses`, or if the number of dimensions (rank) of either `losses` or
  `weights` is missing.