

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.local_variables_initializer

### `tf.local_variables_initializer`

``` python
local_variables_initializer()
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns an Op that initializes all local variables.

This is just a shortcut for `variable_initializer(local_variables())`

#### Returns:

  An Op that initializes all local variables in the graph.