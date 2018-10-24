

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.cyclegan_model

``` python
tf.contrib.gan.cyclegan_model(
    generator_fn,
    discriminator_fn,
    data_x,
    data_y,
    generator_scope='Generator',
    discriminator_scope='Discriminator',
    model_x2y_scope='ModelX2Y',
    model_y2x_scope='ModelY2X',
    check_shapes=True
)
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/train.py).

Returns a CycleGAN model outputs and variables.

See https://arxiv.org/abs/1703.10593 for more details.

#### Args:

* <b>`generator_fn`</b>: A python lambda that takes `data_x` or `data_y` as inputs and
    returns the outputs of the GAN generator.
* <b>`discriminator_fn`</b>: A python lambda that takes `real_data`/`generated data`
    and `generator_inputs`. Outputs a Tensor in the range [-inf, inf].
* <b>`data_x`</b>: A `Tensor` of dataset X. Must be the same shape as `data_y`.
* <b>`data_y`</b>: A `Tensor` of dataset Y. Must be the same shape as `data_x`.
* <b>`generator_scope`</b>: Optional generator variable scope. Useful if you want to
    reuse a subgraph that has already been created. Defaults to 'Generator'.
* <b>`discriminator_scope`</b>: Optional discriminator variable scope. Useful if you
    want to reuse a subgraph that has already been created. Defaults to
    'Discriminator'.
* <b>`model_x2y_scope`</b>: Optional variable scope for model x2y variables. Defaults
    to 'ModelX2Y'.
* <b>`model_y2x_scope`</b>: Optional variable scope for model y2x variables. Defaults
    to 'ModelY2X'.
* <b>`check_shapes`</b>: If `True`, check that generator produces Tensors that are the
    same shape as `data_x` (`data_y`). Otherwise, skip this check.


#### Returns:

A `CycleGANModel` namedtuple.


#### Raises:

* <b>`ValueError`</b>: If `check_shapes` is True and `data_x` or the generator output
    does not have the same shape as `data_y`.