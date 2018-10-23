


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.contrib.framework

### Module `tf.contrib.framework`

Framework utilities. See the [Framework (contrib)](../../../../api_guides/python/contrib.framework) guide.






## Members

[`class VariableDeviceChooser`](../../tf/contrib/framework/VariableDeviceChooser): Device chooser for variables.

[`add_arg_scope(...)`](../../tf/contrib/framework/add_arg_scope): Decorates a function with args so it can be used within an arg_scope.

[`add_model_variable(...)`](../../tf/contrib/framework/add_model_variable): Adds a variable to the `GraphKeys.MODEL_VARIABLES` collection.

[`arg_scope(...)`](../../tf/contrib/framework/arg_scope): Stores the default arguments for the given set of list_ops.

[`arg_scoped_arguments(...)`](../../tf/contrib/framework/arg_scoped_arguments): Returns the list kwargs that arg_scope can set for a func.

[`assert_global_step(...)`](../../tf/contrib/framework/assert_global_step)

[`assert_or_get_global_step(...)`](../../tf/contrib/framework/assert_or_get_global_step): Verifies that a global step tensor is valid or gets one if None is given.

[`assert_same_float_dtype(...)`](../../tf/contrib/framework/assert_same_float_dtype): Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](../../tf/contrib/framework/assert_scalar)

[`assert_scalar_int(...)`](../../tf/contrib/framework/assert_scalar_int): Assert `tensor` is 0-D, of type `tf.int32` or `tf.int64`.

[`assign_from_checkpoint(...)`](../../tf/contrib/framework/assign_from_checkpoint): Creates an operation to assign specific variables from a checkpoint.

[`assign_from_checkpoint_fn(...)`](../../tf/contrib/framework/assign_from_checkpoint_fn): Returns a function that assigns specific variables from a checkpoint.

[`assign_from_values(...)`](../../tf/contrib/framework/assign_from_values): Creates an assignment operation from a given mapping.

[`assign_from_values_fn(...)`](../../tf/contrib/framework/assign_from_values_fn): Returns a function that assigns specific variables from the given values.

[`convert_to_tensor_or_sparse_tensor(...)`](../../tf/convert_to_tensor_or_sparse_tensor): Converts value to a `SparseTensor` or `Tensor`.

[`create_global_step(...)`](../../tf/contrib/framework/create_global_step): Create global step tensor in graph.

[`deprecated(...)`](../../tf/contrib/framework/deprecated): Decorator for marking functions or methods deprecated.

[`deprecated_arg_values(...)`](../../tf/contrib/framework/deprecated_arg_values): Decorator for marking specific function argument values as deprecated.

[`deprecated_args(...)`](../../tf/contrib/framework/deprecated_args): Decorator for marking specific function arguments as deprecated.

[`filter_variables(...)`](../../tf/contrib/framework/filter_variables): Filter a list of variables using regular expressions.

[`get_global_step(...)`](../../tf/contrib/framework/get_global_step)

[`get_graph_from_inputs(...)`](../../tf/contrib/framework/get_graph_from_inputs): Returns the appropriate graph to use for the given inputs.

[`get_local_variables(...)`](../../tf/contrib/framework/get_local_variables): Gets the list of local variables, filtered by scope and/or suffix.

[`get_model_variables(...)`](../../tf/contrib/framework/get_model_variables): Gets the list of model variables, filtered by scope and/or suffix.

[`get_or_create_global_step(...)`](../../tf/contrib/framework/get_or_create_global_step): Returns and create (if necessary) the global step variable.

[`get_unique_variable(...)`](../../tf/contrib/framework/get_unique_variable): Gets the variable uniquely identified by that var_op_name.

[`get_variables(...)`](../../tf/contrib/framework/get_variables): Gets the list of variables, filtered by scope and/or suffix.

[`get_variables_by_name(...)`](../../tf/contrib/framework/get_variables_by_name): Gets the list of variables that were given that name.

[`get_variables_by_suffix(...)`](../../tf/contrib/framework/get_variables_by_suffix): Gets the list of variables that end with the given suffix.

[`get_variables_to_restore(...)`](../../tf/contrib/framework/get_variables_to_restore): Gets the list of the variables to restore.

[`has_arg_scope(...)`](../../tf/contrib/framework/has_arg_scope): Checks whether a func has been decorated with @add_arg_scope or not.

[`init_from_checkpoint(...)`](../../tf/contrib/framework/init_from_checkpoint): Using assingment map initializes current variables with loaded tensors.

[`is_tensor(...)`](../../tf/contrib/framework/is_tensor): Check for tensor types.

[`list_variables(...)`](../../tf/contrib/framework/list_variables): Returns list of all variables in the latest checkpoint.

[`load_checkpoint(...)`](../../tf/contrib/framework/load_checkpoint): Returns CheckpointReader for latest checkpoint.

[`load_variable(...)`](../../tf/contrib/framework/load_variable): Returns a Tensor with the contents of the given variable in the checkpoint.

[`local_variable(...)`](../../tf/contrib/framework/local_variable): Create variable and add it to `GraphKeys.LOCAL_VARIABLES` collection.

[`model_variable(...)`](../../tf/contrib/framework/model_variable): Gets an existing model variable with these parameters or creates a new one.

[`reduce_sum_n(...)`](../../tf/contrib/framework/reduce_sum_n): Reduce tensors to a scalar sum.

[`remove_squeezable_dimensions(...)`](../../tf/contrib/framework/remove_squeezable_dimensions): Squeeze last dim if ranks of `predictions` and `labels` differ by 1.

[`variable(...)`](../../tf/contrib/framework/variable): Gets an existing variable with these parameters or creates a new one.

[`with_same_shape(...)`](../../tf/contrib/framework/with_same_shape): Assert tensors are the same shape, from the same graph.

[`with_shape(...)`](../../tf/contrib/framework/with_shape): Asserts tensor has expected shape.

[`zero_initializer(...)`](../../tf/contrib/framework/zero_initializer): Initialize 'ref' with all zeros, ref tensor should be uninitialized.

Defined in [`tensorflow/contrib/framework/__init__.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/__init__.py).

