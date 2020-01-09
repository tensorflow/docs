page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.framework


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Framework utilities.

<!-- Placeholder for "Used in" -->












## Modules

[`nest`](../../tf/contrib/framework/nest) module: ## Functions for working with arbitrarily nested sequences of elements.

## Classes

[`class BoundedTensorSpec`](../../tf/contrib/framework/BoundedTensorSpec): A `TensorSpec` that specifies minimum and maximum values.

[`class RecordInput`](../../tf/contrib/framework/RecordInput): RecordInput asynchronously reads and randomly yields TFRecords.

[`class TensorSpec`](../../tf/TensorSpec): Describes a tf.Tensor.

[`class VariableDeviceChooser`](../../tf/contrib/framework/VariableDeviceChooser): Device chooser for variables.

[`class convolutional_delta_orthogonal`](../../tf/contrib/framework/convolutional_delta_orthogonal): Initializer that generates a delta orthogonal kernel for ConvNets.

[`class convolutional_orthogonal_1d`](../../tf/contrib/framework/convolutional_orthogonal_1d): Initializer that generates a 1D orthogonal kernel for ConvNets.

[`class convolutional_orthogonal_2d`](../../tf/contrib/framework/convolutional_orthogonal_2d): Initializer that generates a 2D orthogonal kernel for ConvNets.

[`class convolutional_orthogonal_3d`](../../tf/contrib/framework/convolutional_orthogonal_3d): Initializer that generates a 3D orthogonal kernel for ConvNets.

## Functions

[`add_arg_scope(...)`](../../tf/contrib/framework/add_arg_scope): Decorates a function with args so it can be used within an arg_scope.

[`add_model_variable(...)`](../../tf/contrib/framework/add_model_variable): Adds a variable to the <a href="/api_docs/python/tf/GraphKeys#MODEL_VARIABLES"><code>GraphKeys.MODEL_VARIABLES</code></a> collection.

[`arg_scope(...)`](../../tf/contrib/framework/arg_scope): Stores the default arguments for the given set of list_ops.

[`arg_scoped_arguments(...)`](../../tf/contrib/framework/arg_scoped_arguments): Returns the list kwargs that arg_scope can set for a func.

[`argsort(...)`](../../tf/argsort): Returns the indices of a tensor that give its sorted order along an axis.

[`assert_global_step(...)`](../../tf/contrib/framework/assert_global_step): DEPRECATED FUNCTION

[`assert_or_get_global_step(...)`](../../tf/contrib/framework/assert_or_get_global_step): Verifies that a global step tensor is valid or gets one if None is given.

[`assert_same_float_dtype(...)`](../../tf/debugging/assert_same_float_dtype): Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](../../tf/debugging/assert_scalar): Asserts that the given `tensor` is a scalar (i.e. zero-dimensional).

[`assert_scalar_int(...)`](../../tf/contrib/framework/assert_scalar_int): Assert `tensor` is 0-D, of type <a href="../../tf#int32"><code>tf.int32</code></a> or <a href="../../tf#int64"><code>tf.int64</code></a>.

[`assign_from_checkpoint(...)`](../../tf/contrib/framework/assign_from_checkpoint): Creates an operation to assign specific variables from a checkpoint.

[`assign_from_checkpoint_fn(...)`](../../tf/contrib/framework/assign_from_checkpoint_fn): Returns a function that assigns specific variables from a checkpoint.

[`assign_from_values(...)`](../../tf/contrib/framework/assign_from_values): Creates an assignment operation from a given mapping.

[`assign_from_values_fn(...)`](../../tf/contrib/framework/assign_from_values_fn): Returns a function that assigns specific variables from the given values.

[`convert_to_tensor_or_sparse_tensor(...)`](../../tf/convert_to_tensor_or_sparse_tensor): Converts value to a `SparseTensor` or `Tensor`.

[`create_global_step(...)`](../../tf/contrib/framework/create_global_step): Create global step tensor in graph. (deprecated)

[`current_arg_scope(...)`](../../tf/contrib/framework/current_arg_scope)

[`deprecated(...)`](../../tf/contrib/framework/deprecated): Decorator for marking functions or methods deprecated.

[`deprecated_arg_values(...)`](../../tf/contrib/framework/deprecated_arg_values): Decorator for marking specific function argument values as deprecated.

[`deprecated_args(...)`](../../tf/contrib/framework/deprecated_args): Decorator for marking specific function arguments as deprecated.

[`filter_variables(...)`](../../tf/contrib/framework/filter_variables): Filter a list of variables using regular expressions.

[`fuse_op(...)`](../../tf/contrib/framework/fuse_op): Fuse subgraph between input_nodes and output_nodes into a single custom op.

[`get_global_step(...)`](../../tf/contrib/framework/get_global_step): DEPRECATED FUNCTION

[`get_graph_from_inputs(...)`](../../tf/contrib/framework/get_graph_from_inputs): Returns the appropriate graph to use for the given inputs.

[`get_local_variables(...)`](../../tf/contrib/framework/get_local_variables): Gets the list of local variables, filtered by scope and/or suffix.

[`get_model_variables(...)`](../../tf/contrib/framework/get_model_variables): Gets the list of model variables, filtered by scope and/or suffix.

[`get_name_scope(...)`](../../tf/contrib/framework/get_name_scope): Returns the current name scope of the default graph.

[`get_or_create_global_step(...)`](../../tf/contrib/framework/get_or_create_global_step): Returns and create (if necessary) the global step tensor. (deprecated)

[`get_placeholders(...)`](../../tf/contrib/framework/get_placeholders): Get placeholders of a graph.

[`get_trainable_variables(...)`](../../tf/contrib/framework/get_trainable_variables): Gets the list of trainable variables, filtered by scope and/or suffix.

[`get_unique_variable(...)`](../../tf/contrib/framework/get_unique_variable): Gets the variable uniquely identified by that var_op_name.

[`get_variable_full_name(...)`](../../tf/contrib/framework/get_variable_full_name): Returns the full name of a variable.

[`get_variables(...)`](../../tf/contrib/framework/get_variables): Gets the list of variables, filtered by scope and/or suffix.

[`get_variables_by_name(...)`](../../tf/contrib/framework/get_variables_by_name): Gets the list of variables that were given that name.

[`get_variables_by_suffix(...)`](../../tf/contrib/framework/get_variables_by_suffix): Gets the list of variables that end with the given suffix.

[`get_variables_to_restore(...)`](../../tf/contrib/framework/get_variables_to_restore): Gets the list of the variables to restore.

[`global_variable(...)`](../../tf/contrib/framework/global_variable): Create a variable with a value and add it to <a href="/api_docs/python/tf/GraphKeys#GLOBAL_VARIABLES"><code>GraphKeys.GLOBAL_VARIABLES</code></a>.

[`has_arg_scope(...)`](../../tf/contrib/framework/has_arg_scope): Checks whether a func has been decorated with @add_arg_scope or not.

[`init_from_checkpoint(...)`](../../tf/contrib/framework/init_from_checkpoint): Using assignment map initializes current variables with loaded tensors.

[`is_tensor(...)`](../../tf/is_tensor): Checks whether `x` is a tensor or "tensor-like".

[`list_variables(...)`](../../tf/contrib/framework/list_variables): Returns list of all variables in the latest checkpoint.

[`load_and_remap_matrix_initializer(...)`](../../tf/contrib/framework/load_and_remap_matrix_initializer): Returns a var initializer for loading and remapping a 2-D (matrix) tensor.

[`load_checkpoint(...)`](../../tf/contrib/framework/load_checkpoint): Returns CheckpointReader for latest checkpoint.

[`load_embedding_initializer(...)`](../../tf/contrib/framework/load_embedding_initializer): Returns a variable initializer for loading pre-trained embeddings.

[`load_linear_multiclass_bias_initializer(...)`](../../tf/contrib/framework/load_linear_multiclass_bias_initializer): Loads pre-trained multi-class biases for linear models from checkpoint.

[`load_variable(...)`](../../tf/contrib/framework/load_variable): Returns a Tensor with the contents of the given variable in the checkpoint.

[`load_variable_slot_initializer(...)`](../../tf/contrib/framework/load_variable_slot_initializer): Loads pre-trained multi-class slots for linear models from checkpoint.

[`local_variable(...)`](../../tf/contrib/framework/local_variable): Create a variable with a value and add it to <a href="/api_docs/python/tf/GraphKeys#LOCAL_VARIABLES"><code>GraphKeys.LOCAL_VARIABLES</code></a>.

[`model_variable(...)`](../../tf/contrib/framework/model_variable): Gets an existing model variable with these parameters or creates a new one.

[`prepend_name_scope(...)`](../../tf/contrib/framework/prepend_name_scope): Prepends name scope to a name.

[`py_func(...)`](../../tf/contrib/framework/py_func): Wraps a python function and uses it as a TensorFlow op.

[`reduce_sum_n(...)`](../../tf/contrib/framework/reduce_sum_n): Reduce tensors to a scalar sum.

[`remove_squeezable_dimensions(...)`](../../tf/contrib/framework/remove_squeezable_dimensions): Squeeze last dim if ranks of `predictions` and `labels` differ by 1. (deprecated)

[`smart_case(...)`](../../tf/contrib/framework/smart_case): Like tf.case, except attempts to statically evaluate predicates.

[`smart_cond(...)`](../../tf/contrib/framework/smart_cond): Return either `true_fn()` if predicate `pred` is true else `false_fn()`.

[`smart_constant_value(...)`](../../tf/contrib/framework/smart_constant_value): Return the bool value for `pred`, or None if `pred` had a dynamic value.

[`sort(...)`](../../tf/sort): Sorts a tensor.

[`strip_name_scope(...)`](../../tf/contrib/framework/strip_name_scope): Removes name scope from a name.

[`variable(...)`](../../tf/contrib/framework/variable): Gets an existing variable with these parameters or creates a new one.

[`with_same_shape(...)`](../../tf/contrib/framework/with_same_shape): Assert tensors are the same shape, from the same graph.

[`with_shape(...)`](../../tf/contrib/framework/with_shape): Asserts tensor has expected shape.

[`zero_initializer(...)`](../../tf/contrib/framework/zero_initializer): Initialize 'ref' with all zeros, ref tensor should be uninitialized.
