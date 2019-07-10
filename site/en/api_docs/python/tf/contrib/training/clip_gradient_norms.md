page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.clip_gradient_norms

Clips the gradients by the given value.

``` python
tf.contrib.training.clip_gradient_norms(
    gradients_to_variables,
    max_norm
)
```



Defined in [`contrib/training/python/training/training.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/training/python/training/training.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`gradients_to_variables`</b>: A list of gradient to variable pairs (tuples).
* <b>`max_norm`</b>: the maximum norm value.


#### Returns:

A list of clipped gradient to variable pairs.
