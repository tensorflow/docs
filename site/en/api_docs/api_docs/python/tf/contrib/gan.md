

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.gan



Defined in [`tensorflow/contrib/gan/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/gan/__init__.py).

TFGAN grouped API. Please see README.md for details and usage.

## Modules

[`estimator`](../../tf/contrib/gan/estimator) module: TFGAN grouped API. Please see README.md for details and usage.

[`eval`](../../tf/contrib/gan/eval) module: TFGAN grouped API. Please see README.md for details and usage.

[`features`](../../tf/contrib/gan/features) module: TFGAN grouped API. Please see README.md for details and usage.

[`losses`](../../tf/contrib/gan/losses) module: TFGAN grouped API. Please see README.md for details and usage.

## Classes

[`class ACGANModel`](../../tf/contrib/gan/ACGANModel): An ACGANModel contains all the pieces needed for ACGAN training.

[`class GANLoss`](../../tf/contrib/gan/GANLoss): GANLoss contains the generator and discriminator losses.

[`class GANModel`](../../tf/contrib/gan/GANModel): A GANModel contains all the pieces needed for GAN training.

[`class GANTrainOps`](../../tf/contrib/gan/GANTrainOps): GANTrainOps contains the training ops.

[`class GANTrainSteps`](../../tf/contrib/gan/GANTrainSteps): Contains configuration for the GAN Training.

[`class InfoGANModel`](../../tf/contrib/gan/InfoGANModel): An InfoGANModel contains all the pieces needed for InfoGAN training.

## Functions

[`acgan_model(...)`](../../tf/contrib/gan/acgan_model): Returns an ACGANModel contains all the pieces needed for ACGAN training.

[`gan_loss(...)`](../../tf/contrib/gan/gan_loss): Returns losses necessary to train generator and discriminator.

[`gan_model(...)`](../../tf/contrib/gan/gan_model): Returns GAN model outputs and variables.

[`gan_train(...)`](../../tf/contrib/gan/gan_train): A wrapper around `contrib.training.train` that uses GAN hooks.

[`gan_train_ops(...)`](../../tf/contrib/gan/gan_train_ops): Returns GAN train ops.

[`get_joint_train_hooks(...)`](../../tf/contrib/gan/get_joint_train_hooks): Returns a hooks function for sequential GAN training.

[`get_sequential_train_hooks(...)`](../../tf/contrib/gan/get_sequential_train_hooks): Returns a hooks function for sequential GAN training.

[`get_sequential_train_steps(...)`](../../tf/contrib/gan/get_sequential_train_steps): Returns a thin wrapper around slim.learning.train_step, for GANs.

[`infogan_model(...)`](../../tf/contrib/gan/infogan_model): Returns an InfoGAN model outputs and variables.

