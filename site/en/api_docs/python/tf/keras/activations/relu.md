page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.relu

``` python
tf.keras.activations.relu(
    x,
    alpha=0.0,
    max_value=None
)
```



Defined in [`tensorflow/python/keras/activations.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/activations.py).

Rectified Linear Unit.

#### Arguments:

* <b>`x`</b>: Input tensor.
* <b>`alpha`</b>: Slope of the negative part. Defaults to zero.
* <b>`max_value`</b>: Maximum value for the output.


#### Returns:

The (leaky) rectified linear unit activation: `x` if `x > 0`,
  `alpha * x` if `x < 0`. If `max_value` is defined, the result
  is truncated to this value.