page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.losses.cycle_consistency_loss

``` python
tf.contrib.gan.losses.cycle_consistency_loss(
    cyclegan_model,
    scope=None,
    add_summaries=False
)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/tuple_losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/losses/python/tuple_losses_impl.py).

Defines the cycle consistency loss.

Uses `cycle_consistency_loss` to compute the cycle consistency loss for a
`cyclegan_model`.

#### Args:

* <b>`cyclegan_model`</b>: A `CycleGANModel` namedtuple.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
    Defaults to None.
* <b>`add_summaries`</b>: Whether or not to add detailed summaries for the loss.
    Defaults to False.


#### Returns:

A scalar `Tensor` of cycle consistency loss.


#### Raises:

* <b>`ValueError`</b>: If `cyclegan_model` is not a `CycleGANModel` namedtuple.