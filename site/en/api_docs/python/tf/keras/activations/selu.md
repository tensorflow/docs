page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.selu

``` python
tf.keras.activations.selu(x)
```



Defined in [`tensorflow/python/keras/activations.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/activations.py).

Scaled Exponential Linear Unit. (Klambauer et al., 2017).

#### Arguments:

* <b>`x`</b>: A tensor or variable to compute the activation function for.


#### Returns:

    Tensor with the same shape and dtype as `x`.

# Note
    - To be used together with the initialization "lecun_normal".
    - To be used together with the dropout variant "AlphaDropout".