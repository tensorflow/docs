page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.GANTrainSteps

## Class `GANTrainSteps`





Defined in [`tensorflow/contrib/gan/python/namedtuples.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/gan/python/namedtuples.py).

Contains configuration for the GAN Training.

#### Args:

* <b>`generator_train_steps`</b>: Number of generator steps to take in each GAN step.
* <b>`discriminator_train_steps`</b>: Number of discriminator steps to take in each GAN
    step.

<h2 id="__new__"><code>__new__</code></h2>

``` python
__new__(
    _cls,
    generator_train_steps,
    discriminator_train_steps
)
```

Create new instance of GANTrainSteps(generator_train_steps, discriminator_train_steps)



## Properties

<h3 id="generator_train_steps"><code>generator_train_steps</code></h3>



<h3 id="discriminator_train_steps"><code>discriminator_train_steps</code></h3>





