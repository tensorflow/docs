page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.manual_variable_initialization

Sets the manual variable initialization flag.

### Aliases:

* `tf.compat.v1.keras.backend.manual_variable_initialization`
* `tf.compat.v2.keras.backend.manual_variable_initialization`
* `tf.keras.backend.manual_variable_initialization`

``` python
tf.keras.backend.manual_variable_initialization(value)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

This boolean flag determines whether
variables should be initialized
as they are instantiated (default), or if
the user should handle the initialization
(e.g. via <a href="../../../tf/initialize_all_variables"><code>tf.compat.v1.initialize_all_variables()</code></a>).

#### Arguments:


* <b>`value`</b>: Python boolean.