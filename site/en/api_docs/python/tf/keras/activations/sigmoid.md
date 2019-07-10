page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.sigmoid

Sigmoid.

### Aliases:

* `tf.compat.v1.keras.activations.sigmoid`
* `tf.compat.v2.keras.activations.sigmoid`
* `tf.keras.activations.sigmoid`

``` python
tf.keras.activations.sigmoid(x)
```



Defined in [`python/keras/activations.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/activations.py).

<!-- Placeholder for "Used in" -->

Applies the sigmoid activation function. The sigmoid function is defined as
1 divided by (1 + exp(-x)). It's curve is like an "S" and is like a smoothed
version of the Heaviside (Unit Step Function) function. For small values
(<-5) the sigmoid returns a value close to zero and for larger values (>5)
the result of the function gets close to 1.
Arguments:
    x: A tensor or variable.

#### Returns:

A tensor.

Sigmoid activation function.

#### Arguments:


* <b>`x`</b>: Input tensor.


#### Returns:

The sigmoid activation: `(1.0 / (1.0 + exp(-x)))`.
