page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.tanh

Hyperbolic Tangent activation function.

### Aliases:

* `tf.compat.v1.keras.activations.tanh`
* `tf.compat.v2.keras.activations.tanh`
* `tf.keras.activations.tanh`

``` python
tf.keras.activations.tanh(x)
```



Defined in [`python/keras/activations.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/activations.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Input tensor.


#### Returns:

The tanh activation: `tanh(x) = sinh(x)/cosh(x) = ((exp(x) -
exp(-x))/(exp(x) + exp(-x)))`.
