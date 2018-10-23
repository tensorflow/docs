

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.losses.wargs.wasserstein_discriminator_loss

``` python
tf.contrib.gan.losses.wargs.wasserstein_discriminator_loss(
    discriminator_real_outputs,
    discriminator_gen_outputs,
    real_weights=1.0,
    generated_weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=losses.Reduction.SUM_BY_NONZERO_WEIGHTS,
    add_summaries=False
)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/gan/python/losses/python/losses_impl.py).

Wasserstein discriminator loss for GANs.

See `Wasserstein GAN` (https://arxiv.org/abs/1701.07875) for more details.

#### Args:

* <b>`discriminator_real_outputs`</b>: Discriminator output on real data.
* <b>`discriminator_gen_outputs`</b>: Discriminator output on generated data. Expected
    to be in the range of (-inf, inf).
* <b>`real_weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `discriminator_real_outputs`, and must be broadcastable to
    `discriminator_real_outputs` (i.e., all dimensions must be either `1`, or
    the same as the corresponding dimension).
* <b>`generated_weights`</b>: Same as `real_weights`, but for
    `discriminator_gen_outputs`.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which this loss will be added.
* <b>`reduction`</b>: A <a href="../../../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a> to apply to loss.
* <b>`add_summaries`</b>: Whether or not to add summaries for the loss.


#### Returns:

A loss Tensor. The shape depends on `reduction`.