

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.cyclegan_loss

``` python
tf.contrib.gan.cyclegan_loss(
    model,
    generator_loss_fn=tf.contrib.gan.losses.least_squares_generator_loss,
    discriminator_loss_fn=tf.contrib.gan.losses.least_squares_discriminator_loss,
    cycle_consistency_loss_fn=tf.contrib.gan.losses.cycle_consistency_loss,
    cycle_consistency_loss_weight=10.0,
    **kwargs
)
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/gan/python/train.py).

Returns the losses for a `CycleGANModel`.

See https://arxiv.org/abs/1703.10593 for more details.

#### Args:

* <b>`model`</b>: A `CycleGANModel` namedtuple.
* <b>`generator_loss_fn`</b>: The loss function on the generator. Takes a `GANModel`
    named tuple.
* <b>`discriminator_loss_fn`</b>: The loss function on the discriminator. Takes a
    `GANModel` namedtuple.
* <b>`cycle_consistency_loss_fn`</b>: The cycle consistency loss function. Takes a
    `CycleGANModel` namedtuple.
* <b>`cycle_consistency_loss_weight`</b>: A non-negative Python number or a scalar
    `Tensor` indicating how much to weigh the cycle consistency loss.
* <b>`**kwargs`</b>: Keyword args to pass directly to `gan_loss` to construct the loss
    for each partial model of `model`.


#### Returns:

A `CycleGANLoss` namedtuple.


#### Raises:

* <b>`ValueError`</b>: If `model` is not a `CycleGANModel` namedtuple.