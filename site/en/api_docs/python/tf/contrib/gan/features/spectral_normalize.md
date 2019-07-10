page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.features.spectral_normalize

Normalizes a weight matrix by its spectral norm.

``` python
tf.contrib.gan.features.spectral_normalize(
    w,
    power_iteration_rounds=1,
    name=None
)
```



Defined in [`contrib/gan/python/features/python/spectral_normalization_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/features/python/spectral_normalization_impl.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`w`</b>: The weight matrix to be normalized.
* <b>`power_iteration_rounds`</b>: The number of iterations of the power method to
  perform. A higher number yields a better approximation.
* <b>`name`</b>: An optional scope name.


#### Returns:

A normalized weight matrix tensor.
