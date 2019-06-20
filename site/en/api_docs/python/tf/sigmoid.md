page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sigmoid

### Aliases:

* `tf.nn.sigmoid`
* `tf.sigmoid`

``` python
tf.sigmoid(
    x,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/math_ops.py).

See the guide: [Neural Network > Activation Functions](../../../api_guides/python/nn#Activation_Functions)

Computes sigmoid of `x` element-wise.

Specifically, `y = 1 / (1 + exp(-x))`.

#### Args:

* <b>`x`</b>: A Tensor with type `float16`, `float32`, `float64`, `complex64`,
    or `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A Tensor with the same type as `x`.



#### Scipy Compatibility
Equivalent to scipy.special.expit

