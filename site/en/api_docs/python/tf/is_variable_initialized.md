page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.is_variable_initialized

``` python
tf.is_variable_initialized(variable)
```



Defined in [`tensorflow/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/variables.py).

Tests if a variable has been initialized.

#### Args:

* <b>`variable`</b>: A `Variable`.


#### Returns:

  Returns a scalar boolean Tensor, `True` if the variable has been
  initialized, `False` otherwise.


**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.