page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.elu

``` python
tf.keras.activations.elu(
    x,
    alpha=1.0
)
```



Defined in [`tensorflow/python/keras/activations.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/keras/activations.py).

Exponential linear unit.

#### Arguments:

* <b>`x`</b>: Input tensor.
* <b>`alpha`</b>: A scalar, slope of negative section.


#### Returns:

    The exponential linear activation: `x` if `x > 0` and
      `alpha * (exp(x)-1)` if `x < 0`.

Reference:
    - [Fast and Accurate Deep Network Learning by Exponential
      Linear Units (ELUs)](https://arxiv.org/abs/1511.07289)