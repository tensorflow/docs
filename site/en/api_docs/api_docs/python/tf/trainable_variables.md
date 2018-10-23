

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.trainable_variables

``` python
trainable_variables()
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns all variables created with `trainable=True`.

When passed `trainable=True`, the `Variable()` constructor automatically
adds new variables to the graph collection
`GraphKeys.TRAINABLE_VARIABLES`. This convenience function returns the
contents of that collection.

#### Returns:

  A list of Variable objects.