page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.features.spectral_norm_regularizer

Returns a functions that can be used to apply spectral norm regularization.

``` python
tf.contrib.gan.features.spectral_norm_regularizer(
    scale,
    power_iteration_rounds=1,
    scope=None
)
```



Defined in [`contrib/gan/python/features/python/spectral_normalization_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/features/python/spectral_normalization_impl.py).

<!-- Placeholder for "Used in" -->

Small spectral norms enforce a small Lipschitz constant, which is necessary
for Wasserstein GANs.

#### Args:


* <b>`scale`</b>: A scalar multiplier. 0.0 disables the regularizer.
* <b>`power_iteration_rounds`</b>: The number of iterations of the power method to
  perform. A higher number yields a better approximation.
* <b>`scope`</b>: An optional scope name.


#### Returns:

A function with the signature `sn(weights)` that applies spectral norm
regularization.



#### Raises:


* <b>`ValueError`</b>: If scale is negative or if scale is not a float.