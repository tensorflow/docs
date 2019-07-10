page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.set_floatx

Sets the default float type.

### Aliases:

* `tf.compat.v1.keras.backend.set_floatx`
* `tf.compat.v2.keras.backend.set_floatx`
* `tf.keras.backend.set_floatx`

``` python
tf.keras.backend.set_floatx(value)
```



Defined in [`python/keras/backend_config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend_config.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`value`</b>: String; 'float16', 'float32', or 'float64'.
Example: ```python from keras import backend as K K.floatx() >>> 'float32'
  K.set_floatx('float16') K.floatx() >>> 'float16' ```

#### Raises:


* <b>`ValueError`</b>: In case of invalid value.