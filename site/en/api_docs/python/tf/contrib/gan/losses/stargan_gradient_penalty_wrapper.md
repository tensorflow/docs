page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.losses.stargan_gradient_penalty_wrapper

``` python
tf.contrib.gan.losses.stargan_gradient_penalty_wrapper(loss_fn)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/tuple_losses_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/gan/python/losses/python/tuple_losses_impl.py).

Convert a gradient penalty function to take a StarGANModel.

The new function has the same name as the original one.

#### Args:

* <b>`loss_fn`</b>: A python function taking real_data, generated_data,
    generator_inputs for Discriminator's condition (i.e. number of domains),
    discriminator_fn, and discriminator_scope.


#### Returns:

A new function that takes a StarGANModel namedtuple and returns the same
loss.