

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.saved_model.main_op.main_op_with_restore

``` python
tf.saved_model.main_op.main_op_with_restore(restore_op_name)
```



Defined in [`tensorflow/python/saved_model/main_op_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/saved_model/main_op_impl.py).

Returns a main op to init variables, tables and restore the graph.

Returns the main op including the group of ops that initializes all
variables, initialize local variables, initialize all tables and the restore
op name.

#### Args:

* <b>`restore_op_name`</b>: Name of the op to use to restore the graph.


#### Returns:

The set of ops to be run as part of the main op upon the load operation.