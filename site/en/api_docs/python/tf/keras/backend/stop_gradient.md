page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.stop_gradient

Returns `variables` but with zero gradient w.r.t. every other variable.

### Aliases:

* `tf.compat.v1.keras.backend.stop_gradient`
* `tf.compat.v2.keras.backend.stop_gradient`
* `tf.keras.backend.stop_gradient`

``` python
tf.keras.backend.stop_gradient(variables)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`variables`</b>: Tensor or list of tensors to consider constant with respect
  to any other variable.



#### Returns:

A single tensor or a list of tensors (depending on the passed argument)
that has no gradient with respect to any other variable.
