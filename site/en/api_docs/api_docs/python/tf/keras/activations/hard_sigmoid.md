

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.hard_sigmoid

``` python
tf.keras.activations.hard_sigmoid(x)
```



Defined in [`tensorflow/python/keras/activations.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/activations.py).

Hard sigmoid activation function.

Faster to compute than sigmoid activation.

#### Arguments:

* <b>`x`</b>: Input tensor.


#### Returns:

Hard sigmoid activation:
- `0` if `x < -2.5`
- `1` if `x > 2.5`
- `0.2 * x + 0.5` if `-2.5 <= x <= 2.5`.