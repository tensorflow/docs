

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.l2_regularizer

``` python
tf.contrib.layers.l2_regularizer(
    scale,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/regularizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/layers/python/layers/regularizers.py).

See the guide: [Layers (contrib) > Regularizers](../../../../../api_guides/python/contrib.layers#Regularizers)

Returns a function that can be used to apply L2 regularization to weights.

Small values of L2 can help prevent overfitting the training data.

#### Args:

* <b>`scale`</b>: A scalar multiplier `Tensor`. 0.0 disables the regularizer.
* <b>`scope`</b>: An optional scope name.


#### Returns:

A function with signature `l2(weights)` that applies L2 regularization.


#### Raises:

* <b>`ValueError`</b>: If scale is negative or if scale is not a float.