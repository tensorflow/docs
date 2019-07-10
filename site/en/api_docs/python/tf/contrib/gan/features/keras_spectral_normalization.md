page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.features.keras_spectral_normalization

A context manager that enables Spectral Normalization for Keras.

``` python
tf.contrib.gan.features.keras_spectral_normalization(
    *args,
    **kwds
)
```

<!-- Placeholder for "Used in" -->

Keras doesn't respect the `custom_getter` in the VariableScope, so this is a
bit of a hack to make things work.

#### Usage:

with keras_spectral_normalization():
  net = discriminator_fn(net)



#### Args:


* <b>`name_filter`</b>: Optionally, a method that takes a Variable name as input and
  returns whether this Variable should be normalized.
* <b>`power_iteration_rounds`</b>: The number of iterations of the power method to
  perform per step. A higher number yields a better approximation of the
  true spectral norm.


#### Yields:

A context manager that wraps the standard Keras variable creation method
with the `spectral_normalization_custom_getter`.
