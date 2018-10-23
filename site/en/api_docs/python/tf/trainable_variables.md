


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.trainable_variables

### `tf.trainable_variables`

```
tf.trainable_variables()
```


See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns all variables created with `trainable=True`.

When passed `trainable=True`, the `Variable()` constructor automatically
adds new variables to the graph collection
`GraphKeys.TRAINABLE_VARIABLES`. This convenience function returns the
contents of that collection.

#### Returns:

  A list of Variable objects.

Defined in [`tensorflow/python/ops/variables.py`](https://www.tensorflow.org/code/tensorflow/python/ops/variables.py).

