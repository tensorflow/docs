

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.losses.wargs.wasserstein_gradient_penalty

``` python
tf.contrib.gan.losses.wargs.wasserstein_gradient_penalty(
    real_data,
    generated_data,
    generator_inputs,
    discriminator_fn,
    discriminator_scope,
    epsilon=1e-10,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=losses.Reduction.SUM_BY_NONZERO_WEIGHTS,
    add_summaries=False
)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/gan/python/losses/python/losses_impl.py).

The gradient penalty for the Wasserstein discriminator loss.

See `Improved Training of Wasserstein GANs`
(https://arxiv.org/abs/1704.00028) for more details.

#### Args:

* <b>`real_data`</b>: Real data.
* <b>`generated_data`</b>: Output of the generator.
* <b>`generator_inputs`</b>: Exact argument to pass to the generator, which is used
    as optional conditioning to the discriminator.
* <b>`discriminator_fn`</b>: A discriminator function that conforms to TFGAN API.
* <b>`discriminator_scope`</b>: If not `None`, reuse discriminators from this scope.
* <b>`epsilon`</b>: A small positive number added for numerical stability when
    computing the gradient norm.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `real_data` and `generated_data`, and must be broadcastable to
    them (i.e., all dimensions must be either `1`, or the same as the
    corresponding dimension).
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which this loss will be added.
* <b>`reduction`</b>: A `tf.losses.Reduction` to apply to loss.
* <b>`add_summaries`</b>: Whether or not to add summaries for the loss.


#### Returns:

A loss Tensor. The shape depends on `reduction`.


#### Raises:

* <b>`ValueError`</b>: If the rank of data Tensors is unknown.