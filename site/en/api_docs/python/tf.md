page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf



Defined in [`tensorflow/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/__init__.py).

Bring in all of the public TensorFlow interface into this module.

## Modules

[`app`](./tf/app) module: Generic entry point script.

[`bitwise`](./tf/bitwise) module: Operations for manipulating the binary representations of integers.

[`compat`](./tf/compat) module: Functions for Python 2 vs. 3 compatibility.

[`contrib`](./tf/contrib) module: contrib module containing volatile or experimental code.

[`data`](./tf/data) module: <a href="./tf/data/Dataset"><code>tf.data.Dataset</code></a> API for input pipelines.

[`debugging`](./tf/debugging) module: Public API for tf.debugging namespace.

[`distributions`](./tf/distributions) module: Core module for TensorFlow distribution objects and helpers.

[`dtypes`](./tf/dtypes) module: Public API for tf.dtypes namespace.

[`errors`](./tf/errors) module: Exception types for TensorFlow errors.

[`estimator`](./tf/estimator) module: Estimator: High level tools for working with models.

[`feature_column`](./tf/feature_column) module: Public API for tf.feature_column namespace.

[`flags`](./tf/app/flags) module: Import router for absl.flags. See https://github.com/abseil/abseil-py.

[`gfile`](./tf/gfile) module: Import router for file_io.

[`graph_util`](./tf/graph_util) module: Helpers to manipulate a tensor graph in python.

[`image`](./tf/image) module: Image processing and decoding ops.

[`initializers`](./tf/initializers) module: Public API for tf.initializers namespace.

[`io`](./tf/io) module: Public API for tf.io namespace.

[`keras`](./tf/keras) module: Implementation of the Keras API meant to be a high-level API for TensorFlow.

[`layers`](./tf/layers) module: Public API for tf.layers namespace.

[`linalg`](./tf/linalg) module: Operations for linear algebra.

[`logging`](./tf/logging) module: Logging and Summary Operations.

[`losses`](./tf/losses) module: Loss operations for use in neural networks.

[`manip`](./tf/manip) module: Operators for manipulating tensors.

[`math`](./tf/math) module: Basic arithmetic operators.

[`metrics`](./tf/metrics) module: Evaluation-related metrics.

[`nn`](./tf/nn) module: Wrappers for primitive Neural Net (NN) Operations.

[`profiler`](./tf/profiler) module: Public API for tf.profiler namespace.

[`python_io`](./tf/python_io) module: Python functions for directly manipulating TFRecord-formatted files.

[`pywrap_tensorflow`](./tf/pywrap_tensorflow) module: A wrapper for TensorFlow SWIG-generated bindings.

[`quantization`](./tf/quantization) module: Public API for tf.quantization namespace.

[`resource_loader`](./tf/resource_loader) module: Resource management library.

[`saved_model`](./tf/saved_model) module: Public API for tf.saved_model namespace.

[`sets`](./tf/sets) module: Tensorflow set operations.

[`sparse`](./tf/sparse) module: Sparse Tensor Representation.

[`spectral`](./tf/spectral) module: Spectral operators (e.g. DCT, FFT, RFFT).

[`strings`](./tf/strings) module: Operations for working with string Tensors.

[`summary`](./tf/summary) module: Public API for tf.summary namespace.

[`sysconfig`](./tf/sysconfig) module: System configuration library.

[`test`](./tf/test) module: Testing.

[`tools`](./tf/tools) module

[`train`](./tf/train) module: Support for training models.

[`user_ops`](./tf/user_ops) module: Public API for tf.user_ops namespace.

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

[`class GradientTape`](./tf/GradientTape): Record operations for automatic differentiation.

[`class Graph`](./tf/Graph): A TensorFlow computation, represented as a dataflow graph.

[`class GraphDef`](./tf/GraphDef)

[`class GraphKeys`](./tf/GraphKeys): Standard names to use for graph collections.

[`class GraphOptions`](./tf/GraphOptions)

[`class HistogramProto`](./tf/HistogramProto)

[`class IdentityReader`](./tf/IdentityReader): A Reader that outputs the queued work as both the key and value.

[`class IndexedSlices`](./tf/IndexedSlices): A sparse representation of a set of tensor slices at given indices.

[`class InteractiveSession`](./tf/InteractiveSession): A TensorFlow `Session` for use in interactive contexts, such as a shell.

[`class LMDBReader`](./tf/LMDBReader): A Reader that outputs the records from a LMDB file.

[`class LogMessage`](./tf/LogMessage)

[`class MetaGraphDef`](./tf/MetaGraphDef)

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

[`class SummaryMetadata`](./tf/SummaryMetadata)

[`class TFRecordReader`](./tf/TFRecordReader): A Reader that outputs the records from a TFRecords file.

[`class Tensor`](./tf/Tensor): Represents one of the outputs of an `Operation`.

[`class TensorArray`](./tf/TensorArray): Class wrapping dynamic-sized, per-time-step, write-once Tensor arrays.

[`class TensorInfo`](./tf/TensorInfo)

[`class TensorShape`](./tf/TensorShape): Represents the shape of a `Tensor`.

[`class TextLineReader`](./tf/TextLineReader): A Reader that outputs the lines of a file delimited by newlines.

[`class VarLenFeature`](./tf/VarLenFeature): Configuration for parsing a variable-length input feature.

[`class Variable`](./tf/Variable): See the [Variables Guide](https://tensorflow.org/guide/variables).

[`class VariableAggregation`](./tf/VariableAggregation): Indicates how a distributed variable will be aggregated.

[`class VariableScope`](./tf/VariableScope): Variable scope object to carry defaults to provide to `get_variable`.

[`class VariableSynchronization`](./tf/VariableSynchronization): Indicates when a distributed variable will be synced.

[`class WholeFileReader`](./tf/WholeFileReader): A Reader that outputs the entire contents of a file as a value.

[`class constant_initializer`](./tf/keras/initializers/Constant): Initializer that generates tensors with constant values.

[`class name_scope`](./tf/name_scope): A context manager for use when defining a Python op.

[`class ones_initializer`](./tf/keras/initializers/Ones): Initializer that generates tensors initialized to 1.

[`class orthogonal_initializer`](./tf/keras/initializers/Orthogonal): Initializer that generates an orthogonal matrix.

[`class random_normal_initializer`](./tf/initializers/random_normal): Initializer that generates tensors with a normal distribution.

[`class random_uniform_initializer`](./tf/initializers/random_uniform): Initializer that generates tensors with a uniform distribution.

[`class truncated_normal_initializer`](./tf/initializers/truncated_normal): Initializer that generates a truncated normal distribution.

[`class uniform_unit_scaling_initializer`](./tf/initializers/uniform_unit_scaling): Initializer that generates tensors without scaling variance.

[`class variable_scope`](./tf/variable_scope): A context manager for defining ops that creates variables (layers).

[`class variance_scaling_initializer`](./tf/keras/initializers/VarianceScaling): Initializer capable of adapting its scale to the shape of weights tensors.

[`class zeros_initializer`](./tf/keras/initializers/Zeros): Initializer that generates tensors initialized to 0.

## Functions

[`Assert(...)`](./tf/Assert): Asserts that the given condition is true.

[`NoGradient(...)`](./tf/NoGradient): Specifies that ops of type `op_type` is not differentiable.

[`NotDifferentiable(...)`](./tf/NoGradient): Specifies that ops of type `op_type` is not differentiable.

[`Print(...)`](./tf/Print): Prints a list of tensors.

[`abs(...)`](./tf/abs): Computes the absolute value of a tensor.

[`accumulate_n(...)`](./tf/accumulate_n): Returns the element-wise sum of a list of tensors.

[`acos(...)`](./tf/math/acos): Computes acos of x element-wise.

[`acosh(...)`](./tf/math/acosh): Computes inverse hyperbolic cosine of x element-wise.

[`add(...)`](./tf/math/add): Returns x + y element-wise.

[`add_check_numerics_ops(...)`](./tf/add_check_numerics_ops): Connect a `check_numerics` to every floating point tensor.

[`add_n(...)`](./tf/add_n): Adds all input tensors element-wise.

[`add_to_collection(...)`](./tf/add_to_collection): Wrapper for `Graph.add_to_collection()` using the default graph.

[`add_to_collections(...)`](./tf/add_to_collections): Wrapper for `Graph.add_to_collections()` using the default graph.

[`all_variables(...)`](./tf/all_variables): See <a href="./tf/global_variables"><code>tf.global_variables</code></a>. (deprecated)

[`angle(...)`](./tf/angle): Returns the element-wise argument of a complex (or real) tensor.

[`arg_max(...)`](./tf/arg_max): Returns the index with the largest value across dimensions of a tensor. (deprecated)

[`arg_min(...)`](./tf/arg_min): Returns the index with the smallest value across dimensions of a tensor. (deprecated)

[`argmax(...)`](./tf/argmax): Returns the index with the largest value across axes of a tensor. (deprecated arguments)

[`argmin(...)`](./tf/argmin): Returns the index with the smallest value across axes of a tensor. (deprecated arguments)

[`as_dtype(...)`](./tf/as_dtype): Converts the given `type_value` to a `DType`.

[`as_string(...)`](./tf/dtypes/as_string): Converts each entry in the given tensor to strings.  Supports many numeric

[`asin(...)`](./tf/math/asin): Computes asin of x element-wise.

[`asinh(...)`](./tf/math/asinh): Computes inverse hyperbolic sine of x element-wise.

[`assert_equal(...)`](./tf/assert_equal): Assert the condition `x == y` holds element-wise.

[`assert_greater(...)`](./tf/assert_greater): Assert the condition `x > y` holds element-wise.

[`assert_greater_equal(...)`](./tf/assert_greater_equal): Assert the condition `x >= y` holds element-wise.

[`assert_integer(...)`](./tf/assert_integer): Assert that `x` is of integer dtype.

[`assert_less(...)`](./tf/assert_less): Assert the condition `x < y` holds element-wise.

[`assert_less_equal(...)`](./tf/assert_less_equal): Assert the condition `x <= y` holds element-wise.

[`assert_near(...)`](./tf/assert_near): Assert the condition `x` and `y` are close element-wise.

[`assert_negative(...)`](./tf/assert_negative): Assert the condition `x < 0` holds element-wise.

[`assert_non_negative(...)`](./tf/assert_non_negative): Assert the condition `x >= 0` holds element-wise.

[`assert_non_positive(...)`](./tf/assert_non_positive): Assert the condition `x <= 0` holds element-wise.

[`assert_none_equal(...)`](./tf/assert_none_equal): Assert the condition `x != y` holds for all elements.

[`assert_positive(...)`](./tf/assert_positive): Assert the condition `x > 0` holds element-wise.

[`assert_proper_iterable(...)`](./tf/assert_proper_iterable): Static assert that values is a "proper" iterable.

[`assert_rank(...)`](./tf/assert_rank): Assert `x` has rank equal to `rank`.

[`assert_rank_at_least(...)`](./tf/assert_rank_at_least): Assert `x` has rank equal to `rank` or higher.

[`assert_rank_in(...)`](./tf/assert_rank_in): Assert `x` has rank in `ranks`.

[`assert_same_float_dtype(...)`](./tf/assert_same_float_dtype): Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](./tf/assert_scalar)

[`assert_type(...)`](./tf/assert_type): Statically asserts that the given `Tensor` is of the specified type.

[`assert_variables_initialized(...)`](./tf/assert_variables_initialized): Returns an Op to check if variables are initialized.

[`assign(...)`](./tf/assign): Update 'ref' by assigning 'value' to it.

[`assign_add(...)`](./tf/assign_add): Update 'ref' by adding 'value' to it.

[`assign_sub(...)`](./tf/assign_sub): Update 'ref' by subtracting 'value' from it.

[`atan(...)`](./tf/math/atan): Computes atan of x element-wise.

[`atan2(...)`](./tf/math/atan2): Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

[`atanh(...)`](./tf/math/atanh): Computes inverse hyperbolic tangent of x element-wise.

[`batch_gather(...)`](./tf/batch_gather): Gather slices from `params` according to `indices` with leading batch dims.

[`batch_scatter_update(...)`](./tf/batch_scatter_update): Generalization of <a href="./tf/scatter_update"><code>tf.scatter_update</code></a> to axis different than 0.

[`batch_to_space(...)`](./tf/batch_to_space): BatchToSpace for 4-D tensors of type T.

[`batch_to_space_nd(...)`](./tf/manip/batch_to_space_nd): BatchToSpace for N-D tensors of type T.

[`betainc(...)`](./tf/math/betainc): Compute the regularized incomplete beta integral \\(I_x(a, b)\\).

[`bincount(...)`](./tf/bincount): Counts the number of occurrences of each value in an integer array.

[`bitcast(...)`](./tf/bitcast): Bitcasts a tensor from one type to another without copying data.

[`boolean_mask(...)`](./tf/boolean_mask): Apply boolean mask to tensor.  Numpy equivalent is `tensor[mask]`.

[`broadcast_dynamic_shape(...)`](./tf/broadcast_dynamic_shape): Returns the broadcasted dynamic shape between `shape_x` and `shape_y`.

[`broadcast_static_shape(...)`](./tf/broadcast_static_shape): Returns the broadcasted static shape between `shape_x` and `shape_y`.

[`broadcast_to(...)`](./tf/broadcast_to): Broadcast an array for a compatible shape.

[`case(...)`](./tf/case): Create a case operation.

[`cast(...)`](./tf/cast): Casts a tensor to a new type.

[`ceil(...)`](./tf/math/ceil): Returns element-wise smallest integer not less than x.

[`check_numerics(...)`](./tf/debugging/check_numerics): Checks a tensor for NaN and Inf values.

[`cholesky(...)`](./tf/linalg/cholesky): Computes the Cholesky decomposition of one or more square matrices.

[`cholesky_solve(...)`](./tf/cholesky_solve): Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

[`clip_by_average_norm(...)`](./tf/clip_by_average_norm): Clips tensor values to a maximum average L2-norm.

[`clip_by_global_norm(...)`](./tf/clip_by_global_norm): Clips values of multiple tensors by the ratio of the sum of their norms.

[`clip_by_norm(...)`](./tf/clip_by_norm): Clips tensor values to a maximum L2-norm.

[`clip_by_value(...)`](./tf/clip_by_value): Clips tensor values to a specified min and max.

[`colocate_with(...)`](./tf/colocate_with)

[`complex(...)`](./tf/complex): Converts two real numbers to a complex number.

[`concat(...)`](./tf/concat): Concatenates tensors along one dimension.

[`cond(...)`](./tf/cond): Return `true_fn()` if the predicate `pred` is true else `false_fn()`. (deprecated arguments)

[`confusion_matrix(...)`](./tf/confusion_matrix): Computes the confusion matrix from predictions and labels.

[`conj(...)`](./tf/conj): Returns the complex conjugate of a complex number.

[`constant(...)`](./tf/constant): Creates a constant tensor.

[`container(...)`](./tf/container): Wrapper for `Graph.container()` using the default graph.

[`control_dependencies(...)`](./tf/control_dependencies): Wrapper for `Graph.control_dependencies()` using the default graph.

[`convert_to_tensor(...)`](./tf/convert_to_tensor): Converts the given `value` to a `Tensor`.

[`convert_to_tensor_or_indexed_slices(...)`](./tf/convert_to_tensor_or_indexed_slices): Converts the given object to a `Tensor` or an `IndexedSlices`.

[`convert_to_tensor_or_sparse_tensor(...)`](./tf/convert_to_tensor_or_sparse_tensor): Converts value to a `SparseTensor` or `Tensor`.

[`cos(...)`](./tf/math/cos): Computes cos of x element-wise.

[`cosh(...)`](./tf/math/cosh): Computes hyperbolic cosine of x element-wise.

[`count_nonzero(...)`](./tf/count_nonzero): Computes number of nonzero elements across dimensions of a tensor. (deprecated arguments)

[`count_up_to(...)`](./tf/count_up_to): Increments 'ref' until it reaches 'limit'.

[`create_partitioned_variables(...)`](./tf/create_partitioned_variables): Create a list of partitioned variables according to the given `slicing`.

[`cross(...)`](./tf/linalg/cross): Compute the pairwise cross product.

[`cumprod(...)`](./tf/cumprod): Compute the cumulative product of the tensor `x` along `axis`.

[`cumsum(...)`](./tf/cumsum): Compute the cumulative sum of the tensor `x` along `axis`.

[`custom_gradient(...)`](./tf/custom_gradient): Decorator to define a function with a custom gradient.

[`decode_base64(...)`](./tf/io/decode_base64): Decode web-safe base64-encoded strings.

[`decode_compressed(...)`](./tf/io/decode_compressed): Decompress strings.

[`decode_csv(...)`](./tf/decode_csv): Convert CSV records to tensors. Each column maps to one tensor.

[`decode_json_example(...)`](./tf/io/decode_json_example): Convert JSON-encoded Example records to binary protocol buffer strings.

[`decode_raw(...)`](./tf/io/decode_raw): Reinterpret the bytes of a string as a vector of numbers.

[`delete_session_tensor(...)`](./tf/delete_session_tensor): Delete the tensor for the given tensor handle.

[`depth_to_space(...)`](./tf/depth_to_space): DepthToSpace for tensors of type T.

[`dequantize(...)`](./tf/quantization/dequantize): Dequantize the 'input' tensor into a float Tensor.

[`deserialize_many_sparse(...)`](./tf/deserialize_many_sparse): Deserialize and concatenate `SparseTensors` from a serialized minibatch.

[`device(...)`](./tf/device): Wrapper for `Graph.device()` using the default graph.

[`diag(...)`](./tf/linalg/tensor_diag): Returns a diagonal tensor with a given diagonal values.

[`diag_part(...)`](./tf/linalg/tensor_diag_part): Returns the diagonal part of the tensor.

[`digamma(...)`](./tf/math/digamma): Computes Psi, the derivative of Lgamma (the log of the absolute value of

[`disable_resource_variables(...)`](./tf/disable_resource_variables): Opts out of resource variables. (deprecated)

[`div(...)`](./tf/div): Divides x / y elementwise (using Python 2 division operator semantics).

[`div_no_nan(...)`](./tf/div_no_nan): Computes an unsafe divide which returns 0 if the y is zero.

[`divide(...)`](./tf/divide): Computes Python style division of `x` by `y`.

[`dynamic_partition(...)`](./tf/dynamic_partition): Partitions `data` into `num_partitions` tensors using indices from `partitions`.

[`dynamic_stitch(...)`](./tf/dynamic_stitch): Interleave the values from the `data` tensors into a single tensor.

[`edit_distance(...)`](./tf/edit_distance): Computes the Levenshtein distance between sequences.

[`einsum(...)`](./tf/einsum): A generalized contraction between tensors of arbitrary dimension.

[`enable_eager_execution(...)`](./tf/enable_eager_execution): Enables eager execution for the lifetime of this program.

[`enable_resource_variables(...)`](./tf/enable_resource_variables): Creates resource variables by default.

[`encode_base64(...)`](./tf/io/encode_base64): Encode strings into web-safe base64 format.

[`ensure_shape(...)`](./tf/ensure_shape): Updates the shape of a tensor and checks at runtime that the shape holds.

[`equal(...)`](./tf/math/equal): Returns the truth value of (x == y) element-wise.

[`erf(...)`](./tf/erf): Computes the Gauss error function of `x` element-wise.

[`erfc(...)`](./tf/math/erfc): Computes the complementary error function of `x` element-wise.

[`executing_eagerly(...)`](./tf/executing_eagerly): Returns True if the current thread has eager execution enabled.

[`exp(...)`](./tf/math/exp): Computes exponential of x element-wise.  \\(y = e^x\\).

[`expand_dims(...)`](./tf/expand_dims): Inserts a dimension of 1 into a tensor's shape. (deprecated arguments)

[`expm1(...)`](./tf/math/expm1): Computes exponential of x - 1 element-wise.

[`extract_image_patches(...)`](./tf/image/extract_image_patches): Extract `patches` from `images` and put them in the "depth" output dimension.

[`eye(...)`](./tf/eye): Construct an identity matrix, or a batch of matrices.

[`fake_quant_with_min_max_args(...)`](./tf/quantization/fake_quant_with_min_max_args): Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same type.

[`fake_quant_with_min_max_args_gradient(...)`](./tf/quantization/fake_quant_with_min_max_args_gradient): Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`fake_quant_with_min_max_vars(...)`](./tf/quantization/fake_quant_with_min_max_vars): Fake-quantize the 'inputs' tensor of type float via global float scalars `min`

[`fake_quant_with_min_max_vars_gradient(...)`](./tf/quantization/fake_quant_with_min_max_vars_gradient): Compute gradients for a FakeQuantWithMinMaxVars operation.

[`fake_quant_with_min_max_vars_per_channel(...)`](./tf/quantization/fake_quant_with_min_max_vars_per_channel): Fake-quantize the 'inputs' tensor of type float and one of the shapes: `[d]`,

[`fake_quant_with_min_max_vars_per_channel_gradient(...)`](./tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient): Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`fft(...)`](./tf/spectral/fft): Fast Fourier transform.

[`fft2d(...)`](./tf/spectral/fft2d): 2D fast Fourier transform.

[`fft3d(...)`](./tf/spectral/fft3d): 3D fast Fourier transform.

[`fill(...)`](./tf/fill): Creates a tensor filled with a scalar value.

[`fixed_size_partitioner(...)`](./tf/fixed_size_partitioner): Partitioner to specify a fixed number of shards along given axis.

[`floor(...)`](./tf/math/floor): Returns element-wise largest integer not greater than x.

[`floor_div(...)`](./tf/floor_div): Returns x // y element-wise.

[`floordiv(...)`](./tf/floordiv): Divides `x / y` elementwise, rounding toward the most negative integer.

[`floormod(...)`](./tf/floormod): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`foldl(...)`](./tf/foldl): foldl on the list of tensors unpacked from `elems` on dimension 0.

[`foldr(...)`](./tf/foldr): foldr on the list of tensors unpacked from `elems` on dimension 0.

[`gather(...)`](./tf/gather): Gather slices from `params` axis `axis` according to `indices`.

[`gather_nd(...)`](./tf/manip/gather_nd): Gather slices from `params` into a Tensor with shape specified by `indices`.

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

[`global_variables_initializer(...)`](./tf/initializers/global_variables): Returns an Op that initializes global variables.

[`glorot_normal_initializer(...)`](./tf/glorot_normal_initializer): The Glorot normal initializer, also called Xavier normal initializer.

[`glorot_uniform_initializer(...)`](./tf/glorot_uniform_initializer): The Glorot uniform initializer, also called Xavier uniform initializer.

[`gradients(...)`](./tf/gradients): Constructs symbolic derivatives of sum of `ys` w.r.t. x in `xs`.

[`greater(...)`](./tf/math/greater): Returns the truth value of (x > y) element-wise.

[`greater_equal(...)`](./tf/math/greater_equal): Returns the truth value of (x >= y) element-wise.

[`group(...)`](./tf/group): Create an op that groups multiple operations.

[`guarantee_const(...)`](./tf/guarantee_const): Gives a guarantee to the TF runtime that the input tensor is a constant.

[`hessians(...)`](./tf/hessians): Constructs the Hessian of sum of `ys` with respect to `x` in `xs`.

[`histogram_fixed_width(...)`](./tf/histogram_fixed_width): Return histogram of values.

[`histogram_fixed_width_bins(...)`](./tf/histogram_fixed_width_bins): Bins the given values for use in a histogram.

[`identity(...)`](./tf/identity): Return a tensor with the same shape and contents as input.

[`identity_n(...)`](./tf/identity_n): Returns a list of tensors with the same shapes and contents as the input

[`ifft(...)`](./tf/spectral/ifft): Inverse fast Fourier transform.

[`ifft2d(...)`](./tf/spectral/ifft2d): Inverse 2D fast Fourier transform.

[`ifft3d(...)`](./tf/spectral/ifft3d): Inverse 3D fast Fourier transform.

[`igamma(...)`](./tf/math/igamma): Compute the lower regularized incomplete Gamma function `P(a, x)`.

[`igammac(...)`](./tf/math/igammac): Compute the upper regularized incomplete Gamma function `Q(a, x)`.

[`imag(...)`](./tf/imag): Returns the imaginary part of a complex (or real) tensor.

[`import_graph_def(...)`](./tf/import_graph_def): Imports the graph from `graph_def` into the current default `Graph`. (deprecated arguments)

[`init_scope(...)`](./tf/init_scope): A context manager that lifts ops out of control-flow scopes and function-building graphs.

[`initialize_all_tables(...)`](./tf/initialize_all_tables): Returns an Op that initializes all tables of the default graph. (deprecated)

[`initialize_all_variables(...)`](./tf/initialize_all_variables): See <a href="./tf/initializers/global_variables"><code>tf.global_variables_initializer</code></a>. (deprecated)

[`initialize_local_variables(...)`](./tf/initialize_local_variables): See <a href="./tf/initializers/local_variables"><code>tf.local_variables_initializer</code></a>. (deprecated)

[`initialize_variables(...)`](./tf/initialize_variables): See <a href="./tf/initializers/variables"><code>tf.variables_initializer</code></a>. (deprecated)

[`invert_permutation(...)`](./tf/math/invert_permutation): Computes the inverse permutation of a tensor.

[`is_finite(...)`](./tf/debugging/is_finite): Returns which elements of x are finite.

[`is_inf(...)`](./tf/debugging/is_inf): Returns which elements of x are Inf.

[`is_nan(...)`](./tf/debugging/is_nan): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](./tf/is_non_decreasing): Returns `True` if `x` is non-decreasing.

[`is_numeric_tensor(...)`](./tf/is_numeric_tensor)

[`is_strictly_increasing(...)`](./tf/is_strictly_increasing): Returns `True` if `x` is strictly increasing.

[`is_variable_initialized(...)`](./tf/is_variable_initialized): Tests if a variable has been initialized.

[`lbeta(...)`](./tf/lbeta): Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

[`less(...)`](./tf/math/less): Returns the truth value of (x < y) element-wise.

[`less_equal(...)`](./tf/math/less_equal): Returns the truth value of (x <= y) element-wise.

[`lgamma(...)`](./tf/math/lgamma): Computes the log of the absolute value of `Gamma(x)` element-wise.

[`lin_space(...)`](./tf/lin_space): Generates values in an interval.

[`linspace(...)`](./tf/lin_space): Generates values in an interval.

[`load_file_system_library(...)`](./tf/load_file_system_library): Loads a TensorFlow plugin, containing file system implementation.

[`load_op_library(...)`](./tf/load_op_library): Loads a TensorFlow plugin, containing custom ops and kernels.

[`local_variables(...)`](./tf/local_variables): Returns local variables.

[`local_variables_initializer(...)`](./tf/initializers/local_variables): Returns an Op that initializes all local variables.

[`log(...)`](./tf/math/log): Computes natural logarithm of x element-wise.

[`log1p(...)`](./tf/math/log1p): Computes natural logarithm of (1 + x) element-wise.

[`log_sigmoid(...)`](./tf/log_sigmoid): Computes log sigmoid of `x` element-wise.

[`logical_and(...)`](./tf/math/logical_and): Returns the truth value of x AND y element-wise.

[`logical_not(...)`](./tf/math/logical_not): Returns the truth value of NOT x element-wise.

[`logical_or(...)`](./tf/math/logical_or): Returns the truth value of x OR y element-wise.

[`logical_xor(...)`](./tf/logical_xor): x ^ y = (x | y) & ~(x & y).

[`make_ndarray(...)`](./tf/make_ndarray): Create a numpy ndarray from a tensor.

[`make_template(...)`](./tf/make_template): Given an arbitrary function, wrap it so that it does variable sharing.

[`make_tensor_proto(...)`](./tf/make_tensor_proto): Create a TensorProto.

[`map_fn(...)`](./tf/map_fn): map on the list of tensors unpacked from `elems` on dimension 0.

[`matching_files(...)`](./tf/io/matching_files): Returns the set of files matching one or more glob patterns.

[`matmul(...)`](./tf/matmul): Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

[`matrix_band_part(...)`](./tf/linalg/band_part): Copy a tensor setting everything outside a central band in each innermost matrix

[`matrix_determinant(...)`](./tf/linalg/det): Computes the determinant of one or more square matrices.

[`matrix_diag(...)`](./tf/linalg/diag): Returns a batched diagonal tensor with a given batched diagonal values.

[`matrix_diag_part(...)`](./tf/linalg/diag_part): Returns the batched diagonal part of a batched tensor.

[`matrix_inverse(...)`](./tf/linalg/inv): Computes the inverse of one or more square invertible matrices or their

[`matrix_set_diag(...)`](./tf/linalg/set_diag): Returns a batched matrix tensor with new batched diagonal values.

[`matrix_solve(...)`](./tf/linalg/solve): Solves systems of linear equations.

[`matrix_solve_ls(...)`](./tf/matrix_solve_ls): Solves one or more linear least-squares problems.

[`matrix_transpose(...)`](./tf/matrix_transpose): Transposes last two dimensions of tensor `a`.

[`matrix_triangular_solve(...)`](./tf/linalg/triangular_solve): Solves systems of linear equations with upper or lower triangular matrices by

[`maximum(...)`](./tf/math/maximum): Returns the max of x and y (i.e. x > y ? x : y) element-wise.

[`meshgrid(...)`](./tf/meshgrid): Broadcasts parameters for evaluation on an N-D grid.

[`min_max_variable_partitioner(...)`](./tf/min_max_variable_partitioner): Partitioner to allocate minimum size per slice.

[`minimum(...)`](./tf/math/minimum): Returns the min of x and y (i.e. x < y ? x : y) element-wise.

[`mod(...)`](./tf/floormod): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`model_variables(...)`](./tf/model_variables): Returns all variables in the MODEL_VARIABLES collection.

[`moving_average_variables(...)`](./tf/moving_average_variables): Returns all variables that maintain their moving averages.

[`multinomial(...)`](./tf/multinomial): Draws samples from a multinomial distribution.

[`multiply(...)`](./tf/multiply): Returns x * y element-wise.

[`negative(...)`](./tf/negative): Computes numerical negative value element-wise.

[`no_op(...)`](./tf/no_op): Does nothing. Only useful as a placeholder for control edges.

[`no_regularizer(...)`](./tf/no_regularizer): Use this function to prevent regularization of variables.

[`norm(...)`](./tf/norm): Computes the norm of vectors, matrices, and tensors. (deprecated arguments)

[`not_equal(...)`](./tf/math/not_equal): Returns the truth value of (x != y) element-wise.

[`one_hot(...)`](./tf/one_hot): Returns a one-hot tensor.

[`ones(...)`](./tf/ones): Creates a tensor with all elements set to 1.

[`ones_like(...)`](./tf/ones_like): Creates a tensor with all elements set to 1.

[`op_scope(...)`](./tf/op_scope): DEPRECATED. Same as name_scope above, just different argument order.

[`pad(...)`](./tf/pad): Pads a tensor.

[`parallel_stack(...)`](./tf/parallel_stack): Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor in parallel.

[`parse_example(...)`](./tf/parse_example): Parses `Example` protos into a `dict` of tensors.

[`parse_single_example(...)`](./tf/parse_single_example): Parses a single `Example` proto.

[`parse_single_sequence_example(...)`](./tf/parse_single_sequence_example): Parses a single `SequenceExample` proto.

[`parse_tensor(...)`](./tf/io/parse_tensor): Transforms a serialized tensorflow.TensorProto proto into a Tensor.

[`placeholder(...)`](./tf/placeholder): Inserts a placeholder for a tensor that will be always fed.

[`placeholder_with_default(...)`](./tf/placeholder_with_default): A placeholder op that passes through `input` when its output is not fed.

[`polygamma(...)`](./tf/math/polygamma): Compute the polygamma function \\(\psi^{(n)} (x)\\).

[`pow(...)`](./tf/pow): Computes the power of one value to another.

[`py_func(...)`](./tf/py_func): Wraps a python function and uses it as a TensorFlow op.

[`qr(...)`](./tf/linalg/qr): Computes the QR decompositions of one or more matrices.

[`quantize(...)`](./tf/quantize): Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

[`quantize_v2(...)`](./tf/quantize_v2): Please use <a href="./tf/quantize"><code>tf.quantize</code></a> instead.

[`quantized_concat(...)`](./tf/quantization/quantized_concat): Concatenates quantized tensors along one dimension.

[`random_crop(...)`](./tf/random_crop): Randomly crops a tensor to a given size.

[`random_gamma(...)`](./tf/random_gamma): Draws `shape` samples from each of the given Gamma distribution(s).

[`random_normal(...)`](./tf/random_normal): Outputs random values from a normal distribution.

[`random_poisson(...)`](./tf/random_poisson): Draws `shape` samples from each of the given Poisson distribution(s).

[`random_shuffle(...)`](./tf/random_shuffle): Randomly shuffles a tensor along its first dimension.

[`random_uniform(...)`](./tf/random_uniform): Outputs random values from a uniform distribution.

[`range(...)`](./tf/range): Creates a sequence of numbers.

[`rank(...)`](./tf/rank): Returns the rank of a tensor.

[`read_file(...)`](./tf/io/read_file): Reads and outputs the entire contents of the input filename.

[`real(...)`](./tf/real): Returns the real part of a complex (or real) tensor.

[`realdiv(...)`](./tf/realdiv): Returns x / y element-wise for real types.

[`reciprocal(...)`](./tf/math/reciprocal): Computes the reciprocal of x element-wise.

[`reduce_all(...)`](./tf/reduce_all): Computes the "logical and" of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_any(...)`](./tf/reduce_any): Computes the "logical or" of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_join(...)`](./tf/reduce_join): Joins a string Tensor across the given dimensions.

[`reduce_logsumexp(...)`](./tf/reduce_logsumexp): Computes log(sum(exp(elements across dimensions of a tensor))). (deprecated arguments)

[`reduce_max(...)`](./tf/reduce_max): Computes the maximum of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_mean(...)`](./tf/reduce_mean): Computes the mean of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_min(...)`](./tf/reduce_min): Computes the minimum of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_prod(...)`](./tf/reduce_prod): Computes the product of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_sum(...)`](./tf/reduce_sum): Computes the sum of elements across dimensions of a tensor. (deprecated arguments)

[`regex_replace(...)`](./tf/strings/regex_replace): Replaces the match of pattern in input with rewrite.

[`register_tensor_conversion_function(...)`](./tf/register_tensor_conversion_function): Registers a function for converting objects of `base_type` to `Tensor`.

[`report_uninitialized_variables(...)`](./tf/report_uninitialized_variables): Adds ops to list the names of uninitialized variables.

[`required_space_to_batch_paddings(...)`](./tf/required_space_to_batch_paddings): Calculate padding required to make block_shape divide input_shape.

[`reset_default_graph(...)`](./tf/reset_default_graph): Clears the default graph stack and resets the global default graph.

[`reshape(...)`](./tf/manip/reshape): Reshapes a tensor.

[`reverse(...)`](./tf/manip/reverse): Reverses specific dimensions of a tensor.

[`reverse_sequence(...)`](./tf/reverse_sequence): Reverses variable length slices.

[`reverse_v2(...)`](./tf/manip/reverse): Reverses specific dimensions of a tensor.

[`rint(...)`](./tf/math/rint): Returns element-wise integer closest to x.

[`round(...)`](./tf/round): Rounds the values of a tensor to the nearest integer, element-wise.

[`rsqrt(...)`](./tf/math/rsqrt): Computes reciprocal of square root of x element-wise.

[`saturate_cast(...)`](./tf/saturate_cast): Performs a safe saturating cast of `value` to `dtype`.

[`scalar_mul(...)`](./tf/scalar_mul): Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

[`scan(...)`](./tf/scan): scan on the list of tensors unpacked from `elems` on dimension 0.

[`scatter_add(...)`](./tf/scatter_add): Adds sparse updates to the variable referenced by `resource`.

[`scatter_div(...)`](./tf/scatter_div): Divides a variable reference by sparse updates.

[`scatter_max(...)`](./tf/scatter_max): Reduces sparse updates into a variable reference using the `max` operation.

[`scatter_min(...)`](./tf/scatter_min): Reduces sparse updates into a variable reference using the `min` operation.

[`scatter_mul(...)`](./tf/scatter_mul): Multiplies sparse updates into a variable reference.

[`scatter_nd(...)`](./tf/manip/scatter_nd): Scatter `updates` into a new tensor according to `indices`.

[`scatter_nd_add(...)`](./tf/scatter_nd_add): Applies sparse addition to individual values or slices in a Variable.

[`scatter_nd_sub(...)`](./tf/scatter_nd_sub): Applies sparse subtraction to individual values or slices in a Variable.

[`scatter_nd_update(...)`](./tf/scatter_nd_update): Applies sparse `updates` to individual values or slices in a Variable.

[`scatter_sub(...)`](./tf/scatter_sub): Subtracts sparse updates to a variable reference.

[`scatter_update(...)`](./tf/scatter_update): Applies sparse updates to a variable reference.

[`segment_max(...)`](./tf/math/segment_max): Computes the maximum along segments of a tensor.

[`segment_mean(...)`](./tf/math/segment_mean): Computes the mean along segments of a tensor.

[`segment_min(...)`](./tf/math/segment_min): Computes the minimum along segments of a tensor.

[`segment_prod(...)`](./tf/math/segment_prod): Computes the product along segments of a tensor.

[`segment_sum(...)`](./tf/math/segment_sum): Computes the sum along segments of a tensor.

[`self_adjoint_eig(...)`](./tf/self_adjoint_eig): Computes the eigen decomposition of a batch of self-adjoint matrices.

[`self_adjoint_eigvals(...)`](./tf/self_adjoint_eigvals): Computes the eigenvalues of one or more self-adjoint matrices.

[`sequence_mask(...)`](./tf/sequence_mask): Returns a mask tensor representing the first N positions of each cell.

[`serialize_many_sparse(...)`](./tf/serialize_many_sparse): Serialize `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor`.

[`serialize_sparse(...)`](./tf/serialize_sparse): Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

[`serialize_tensor(...)`](./tf/serialize_tensor): Transforms a Tensor into a serialized TensorProto proto.

[`set_random_seed(...)`](./tf/set_random_seed): Sets the graph-level random seed.

[`setdiff1d(...)`](./tf/setdiff1d): Computes the difference between two lists of numbers or strings.

[`shape(...)`](./tf/shape): Returns the shape of a tensor.

[`shape_n(...)`](./tf/shape_n): Returns shape of tensors.

[`sigmoid(...)`](./tf/nn/sigmoid): Computes sigmoid of `x` element-wise.

[`sign(...)`](./tf/sign): Returns an element-wise indication of the sign of a number.

[`sin(...)`](./tf/math/sin): Computes sin of x element-wise.

[`sinh(...)`](./tf/math/sinh): Computes hyperbolic sine of x element-wise.

[`size(...)`](./tf/size): Returns the size of a tensor.

[`slice(...)`](./tf/slice): Extracts a slice from a tensor.

[`space_to_batch(...)`](./tf/space_to_batch): SpaceToBatch for 4-D tensors of type T.

[`space_to_batch_nd(...)`](./tf/manip/space_to_batch_nd): SpaceToBatch for N-D tensors of type T.

[`space_to_depth(...)`](./tf/space_to_depth): SpaceToDepth for tensors of type T.

[`sparse_add(...)`](./tf/sparse_add): Adds two tensors, at least one of each is a `SparseTensor`.

[`sparse_concat(...)`](./tf/sparse_concat): Concatenates a list of `SparseTensor` along the specified dimension. (deprecated arguments)

[`sparse_fill_empty_rows(...)`](./tf/sparse_fill_empty_rows): Fills empty rows in the input 2-D `SparseTensor` with a default value.

[`sparse_mask(...)`](./tf/sparse_mask): Masks elements of `IndexedSlices`.

[`sparse_matmul(...)`](./tf/sparse_matmul): Multiply matrix "a" by matrix "b".

[`sparse_maximum(...)`](./tf/sparse_maximum): Returns the element-wise max of two SparseTensors.

[`sparse_merge(...)`](./tf/sparse_merge): Combines a batch of feature ids and values into a single `SparseTensor`.

[`sparse_minimum(...)`](./tf/sparse_minimum): Returns the element-wise min of two SparseTensors.

[`sparse_placeholder(...)`](./tf/sparse_placeholder): Inserts a placeholder for a sparse tensor that will be always fed.

[`sparse_reduce_max(...)`](./tf/sparse_reduce_max): Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

[`sparse_reduce_max_sparse(...)`](./tf/sparse_reduce_max_sparse): Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

[`sparse_reduce_sum(...)`](./tf/sparse_reduce_sum): Computes the sum of elements across dimensions of a SparseTensor. (deprecated arguments)

[`sparse_reduce_sum_sparse(...)`](./tf/sparse_reduce_sum_sparse): Computes the sum of elements across dimensions of a SparseTensor. (deprecated arguments)

[`sparse_reorder(...)`](./tf/sparse_reorder): Reorders a `SparseTensor` into the canonical, row-major ordering.

[`sparse_reset_shape(...)`](./tf/sparse_reset_shape): Resets the shape of a `SparseTensor` with indices and values unchanged.

[`sparse_reshape(...)`](./tf/sparse_reshape): Reshapes a `SparseTensor` to represent values in a new dense shape.

[`sparse_retain(...)`](./tf/sparse_retain): Retains specified non-empty values within a `SparseTensor`.

[`sparse_segment_mean(...)`](./tf/sparse_segment_mean): Computes the mean along sparse segments of a tensor.

[`sparse_segment_sqrt_n(...)`](./tf/sparse_segment_sqrt_n): Computes the sum along sparse segments of a tensor divided by the sqrt(N).

[`sparse_segment_sum(...)`](./tf/sparse_segment_sum): Computes the sum along sparse segments of a tensor.

[`sparse_slice(...)`](./tf/sparse_slice): Slice a `SparseTensor` based on the `start` and `size.

[`sparse_softmax(...)`](./tf/sparse_softmax): Applies softmax to a batched N-D `SparseTensor`.

[`sparse_split(...)`](./tf/sparse_split): Split a `SparseTensor` into `num_split` tensors along `axis`. (deprecated arguments)

[`sparse_tensor_dense_matmul(...)`](./tf/sparse_tensor_dense_matmul): Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

[`sparse_tensor_to_dense(...)`](./tf/sparse_tensor_to_dense): Converts a `SparseTensor` into a dense tensor.

[`sparse_to_dense(...)`](./tf/sparse_to_dense): Converts a sparse representation into a dense tensor.

[`sparse_to_indicator(...)`](./tf/sparse_to_indicator): Converts a `SparseTensor` of ids into a dense bool indicator tensor.

[`sparse_transpose(...)`](./tf/sparse_transpose): Transposes a `SparseTensor`

[`split(...)`](./tf/split): Splits a tensor into sub tensors.

[`sqrt(...)`](./tf/sqrt): Computes square root of x element-wise.

[`square(...)`](./tf/square): Computes square of x element-wise.

[`squared_difference(...)`](./tf/math/squared_difference): Returns (x - y)(x - y) element-wise.

[`squeeze(...)`](./tf/squeeze): Removes dimensions of size 1 from the shape of a tensor. (deprecated arguments)

[`stack(...)`](./tf/stack): Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor.

[`stop_gradient(...)`](./tf/stop_gradient): Stops gradient computation.

[`strided_slice(...)`](./tf/strided_slice): Extracts a strided slice of a tensor (generalized python array indexing).

[`string_join(...)`](./tf/strings/join): Joins the strings in the given list of string tensors into one tensor;

[`string_split(...)`](./tf/string_split): Split elements of `source` based on `delimiter` into a `SparseTensor`.

[`string_strip(...)`](./tf/strings/strip): Strip leading and trailing whitespaces from the Tensor.

[`string_to_hash_bucket(...)`](./tf/strings/to_hash_bucket): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_hash_bucket_fast(...)`](./tf/strings/to_hash_bucket_fast): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_hash_bucket_strong(...)`](./tf/strings/to_hash_bucket_strong): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_number(...)`](./tf/strings/to_number): Converts each string in the input Tensor to the specified numeric type.

[`substr(...)`](./tf/strings/substr): Return substrings from `Tensor` of strings.

[`subtract(...)`](./tf/subtract): Returns x - y element-wise.

[`svd(...)`](./tf/svd): Computes the singular value decompositions of one or more matrices.

[`tables_initializer(...)`](./tf/tables_initializer): Returns an Op that initializes all tables of the default graph.

[`tan(...)`](./tf/math/tan): Computes tan of x element-wise.

[`tanh(...)`](./tf/nn/tanh): Computes hyperbolic tangent of `x` element-wise.

[`tensordot(...)`](./tf/tensordot): Tensor contraction of a and b along specified axes.

[`tile(...)`](./tf/manip/tile): Constructs a tensor by tiling a given tensor.

[`timestamp(...)`](./tf/timestamp): Provides the time since epoch in seconds.

[`to_bfloat16(...)`](./tf/to_bfloat16): Casts a tensor to type `bfloat16`.

[`to_complex128(...)`](./tf/to_complex128): Casts a tensor to type `complex128`.

[`to_complex64(...)`](./tf/to_complex64): Casts a tensor to type `complex64`.

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

[`truncatemod(...)`](./tf/truncatemod): Returns element-wise remainder of division. This emulates C semantics in that

[`tuple(...)`](./tf/tuple): Group tensors together.

[`unique(...)`](./tf/unique): Finds unique elements in a 1-D tensor.

[`unique_with_counts(...)`](./tf/unique_with_counts): Finds unique elements in a 1-D tensor.

[`unravel_index(...)`](./tf/unravel_index): Converts a flat index or array of flat indices into a tuple of

[`unsorted_segment_max(...)`](./tf/math/unsorted_segment_max): Computes the maximum along segments of a tensor.

[`unsorted_segment_mean(...)`](./tf/unsorted_segment_mean): Computes the mean along segments of a tensor.

[`unsorted_segment_min(...)`](./tf/math/unsorted_segment_min): Computes the minimum along segments of a tensor.

[`unsorted_segment_prod(...)`](./tf/math/unsorted_segment_prod): Computes the product along segments of a tensor.

[`unsorted_segment_sqrt_n(...)`](./tf/unsorted_segment_sqrt_n): Computes the sum along segments of a tensor divided by the sqrt(N).

[`unsorted_segment_sum(...)`](./tf/math/unsorted_segment_sum): Computes the sum along segments of a tensor.

[`unstack(...)`](./tf/unstack): Unpacks the given dimension of a rank-`R` tensor into rank-`(R-1)` tensors.

[`variable_axis_size_partitioner(...)`](./tf/variable_axis_size_partitioner): Get a partitioner for VariableScope to keep shards below `max_shard_bytes`.

[`variable_op_scope(...)`](./tf/variable_op_scope): Deprecated: context manager for defining an op that creates variables.

[`variables_initializer(...)`](./tf/initializers/variables): Returns an Op that initializes a list of variables.

[`verify_tensor_all_finite(...)`](./tf/verify_tensor_all_finite): Assert that the tensor does not contain any NaN's or Inf's.

[`where(...)`](./tf/where): Return the elements, either from `x` or `y`, depending on the `condition`.

[`while_loop(...)`](./tf/while_loop): Repeat `body` while the condition `cond` is true.

[`write_file(...)`](./tf/io/write_file): Writes contents to the file at input filename. Creates file and recursively

[`zeros(...)`](./tf/zeros): Creates a tensor with all elements set to zero.

[`zeros_like(...)`](./tf/zeros_like): Creates a tensor with all elements set to zero.

[`zeta(...)`](./tf/math/zeta): Compute the Hurwitz zeta function \\(\zeta(x, q)\\).

## Other Members

`AUTO_REUSE`

`COMPILER_VERSION`

`CXX11_ABI_FLAG`

`GIT_VERSION`

`GRAPH_DEF_VERSION`

`GRAPH_DEF_VERSION_MIN_CONSUMER`

`GRAPH_DEF_VERSION_MIN_PRODUCER`

`MONOLITHIC_BUILD`

`QUANTIZED_DTYPES`

`VERSION`

`__all__`

`__compiler_version__`

`__cxx11_abi_flag__`

`__git_version__`

`__monolithic_build__`

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

`uint32`

`uint64`

`uint8`

`variant`

