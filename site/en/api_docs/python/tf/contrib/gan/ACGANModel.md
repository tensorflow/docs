page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.ACGANModel

## Class `ACGANModel`





Defined in [`tensorflow/contrib/gan/python/namedtuples.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/namedtuples.py).

An ACGANModel contains all the pieces needed for ACGAN training.

See https://arxiv.org/abs/1610.09585 for more details.

#### Args:

* <b>`one_hot_labels`</b>: A Tensor holding one-hot-labels for the batch.
* <b>`discriminator_real_classification_logits`</b>: Classification logits for real
    data.
* <b>`discriminator_gen_classification_logits`</b>: Classification logits for generated
    data.

## Properties

<h3 id="discriminator_fn"><code>discriminator_fn</code></h3>

Alias for field number 10

<h3 id="discriminator_gen_classification_logits"><code>discriminator_gen_classification_logits</code></h3>

Alias for field number 13

<h3 id="discriminator_gen_outputs"><code>discriminator_gen_outputs</code></h3>

Alias for field number 7

<h3 id="discriminator_real_classification_logits"><code>discriminator_real_classification_logits</code></h3>

Alias for field number 12

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

<h3 id="one_hot_labels"><code>one_hot_labels</code></h3>

Alias for field number 11

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
    discriminator_fn,
    one_hot_labels,
    discriminator_real_classification_logits,
    discriminator_gen_classification_logits
)
```

Create new instance of ACGANModel(generator_inputs, generated_data, generator_variables, generator_scope, generator_fn, real_data, discriminator_real_outputs, discriminator_gen_outputs, discriminator_variables, discriminator_scope, discriminator_fn, one_hot_labels, discriminator_real_classification_logits, discriminator_gen_classification_logits)



