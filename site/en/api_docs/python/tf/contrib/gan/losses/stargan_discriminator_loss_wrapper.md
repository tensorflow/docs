page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.losses.stargan_discriminator_loss_wrapper

``` python
tf.contrib.gan.losses.stargan_discriminator_loss_wrapper(loss_fn)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/tuple_losses_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/gan/python/losses/python/tuple_losses_impl.py).

Convert a discriminator loss function to take a StarGANModel.

The new function has the same name as the original one.

#### Args:

* <b>`loss_fn`</b>: A python function taking Discriminator's real/fake prediction for
    real data and generated data.


#### Returns:

A new function that takes a StarGANModel namedtuple and returns the same
loss.