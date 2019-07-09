page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.InfoGANModel

## Class `InfoGANModel`





Defined in [`tensorflow/contrib/gan/python/namedtuples.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/gan/python/namedtuples.py).

An InfoGANModel contains all the pieces needed for InfoGAN training.

See https://arxiv.org/abs/1606.03657 for more details.

#### Args:

* <b>`structured_generator_inputs`</b>: A list of Tensors representing the random noise
    that must  have high mutual information with the generator output. List
    length should match `predicted_distributions`.
* <b>`predicted_distributions`</b>: A list of `tfp.distributions.Distribution`s.
    Predicted by the recognizer, and used to evaluate the likelihood of the
    structured noise. List length should match `structured_generator_inputs`.
* <b>`discriminator_and_aux_fn`</b>: The original discriminator function that returns
    a tuple of (logits, `predicted_distributions`).

<h2 id="__new__"><code>__new__</code></h2>

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
    discriminator_fn,
    structured_generator_inputs,
    predicted_distributions,
    discriminator_and_aux_fn
)
```

Create new instance of InfoGANModel(generator_inputs, generated_data, generator_variables, generator_scope, generator_fn, real_data, discriminator_real_outputs, discriminator_gen_outputs, discriminator_variables, discriminator_scope, discriminator_fn, structured_generator_inputs, predicted_distributions, discriminator_and_aux_fn)



## Properties

<h3 id="generator_inputs"><code>generator_inputs</code></h3>



<h3 id="generated_data"><code>generated_data</code></h3>



<h3 id="generator_variables"><code>generator_variables</code></h3>



<h3 id="generator_scope"><code>generator_scope</code></h3>



<h3 id="generator_fn"><code>generator_fn</code></h3>



<h3 id="real_data"><code>real_data</code></h3>



<h3 id="discriminator_real_outputs"><code>discriminator_real_outputs</code></h3>



<h3 id="discriminator_gen_outputs"><code>discriminator_gen_outputs</code></h3>



<h3 id="discriminator_variables"><code>discriminator_variables</code></h3>



<h3 id="discriminator_scope"><code>discriminator_scope</code></h3>



<h3 id="discriminator_fn"><code>discriminator_fn</code></h3>



<h3 id="structured_generator_inputs"><code>structured_generator_inputs</code></h3>



<h3 id="predicted_distributions"><code>predicted_distributions</code></h3>



<h3 id="discriminator_and_aux_fn"><code>discriminator_and_aux_fn</code></h3>





