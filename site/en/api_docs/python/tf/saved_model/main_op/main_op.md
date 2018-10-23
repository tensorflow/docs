


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.saved_model.main_op.main_op

### `tf.saved_model.main_op.main_op`

```
tf.saved_model.main_op.main_op()
```


Returns a main op to init variables and tables.

Returns the main op including the group of ops that initializes all
variables, initializes local variables and initialize all tables.

#### Returns:

  The set of ops to be run as part of the main op upon the load operation.

Defined in [`tensorflow/python/saved_model/main_op_impl.py`](https://www.tensorflow.org/code/tensorflow/python/saved_model/main_op_impl.py).

