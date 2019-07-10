page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.estimator.get_latent_gan_estimator

Gets an estimator that passes gradients to the input.

### Aliases:

* `tf.contrib.gan.estimator.get_latent_gan_estimator`
* `tf.contrib.gan.estimator.latent_gan_estimator.get_latent_gan_estimator`

``` python
tf.contrib.gan.estimator.get_latent_gan_estimator(
    generator_fn,
    discriminator_fn,
    loss_fn,
    optimizer,
    params,
    config,
    ckpt_dir,
    warmstart_options=True
)
```



Defined in [`contrib/gan/python/estimator/python/latent_gan_estimator_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/estimator/python/latent_gan_estimator_impl.py).

<!-- Placeholder for "Used in" -->

This function takes in a generator and adds a trainable z variable that is
used as input to this generator_fn. The generator itself is treated as a black
box through which gradients can pass through without updating any weights. The
result is a trainable way to traverse the GAN latent space. The loss_fn is
used to actually train the z variable. The generator_fn and discriminator_fn
should be previously trained by the tfgan library (on reload, the variables
are expected to follow the tfgan format. It may be possible to use the
latent gan estimator with entirely custom GANs that do not use the tfgan
library as long as the appropriate variables are wired properly).

#### Args:

generator_fn: a function defining a Tensorflow graph for a GAN generator.
  The weights defined in this graph should already be defined in the given
  checkpoint location. Should have 'mode' as an argument.
discriminator_fn: a function defining a Tensorflow graph for a GAN
  discriminator. Should have 'mode' as an argument.
loss_fn: a function defining a Tensorflow graph for a GAN loss. Takes in a
  GANModel tuple, features, labels, and add_summaries as inputs.
optimizer: a tf.Optimizer or a function that returns a tf.Optimizer with no
  inputs.

* <b>`params`</b>: An object containing the following parameters:
   - batch_size: an int indicating the size of the training batch.
   - z_shape: the desired shape of the input z values (not counting batch).
   - learning_rate: a scalar or function defining a learning rate applied to
     optimizer.
   - input_clip: the amount to clip the x training variable by.
   - add_summaries: whether or not to add summaries.
   - opt_kwargs: optimizer kwargs.
 config: tf.RunConfig. Should point model to output dir and should indicate
  whether to save checkpoints (to avoid saving checkpoints, set
  save_checkpoints_steps to a number larger than the number of train steps).
  The model_dir field in the RunConfig should point to a directory WITHOUT
  any saved checkpoints.
 ckpt_dir: the directory where the model checkpoints live. The checkpoint is
  used to warm start the underlying GAN. This should NOT be the same as
  config.model_dir.
 warmstart_options: boolean, None, or a WarmStartSettings object. If set to
   True, uses a default WarmStartSettings object. If set to False or None,
   does not use warm start. If using a custom WarmStartSettings object, make
   sure that new variables are properly accounted for when reloading the
   underlying GAN. Defaults to True.

#### Returns:

An estimator spec defining a GAN input training estimator.
