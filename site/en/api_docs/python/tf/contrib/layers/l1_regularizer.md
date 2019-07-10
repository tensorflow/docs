page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.l1_regularizer

Returns a function that can be used to apply L1 regularization to weights.

``` python
tf.contrib.layers.l1_regularizer(
    scale,
    scope=None
)
```



Defined in [`contrib/layers/python/layers/regularizers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/regularizers.py).

<!-- Placeholder for "Used in" -->

L1 regularization encourages sparsity.

#### Args:


* <b>`scale`</b>: A scalar multiplier `Tensor`. 0.0 disables the regularizer.
* <b>`scope`</b>: An optional scope name.


#### Returns:

A function with signature `l1(weights)` that apply L1 regularization.



#### Raises:


* <b>`ValueError`</b>: If scale is negative or if scale is not a float.