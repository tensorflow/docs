page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.squeeze

Removes a 1-dimension from the tensor at index "axis".

### Aliases:

* `tf.compat.v1.keras.backend.squeeze`
* `tf.compat.v2.keras.backend.squeeze`
* `tf.keras.backend.squeeze`

``` python
tf.keras.backend.squeeze(
    x,
    axis
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: Axis to drop.


#### Returns:

A tensor with the same data as `x` but reduced dimensions.
