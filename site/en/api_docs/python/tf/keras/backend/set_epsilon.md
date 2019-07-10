page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.set_epsilon

Sets the value of the fuzz factor used in numeric expressions.

### Aliases:

* `tf.compat.v1.keras.backend.set_epsilon`
* `tf.compat.v2.keras.backend.set_epsilon`
* `tf.keras.backend.set_epsilon`

``` python
tf.keras.backend.set_epsilon(value)
```



Defined in [`python/keras/backend_config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend_config.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`value`</b>: float. New value of epsilon.
Example: ```python from keras import backend as K K.epsilon() >>> 1e-07
  K.set_epsilon(1e-05) K.epsilon() >>> 1e-05 ```