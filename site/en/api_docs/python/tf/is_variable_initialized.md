

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.is_variable_initialized

### `tf.is_variable_initialized`

``` python
is_variable_initialized(variable)
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Tests if a variable has been initialized.

#### Args:

* <b>`variable`</b>: A `Variable`.


#### Returns:

  Returns a scalar boolean Tensor, `True` if the variable has been
  initialized, `False` otherwise.