page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.acgan_model

``` python
tf.contrib.gan.acgan_model(
    generator_fn,
    discriminator_fn,
    real_data,
    generator_inputs,
    one_hot_labels,
    generator_scope='Generator',
    discriminator_scope='Discriminator',
    check_shapes=True
)
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/gan/python/train.py).

Returns an ACGANModel contains all the pieces needed for ACGAN training.

The `acgan_model` is the same as the `gan_model` with the only difference
being that the discriminator additionally outputs logits to classify the input
(real or generated).
Therefore, an explicit field holding one_hot_labels is necessary, as well as a
discriminator_fn that outputs a 2-tuple holding the logits for real/fake and
classification.

See https://arxiv.org/abs/1610.09585 for more details.

#### Args:

* <b>`generator_fn`</b>: A python lambda that takes `generator_inputs` as inputs and
    returns the outputs of the GAN generator.
* <b>`discriminator_fn`</b>: A python lambda that takes `real_data`/`generated data`
    and `generator_inputs`. Outputs a tuple consisting of two Tensors:
      (1) real/fake logits in the range [-inf, inf]
      (2) classification logits in the range [-inf, inf]
* <b>`real_data`</b>: A Tensor representing the real data.
* <b>`generator_inputs`</b>: A Tensor or list of Tensors to the generator. In the
    vanilla GAN case, this might be a single noise Tensor. In the conditional
    GAN case, this might be the generator's conditioning.
* <b>`one_hot_labels`</b>: A Tensor holding one-hot-labels for the batch. Needed by
    acgan_loss.
* <b>`generator_scope`</b>: Optional generator variable scope. Useful if you want to
    reuse a subgraph that has already been created.
* <b>`discriminator_scope`</b>: Optional discriminator variable scope. Useful if you
    want to reuse a subgraph that has already been created.
* <b>`check_shapes`</b>: If `True`, check that generator produces Tensors that are the
    same shape as real data. Otherwise, skip this check.


#### Returns:

A ACGANModel namedtuple.


#### Raises:

* <b>`ValueError`</b>: If the generator outputs a Tensor that isn't the same shape as
    `real_data`.
* <b>`TypeError`</b>: If the discriminator does not output a tuple consisting of
  (discrimination logits, classification logits).