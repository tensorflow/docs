page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.selu

``` python
tf.keras.activations.selu(x)
```



Defined in [`tensorflow/python/keras/activations.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/activations.py).

Scaled Exponential Linear Unit (SELU).

SELU is equal to: `scale * elu(x, alpha)`, where alpha and scale
are pre-defined constants. The values of `alpha` and `scale` are
chosen so that the mean and variance of the inputs are preserved
between two consecutive layers as long as the weights are initialized
correctly (see `lecun_normal` initialization) and the number of inputs
is "large enough" (see references for more information).

#### Arguments:

* <b>`x`</b>: A tensor or variable to compute the activation function for.


#### Returns:

    The scaled exponential unit activation: `scale * elu(x, alpha)`.

# Note
    - To be used together with the initialization "lecun_normal".
    - To be used together with the dropout variant "AlphaDropout".

References:
    - [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)