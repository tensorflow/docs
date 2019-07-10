page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.sum_regularizer

Returns a function that applies the sum of multiple regularizers.

``` python
tf.contrib.layers.sum_regularizer(
    regularizer_list,
    scope=None
)
```



Defined in [`contrib/layers/python/layers/regularizers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/regularizers.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`regularizer_list`</b>: A list of regularizers to apply.
* <b>`scope`</b>: An optional scope name


#### Returns:

A function with signature `sum_reg(weights)` that applies the
sum of all the input regularizers.
