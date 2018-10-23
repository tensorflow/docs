

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.global_variables

``` python
global_variables()
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns global variables.

Global variables are variables that are shared across machines in a
distributed environment. The `Variable()` constructor or `get_variable()`
automatically adds new variables to the graph collection
`GraphKeys.GLOBAL_VARIABLES`.
This convenience function returns the contents of that collection.

An alternative to global variables are local variables. See
[`tf.local_variables`](../tf/local_variables)

#### Returns:

  A list of `Variable` objects.