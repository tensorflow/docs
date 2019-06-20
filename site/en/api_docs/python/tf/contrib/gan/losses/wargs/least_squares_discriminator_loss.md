page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.losses.wargs.least_squares_discriminator_loss

``` python
tf.contrib.gan.losses.wargs.least_squares_discriminator_loss(
    discriminator_real_outputs,
    discriminator_gen_outputs,
    real_label=1,
    fake_label=0,
    real_weights=1.0,
    generated_weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=losses.Reduction.SUM_BY_NONZERO_WEIGHTS,
    add_summaries=False
)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/gan/python/losses/python/losses_impl.py).

Least squares discriminator loss.

This loss comes from `Least Squares Generative Adversarial Networks`
(https://arxiv.org/abs/1611.04076).

L = 1/2 * (D(x) - `real`) ** 2 +
    1/2 * (D(G(z)) - `fake_label`) ** 2

where D(y) are discriminator logits.

#### Args:

* <b>`discriminator_real_outputs`</b>: Discriminator output on real data.
* <b>`discriminator_gen_outputs`</b>: Discriminator output on generated data. Expected
    to be in the range of (-inf, inf).
* <b>`real_label`</b>: The value that the discriminator tries to output for real data.
* <b>`fake_label`</b>: The value that the discriminator tries to output for fake data.
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