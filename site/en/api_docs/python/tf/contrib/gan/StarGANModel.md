page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.StarGANModel

## Class `StarGANModel`





Defined in [`tensorflow/contrib/gan/python/namedtuples.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/gan/python/namedtuples.py).

A StarGANModel contains all the pieces needed for StarGAN training.

#### Args:

* <b>`input_data`</b>: The real images that need to be transferred by the generator.
* <b>`input_data_domain_label`</b>: The real domain labels associated with the real
    images.
* <b>`generated_data`</b>: The generated images produced by the generator. It has the
    same shape as the input_data.
* <b>`generated_data_domain_target`</b>: The target domain that the generated images
    belong to. It has the same shape as the input_data_domain_label.
* <b>`reconstructed_data`</b>: The reconstructed images produced by the G(enerator).
    reconstructed_data = G(G(input_data, generated_data_domain_target),
    input_data_domain_label).
* <b>`discriminator_input_data_source`</b>: The discriminator's output for predicting
    the source (real/generated) of input_data.
* <b>`discriminator_generated_data_source`</b>: The discriminator's output for
    predicting the source (real/generated) of  generated_data.
* <b>`discriminator_input_data_domain_predication`</b>: The discriminator's output for
    predicting the domain_label for the input_data.
* <b>`discriminator_generated_data_domain_predication`</b>: The discriminatorr's output
    for predicting the domain_target for the generated_data.
* <b>`generator_variables`</b>: A list of all generator variables.
* <b>`generator_scope`</b>: Variable scope all generator variables live in.
* <b>`generator_fn`</b>: The generator function.
* <b>`discriminator_variables`</b>: A list of all discriminator variables.
* <b>`discriminator_scope`</b>: Variable scope all discriminator variables live in.
* <b>`discriminator_fn`</b>: The discriminator function.

<h2 id="__new__"><code>__new__</code></h2>

``` python
__new__(
    _cls,
    input_data,
    input_data_domain_label,
    generated_data,
    generated_data_domain_target,
    reconstructed_data,
    discriminator_input_data_source_predication,
    discriminator_generated_data_source_predication,
    discriminator_input_data_domain_predication,
    discriminator_generated_data_domain_predication,
    generator_variables,
    generator_scope,
    generator_fn,
    discriminator_variables,
    discriminator_scope,
    discriminator_fn
)
```

Create new instance of StarGANModel(input_data, input_data_domain_label, generated_data, generated_data_domain_target, reconstructed_data, discriminator_input_data_source_predication, discriminator_generated_data_source_predication, discriminator_input_data_domain_predication, discriminator_generated_data_domain_predication, generator_variables, generator_scope, generator_fn, discriminator_variables, discriminator_scope, discriminator_fn)



## Properties

<h3 id="input_data"><code>input_data</code></h3>



<h3 id="input_data_domain_label"><code>input_data_domain_label</code></h3>



<h3 id="generated_data"><code>generated_data</code></h3>



<h3 id="generated_data_domain_target"><code>generated_data_domain_target</code></h3>



<h3 id="reconstructed_data"><code>reconstructed_data</code></h3>



<h3 id="discriminator_input_data_source_predication"><code>discriminator_input_data_source_predication</code></h3>



<h3 id="discriminator_generated_data_source_predication"><code>discriminator_generated_data_source_predication</code></h3>



<h3 id="discriminator_input_data_domain_predication"><code>discriminator_input_data_domain_predication</code></h3>



<h3 id="discriminator_generated_data_domain_predication"><code>discriminator_generated_data_domain_predication</code></h3>



<h3 id="generator_variables"><code>generator_variables</code></h3>



<h3 id="generator_scope"><code>generator_scope</code></h3>



<h3 id="generator_fn"><code>generator_fn</code></h3>



<h3 id="discriminator_variables"><code>discriminator_variables</code></h3>



<h3 id="discriminator_scope"><code>discriminator_scope</code></h3>



<h3 id="discriminator_fn"><code>discriminator_fn</code></h3>





