page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.ACGANModel

## Class `ACGANModel`

An ACGANModel contains all the pieces needed for ACGAN training.





Defined in [`contrib/gan/python/namedtuples.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/namedtuples.py).

<!-- Placeholder for "Used in" -->

See https://arxiv.org/abs/1610.09585 for more details.

#### Args:


* <b>`one_hot_labels`</b>: A Tensor holding one-hot-labels for the batch.
* <b>`discriminator_real_classification_logits`</b>: Classification logits for real
  data.
* <b>`discriminator_gen_classification_logits`</b>: Classification logits for generated
  data.

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




<h3 id="one_hot_labels"><code>one_hot_labels</code></h3>




<h3 id="discriminator_real_classification_logits"><code>discriminator_real_classification_logits</code></h3>




<h3 id="discriminator_gen_classification_logits"><code>discriminator_gen_classification_logits</code></h3>






