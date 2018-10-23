

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.global_variables_initializer

### `tf.global_variables_initializer`

``` python
global_variables_initializer()
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns an Op that initializes global variables.

This is just a shortcut for `variable_initializers(global_variables())`

#### Returns:

  An Op that initializes global variables in the graph.