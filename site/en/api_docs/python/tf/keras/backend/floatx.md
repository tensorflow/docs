page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.floatx

Returns the default float type, as a string.

### Aliases:

* `tf.compat.v1.keras.backend.floatx`
* `tf.compat.v2.keras.backend.floatx`
* `tf.keras.backend.floatx`

``` python
tf.keras.backend.floatx()
```



Defined in [`python/keras/backend_config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend_config.py).

<!-- Placeholder for "Used in" -->

E.g. 'float16', 'float32', 'float64'.

#### Returns:

String, the current default float type.



#### Example:


```python
keras.backend.floatx() >>> 'float32'
```