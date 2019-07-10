page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.features.spectral_normalization_custom_getter

Custom getter that performs Spectral Normalization on a weight tensor.

``` python
tf.contrib.gan.features.spectral_normalization_custom_getter(
    name_filter=_default_name_filter,
    power_iteration_rounds=1
)
```



Defined in [`contrib/gan/python/features/python/spectral_normalization_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/features/python/spectral_normalization_impl.py).

<!-- Placeholder for "Used in" -->

Specifically it divides the weight tensor by its largest singular value. This
is intended to stabilize GAN training, by making the discriminator satisfy a
local 1-Lipschitz constraint.

Based on [Spectral Normalization for Generative Adversarial Networks][sn-gan].

[sn-gan]: https://openreview.net/forum?id=B1QRgziT-

To reproduce an SN-GAN, apply this custom_getter to every weight tensor of
your discriminator. The last dimension of the weight tensor must be the number
of output channels.

Apply this to layers by supplying this as the `custom_getter` of a
<a href="../../../../tf/variable_scope"><code>tf.compat.v1.variable_scope</code></a>. For example:

  with tf.compat.v1.variable_scope('discriminator',
                         custom_getter=spectral_norm_getter()):
    net = discriminator_fn(net)

IMPORTANT: Keras does not respect the custom_getter supplied by the
VariableScope, so Keras users should use `keras_spectral_normalization`
instead of (or in addition to) this approach.

It is important to carefully select to which weights you want to apply
Spectral Normalization. In general you want to normalize the kernels of
convolution and dense layers, but you do not want to normalize biases. You
also want to avoid normalizing batch normalization (and similar) variables,
but in general such layers play poorly with Spectral Normalization, since the
gamma can cancel out the normalization in other layers. By default we supply a
filter that matches the kernel variable names of the dense and convolution
layers of the tf.layers, tf.contrib.layers, tf.keras and tf.contrib.slim
libraries. If you are using anything else you'll need a custom `name_filter`.

This custom getter internally creates a variable used to compute the spectral
norm by power iteration. It will update every time the variable is accessed,
which means the normalized discriminator weights may change slightly whilst
training the generator. Whilst unusual, this matches how the paper's authors
implement it, and in general additional rounds of power iteration can't hurt.

#### Args:


* <b>`name_filter`</b>: Optionally, a method that takes a Variable name as input and
  returns whether this Variable should be normalized.
* <b>`power_iteration_rounds`</b>: The number of iterations of the power method to
  perform per step. A higher number yields a better approximation of the
  true spectral norm.


#### Returns:

A custom getter function that applies Spectral Normalization to all
Variables whose names match `name_filter`.



#### Raises:


* <b>`ValueError`</b>: If name_filter is not callable.