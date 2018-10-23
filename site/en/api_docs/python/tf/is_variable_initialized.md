

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.is_variable_initialized

``` python
tf.is_variable_initialized(variable)
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Tests if a variable has been initialized.

#### Args:

* <b>`variable`</b>: A `Variable`.


#### Returns:

  Returns a scalar boolean Tensor, `True` if the variable has been
  initialized, `False` otherwise.


**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.