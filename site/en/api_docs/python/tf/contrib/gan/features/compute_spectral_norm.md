page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.features.compute_spectral_norm

Estimates the largest singular value in the weight tensor.

``` python
tf.contrib.gan.features.compute_spectral_norm(
    w_tensor,
    power_iteration_rounds=1,
    name=None
)
```



Defined in [`contrib/gan/python/features/python/spectral_normalization_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/features/python/spectral_normalization_impl.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`w_tensor`</b>: The weight matrix whose spectral norm should be computed.
* <b>`power_iteration_rounds`</b>: The number of iterations of the power method to
  perform. A higher number yields a better approximation.
* <b>`name`</b>: An optional scope name.


#### Returns:

The largest singular value (the spectral norm) of w.
