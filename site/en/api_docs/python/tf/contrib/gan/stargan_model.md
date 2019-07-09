page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.stargan_model

``` python
tf.contrib.gan.stargan_model(
    generator_fn,
    discriminator_fn,
    input_data,
    input_data_domain_label,
    generator_scope='Generator',
    discriminator_scope='Discriminator'
)
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/gan/python/train.py).

Returns a StarGAN model outputs and variables.

See https://arxiv.org/abs/1711.09020 for more details.

#### Args:

* <b>`generator_fn`</b>: A python lambda that takes `inputs` and `targets` as inputs
    and returns 'generated_data' as the transformed version of `input` based
    on the `target`. `input` has shape (n, h, w, c), `targets` has shape (n,
    num_domains), and `generated_data` has the same shape as `input`.
* <b>`discriminator_fn`</b>: A python lambda that takes `inputs` and `num_domains` as
    inputs and returns a tuple (`source_prediction`, `domain_prediction`).
    `source_prediction` represents the source(real/generated) prediction by
    the discriminator, and `domain_prediction` represents the domain
    prediction/classification by the discriminator. `source_prediction` has
    shape (n) and `domain_prediction` has shape (n, num_domains).
* <b>`input_data`</b>: Tensor or a list of tensor of shape (n, h, w, c) representing
    the real input images.
* <b>`input_data_domain_label`</b>: Tensor or a list of tensor of shape (batch_size,
    num_domains) representing the domain label associated with the real
    images.
* <b>`generator_scope`</b>: Optional generator variable scope. Useful if you want to
    reuse a subgraph that has already been created.
* <b>`discriminator_scope`</b>: Optional discriminator variable scope. Useful if you
    want to reuse a subgraph that has already been created.


#### Returns:

StarGANModel nametuple return the tensor that are needed to compute the
loss.


#### Raises:

* <b>`ValueError`</b>: If the shape of `input_data_domain_label` is not rank 2 or fully
  defined in every dimensions.