

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf

### Module `tf`



Defined in [`tensorflow/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/__init__.py).



## Modules

[`app`](./tf/app) module: Generic entry point script.

[`compat`](./tf/compat) module: Functions for Python 2 vs. 3 compatibility.

[`contrib`](./tf/contrib) module: contrib module containing volatile or experimental code.

[`errors`](./tf/errors) module: Exception types for TensorFlow errors.

[`estimator`](./tf/estimator) module: Estimator: High level tools for working with models.

[`flags`](./tf/flags) module: Implementation of the flags interface.

[`gfile`](./tf/gfile) module: Import router for file_io.

[`graph_util`](./tf/graph_util) module: Helpers to manipulate a tensor graph in python.

[`image`](./tf/image) module: Image processing and decoding ops.

[`layers`](./tf/layers) module: This library provides a set of high-level neural networks layers.

[`logging`](./tf/logging) module: Logging utilities.

[`losses`](./tf/losses) module: Loss operations for use in neural networks.

[`metrics`](./tf/metrics) module: Evaluation-related metrics.

[`nn`](./tf/nn) module: Neural network support.

[`python_io`](./tf/python_io) module: Python functions for directly manipulating TFRecord-formatted files.

[`pywrap_tensorflow`](./tf/pywrap_tensorflow) module: pywrap_tensorflow wrapper that exports all symbols with RTLD_GLOBAL.

[`resource_loader`](./tf/resource_loader) module: Resource management library.

[`saved_model`](./tf/saved_model) module: Convenience functions to save a model.

[`sdca`](./tf/sdca) module: A Dual Coordinate Ascent optimizer library for training fast linear models.

[`sets`](./tf/sets) module: Tensorflow set operations.

[`spectral`](./tf/spectral) module: Spectral operators (e.g. FFT, RFFT).

[`summary`](./tf/summary) module: Tensor summaries for exporting information about a model.

[`sysconfig`](./tf/sysconfig) module: System configuration library.

[`test`](./tf/test) module: Testing.

[`tools`](./tf/tools) module

[`train`](./tf/train) module: Support for training models.

[`user_ops`](./tf/user_ops) module: All user ops.

## Classes

[`class AggregationMethod`](./tf/AggregationMethod): A class listing aggregation methods used to combine gradients.

[`class AttrValue`](./tf/AttrValue)

[`class ConditionalAccumulator`](./tf/ConditionalAccumulator): A conditional accumulator for aggregating gradients.

[`class ConditionalAccumulatorBase`](./tf/ConditionalAccumulatorBase): A conditional accumulator for aggregating gradients.

[`class ConfigProto`](./tf/ConfigProto)

[`class DType`](./tf/DType): Represents the type of the elements in a `Tensor`.

[`class DeviceSpec`](./tf/DeviceSpec): Represents a (possibly partial) specification for a TensorFlow device.

[`class Dimension`](./tf/Dimension): Represents the value of one dimension in a TensorShape.

[`class Event`](./tf/Event)

[`class FIFOQueue`](./tf/FIFOQueue): A queue implementation that dequeues elements in first-in first-out order.

[`class FixedLenFeature`](./tf/FixedLenFeature): Configuration for parsing a fixed-length input feature.

[`class FixedLenSequenceFeature`](./tf/FixedLenSequenceFeature): Configuration for parsing a variable-length input feature into a `Tensor`.

[`class FixedLengthRecordReader`](./tf/FixedLengthRecordReader): A Reader that outputs fixed-length records from a file.

[`class GPUOptions`](./tf/GPUOptions)

[`class Graph`](./tf/Graph): A TensorFlow computation, represented as a dataflow graph.

[`class GraphDef`](./tf/GraphDef)

[`class GraphKeys`](./tf/GraphKeys): Standard names to use for graph collections.

[`class GraphOptions`](./tf/GraphOptions)

[`class HistogramProto`](./tf/HistogramProto)

[`class IdentityReader`](./tf/IdentityReader): A Reader that outputs the queued work as both the key and value.

[`class IndexedSlices`](./tf/IndexedSlices): A sparse representation of a set of tensor slices at given indices.

[`class InteractiveSession`](./tf/InteractiveSession): A TensorFlow `Session` for use in interactive contexts, such as a shell.

[`class LogMessage`](./tf/LogMessage)

[`class NameAttrList`](./tf/NameAttrList)

[`class NodeDef`](./tf/NodeDef)

[`class OpError`](./tf/OpError): A generic error that is raised when TensorFlow execution fails.

[`class Operation`](./tf/Operation): Represents a graph node that performs computation on tensors.

[`class OptimizerOptions`](./tf/OptimizerOptions)

[`class PaddingFIFOQueue`](./tf/PaddingFIFOQueue): A FIFOQueue that supports batching variable-sized tensors by padding.

[`class PriorityQueue`](./tf/PriorityQueue): A queue implementation that dequeues elements in prioritized order.

[`class QueueBase`](./tf/QueueBase): Base class for queue implementations.

[`class RandomShuffleQueue`](./tf/RandomShuffleQueue): A queue implementation that dequeues elements in a random order.

[`class ReaderBase`](./tf/ReaderBase): Base class for different Reader types, that produce a record every step.

[`class RegisterGradient`](./tf/RegisterGradient): A decorator for registering the gradient function for an op type.

[`class RunMetadata`](./tf/RunMetadata)

[`class RunOptions`](./tf/RunOptions)

[`class Session`](./tf/Session): A class for running TensorFlow operations.

[`class SessionLog`](./tf/SessionLog)

[`class SparseConditionalAccumulator`](./tf/SparseConditionalAccumulator): A conditional accumulator for aggregating sparse gradients.

[`class SparseFeature`](./tf/SparseFeature): Configuration for parsing a sparse input feature from an `Example`.

[`class SparseTensor`](./tf/SparseTensor): Represents a sparse tensor.

[`class SparseTensorValue`](./tf/SparseTensorValue): SparseTensorValue(indices, values, dense_shape)

[`class Summary`](./tf/Summary)

[`class TFRecordReader`](./tf/TFRecordReader): A Reader that outputs the records from a TFRecords file.

[`class Tensor`](./tf/Tensor): Represents one of the outputs of an `Operation`.

[`class TensorArray`](./tf/TensorArray): Class wrapping dynamic-sized, per-time-step, write-once Tensor arrays.

[`class TensorInfo`](./tf/TensorInfo)

[`class TensorShape`](./tf/TensorShape): Represents the shape of a `Tensor`.

[`class TextLineReader`](./tf/TextLineReader): A Reader that outputs the lines of a file delimited by newlines.

[`class VarLenFeature`](./tf/VarLenFeature): Configuration for parsing a variable-length input feature.

[`class Variable`](./tf/Variable): See the [Variables How To](../../programmers_guide/variables) for a high

[`class VariableScope`](./tf/VariableScope): Variable scope object to carry defaults to provide to `get_variable`.

[`class WholeFileReader`](./tf/WholeFileReader): A Reader that outputs the entire contents of a file as a value.

[`class constant_initializer`](./tf/constant_initializer): Initializer that generates tensors with constant values.

[`class ones_initializer`](./tf/ones_initializer): Initializer that generates tensors initialized to 1.

[`class orthogonal_initializer`](./tf/orthogonal_initializer): Initializer that generates an orthogonal matrix.

[`class random_normal_initializer`](./tf/random_normal_initializer): Initializer that generates tensors with a normal distribution.

[`class random_uniform_initializer`](./tf/random_uniform_initializer): Initializer that generates tensors with a uniform distribution.

[`class truncated_normal_initializer`](./tf/truncated_normal_initializer): Initializer that generates a truncated normal distribution.

[`class uniform_unit_scaling_initializer`](./tf/uniform_unit_scaling_initializer): Initializer that generates tensors without scaling variance.

[`class zeros_initializer`](./tf/zeros_initializer): Initializer that generates tensors initialized to 0.

## Functions

[`Assert(...)`](./tf/Assert): Asserts that the given condition is true.

[`NoGradient(...)`](./tf/NoGradient): Specifies that ops of type `op_type` is not differentiable.

[`NotDifferentiable(...)`](./tf/NoGradient): Specifies that ops of type `op_type` is not differentiable.

[`Print(...)`](./tf/Print): Prints a list of tensors.

[`abs(...)`](./tf/abs): Computes the absolute value of a tensor.

[`accumulate_n(...)`](./tf/accumulate_n): Returns the element-wise sum of a list of tensors.

[`acos(...)`](./tf/acos): Computes acos of x element-wise.

[`add(...)`](./tf/add): Returns x + y element-wise.

[`add_check_numerics_ops(...)`](./tf/add_check_numerics_ops): Connect a `check_numerics` to every floating point tensor.

[`add_n(...)`](./tf/add_n): Adds all input tensors element-wise.

[`add_to_collection(...)`](./tf/add_to_collection): Wrapper for `Graph.add_to_collection()` using the default graph.

[`all_variables(...)`](./tf/all_variables): See `tf.global_variables`. (deprecated)

[`arg_max(...)`](./tf/arg_max): Returns the index with the largest value across dimensions of a tensor.

[`arg_min(...)`](./tf/arg_min): Returns the index with the smallest value across dimensions of a tensor.

[`argmax(...)`](./tf/argmax): Returns the index with the largest value across axes of a tensor.

[`argmin(...)`](./tf/argmin): Returns the index with the smallest value across axes of a tensor.

[`as_dtype(...)`](./tf/as_dtype): Converts the given `type_value` to a `DType`.

[`as_string(...)`](./tf/as_string): Converts each entry in the given tensor to strings.  Supports many numeric

[`asin(...)`](./tf/asin): Computes asin of x element-wise.

[`assert_equal(...)`](./tf/assert_equal): Assert the condition `x == y` holds element-wise.

[`assert_greater(...)`](./tf/assert_greater): Assert the condition `x > y` holds element-wise.

[`assert_greater_equal(...)`](./tf/assert_greater_equal): Assert the condition `x >= y` holds element-wise.

[`assert_integer(...)`](./tf/assert_integer): Assert that `x` is of integer dtype.

[`assert_less(...)`](./tf/assert_less): Assert the condition `x < y` holds element-wise.

[`assert_less_equal(...)`](./tf/assert_less_equal): Assert the condition `x <= y` holds element-wise.

[`assert_negative(...)`](./tf/assert_negative): Assert the condition `x < 0` holds element-wise.

[`assert_non_negative(...)`](./tf/assert_non_negative): Assert the condition `x >= 0` holds element-wise.

[`assert_non_positive(...)`](./tf/assert_non_positive): Assert the condition `x <= 0` holds element-wise.

[`assert_none_equal(...)`](./tf/assert_none_equal): Assert the condition `x != y` holds for all elements.

[`assert_positive(...)`](./tf/assert_positive): Assert the condition `x > 0` holds element-wise.

[`assert_proper_iterable(...)`](./tf/assert_proper_iterable): Static assert that values is a "proper" iterable.

[`assert_rank(...)`](./tf/assert_rank): Assert `x` has rank equal to `rank`.

[`assert_rank_at_least(...)`](./tf/assert_rank_at_least): Assert `x` has rank equal to `rank` or higher.

[`assert_type(...)`](./tf/assert_type): Statically asserts that the given `Tensor` is of the specified type.

[`assert_variables_initialized(...)`](./tf/assert_variables_initialized): Returns an Op to check if variables are initialized.

[`assign(...)`](./tf/assign): Update 'ref' by assigning 'value' to it.

[`assign_add(...)`](./tf/assign_add): Update 'ref' by adding 'value' to it.

[`assign_sub(...)`](./tf/assign_sub): Update 'ref' by subtracting 'value' from it.

[`atan(...)`](./tf/atan): Computes atan of x element-wise.

[`batch_to_space(...)`](./tf/batch_to_space): BatchToSpace for 4-D tensors of type T.

[`batch_to_space_nd(...)`](./tf/batch_to_space_nd): BatchToSpace for N-D tensors of type T.

[`betainc(...)`](./tf/betainc): Compute the regularized incomplete beta integral \\(I_x(a, b)\\).

[`bincount(...)`](./tf/bincount): Counts the number of occurrences of each value in an integer array.

[`bitcast(...)`](./tf/bitcast): Bitcasts a tensor from one type to another without copying data.

[`boolean_mask(...)`](./tf/boolean_mask): Apply boolean mask to tensor.  Numpy equivalent is `tensor[mask]`.

[`broadcast_dynamic_shape(...)`](./tf/broadcast_dynamic_shape): Returns the broadcasted dynamic shape between `shape_x` and `shape_y`.

[`broadcast_static_shape(...)`](./tf/broadcast_static_shape): Returns the broadcasted static shape between `shape_x` and `shape_y`.

[`case(...)`](./tf/case): Create a case operation.

[`cast(...)`](./tf/cast): Casts a tensor to a new type.

[`ceil(...)`](./tf/ceil): Returns element-wise smallest integer in not less than x.

[`check_numerics(...)`](./tf/check_numerics): Checks a tensor for NaN and Inf values.

[`cholesky(...)`](./tf/cholesky): Computes the Cholesky decomposition of one or more square matrices.

[`cholesky_solve(...)`](./tf/cholesky_solve): Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

[`clip_by_average_norm(...)`](./tf/clip_by_average_norm): Clips tensor values to a maximum average L2-norm.

[`clip_by_global_norm(...)`](./tf/clip_by_global_norm): Clips values of multiple tensors by the ratio of the sum of their norms.

[`clip_by_norm(...)`](./tf/clip_by_norm): Clips tensor values to a maximum L2-norm.

[`clip_by_value(...)`](./tf/clip_by_value): Clips tensor values to a specified min and max.

[`complex(...)`](./tf/complex): Converts two real numbers to a complex number.

[`concat(...)`](./tf/concat): Concatenates tensors along one dimension.

[`cond(...)`](./tf/cond): Return either fn1() or fn2() based on the boolean predicate `pred`.

[`confusion_matrix(...)`](./tf/confusion_matrix): Computes the confusion matrix from predictions and labels.

[`conj(...)`](./tf/conj): Returns the complex conjugate of a complex number.

[`constant(...)`](./tf/constant): Creates a constant tensor.

[`container(...)`](./tf/container): Wrapper for `Graph.container()` using the default graph.

[`control_dependencies(...)`](./tf/control_dependencies): Wrapper for `Graph.control_dependencies()` using the default graph.

[`convert_to_tensor(...)`](./tf/convert_to_tensor): Converts the given `value` to a `Tensor`.

[`convert_to_tensor_or_indexed_slices(...)`](./tf/convert_to_tensor_or_indexed_slices): Converts the given object to a `Tensor` or an `IndexedSlices`.

[`convert_to_tensor_or_sparse_tensor(...)`](./tf/convert_to_tensor_or_sparse_tensor): Converts value to a `SparseTensor` or `Tensor`.

[`cos(...)`](./tf/cos): Computes cos of x element-wise.

[`count_nonzero(...)`](./tf/count_nonzero): Computes number of nonzero elements across dimensions of a tensor.

[`count_up_to(...)`](./tf/count_up_to): Increments 'ref' until it reaches 'limit'.

[`create_partitioned_variables(...)`](./tf/create_partitioned_variables): Create a list of partitioned variables according to the given `slicing`.

[`cross(...)`](./tf/cross): Compute the pairwise cross product.

[`cumprod(...)`](./tf/cumprod): Compute the cumulative product of the tensor `x` along `axis`.

[`cumsum(...)`](./tf/cumsum): Compute the cumulative sum of the tensor `x` along `axis`.

[`decode_base64(...)`](./tf/decode_base64): Decode web-safe base64-encoded strings.

[`decode_csv(...)`](./tf/decode_csv): Convert CSV records to tensors. Each column maps to one tensor.

[`decode_json_example(...)`](./tf/decode_json_example): Convert JSON-encoded Example records to binary protocol buffer strings.

[`decode_raw(...)`](./tf/decode_raw): Reinterpret the bytes of a string as a vector of numbers.

[`delete_session_tensor(...)`](./tf/delete_session_tensor): Delete the tensor for the given tensor handle.

[`depth_to_space(...)`](./tf/depth_to_space): DepthToSpace for tensors of type T.

[`dequantize(...)`](./tf/dequantize): Dequantize the 'input' tensor into a float Tensor.

[`deserialize_many_sparse(...)`](./tf/deserialize_many_sparse): Deserialize and concatenate `SparseTensors` from a serialized minibatch.

[`device(...)`](./tf/device): Wrapper for `Graph.device()` using the default graph.

[`diag(...)`](./tf/diag): Returns a diagonal tensor with a given diagonal values.

[`diag_part(...)`](./tf/diag_part): Returns the diagonal part of the tensor.

[`digamma(...)`](./tf/digamma): Computes Psi, the derivative of Lgamma (the log of the absolute value of

[`div(...)`](./tf/div): Divides x / y elementwise (using Python 2 division operator semantics).

[`divide(...)`](./tf/divide): Computes Python style division of `x` by `y`.

[`dynamic_partition(...)`](./tf/dynamic_partition): Partitions `data` into `num_partitions` tensors using indices from `partitions`.

[`dynamic_stitch(...)`](./tf/dynamic_stitch): Interleave the values from the `data` tensors into a single tensor.

[`edit_distance(...)`](./tf/edit_distance): Computes the Levenshtein distance between sequences.

[`einsum(...)`](./tf/einsum): A generalized contraction between tensors of arbitrary dimension.

[`encode_base64(...)`](./tf/encode_base64): Encode strings into web-safe base64 format.

[`equal(...)`](./tf/equal): Returns the truth value of (x == y) element-wise.

[`erf(...)`](./tf/erf): Computes the Gauss error function of `x` element-wise.

[`erfc(...)`](./tf/erfc): Computes the complementary error function of `x` element-wise.

[`exp(...)`](./tf/exp): Computes exponential of x element-wise.  \\(y = e^x\\).

[`expand_dims(...)`](./tf/expand_dims): Inserts a dimension of 1 into a tensor's shape.

[`expm1(...)`](./tf/expm1): Computes exponential of x - 1 element-wise.

[`extract_image_patches(...)`](./tf/extract_image_patches): Extract `patches` from `images` and put them in the "depth" output dimension.

[`eye(...)`](./tf/eye): Construct an identity matrix, or a batch of matrices.

[`fake_quant_with_min_max_args(...)`](./tf/fake_quant_with_min_max_args): Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same type.

[`fake_quant_with_min_max_args_gradient(...)`](./tf/fake_quant_with_min_max_args_gradient): Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`fake_quant_with_min_max_vars(...)`](./tf/fake_quant_with_min_max_vars): Fake-quantize the 'inputs' tensor of type float via global float scalars `min`

[`fake_quant_with_min_max_vars_gradient(...)`](./tf/fake_quant_with_min_max_vars_gradient): Compute gradients for a FakeQuantWithMinMaxVars operation.

[`fake_quant_with_min_max_vars_per_channel(...)`](./tf/fake_quant_with_min_max_vars_per_channel): Fake-quantize the 'inputs' tensor of type float and one of the shapes: `[d]`,

[`fake_quant_with_min_max_vars_per_channel_gradient(...)`](./tf/fake_quant_with_min_max_vars_per_channel_gradient): Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`fft(...)`](./tf/fft): Compute the 1-dimensional discrete Fourier Transform over the inner-most

[`fft2d(...)`](./tf/fft2d): Compute the 2-dimensional discrete Fourier Transform over the inner-most

[`fft3d(...)`](./tf/fft3d): Compute the 3-dimensional discrete Fourier Transform over the inner-most 3

[`fill(...)`](./tf/fill): Creates a tensor filled with a scalar value.

[`fixed_size_partitioner(...)`](./tf/fixed_size_partitioner): Partitioner to specify a fixed number of shards along given axis.

[`floor(...)`](./tf/floor): Returns element-wise largest integer not greater than x.

[`floor_div(...)`](./tf/floor_div): Returns x // y element-wise.

[`floordiv(...)`](./tf/floordiv): Divides `x / y` elementwise, rounding toward the most negative integer.

[`floormod(...)`](./tf/floormod): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`foldl(...)`](./tf/foldl): foldl on the list of tensors unpacked from `elems` on dimension 0.

[`foldr(...)`](./tf/foldr): foldr on the list of tensors unpacked from `elems` on dimension 0.

[`gather(...)`](./tf/gather): Gather slices from `params` according to `indices`.

[`gather_nd(...)`](./tf/gather_nd): Gather values or slices from `params` according to `indices`.

[`get_collection(...)`](./tf/get_collection): Wrapper for `Graph.get_collection()` using the default graph.

[`get_collection_ref(...)`](./tf/get_collection_ref): Wrapper for `Graph.get_collection_ref()` using the default graph.

[`get_default_graph(...)`](./tf/get_default_graph): Returns the default graph for the current thread.

[`get_default_session(...)`](./tf/get_default_session): Returns the default session for the current thread.

[`get_local_variable(...)`](./tf/get_local_variable): Gets an existing *local* variable or creates a new one.

[`get_seed(...)`](./tf/get_seed): Returns the local seeds an operation should use given an op-specific seed.

[`get_session_handle(...)`](./tf/get_session_handle): Return the handle of `data`.

[`get_session_tensor(...)`](./tf/get_session_tensor): Get the tensor of type `dtype` by feeding a tensor handle.

[`get_variable(...)`](./tf/get_variable): Gets an existing variable with these parameters or create a new one.

[`get_variable_scope(...)`](./tf/get_variable_scope): Returns the current variable scope.

[`global_norm(...)`](./tf/global_norm): Computes the global norm of multiple tensors.

[`global_variables(...)`](./tf/global_variables): Returns global variables.

[`global_variables_initializer(...)`](./tf/global_variables_initializer): Returns an Op that initializes global variables.

[`gradients(...)`](./tf/gradients): Constructs symbolic partial derivatives of sum of `ys` w.r.t. x in `xs`.

[`greater(...)`](./tf/greater): Returns the truth value of (x > y) element-wise.

[`greater_equal(...)`](./tf/greater_equal): Returns the truth value of (x >= y) element-wise.

[`group(...)`](./tf/group): Create an op that groups multiple operations.

[`hessians(...)`](./tf/hessians): Constructs the Hessian of sum of `ys` with respect to `x` in `xs`.

[`histogram_fixed_width(...)`](./tf/histogram_fixed_width): Return histogram of values.

[`identity(...)`](./tf/identity): Return a tensor with the same shape and contents as the input tensor or value.

[`ifft(...)`](./tf/ifft): Compute the inverse 1-dimensional discrete Fourier Transform over the inner-most

[`ifft2d(...)`](./tf/ifft2d): Compute the inverse 2-dimensional discrete Fourier Transform over the inner-most

[`ifft3d(...)`](./tf/ifft3d): Compute the inverse 3-dimensional discrete Fourier Transform over the inner-most

[`igamma(...)`](./tf/igamma): Compute the lower regularized incomplete Gamma function `Q(a, x)`.

[`igammac(...)`](./tf/igammac): Compute the upper regularized incomplete Gamma function `Q(a, x)`.

[`imag(...)`](./tf/imag): Returns the imaginary part of a complex number.

[`import_graph_def(...)`](./tf/import_graph_def): Imports the graph from `graph_def` into the current default `Graph`.

[`initialize_all_tables(...)`](./tf/initialize_all_tables): Returns an Op that initializes all tables of the default graph. (deprecated)

[`initialize_all_variables(...)`](./tf/initialize_all_variables): See `tf.global_variables_initializer`. (deprecated)

[`initialize_local_variables(...)`](./tf/initialize_local_variables): See `tf.local_variables_initializer`. (deprecated)

[`initialize_variables(...)`](./tf/initialize_variables): See `tf.variables_initializer`. (deprecated)

[`invert_permutation(...)`](./tf/invert_permutation): Computes the inverse permutation of a tensor.

[`is_finite(...)`](./tf/is_finite): Returns which elements of x are finite.

[`is_inf(...)`](./tf/is_inf): Returns which elements of x are Inf.

[`is_nan(...)`](./tf/is_nan): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](./tf/is_non_decreasing): Returns `True` if `x` is non-decreasing.

[`is_numeric_tensor(...)`](./tf/is_numeric_tensor)

[`is_strictly_increasing(...)`](./tf/is_strictly_increasing): Returns `True` if `x` is strictly increasing.

[`is_variable_initialized(...)`](./tf/is_variable_initialized): Tests if a variable has been initialized.

[`lbeta(...)`](./tf/lbeta): Computes `ln(|Beta(x)|)`, reducing along the last dimension.

[`less(...)`](./tf/less): Returns the truth value of (x < y) element-wise.

[`less_equal(...)`](./tf/less_equal): Returns the truth value of (x <= y) element-wise.

[`lgamma(...)`](./tf/lgamma): Computes the log of the absolute value of `Gamma(x)` element-wise.

[`lin_space(...)`](./tf/lin_space): Generates values in an interval.

[`linspace(...)`](./tf/lin_space): Generates values in an interval.

[`load_file_system_library(...)`](./tf/load_file_system_library): Loads a TensorFlow plugin, containing file system implementation.

[`load_op_library(...)`](./tf/load_op_library): Loads a TensorFlow plugin, containing custom ops and kernels.

[`local_variables(...)`](./tf/local_variables): Returns local variables.

[`local_variables_initializer(...)`](./tf/local_variables_initializer): Returns an Op that initializes all local variables.

[`log(...)`](./tf/log): Computes natural logarithm of x element-wise.

[`log1p(...)`](./tf/log1p): Computes natural logarithm of (1 + x) element-wise.

[`logical_and(...)`](./tf/logical_and): Returns the truth value of x AND y element-wise.

[`logical_not(...)`](./tf/logical_not): Returns the truth value of NOT x element-wise.

[`logical_or(...)`](./tf/logical_or): Returns the truth value of x OR y element-wise.

[`logical_xor(...)`](./tf/logical_xor): x ^ y = (x | y) & ~(x & y).

[`make_template(...)`](./tf/make_template): Given an arbitrary function, wrap it so that it does variable sharing.

[`map_fn(...)`](./tf/map_fn): map on the list of tensors unpacked from `elems` on dimension 0.

[`matching_files(...)`](./tf/matching_files): Returns the set of files matching one or more glob patterns.

[`matmul(...)`](./tf/matmul): Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

[`matrix_band_part(...)`](./tf/matrix_band_part): Copy a tensor setting everything outside a central band in each innermost matrix

[`matrix_determinant(...)`](./tf/matrix_determinant): Computes the determinant of one ore more square matrices.

[`matrix_diag(...)`](./tf/matrix_diag): Returns a batched diagonal tensor with a given batched diagonal values.

[`matrix_diag_part(...)`](./tf/matrix_diag_part): Returns the batched diagonal part of a batched tensor.

[`matrix_inverse(...)`](./tf/matrix_inverse): Computes the inverse of one or more square invertible matrices or their

[`matrix_set_diag(...)`](./tf/matrix_set_diag): Returns a batched matrix tensor with new batched diagonal values.

[`matrix_solve(...)`](./tf/matrix_solve): Solves systems of linear equations.

[`matrix_solve_ls(...)`](./tf/matrix_solve_ls): Solves one or more linear least-squares problems.

[`matrix_transpose(...)`](./tf/matrix_transpose): Transposes last two dimensions of tensor `a`.

[`matrix_triangular_solve(...)`](./tf/matrix_triangular_solve): Solves systems of linear equations with upper or lower triangular matrices by

[`maximum(...)`](./tf/maximum): Returns the max of x and y (i.e. x > y ? x : y) element-wise.

[`meshgrid(...)`](./tf/meshgrid): Broadcasts parameters for evaluation on an N-D grid.

[`min_max_variable_partitioner(...)`](./tf/min_max_variable_partitioner): Partitioner to allocate minimum size per slice.

[`minimum(...)`](./tf/minimum): Returns the min of x and y (i.e. x < y ? x : y) element-wise.

[`mod(...)`](./tf/floormod): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`model_variables(...)`](./tf/model_variables): Returns all variables in the MODEL_VARIABLES collection.

[`moving_average_variables(...)`](./tf/moving_average_variables): Returns all variables that maintain their moving averages.

[`multinomial(...)`](./tf/multinomial): Draws samples from a multinomial distribution.

[`multiply(...)`](./tf/multiply): Returns x * y element-wise.

[`name_scope(...)`](./tf/name_scope): Returns a context manager for use when defining a Python op.

[`negative(...)`](./tf/negative): Computes numerical negative value element-wise.

[`no_op(...)`](./tf/no_op): Does nothing. Only useful as a placeholder for control edges.

[`no_regularizer(...)`](./tf/no_regularizer): Use this function to prevent regularization of variables.

[`norm(...)`](./tf/norm): Computes the norm of vectors, matrices, and tensors.

[`not_equal(...)`](./tf/not_equal): Returns the truth value of (x != y) element-wise.

[`one_hot(...)`](./tf/one_hot): Returns a one-hot tensor.

[`ones(...)`](./tf/ones): Creates a tensor with all elements set to 1.

[`ones_like(...)`](./tf/ones_like): Creates a tensor with all elements set to 1.

[`op_scope(...)`](./tf/op_scope): DEPRECATED. Same as name_scope above, just different argument order.

[`pad(...)`](./tf/pad): Pads a tensor.

[`parallel_stack(...)`](./tf/parallel_stack): Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor in parallel.

[`parse_example(...)`](./tf/parse_example): Parses `Example` protos into a `dict` of tensors.

[`parse_single_example(...)`](./tf/parse_single_example): Parses a single `Example` proto.

[`parse_single_sequence_example(...)`](./tf/parse_single_sequence_example): Parses a single `SequenceExample` proto.

[`parse_tensor(...)`](./tf/parse_tensor): Transforms a serialized tensorflow.TensorProto proto into a Tensor.

[`placeholder(...)`](./tf/placeholder): Inserts a placeholder for a tensor that will be always fed.

[`placeholder_with_default(...)`](./tf/placeholder_with_default): A placeholder op that passes through `input` when its output is not fed.

[`polygamma(...)`](./tf/polygamma): Compute the polygamma function \\(\psi^{(n)} (x)\\).

[`pow(...)`](./tf/pow): Computes the power of one value to another.

[`py_func(...)`](./tf/py_func): Wraps a python function and uses it as a TensorFlow op.

[`qr(...)`](./tf/qr): Computes the QR decompositions of one or more matrices.

[`quantize_v2(...)`](./tf/quantize_v2): Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

[`quantized_concat(...)`](./tf/quantized_concat): Concatenates quantized tensors along one dimension.

[`random_crop(...)`](./tf/random_crop): Randomly crops a tensor to a given size.

[`random_gamma(...)`](./tf/random_gamma): Draws `shape` samples from each of the given Gamma distribution(s).

[`random_normal(...)`](./tf/random_normal): Outputs random values from a normal distribution.

[`random_poisson(...)`](./tf/random_poisson): Draws `shape` samples from each of the given Poisson distribution(s).

[`random_shuffle(...)`](./tf/random_shuffle): Randomly shuffles a tensor along its first dimension.

[`random_uniform(...)`](./tf/random_uniform): Outputs random values from a uniform distribution.

[`range(...)`](./tf/range): Creates a sequence of numbers.

[`rank(...)`](./tf/rank): Returns the rank of a tensor.

[`read_file(...)`](./tf/read_file): Reads and outputs the entire contents of the input filename.

[`real(...)`](./tf/real): Returns the real part of a complex number.

[`realdiv(...)`](./tf/realdiv): Returns x / y element-wise for real types.

[`reciprocal(...)`](./tf/reciprocal): Computes the reciprocal of x element-wise.

[`reduce_all(...)`](./tf/reduce_all): Computes the "logical and" of elements across dimensions of a tensor.

[`reduce_any(...)`](./tf/reduce_any): Computes the "logical or" of elements across dimensions of a tensor.

[`reduce_join(...)`](./tf/reduce_join): Joins a string Tensor across the given dimensions.

[`reduce_logsumexp(...)`](./tf/reduce_logsumexp): Computes log(sum(exp(elements across dimensions of a tensor))).

[`reduce_max(...)`](./tf/reduce_max): Computes the maximum of elements across dimensions of a tensor.

[`reduce_mean(...)`](./tf/reduce_mean): Computes the mean of elements across dimensions of a tensor.

[`reduce_min(...)`](./tf/reduce_min): Computes the minimum of elements across dimensions of a tensor.

[`reduce_prod(...)`](./tf/reduce_prod): Computes the product of elements across dimensions of a tensor.

[`reduce_sum(...)`](./tf/reduce_sum): Computes the sum of elements across dimensions of a tensor.

[`register_tensor_conversion_function(...)`](./tf/register_tensor_conversion_function): Registers a function for converting objects of `base_type` to `Tensor`.

[`report_uninitialized_variables(...)`](./tf/report_uninitialized_variables): Adds ops to list the names of uninitialized variables.

[`required_space_to_batch_paddings(...)`](./tf/required_space_to_batch_paddings): Calculate padding required to make block_shape divide input_shape.

[`reset_default_graph(...)`](./tf/reset_default_graph): Clears the default graph stack and resets the global default graph.

[`reshape(...)`](./tf/reshape): Reshapes a tensor.

[`reverse(...)`](./tf/reverse): Reverses specific dimensions of a tensor.

[`reverse_sequence(...)`](./tf/reverse_sequence): Reverses variable length slices.

[`reverse_v2(...)`](./tf/reverse_v2): Reverses specific dimensions of a tensor.

[`rint(...)`](./tf/rint): Returns element-wise integer closest to x.

[`round(...)`](./tf/round): Rounds the values of a tensor to the nearest integer, element-wise.

[`rsqrt(...)`](./tf/rsqrt): Computes reciprocal of square root of x element-wise.

[`saturate_cast(...)`](./tf/saturate_cast): Performs a safe saturating cast of `value` to `dtype`.

[`scalar_mul(...)`](./tf/scalar_mul): Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

[`scan(...)`](./tf/scan): scan on the list of tensors unpacked from `elems` on dimension 0.

[`scatter_add(...)`](./tf/scatter_add): Adds sparse updates to a variable reference.

[`scatter_div(...)`](./tf/scatter_div): Divides a variable reference by sparse updates.

[`scatter_mul(...)`](./tf/scatter_mul): Multiplies sparse updates into a variable reference.

[`scatter_nd(...)`](./tf/scatter_nd): Creates a new tensor by applying sparse `updates` to individual

[`scatter_nd_add(...)`](./tf/scatter_nd_add): Applies sparse addition between `updates` and individual values or slices

[`scatter_nd_sub(...)`](./tf/scatter_nd_sub): Applies sparse subtraction between `updates` and individual values or slices

[`scatter_nd_update(...)`](./tf/scatter_nd_update): Applies sparse `updates` to individual values or slices within a given

[`scatter_sub(...)`](./tf/scatter_sub): Subtracts sparse updates to a variable reference.

[`scatter_update(...)`](./tf/scatter_update): Applies sparse updates to a variable reference.

[`segment_max(...)`](./tf/segment_max): Computes the maximum along segments of a tensor.

[`segment_mean(...)`](./tf/segment_mean): Computes the mean along segments of a tensor.

[`segment_min(...)`](./tf/segment_min): Computes the minimum along segments of a tensor.

[`segment_prod(...)`](./tf/segment_prod): Computes the product along segments of a tensor.

[`segment_sum(...)`](./tf/segment_sum): Computes the sum along segments of a tensor.

[`self_adjoint_eig(...)`](./tf/self_adjoint_eig): Computes the eigen decomposition of a batch of self-adjoint matrices.

[`self_adjoint_eigvals(...)`](./tf/self_adjoint_eigvals): Computes the eigenvalues of one or more self-adjoint matrices.

[`sequence_mask(...)`](./tf/sequence_mask): Return a mask tensor representing the first N positions of each row.

[`serialize_many_sparse(...)`](./tf/serialize_many_sparse): Serialize an `N`-minibatch `SparseTensor` into an `[N, 3]` string `Tensor`.

[`serialize_sparse(...)`](./tf/serialize_sparse): Serialize a `SparseTensor` into a string 3-vector (1-D `Tensor`) object.

[`set_random_seed(...)`](./tf/set_random_seed): Sets the graph-level random seed.

[`setdiff1d(...)`](./tf/setdiff1d): Computes the difference between two lists of numbers or strings.

[`shape(...)`](./tf/shape): Returns the shape of a tensor.

[`shape_n(...)`](./tf/shape_n): Returns shape of tensors.

[`sigmoid(...)`](./tf/sigmoid): Computes sigmoid of `x` element-wise.

[`sign(...)`](./tf/sign): Returns an element-wise indication of the sign of a number.

[`sin(...)`](./tf/sin): Computes sin of x element-wise.

[`size(...)`](./tf/size): Returns the size of a tensor.

[`slice(...)`](./tf/slice): Extracts a slice from a tensor.

[`space_to_batch(...)`](./tf/space_to_batch): SpaceToBatch for 4-D tensors of type T.

[`space_to_batch_nd(...)`](./tf/space_to_batch_nd): SpaceToBatch for N-D tensors of type T.

[`space_to_depth(...)`](./tf/space_to_depth): SpaceToDepth for tensors of type T.

[`sparse_add(...)`](./tf/sparse_add): Adds two tensors, at least one of each is a `SparseTensor`.

[`sparse_concat(...)`](./tf/sparse_concat): Concatenates a list of `SparseTensor` along the specified dimension.

[`sparse_fill_empty_rows(...)`](./tf/sparse_fill_empty_rows): Fills empty rows in the input 2-D `SparseTensor` with a default value.

[`sparse_mask(...)`](./tf/sparse_mask): Masks elements of `IndexedSlices`.

[`sparse_matmul(...)`](./tf/sparse_matmul): Multiply matrix "a" by matrix "b".

[`sparse_maximum(...)`](./tf/sparse_maximum): Returns the element-wise max of two SparseTensors.

[`sparse_merge(...)`](./tf/sparse_merge): Combines a batch of feature ids and values into a single `SparseTensor`.

[`sparse_minimum(...)`](./tf/sparse_minimum): Returns the element-wise min of two SparseTensors.

[`sparse_placeholder(...)`](./tf/sparse_placeholder): Inserts a placeholder for a sparse tensor that will be always fed.

[`sparse_reduce_sum(...)`](./tf/sparse_reduce_sum): Computes the sum of elements across dimensions of a SparseTensor.

[`sparse_reduce_sum_sparse(...)`](./tf/sparse_reduce_sum_sparse): Computes the sum of elements across dimensions of a SparseTensor.

[`sparse_reorder(...)`](./tf/sparse_reorder): Reorders a `SparseTensor` into the canonical, row-major ordering.

[`sparse_reset_shape(...)`](./tf/sparse_reset_shape): Resets the shape of a `SparseTensor` with indices and values unchanged.

[`sparse_reshape(...)`](./tf/sparse_reshape): Reshapes a `SparseTensor` to represent values in a new dense shape.

[`sparse_retain(...)`](./tf/sparse_retain): Retains specified non-empty values within a `SparseTensor`.

[`sparse_segment_mean(...)`](./tf/sparse_segment_mean): Computes the mean along sparse segments of a tensor.

[`sparse_segment_sqrt_n(...)`](./tf/sparse_segment_sqrt_n): Computes the sum along sparse segments of a tensor divided by the sqrt of N.

[`sparse_segment_sum(...)`](./tf/sparse_segment_sum): Computes the sum along sparse segments of a tensor.

[`sparse_softmax(...)`](./tf/sparse_softmax): Applies softmax to a batched N-D `SparseTensor`.

[`sparse_split(...)`](./tf/sparse_split): Split a `SparseTensor` into `num_split` tensors along `axis`.

[`sparse_tensor_dense_matmul(...)`](./tf/sparse_tensor_dense_matmul): Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

[`sparse_tensor_to_dense(...)`](./tf/sparse_tensor_to_dense): Converts a `SparseTensor` into a dense tensor.

[`sparse_to_dense(...)`](./tf/sparse_to_dense): Converts a sparse representation into a dense tensor.

[`sparse_to_indicator(...)`](./tf/sparse_to_indicator): Converts a `SparseTensor` of ids into a dense bool indicator tensor.

[`sparse_transpose(...)`](./tf/sparse_transpose): Transposes a `SparseTensor`

[`split(...)`](./tf/split): Splits a tensor into sub tensors.

[`sqrt(...)`](./tf/sqrt): Computes square root of x element-wise.

[`square(...)`](./tf/square): Computes square of x element-wise.

[`squared_difference(...)`](./tf/squared_difference): Returns (x - y)(x - y) element-wise.

[`squeeze(...)`](./tf/squeeze): Removes dimensions of size 1 from the shape of a tensor.

[`stack(...)`](./tf/stack): Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor.

[`stop_gradient(...)`](./tf/stop_gradient): Stops gradient computation.

[`strided_slice(...)`](./tf/strided_slice): Extracts a strided slice from a tensor.

[`string_join(...)`](./tf/string_join): Joins the strings in the given list of string tensors into one tensor;

[`string_split(...)`](./tf/string_split): Split elements of `source` based on `delimiter` into a `SparseTensor`.

[`string_to_hash_bucket(...)`](./tf/string_to_hash_bucket): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_hash_bucket_fast(...)`](./tf/string_to_hash_bucket_fast): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_hash_bucket_strong(...)`](./tf/string_to_hash_bucket_strong): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_number(...)`](./tf/string_to_number): Converts each string in the input Tensor to the specified numeric type.

[`substr(...)`](./tf/substr): Return substrings from `Tensor` of strings.

[`subtract(...)`](./tf/subtract): Returns x - y element-wise.

[`svd(...)`](./tf/svd): Computes the singular value decompositions of one or more matrices.

[`tables_initializer(...)`](./tf/tables_initializer): Returns an Op that initializes all tables of the default graph.

[`tan(...)`](./tf/tan): Computes tan of x element-wise.

[`tanh(...)`](./tf/tanh): Computes hyperbolic tangent of `x` element-wise.

[`tensordot(...)`](./tf/tensordot): Tensor contraction of a and b along specified axes.

[`tile(...)`](./tf/tile): Constructs a tensor by tiling a given tensor.

[`to_bfloat16(...)`](./tf/to_bfloat16): Casts a tensor to type `bfloat16`.

[`to_double(...)`](./tf/to_double): Casts a tensor to type `float64`.

[`to_float(...)`](./tf/to_float): Casts a tensor to type `float32`.

[`to_int32(...)`](./tf/to_int32): Casts a tensor to type `int32`.

[`to_int64(...)`](./tf/to_int64): Casts a tensor to type `int64`.

[`trace(...)`](./tf/trace): Compute the trace of a tensor `x`.

[`trainable_variables(...)`](./tf/trainable_variables): Returns all variables created with `trainable=True`.

[`transpose(...)`](./tf/transpose): Transposes `a`. Permutes the dimensions according to `perm`.

[`truediv(...)`](./tf/truediv): Divides x / y elementwise (using Python 3 division operator semantics).

[`truncated_normal(...)`](./tf/truncated_normal): Outputs random values from a truncated normal distribution.

[`truncatediv(...)`](./tf/truncatediv): Returns x / y element-wise for integer types.

[`truncatemod(...)`](./tf/truncatemod): Returns element-wise remainder of division. This emulates C semantics where

[`tuple(...)`](./tf/tuple): Group tensors together.

[`unique(...)`](./tf/unique): Finds unique elements in a 1-D tensor.

[`unique_with_counts(...)`](./tf/unique_with_counts): Finds unique elements in a 1-D tensor.

[`unsorted_segment_max(...)`](./tf/unsorted_segment_max): Computes the Max along segments of a tensor.

[`unsorted_segment_sum(...)`](./tf/unsorted_segment_sum): Computes the sum along segments of a tensor.

[`unstack(...)`](./tf/unstack): Unpacks the given dimension of a rank-`R` tensor into rank-`(R-1)` tensors.

[`variable_axis_size_partitioner(...)`](./tf/variable_axis_size_partitioner): Get a partitioner for VariableScope to keep shards below `max_shard_bytes`.

[`variable_op_scope(...)`](./tf/variable_op_scope): Deprecated: context manager for defining an op that creates variables.

[`variable_scope(...)`](./tf/variable_scope): Returns a context manager for defining ops that creates variables (layers).

[`variables_initializer(...)`](./tf/variables_initializer): Returns an Op that initializes a list of variables.

[`verify_tensor_all_finite(...)`](./tf/verify_tensor_all_finite): Assert that the tensor does not contain any NaN's or Inf's.

[`where(...)`](./tf/where): Return the elements, either from `x` or `y`, depending on the `condition`.

[`while_loop(...)`](./tf/while_loop): Repeat `body` while the condition `cond` is true.

[`write_file(...)`](./tf/write_file): Writes contents to the file at input filename. Creates file if not existing.

[`zeros(...)`](./tf/zeros): Creates a tensor with all elements set to zero.

[`zeros_like(...)`](./tf/zeros_like): Creates a tensor with all elements set to zero.

[`zeta(...)`](./tf/zeta): Compute the Hurwitz zeta function \\(\zeta(x, q)\\).

## Other Members

`COMPILER_VERSION`

`GIT_VERSION`

`GRAPH_DEF_VERSION`

`GRAPH_DEF_VERSION_MIN_CONSUMER`

`GRAPH_DEF_VERSION_MIN_PRODUCER`

`QUANTIZED_DTYPES`

`VERSION`

`__compiler_version__`

`__git_version__`

`__version__`

`bfloat16`

`bool`

`complex128`

`complex64`

`double`

`float16`

`float32`

`float64`

`half`

`int16`

`int32`

`int64`

`int8`

`newaxis`

`qint16`

`qint32`

`qint8`

`quint16`

`quint8`

`resource`

`string`

`uint16`

`uint8`

