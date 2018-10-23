

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.losses.wargs.wasserstein_generator_loss

``` python
wasserstein_generator_loss(
    discriminator_gen_outputs,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=losses.Reduction.SUM_BY_NONZERO_WEIGHTS,
    add_summaries=False
)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/gan/python/losses/python/losses_impl.py).

Wasserstein generator loss for GANs.

See `Wasserstein GAN` (https://arxiv.org/abs/1701.07875) for more details.

#### Args:

* <b>`discriminator_gen_outputs`</b>: Discriminator output on generated data. Expected
    to be in the range of (-inf, inf).
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `discriminator_gen_outputs`, and must be broadcastable to
    `discriminator_gen_outputs` (i.e., all dimensions must be either `1`, or
    the same as the corresponding dimension).
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which this loss will be added.
* <b>`reduction`</b>: A `tf.losses.Reduction` to apply to loss.
* <b>`add_summaries`</b>: Whether or not to add detailed summaries for the loss.


#### Returns:

A loss Tensor. The shape depends on `reduction`.