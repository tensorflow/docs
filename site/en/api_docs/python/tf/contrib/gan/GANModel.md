

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.GANModel

## Class `GANModel`





Defined in [`tensorflow/contrib/gan/python/namedtuples.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/gan/python/namedtuples.py).

A GANModel contains all the pieces needed for GAN training.

Generative Adversarial Networks (https://arxiv.org/abs/1406.2661) attempt
to create an implicit generative model of data by solving a two agent game.
The generator generates candidate examples that are supposed to match the
data distribution, and the discriminator aims to tell the real examples
apart from the generated samples.

#### Args:

* <b>`generator_inputs`</b>: The random noise source that acts as input to the
    generator.
* <b>`generated_data`</b>: The generated output data of the GAN.
* <b>`generator_variables`</b>: A list of all generator variables.
* <b>`generator_scope`</b>: Variable scope all generator variables live in.
* <b>`generator_fn`</b>: The generator function.
* <b>`real_data`</b>: A tensor or real data.
* <b>`discriminator_real_outputs`</b>: The discriminator's output on real data.
* <b>`discriminator_gen_outputs`</b>: The discriminator's output on generated data.
* <b>`discriminator_variables`</b>: A list of all discriminator variables.
* <b>`discriminator_scope`</b>: Variable scope all discriminator variables live in.
* <b>`discriminator_fn`</b>: The discriminator function.

## Properties

<h3 id="discriminator_fn"><code>discriminator_fn</code></h3>

Alias for field number 10

<h3 id="discriminator_gen_outputs"><code>discriminator_gen_outputs</code></h3>

Alias for field number 7

<h3 id="discriminator_real_outputs"><code>discriminator_real_outputs</code></h3>

Alias for field number 6

<h3 id="discriminator_scope"><code>discriminator_scope</code></h3>

Alias for field number 9

<h3 id="discriminator_variables"><code>discriminator_variables</code></h3>

Alias for field number 8

<h3 id="generated_data"><code>generated_data</code></h3>

Alias for field number 1

<h3 id="generator_fn"><code>generator_fn</code></h3>

Alias for field number 4

<h3 id="generator_inputs"><code>generator_inputs</code></h3>

Alias for field number 0

<h3 id="generator_scope"><code>generator_scope</code></h3>

Alias for field number 3

<h3 id="generator_variables"><code>generator_variables</code></h3>

Alias for field number 2

<h3 id="real_data"><code>real_data</code></h3>

Alias for field number 5



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
__new__(
    _cls,
    generator_inputs,
    generated_data,
    generator_variables,
    generator_scope,
    generator_fn,
    real_data,
    discriminator_real_outputs,
    discriminator_gen_outputs,
    discriminator_variables,
    discriminator_scope,
    discriminator_fn
)
```

Create new instance of GANModel(generator_inputs, generated_data, generator_variables, generator_scope, generator_fn, real_data, discriminator_real_outputs, discriminator_gen_outputs, discriminator_variables, discriminator_scope, discriminator_fn)



