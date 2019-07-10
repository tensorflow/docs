page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.is_variable_initialized

Tests if a variable has been initialized.

### Aliases:

* `tf.compat.v1.is_variable_initialized`
* `tf.is_variable_initialized`

``` python
tf.is_variable_initialized(variable)
```



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`variable`</b>: A `Variable`.


#### Returns:

Returns a scalar boolean Tensor, `True` if the variable has been
initialized, `False` otherwise.



**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.