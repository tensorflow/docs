


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.local_variables

### `tf.local_variables`

```
tf.local_variables()
```


See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns local variables.

Local variables - per process variables, usually not saved/restored to
checkpoint and used for temporary or intermediate values.
For example, they can be used as counters for metrics computation or
number of epochs this machine has read data.
The `local_variable()` automatically adds new variable to
`GraphKeys.LOCAL_VARIABLES`.
This convenience function returns the contents of that collection.

An alternative to local variables are global variables. See
[`tf.global_variables`](../tf/global_variables)

#### Returns:

  A list of local `Variable` objects.

Defined in [`tensorflow/python/ops/variables.py`](https://www.tensorflow.org/code/tensorflow/python/ops/variables.py).

