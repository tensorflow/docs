page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.unit_norm

Normalizes the given input across the specified dimension to unit length.

``` python
tf.contrib.layers.unit_norm(
    inputs,
    dim,
    epsilon=1e-07,
    scope=None
)
```



Defined in [`contrib/layers/python/layers/layers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/layers.py).

<!-- Placeholder for "Used in" -->

Note that the rank of `input` must be known.

#### Args:


* <b>`inputs`</b>: A `Tensor` of arbitrary size.
* <b>`dim`</b>: The dimension along which the input is normalized.
* <b>`epsilon`</b>: A small value to add to the inputs to avoid dividing by zero.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

The normalized `Tensor`.



#### Raises:


* <b>`ValueError`</b>: If dim is smaller than the number of dimensions in 'inputs'.