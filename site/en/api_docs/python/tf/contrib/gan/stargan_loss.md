page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.stargan_loss

``` python
tf.contrib.gan.stargan_loss(
    model,
    generator_loss_fn=tfgan_losses.stargan_generator_loss_wrapper(tfgan_losses_impl.\n    wasserstein_generator_loss),
    discriminator_loss_fn=tfgan_losses.stargan_discriminator_loss_wrapper(tfgan_losses_impl.\n    wasserstein_discriminator_loss),
    gradient_penalty_weight=10.0,
    gradient_penalty_epsilon=1e-10,
    gradient_penalty_target=1.0,
    gradient_penalty_one_sided=False,
    reconstruction_loss_fn=tf.losses.absolute_difference,
    reconstruction_loss_weight=10.0,
    classification_loss_fn=tf.losses.softmax_cross_entropy,
    classification_loss_weight=1.0,
    classification_one_hot=True,
    add_summaries=True
)
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/gan/python/train.py).

StarGAN Loss.

The four major part can be found here: http://screen/tMRMBAohDYG.

#### Args:

* <b>`model`</b>: (StarGAN) Model output of the stargan_model() function call.
* <b>`generator_loss_fn`</b>: The loss function on the generator. Takes a
    `StarGANModel` named tuple.
* <b>`discriminator_loss_fn`</b>: The loss function on the discriminator. Takes a
    `StarGANModel` namedtuple.
* <b>`gradient_penalty_weight`</b>: (float) Gradient penalty weight. Default to 10 per
    the original paper https://arxiv.org/abs/1711.09020. Set to 0 or None to
    turn off gradient penalty.
* <b>`gradient_penalty_epsilon`</b>: (float) A small positive number added for
    numerical stability when computing the gradient norm.
* <b>`gradient_penalty_target`</b>: (float, or tf.float `Tensor`) The target value of
    gradient norm. Defaults to 1.0.
* <b>`gradient_penalty_one_sided`</b>: (bool) If `True`, penalty proposed in
    https://arxiv.org/abs/1709.08894 is used. Defaults to `False`.
* <b>`reconstruction_loss_fn`</b>: The reconstruction loss function. Default to L1-norm
    and the function must conform to the <a href="../../../tf/losses"><code>tf.losses</code></a> API.
* <b>`reconstruction_loss_weight`</b>: Reconstruction loss weight. Default to 10.0.
* <b>`classification_loss_fn`</b>: The loss function on the discriminator's ability to
    classify domain of the input. Default to one-hot softmax cross entropy
    loss, and the function must conform to the <a href="../../../tf/losses"><code>tf.losses</code></a> API.
* <b>`classification_loss_weight`</b>: (float) Classification loss weight. Default to
    1.0.
* <b>`classification_one_hot`</b>: (bool) If the label is one hot representation.
    Default to True. If False, classification classification_loss_fn need to
    be sigmoid cross entropy loss instead.
* <b>`add_summaries`</b>: (bool) Add the loss to the summary


#### Returns:

GANLoss namedtuple where we have generator loss and discriminator loss.


#### Raises:

* <b>`ValueError`</b>: If input StarGANModel.input_data_domain_label does not have rank
  2, or dimension 2 is not defined.