page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



TensorFlow root package

<!-- Placeholder for "Used in" -->


## Modules

[`app`](./tf/app) module: Generic entry point script.

[`audio`](./tf/audio) module: Public API for tf.audio namespace.

[`autograph`](./tf/autograph) module: Conversion of plain Python into TensorFlow graph code.

[`bitwise`](./tf/bitwise) module: Operations for manipulating the binary representations of integers.

[`compat`](./tf/compat) module: Functions for Python 2 vs. 3 compatibility.

[`config`](./tf/config) module: Public API for tf.config namespace.

[`contrib`](./tf/contrib) module: Contrib module containing volatile or experimental code.

[`data`](./tf/data) module: <a href="./tf/data/Dataset"><code>tf.data.Dataset</code></a> API for input pipelines.

[`debugging`](./tf/debugging) module: Public API for tf.debugging namespace.

[`distribute`](./tf/distribute) module: Library for running a computation across multiple devices.

[`distributions`](./tf/distributions) module: Core module for TensorFlow distribution objects and helpers.

[`dtypes`](./tf/dtypes) module: Public API for tf.dtypes namespace.

[`errors`](./tf/errors) module: Exception types for TensorFlow errors.

[`estimator`](./tf/estimator) module: Estimator: High level tools for working with models.

[`experimental`](./tf/experimental) module: Public API for tf.experimental namespace.

[`feature_column`](./tf/feature_column) module: Public API for tf.feature_column namespace.

[`gfile`](./tf/gfile) module: Import router for file_io.

[`graph_util`](./tf/graph_util) module: Helpers to manipulate a tensor graph in python.

[`image`](./tf/image) module: Image processing and decoding ops.

[`initializers`](./tf/initializers) module: Public API for tf.initializers namespace.

[`io`](./tf/io) module: Public API for tf.io namespace.

[`keras`](./tf/keras) module: Implementation of the Keras API meant to be a high-level API for TensorFlow.

[`layers`](./tf/layers) module: Public API for tf.layers namespace.

[`linalg`](./tf/linalg) module: Operations for linear algebra.

[`lite`](./tf/lite) module: Public API for tf.lite namespace.

[`logging`](./tf/logging) module: Logging and Summary Operations.

[`lookup`](./tf/lookup) module: Public API for tf.lookup namespace.

[`losses`](./tf/losses) module: Loss operations for use in neural networks.

[`manip`](./tf/manip) module: Operators for manipulating tensors.

[`math`](./tf/math) module: Math Operations.

[`metrics`](./tf/metrics) module: Evaluation-related metrics.

[`nest`](./tf/nest) module: Public API for tf.nest namespace.

[`nn`](./tf/nn) module: Wrappers for primitive Neural Net (NN) Operations.

[`profiler`](./tf/profiler) module: Public API for tf.profiler namespace.

[`python_io`](./tf/python_io) module: Python functions for directly manipulating TFRecord-formatted files.

[`quantization`](./tf/quantization) module: Public API for tf.quantization namespace.

[`queue`](./tf/queue) module: Public API for tf.queue namespace.

[`ragged`](./tf/ragged) module: Ragged Tensors.

[`random`](./tf/random) module: Public API for tf.random namespace.

[`raw_ops`](./tf/raw_ops) module: Note: <a href="./tf/raw_ops"><code>tf.raw_ops</code></a> provides direct/low level access to all TensorFlow ops. See   [the RFC](https://github.com/tensorflow/community/blob/master/rfcs/20181225-tf-raw-ops.md)

[`resource_loader`](./tf/resource_loader) module: Resource management library.

[`saved_model`](./tf/saved_model) module: Public API for tf.saved_model namespace.

[`sets`](./tf/sets) module: Tensorflow set operations.

[`signal`](./tf/signal) module: Signal processing operations.

[`sparse`](./tf/sparse) module: Sparse Tensor Representation.

[`spectral`](./tf/spectral) module: Public API for tf.spectral namespace.

[`strings`](./tf/strings) module: Operations for working with string Tensors.

[`summary`](./tf/summary) module: Operations for writing summary data, for use in analysis and visualization.

[`sysconfig`](./tf/sysconfig) module: System configuration library.

[`test`](./tf/test) module: Testing.

[`tpu`](./tf/tpu) module: Ops related to Tensor Processing Units.

[`train`](./tf/train) module: Support for training models.

[`user_ops`](./tf/user_ops) module: Public API for tf.user_ops namespace.

[`version`](./tf/version) module: Public API for tf.version namespace.

[`xla`](./tf/xla) module: Public API for tf.xla namespace.

## Classes

[`class AggregationMethod`](./tf/AggregationMethod): A class listing aggregation methods used to combine gradients.

[`class AttrValue`](./tf/AttrValue): A ProtocolMessage

[`class ConditionalAccumulator`](./tf/ConditionalAccumulator): A conditional accumulator for aggregating gradients.

[`class ConditionalAccumulatorBase`](./tf/ConditionalAccumulatorBase): A conditional accumulator for aggregating gradients.

[`class ConfigProto`](./tf/ConfigProto): A ProtocolMessage

[`class CriticalSection`](./tf/CriticalSection): Critical section.

[`class DType`](./tf/dtypes/DType): Represents the type of the elements in a `Tensor`.

[`class DeviceSpec`](./tf/DeviceSpec): Represents a (possibly partial) specification for a TensorFlow device.

[`class Dimension`](./tf/Dimension): Represents the value of one dimension in a TensorShape.

[`class Event`](./tf/Event): A ProtocolMessage

[`class FIFOQueue`](./tf/queue/FIFOQueue): A queue implementation that dequeues elements in first-in first-out order.

[`class FixedLenFeature`](./tf/io/FixedLenFeature): Configuration for parsing a fixed-length input feature.

[`class FixedLenSequenceFeature`](./tf/io/FixedLenSequenceFeature): Configuration for parsing a variable-length input feature into a `Tensor`.

[`class FixedLengthRecordReader`](./tf/FixedLengthRecordReader): A Reader that outputs fixed-length records from a file.

[`class GPUOptions`](./tf/GPUOptions): A ProtocolMessage

[`class GradientTape`](./tf/GradientTape): Record operations for automatic differentiation.

[`class Graph`](./tf/Graph): A TensorFlow computation, represented as a dataflow graph.

[`class GraphDef`](./tf/GraphDef): A ProtocolMessage

[`class GraphKeys`](./tf/GraphKeys): Standard names to use for graph collections.

[`class GraphOptions`](./tf/GraphOptions): A ProtocolMessage

[`class HistogramProto`](./tf/HistogramProto): A ProtocolMessage

[`class IdentityReader`](./tf/IdentityReader): A Reader that outputs the queued work as both the key and value.

[`class IndexedSlices`](./tf/IndexedSlices): A sparse representation of a set of tensor slices at given indices.

[`class IndexedSlicesSpec`](./tf/IndexedSlicesSpec): Type specification for a <a href="./tf/IndexedSlices"><code>tf.IndexedSlices</code></a>.

[`class InteractiveSession`](./tf/InteractiveSession): A TensorFlow `Session` for use in interactive contexts, such as a shell.

[`class LMDBReader`](./tf/LMDBReader): A Reader that outputs the records from a LMDB file.

[`class LogMessage`](./tf/LogMessage): A ProtocolMessage

[`class MetaGraphDef`](./tf/MetaGraphDef): A ProtocolMessage

[`class Module`](./tf/Module): Base neural network module class.

[`class NameAttrList`](./tf/NameAttrList): A ProtocolMessage

[`class NodeDef`](./tf/NodeDef): A ProtocolMessage

[`class OpError`](./tf/errors/OpError): A generic error that is raised when TensorFlow execution fails.

[`class Operation`](./tf/Operation): Represents a graph node that performs computation on tensors.

[`class OptimizerOptions`](./tf/OptimizerOptions): A ProtocolMessage

[`class OptionalSpec`](./tf/OptionalSpec): Represents an optional potentially containing a structured value.

[`class PaddingFIFOQueue`](./tf/queue/PaddingFIFOQueue): A FIFOQueue that supports batching variable-sized tensors by padding.

[`class PriorityQueue`](./tf/queue/PriorityQueue): A queue implementation that dequeues elements in prioritized order.

[`class QueueBase`](./tf/queue/QueueBase): Base class for queue implementations.

[`class RaggedTensor`](./tf/RaggedTensor): Represents a ragged tensor.

[`class RaggedTensorSpec`](./tf/RaggedTensorSpec): Type specification for a <a href="./tf/RaggedTensor"><code>tf.RaggedTensor</code></a>.

[`class RandomShuffleQueue`](./tf/queue/RandomShuffleQueue): A queue implementation that dequeues elements in a random order.

[`class ReaderBase`](./tf/ReaderBase): Base class for different Reader types, that produce a record every step.

[`class RegisterGradient`](./tf/RegisterGradient): A decorator for registering the gradient function for an op type.

[`class RunMetadata`](./tf/RunMetadata): A ProtocolMessage

[`class RunOptions`](./tf/RunOptions): A ProtocolMessage

[`class Session`](./tf/Session): A class for running TensorFlow operations.

[`class SessionLog`](./tf/SessionLog): A ProtocolMessage

[`class SparseConditionalAccumulator`](./tf/sparse/SparseConditionalAccumulator): A conditional accumulator for aggregating sparse gradients.

[`class SparseFeature`](./tf/io/SparseFeature): Configuration for parsing a sparse input feature from an `Example`.

[`class SparseTensor`](./tf/sparse/SparseTensor): Represents a sparse tensor.

[`class SparseTensorSpec`](./tf/SparseTensorSpec): Type specification for a <a href="./tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a>.

[`class SparseTensorValue`](./tf/SparseTensorValue): SparseTensorValue(indices, values, dense_shape)

[`class Summary`](./tf/Summary): A ProtocolMessage

[`class SummaryMetadata`](./tf/SummaryMetadata): A ProtocolMessage

[`class TFRecordReader`](./tf/TFRecordReader): A Reader that outputs the records from a TFRecords file.

[`class Tensor`](./tf/Tensor): Represents one of the outputs of an `Operation`.

[`class TensorArray`](./tf/TensorArray): Class wrapping dynamic-sized, per-time-step, write-once Tensor arrays.

[`class TensorArraySpec`](./tf/TensorArraySpec): Type specification for a <a href="./tf/TensorArray"><code>tf.TensorArray</code></a>.

[`class TensorInfo`](./tf/TensorInfo): A ProtocolMessage

[`class TensorShape`](./tf/TensorShape): Represents the shape of a `Tensor`.

[`class TensorSpec`](./tf/TensorSpec): Describes a tf.Tensor.

[`class TextLineReader`](./tf/TextLineReader): A Reader that outputs the lines of a file delimited by newlines.

[`class TypeSpec`](./tf/TypeSpec): Specifies a TensorFlow value type.

[`class UnconnectedGradients`](./tf/UnconnectedGradients): Controls how gradient computation behaves when y does not depend on x.

[`class VarLenFeature`](./tf/io/VarLenFeature): Configuration for parsing a variable-length input feature.

[`class Variable`](./tf/Variable): See the [Variables Guide](https://tensorflow.org/guide/variables).

[`class VariableAggregation`](./tf/VariableAggregation): Indicates how a distributed variable will be aggregated.

[`class VariableScope`](./tf/VariableScope): Variable scope object to carry defaults to provide to `get_variable`.

[`class VariableSynchronization`](./tf/VariableSynchronization): Indicates when a distributed variable will be synced.

[`class WholeFileReader`](./tf/WholeFileReader): A Reader that outputs the entire contents of a file as a value.

[`class constant_initializer`](./tf/initializers/constant): Initializer that generates tensors with constant values.

[`class glorot_normal_initializer`](./tf/glorot_normal_initializer): The Glorot normal initializer, also called Xavier normal initializer.

[`class glorot_uniform_initializer`](./tf/glorot_uniform_initializer): The Glorot uniform initializer, also called Xavier uniform initializer.

[`class name_scope`](./tf/name_scope): A context manager for use when defining a Python op.

[`class ones_initializer`](./tf/initializers/ones): Initializer that generates tensors initialized to 1.

[`class orthogonal_initializer`](./tf/initializers/orthogonal): Initializer that generates an orthogonal matrix.

[`class random_normal_initializer`](./tf/random_normal_initializer): Initializer that generates tensors with a normal distribution.

[`class random_uniform_initializer`](./tf/random_uniform_initializer): Initializer that generates tensors with a uniform distribution.

[`class truncated_normal_initializer`](./tf/initializers/truncated_normal): Initializer that generates a truncated normal distribution.

[`class uniform_unit_scaling_initializer`](./tf/initializers/uniform_unit_scaling): Initializer that generates tensors without scaling variance.

[`class variable_scope`](./tf/variable_scope): A context manager for defining ops that creates variables (layers).

[`class variance_scaling_initializer`](./tf/initializers/variance_scaling): Initializer capable of adapting its scale to the shape of weights tensors.

[`class zeros_initializer`](./tf/zeros_initializer): Initializer that generates tensors initialized to 0.

## Functions

[`Assert(...)`](./tf/debugging/Assert): Asserts that the given condition is true.

[`NoGradient(...)`](./tf/no_gradient): Specifies that ops of type `op_type` is not differentiable.

[`NotDifferentiable(...)`](./tf/no_gradient): Specifies that ops of type `op_type` is not differentiable.

[`Print(...)`](./tf/Print): Prints a list of tensors. (deprecated)

[`abs(...)`](./tf/math/abs): Computes the absolute value of a tensor.

[`accumulate_n(...)`](./tf/math/accumulate_n): Returns the element-wise sum of a list of tensors.

[`acos(...)`](./tf/math/acos): Computes acos of x element-wise.

[`acosh(...)`](./tf/math/acosh): Computes inverse hyperbolic cosine of x element-wise.

[`add(...)`](./tf/math/add): Returns x + y element-wise.

[`add_check_numerics_ops(...)`](./tf/add_check_numerics_ops): Connect a <a href="./tf/debugging/check_numerics"><code>tf.debugging.check_numerics</code></a> to every floating point tensor.

[`add_n(...)`](./tf/math/add_n): Adds all input tensors element-wise.

[`add_to_collection(...)`](./tf/add_to_collection): Wrapper for <a href="./tf/Graph#add_to_collection"><code>Graph.add_to_collection()</code></a> using the default graph.

[`add_to_collections(...)`](./tf/add_to_collections): Wrapper for <a href="./tf/Graph#add_to_collections"><code>Graph.add_to_collections()</code></a> using the default graph.

[`all_variables(...)`](./tf/all_variables): Use <a href="./tf/global_variables"><code>tf.compat.v1.global_variables</code></a> instead. (deprecated)

[`angle(...)`](./tf/math/angle): Returns the element-wise argument of a complex (or real) tensor.

[`arg_max(...)`](./tf/arg_max): Returns the index with the largest value across dimensions of a tensor.

[`arg_min(...)`](./tf/arg_min): Returns the index with the smallest value across dimensions of a tensor.

[`argmax(...)`](./tf/math/argmax): Returns the index with the largest value across axes of a tensor. (deprecated arguments)

[`argmin(...)`](./tf/math/argmin): Returns the index with the smallest value across axes of a tensor. (deprecated arguments)

[`argsort(...)`](./tf/argsort): Returns the indices of a tensor that give its sorted order along an axis.

[`as_dtype(...)`](./tf/dtypes/as_dtype): Converts the given `type_value` to a `DType`.

[`as_string(...)`](./tf/strings/as_string): Converts each entry in the given tensor to strings.

[`asin(...)`](./tf/math/asin): Computes the trignometric inverse sine of x element-wise.

[`asinh(...)`](./tf/math/asinh): Computes inverse hyperbolic sine of x element-wise.

[`assert_equal(...)`](./tf/debugging/assert_equal): Assert the condition `x == y` holds element-wise.

[`assert_greater(...)`](./tf/debugging/assert_greater): Assert the condition `x > y` holds element-wise.

[`assert_greater_equal(...)`](./tf/debugging/assert_greater_equal): Assert the condition `x >= y` holds element-wise.

[`assert_integer(...)`](./tf/debugging/assert_integer): Assert that `x` is of integer dtype.

[`assert_less(...)`](./tf/debugging/assert_less): Assert the condition `x < y` holds element-wise.

[`assert_less_equal(...)`](./tf/debugging/assert_less_equal): Assert the condition `x <= y` holds element-wise.

[`assert_near(...)`](./tf/debugging/assert_near): Assert the condition `x` and `y` are close element-wise.

[`assert_negative(...)`](./tf/debugging/assert_negative): Assert the condition `x < 0` holds element-wise.

[`assert_non_negative(...)`](./tf/debugging/assert_non_negative): Assert the condition `x >= 0` holds element-wise.

[`assert_non_positive(...)`](./tf/debugging/assert_non_positive): Assert the condition `x <= 0` holds element-wise.

[`assert_none_equal(...)`](./tf/debugging/assert_none_equal): Assert the condition `x != y` holds element-wise.

[`assert_positive(...)`](./tf/debugging/assert_positive): Assert the condition `x > 0` holds element-wise.

[`assert_proper_iterable(...)`](./tf/debugging/assert_proper_iterable): Static assert that values is a "proper" iterable.

[`assert_rank(...)`](./tf/debugging/assert_rank): Assert `x` has rank equal to `rank`.

[`assert_rank_at_least(...)`](./tf/debugging/assert_rank_at_least): Assert `x` has rank equal to `rank` or higher.

[`assert_rank_in(...)`](./tf/debugging/assert_rank_in): Assert `x` has rank in `ranks`.

[`assert_same_float_dtype(...)`](./tf/debugging/assert_same_float_dtype): Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](./tf/debugging/assert_scalar): Asserts that the given `tensor` is a scalar (i.e. zero-dimensional).

[`assert_type(...)`](./tf/debugging/assert_type): Statically asserts that the given `Tensor` is of the specified type.

[`assert_variables_initialized(...)`](./tf/assert_variables_initialized): Returns an Op to check if variables are initialized.

[`assign(...)`](./tf/assign): Update `ref` by assigning `value` to it.

[`assign_add(...)`](./tf/assign_add): Update `ref` by adding `value` to it.

[`assign_sub(...)`](./tf/assign_sub): Update `ref` by subtracting `value` from it.

[`atan(...)`](./tf/math/atan): Computes the trignometric inverse tangent of x element-wise.

[`atan2(...)`](./tf/math/atan2): Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

[`atanh(...)`](./tf/math/atanh): Computes inverse hyperbolic tangent of x element-wise.

[`batch_gather(...)`](./tf/batch_gather): Gather slices from params according to indices with leading batch dims. (deprecated)

[`batch_scatter_update(...)`](./tf/batch_scatter_update): Generalization of <a href="./tf/scatter_update"><code>tf.compat.v1.scatter_update</code></a> to axis different than 0. (deprecated)

[`batch_to_space(...)`](./tf/batch_to_space): BatchToSpace for 4-D tensors of type T.

[`batch_to_space_nd(...)`](./tf/batch_to_space_nd): BatchToSpace for N-D tensors of type T.

[`betainc(...)`](./tf/math/betainc): Compute the regularized incomplete beta integral \\(I_x(a, b)\\).

[`bincount(...)`](./tf/math/bincount): Counts the number of occurrences of each value in an integer array.

[`bitcast(...)`](./tf/bitcast): Bitcasts a tensor from one type to another without copying data.

[`boolean_mask(...)`](./tf/boolean_mask): Apply boolean mask to tensor.

[`broadcast_dynamic_shape(...)`](./tf/broadcast_dynamic_shape): Computes the shape of a broadcast given symbolic shapes.

[`broadcast_static_shape(...)`](./tf/broadcast_static_shape): Computes the shape of a broadcast given known shapes.

[`broadcast_to(...)`](./tf/broadcast_to): Broadcast an array for a compatible shape.

[`case(...)`](./tf/case): Create a case operation.

[`cast(...)`](./tf/cast): Casts a tensor to a new type.

[`ceil(...)`](./tf/math/ceil): Returns element-wise smallest integer not less than x.

[`check_numerics(...)`](./tf/debugging/check_numerics): Checks a tensor for NaN and Inf values.

[`cholesky(...)`](./tf/linalg/cholesky): Computes the Cholesky decomposition of one or more square matrices.

[`cholesky_solve(...)`](./tf/linalg/cholesky_solve): Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

[`clip_by_average_norm(...)`](./tf/clip_by_average_norm): Clips tensor values to a maximum average L2-norm. (deprecated)

[`clip_by_global_norm(...)`](./tf/clip_by_global_norm): Clips values of multiple tensors by the ratio of the sum of their norms.

[`clip_by_norm(...)`](./tf/clip_by_norm): Clips tensor values to a maximum L2-norm.

[`clip_by_value(...)`](./tf/clip_by_value): Clips tensor values to a specified min and max.

[`colocate_with(...)`](./tf/colocate_with): DEPRECATED FUNCTION

[`complex(...)`](./tf/dtypes/complex): Converts two real numbers to a complex number.

[`concat(...)`](./tf/concat): Concatenates tensors along one dimension.

[`cond(...)`](./tf/cond): Return `true_fn()` if the predicate `pred` is true else `false_fn()`. (deprecated arguments)

[`confusion_matrix(...)`](./tf/math/confusion_matrix): Computes the confusion matrix from predictions and labels.

[`conj(...)`](./tf/math/conj): Returns the complex conjugate of a complex number.

[`constant(...)`](./tf/constant): Creates a constant tensor.

[`container(...)`](./tf/container): Wrapper for <a href="./tf/Graph#container"><code>Graph.container()</code></a> using the default graph.

[`control_dependencies(...)`](./tf/control_dependencies): Wrapper for <a href="./tf/Graph#control_dependencies"><code>Graph.control_dependencies()</code></a> using the default graph.

[`control_flow_v2_enabled(...)`](./tf/control_flow_v2_enabled): Returns `True` if v2 control flow is enabled.

[`convert_to_tensor(...)`](./tf/convert_to_tensor): Converts the given `value` to a `Tensor`.

[`convert_to_tensor_or_indexed_slices(...)`](./tf/convert_to_tensor_or_indexed_slices): Converts the given object to a `Tensor` or an `IndexedSlices`.

[`convert_to_tensor_or_sparse_tensor(...)`](./tf/convert_to_tensor_or_sparse_tensor): Converts value to a `SparseTensor` or `Tensor`.

[`cos(...)`](./tf/math/cos): Computes cos of x element-wise.

[`cosh(...)`](./tf/math/cosh): Computes hyperbolic cosine of x element-wise.

[`count_nonzero(...)`](./tf/math/count_nonzero): Computes number of nonzero elements across dimensions of a tensor. (deprecated arguments) (deprecated arguments)

[`count_up_to(...)`](./tf/count_up_to): Increments 'ref' until it reaches 'limit'. (deprecated)

[`create_partitioned_variables(...)`](./tf/create_partitioned_variables): Create a list of partitioned variables according to the given `slicing`. (deprecated)

[`cross(...)`](./tf/linalg/cross): Compute the pairwise cross product.

[`cumprod(...)`](./tf/math/cumprod): Compute the cumulative product of the tensor `x` along `axis`.

[`cumsum(...)`](./tf/math/cumsum): Compute the cumulative sum of the tensor `x` along `axis`.

[`custom_gradient(...)`](./tf/custom_gradient): Decorator to define a function with a custom gradient.

[`decode_base64(...)`](./tf/io/decode_base64): Decode web-safe base64-encoded strings.

[`decode_compressed(...)`](./tf/io/decode_compressed): Decompress strings.

[`decode_csv(...)`](./tf/io/decode_csv): Convert CSV records to tensors. Each column maps to one tensor.

[`decode_json_example(...)`](./tf/io/decode_json_example): Convert JSON-encoded Example records to binary protocol buffer strings.

[`decode_raw(...)`](./tf/decode_raw): Convert raw byte strings into tensors. (deprecated arguments)

[`delete_session_tensor(...)`](./tf/delete_session_tensor): Delete the tensor for the given tensor handle.

[`depth_to_space(...)`](./tf/nn/depth_to_space): DepthToSpace for tensors of type T.

[`dequantize(...)`](./tf/quantization/dequantize): Dequantize the 'input' tensor into a float Tensor.

[`deserialize_many_sparse(...)`](./tf/io/deserialize_many_sparse): Deserialize and concatenate `SparseTensors` from a serialized minibatch.

[`device(...)`](./tf/device): Wrapper for <a href="./tf/Graph#device"><code>Graph.device()</code></a> using the default graph.

[`diag(...)`](./tf/linalg/tensor_diag): Returns a diagonal tensor with a given diagonal values.

[`diag_part(...)`](./tf/linalg/tensor_diag_part): Returns the diagonal part of the tensor.

[`digamma(...)`](./tf/math/digamma): Computes Psi, the derivative of Lgamma (the log of the absolute value of

[`dimension_at_index(...)`](./tf/compat/dimension_at_index): Compatibility utility required to allow for both V1 and V2 behavior in TF.

[`dimension_value(...)`](./tf/compat/dimension_value): Compatibility utility required to allow for both V1 and V2 behavior in TF.

[`disable_control_flow_v2(...)`](./tf/disable_control_flow_v2): Opts out of control flow v2.

[`disable_eager_execution(...)`](./tf/disable_eager_execution): Disables eager execution.

[`disable_resource_variables(...)`](./tf/disable_resource_variables): Opts out of resource variables. (deprecated)

[`disable_tensor_equality(...)`](./tf/disable_tensor_equality): Compare Tensors by their id and be hashable.

[`disable_v2_behavior(...)`](./tf/disable_v2_behavior): Disables TensorFlow 2.x behaviors.

[`disable_v2_tensorshape(...)`](./tf/disable_v2_tensorshape): Disables the V2 TensorShape behavior and reverts to V1 behavior.

[`div(...)`](./tf/div): Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)

[`div_no_nan(...)`](./tf/math/divide_no_nan): Computes an unsafe divide which returns 0 if the y is zero.

[`divide(...)`](./tf/math/divide): Computes Python style division of `x` by `y`.

[`dynamic_partition(...)`](./tf/dynamic_partition): Partitions `data` into `num_partitions` tensors using indices from `partitions`.

[`dynamic_stitch(...)`](./tf/dynamic_stitch): Interleave the values from the `data` tensors into a single tensor.

[`edit_distance(...)`](./tf/edit_distance): Computes the Levenshtein distance between sequences.

[`einsum(...)`](./tf/einsum): Tensor contraction over specified indices and outer product.

[`enable_control_flow_v2(...)`](./tf/enable_control_flow_v2): Use control flow v2.

[`enable_eager_execution(...)`](./tf/enable_eager_execution): Enables eager execution for the lifetime of this program.

[`enable_resource_variables(...)`](./tf/enable_resource_variables): Creates resource variables by default.

[`enable_tensor_equality(...)`](./tf/enable_tensor_equality): Compare Tensors with element-wise comparison and thus be unhashable.

[`enable_v2_behavior(...)`](./tf/enable_v2_behavior): Enables TensorFlow 2.x behaviors.

[`enable_v2_tensorshape(...)`](./tf/enable_v2_tensorshape): In TensorFlow 2.0, iterating over a TensorShape instance returns values.

[`encode_base64(...)`](./tf/io/encode_base64): Encode strings into web-safe base64 format.

[`ensure_shape(...)`](./tf/ensure_shape): Updates the shape of a tensor and checks at runtime that the shape holds.

[`equal(...)`](./tf/math/equal): Returns the truth value of (x == y) element-wise.

[`erf(...)`](./tf/math/erf): Computes the Gauss error function of `x` element-wise.

[`erfc(...)`](./tf/math/erfc): Computes the complementary error function of `x` element-wise.

[`executing_eagerly(...)`](./tf/executing_eagerly): Returns True if the current thread has eager execution enabled.

[`exp(...)`](./tf/math/exp): Computes exponential of x element-wise.  \\(y = e^x\\).

[`expand_dims(...)`](./tf/expand_dims): Inserts a dimension of 1 into a tensor's shape. (deprecated arguments)

[`expm1(...)`](./tf/math/expm1): Computes `exp(x) - 1` element-wise.

[`extract_image_patches(...)`](./tf/image/extract_image_patches): Extract `patches` from `images` and put them in the "depth" output dimension.

[`extract_volume_patches(...)`](./tf/extract_volume_patches): Extract `patches` from `input` and put them in the "depth" output dimension. 3D extension of `extract_image_patches`.

[`eye(...)`](./tf/eye): Construct an identity matrix, or a batch of matrices.

[`fake_quant_with_min_max_args(...)`](./tf/quantization/fake_quant_with_min_max_args): Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same type.

[`fake_quant_with_min_max_args_gradient(...)`](./tf/quantization/fake_quant_with_min_max_args_gradient): Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`fake_quant_with_min_max_vars(...)`](./tf/quantization/fake_quant_with_min_max_vars): Fake-quantize the 'inputs' tensor of type float via global float scalars `min`

[`fake_quant_with_min_max_vars_gradient(...)`](./tf/quantization/fake_quant_with_min_max_vars_gradient): Compute gradients for a FakeQuantWithMinMaxVars operation.

[`fake_quant_with_min_max_vars_per_channel(...)`](./tf/quantization/fake_quant_with_min_max_vars_per_channel): Fake-quantize the 'inputs' tensor of type float and one of the shapes: `[d]`,

[`fake_quant_with_min_max_vars_per_channel_gradient(...)`](./tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient): Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`fft(...)`](./tf/signal/fft): Fast Fourier transform.

[`fft2d(...)`](./tf/signal/fft2d): 2D fast Fourier transform.

[`fft3d(...)`](./tf/signal/fft3d): 3D fast Fourier transform.

[`fill(...)`](./tf/fill): Creates a tensor filled with a scalar value.

[`fingerprint(...)`](./tf/fingerprint): Generates fingerprint values.

[`fixed_size_partitioner(...)`](./tf/fixed_size_partitioner): Partitioner to specify a fixed number of shards along given axis.

[`floor(...)`](./tf/math/floor): Returns element-wise largest integer not greater than x.

[`floor_div(...)`](./tf/floor_div): Returns x // y element-wise.

[`floordiv(...)`](./tf/math/floordiv): Divides `x / y` elementwise, rounding toward the most negative integer.

[`floormod(...)`](./tf/math/floormod): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`foldl(...)`](./tf/foldl): foldl on the list of tensors unpacked from `elems` on dimension 0.

[`foldr(...)`](./tf/foldr): foldr on the list of tensors unpacked from `elems` on dimension 0.

[`function(...)`](./tf/function): Creates a callable TensorFlow graph from a Python function.

[`gather(...)`](./tf/gather): Gather slices from params axis axis according to indices.

[`gather_nd(...)`](./tf/gather_nd): Gather slices from `params` into a Tensor with shape specified by `indices`.

[`get_collection(...)`](./tf/get_collection): Wrapper for <a href="./tf/Graph#get_collection"><code>Graph.get_collection()</code></a> using the default graph.

[`get_collection_ref(...)`](./tf/get_collection_ref): Wrapper for <a href="./tf/Graph#get_collection_ref"><code>Graph.get_collection_ref()</code></a> using the default graph.

[`get_default_graph(...)`](./tf/get_default_graph): Returns the default graph for the current thread.

[`get_default_session(...)`](./tf/get_default_session): Returns the default session for the current thread.

[`get_local_variable(...)`](./tf/get_local_variable): Gets an existing *local* variable or creates a new one.

[`get_logger(...)`](./tf/get_logger): Return TF logger instance.

[`get_seed(...)`](./tf/random/get_seed): Returns the local seeds an operation should use given an op-specific seed.

[`get_session_handle(...)`](./tf/get_session_handle): Return the handle of `data`.

[`get_session_tensor(...)`](./tf/get_session_tensor): Get the tensor of type `dtype` by feeding a tensor handle.

[`get_static_value(...)`](./tf/get_static_value): Returns the constant value of the given tensor, if efficiently calculable.

[`get_variable(...)`](./tf/get_variable): Gets an existing variable with these parameters or create a new one.

[`get_variable_scope(...)`](./tf/get_variable_scope): Returns the current variable scope.

[`global_norm(...)`](./tf/linalg/global_norm): Computes the global norm of multiple tensors.

[`global_variables(...)`](./tf/global_variables): Returns global variables.

[`global_variables_initializer(...)`](./tf/initializers/global_variables): Returns an Op that initializes global variables.

[`grad_pass_through(...)`](./tf/grad_pass_through): Creates a grad-pass-through op with the forward behavior provided in f.

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

[`ifft(...)`](./tf/signal/ifft): Inverse fast Fourier transform.

[`ifft2d(...)`](./tf/signal/ifft2d): Inverse 2D fast Fourier transform.

[`ifft3d(...)`](./tf/signal/ifft3d): Inverse 3D fast Fourier transform.

[`igamma(...)`](./tf/math/igamma): Compute the lower regularized incomplete Gamma function `P(a, x)`.

[`igammac(...)`](./tf/math/igammac): Compute the upper regularized incomplete Gamma function `Q(a, x)`.

[`imag(...)`](./tf/math/imag): Returns the imaginary part of a complex (or real) tensor.

[`import_graph_def(...)`](./tf/graph_util/import_graph_def): Imports the graph from `graph_def` into the current default `Graph`. (deprecated arguments)

[`init_scope(...)`](./tf/init_scope): A context manager that lifts ops out of control-flow scopes and function-building graphs.

[`initialize_all_tables(...)`](./tf/initialize_all_tables): Returns an Op that initializes all tables of the default graph. (deprecated)

[`initialize_all_variables(...)`](./tf/initialize_all_variables): See <a href="./tf/initializers/global_variables"><code>tf.compat.v1.global_variables_initializer</code></a>. (deprecated)

[`initialize_local_variables(...)`](./tf/initialize_local_variables): See <a href="./tf/initializers/local_variables"><code>tf.compat.v1.local_variables_initializer</code></a>. (deprecated)

[`initialize_variables(...)`](./tf/initialize_variables): See <a href="./tf/initializers/variables"><code>tf.compat.v1.variables_initializer</code></a>. (deprecated)

[`invert_permutation(...)`](./tf/math/invert_permutation): Computes the inverse permutation of a tensor.

[`is_finite(...)`](./tf/math/is_finite): Returns which elements of x are finite.

[`is_inf(...)`](./tf/math/is_inf): Returns which elements of x are Inf.

[`is_nan(...)`](./tf/math/is_nan): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](./tf/math/is_non_decreasing): Returns `True` if `x` is non-decreasing.

[`is_numeric_tensor(...)`](./tf/debugging/is_numeric_tensor): Returns `True` if the elements of `tensor` are numbers.

[`is_strictly_increasing(...)`](./tf/math/is_strictly_increasing): Returns `True` if `x` is strictly increasing.

[`is_tensor(...)`](./tf/is_tensor): Checks whether `x` is a tensor or "tensor-like".

[`is_variable_initialized(...)`](./tf/is_variable_initialized): Tests if a variable has been initialized.

[`lbeta(...)`](./tf/math/lbeta): Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

[`less(...)`](./tf/math/less): Returns the truth value of (x < y) element-wise.

[`less_equal(...)`](./tf/math/less_equal): Returns the truth value of (x <= y) element-wise.

[`lgamma(...)`](./tf/math/lgamma): Computes the log of the absolute value of `Gamma(x)` element-wise.

[`lin_space(...)`](./tf/linspace): Generates values in an interval.

[`linspace(...)`](./tf/linspace): Generates values in an interval.

[`load_file_system_library(...)`](./tf/load_file_system_library): Loads a TensorFlow plugin, containing file system implementation. (deprecated)

[`load_library(...)`](./tf/load_library): Loads a TensorFlow plugin.

[`load_op_library(...)`](./tf/load_op_library): Loads a TensorFlow plugin, containing custom ops and kernels.

[`local_variables(...)`](./tf/local_variables): Returns local variables.

[`local_variables_initializer(...)`](./tf/initializers/local_variables): Returns an Op that initializes all local variables.

[`log(...)`](./tf/math/log): Computes natural logarithm of x element-wise.

[`log1p(...)`](./tf/math/log1p): Computes natural logarithm of (1 + x) element-wise.

[`log_sigmoid(...)`](./tf/math/log_sigmoid): Computes log sigmoid of `x` element-wise.

[`logical_and(...)`](./tf/math/logical_and): Returns the truth value of x AND y element-wise.

[`logical_not(...)`](./tf/math/logical_not): Returns the truth value of NOT x element-wise.

[`logical_or(...)`](./tf/math/logical_or): Returns the truth value of x OR y element-wise.

[`logical_xor(...)`](./tf/math/logical_xor): Logical XOR function.

[`make_ndarray(...)`](./tf/make_ndarray): Create a numpy ndarray from a tensor.

[`make_template(...)`](./tf/make_template): Given an arbitrary function, wrap it so that it does variable sharing.

[`make_tensor_proto(...)`](./tf/make_tensor_proto): Create a TensorProto.

[`map_fn(...)`](./tf/map_fn): map on the list of tensors unpacked from `elems` on dimension 0.

[`matching_files(...)`](./tf/io/matching_files): Returns the set of files matching one or more glob patterns.

[`matmul(...)`](./tf/linalg/matmul): Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

[`matrix_band_part(...)`](./tf/linalg/band_part): Copy a tensor setting everything outside a central band in each innermost matrix

[`matrix_determinant(...)`](./tf/linalg/det): Computes the determinant of one or more square matrices.

[`matrix_diag(...)`](./tf/linalg/diag): Returns a batched diagonal tensor with given batched diagonal values.

[`matrix_diag_part(...)`](./tf/linalg/diag_part): Returns the batched diagonal part of a batched tensor.

[`matrix_inverse(...)`](./tf/linalg/inv): Computes the inverse of one or more square invertible matrices or their

[`matrix_set_diag(...)`](./tf/linalg/set_diag): Returns a batched matrix tensor with new batched diagonal values.

[`matrix_solve(...)`](./tf/linalg/solve): Solves systems of linear equations.

[`matrix_solve_ls(...)`](./tf/linalg/lstsq): Solves one or more linear least-squares problems.

[`matrix_square_root(...)`](./tf/linalg/sqrtm): Computes the matrix square root of one or more square matrices:

[`matrix_transpose(...)`](./tf/linalg/matrix_transpose): Transposes last two dimensions of tensor `a`.

[`matrix_triangular_solve(...)`](./tf/linalg/triangular_solve): Solves systems of linear equations with upper or lower triangular matrices by backsubstitution.

[`maximum(...)`](./tf/math/maximum): Returns the max of x and y (i.e. x > y ? x : y) element-wise.

[`meshgrid(...)`](./tf/meshgrid): Broadcasts parameters for evaluation on an N-D grid.

[`min_max_variable_partitioner(...)`](./tf/min_max_variable_partitioner): Partitioner to allocate minimum size per slice.

[`minimum(...)`](./tf/math/minimum): Returns the min of x and y (i.e. x < y ? x : y) element-wise.

[`mod(...)`](./tf/math/floormod): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`model_variables(...)`](./tf/model_variables): Returns all variables in the MODEL_VARIABLES collection.

[`moving_average_variables(...)`](./tf/moving_average_variables): Returns all variables that maintain their moving averages.

[`multinomial(...)`](./tf/random/multinomial): Draws samples from a multinomial distribution. (deprecated)

[`multiply(...)`](./tf/math/multiply): Returns x * y element-wise.

[`negative(...)`](./tf/math/negative): Computes numerical negative value element-wise.

[`no_gradient(...)`](./tf/no_gradient): Specifies that ops of type `op_type` is not differentiable.

[`no_op(...)`](./tf/no_op): Does nothing. Only useful as a placeholder for control edges.

[`no_regularizer(...)`](./tf/no_regularizer): Use this function to prevent regularization of variables.

[`nondifferentiable_batch_function(...)`](./tf/nondifferentiable_batch_function): Batches the computation done by the decorated function.

[`norm(...)`](./tf/norm): Computes the norm of vectors, matrices, and tensors. (deprecated arguments)

[`not_equal(...)`](./tf/math/not_equal): Returns the truth value of (x != y) element-wise.

[`numpy_function(...)`](./tf/numpy_function): Wraps a python function and uses it as a TensorFlow op.

[`one_hot(...)`](./tf/one_hot): Returns a one-hot tensor.

[`ones(...)`](./tf/ones): Creates a tensor with all elements set to 1.

[`ones_like(...)`](./tf/ones_like): Creates a tensor with all elements set to 1.

[`op_scope(...)`](./tf/op_scope): DEPRECATED. Same as name_scope above, just different argument order.

[`pad(...)`](./tf/pad): Pads a tensor.

[`parallel_stack(...)`](./tf/parallel_stack): Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor in parallel.

[`parse_example(...)`](./tf/io/parse_example): Parses `Example` protos into a `dict` of tensors.

[`parse_single_example(...)`](./tf/io/parse_single_example): Parses a single `Example` proto.

[`parse_single_sequence_example(...)`](./tf/io/parse_single_sequence_example): Parses a single `SequenceExample` proto.

[`parse_tensor(...)`](./tf/io/parse_tensor): Transforms a serialized tensorflow.TensorProto proto into a Tensor.

[`placeholder(...)`](./tf/placeholder): Inserts a placeholder for a tensor that will be always fed.

[`placeholder_with_default(...)`](./tf/placeholder_with_default): A placeholder op that passes through `input` when its output is not fed.

[`polygamma(...)`](./tf/math/polygamma): Compute the polygamma function \\(\psi^{(n)}(x)\\).

[`pow(...)`](./tf/math/pow): Computes the power of one value to another.

[`print(...)`](./tf/print): Print the specified inputs.

[`py_func(...)`](./tf/py_func): Wraps a python function and uses it as a TensorFlow op.

[`py_function(...)`](./tf/py_function): Wraps a python function into a TensorFlow op that executes it eagerly.

[`qr(...)`](./tf/linalg/qr): Computes the QR decompositions of one or more matrices.

[`quantize(...)`](./tf/quantization/quantize): Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

[`quantize_v2(...)`](./tf/quantize_v2): Please use <a href="./tf/quantization/quantize"><code>tf.quantization.quantize</code></a> instead.

[`quantized_concat(...)`](./tf/quantization/quantized_concat): Concatenates quantized tensors along one dimension.

[`random_crop(...)`](./tf/image/random_crop): Randomly crops a tensor to a given size.

[`random_gamma(...)`](./tf/random/gamma): Draws `shape` samples from each of the given Gamma distribution(s).

[`random_normal(...)`](./tf/random/normal): Outputs random values from a normal distribution.

[`random_poisson(...)`](./tf/random/poisson): Draws `shape` samples from each of the given Poisson distribution(s).

[`random_shuffle(...)`](./tf/random/shuffle): Randomly shuffles a tensor along its first dimension.

[`random_uniform(...)`](./tf/random/uniform): Outputs random values from a uniform distribution.

[`range(...)`](./tf/range): Creates a sequence of numbers.

[`rank(...)`](./tf/rank): Returns the rank of a tensor.

[`read_file(...)`](./tf/io/read_file): Reads and outputs the entire contents of the input filename.

[`real(...)`](./tf/math/real): Returns the real part of a complex (or real) tensor.

[`realdiv(...)`](./tf/realdiv): Returns x / y element-wise for real types.

[`reciprocal(...)`](./tf/math/reciprocal): Computes the reciprocal of x element-wise.

[`recompute_grad(...)`](./tf/recompute_grad): An eager-compatible version of recompute_grad.

[`reduce_all(...)`](./tf/math/reduce_all): Computes the "logical and" of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_any(...)`](./tf/math/reduce_any): Computes the "logical or" of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_join(...)`](./tf/strings/reduce_join): Joins a string Tensor across the given dimensions.

[`reduce_logsumexp(...)`](./tf/math/reduce_logsumexp): Computes log(sum(exp(elements across dimensions of a tensor))). (deprecated arguments)

[`reduce_max(...)`](./tf/math/reduce_max): Computes the maximum of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_mean(...)`](./tf/math/reduce_mean): Computes the mean of elements across dimensions of a tensor.

[`reduce_min(...)`](./tf/math/reduce_min): Computes the minimum of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_prod(...)`](./tf/math/reduce_prod): Computes the product of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_sum(...)`](./tf/math/reduce_sum): Computes the sum of elements across dimensions of a tensor. (deprecated arguments)

[`regex_replace(...)`](./tf/strings/regex_replace): Replace elements of `input` matching regex `pattern` with `rewrite`.

[`register_tensor_conversion_function(...)`](./tf/register_tensor_conversion_function): Registers a function for converting objects of `base_type` to `Tensor`.

[`repeat(...)`](./tf/repeat): Repeat elements of `input`

[`report_uninitialized_variables(...)`](./tf/report_uninitialized_variables): Adds ops to list the names of uninitialized variables.

[`required_space_to_batch_paddings(...)`](./tf/required_space_to_batch_paddings): Calculate padding required to make block_shape divide input_shape.

[`reset_default_graph(...)`](./tf/reset_default_graph): Clears the default graph stack and resets the global default graph.

[`reshape(...)`](./tf/reshape): Reshapes a tensor.

[`resource_variables_enabled(...)`](./tf/resource_variables_enabled): Returns `True` if resource variables are enabled.

[`reverse(...)`](./tf/reverse): Reverses specific dimensions of a tensor.

[`reverse_sequence(...)`](./tf/reverse_sequence): Reverses variable length slices.

[`reverse_v2(...)`](./tf/reverse): Reverses specific dimensions of a tensor.

[`rint(...)`](./tf/math/rint): Returns element-wise integer closest to x.

[`roll(...)`](./tf/roll): Rolls the elements of a tensor along an axis.

[`round(...)`](./tf/math/round): Rounds the values of a tensor to the nearest integer, element-wise.

[`rsqrt(...)`](./tf/math/rsqrt): Computes reciprocal of square root of x element-wise.

[`saturate_cast(...)`](./tf/dtypes/saturate_cast): Performs a safe saturating cast of `value` to `dtype`.

[`scalar_mul(...)`](./tf/math/scalar_mul): Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

[`scan(...)`](./tf/scan): scan on the list of tensors unpacked from `elems` on dimension 0.

[`scatter_add(...)`](./tf/scatter_add): Adds sparse updates to the variable referenced by `resource`.

[`scatter_div(...)`](./tf/scatter_div): Divides a variable reference by sparse updates.

[`scatter_max(...)`](./tf/scatter_max): Reduces sparse updates into a variable reference using the `max` operation.

[`scatter_min(...)`](./tf/scatter_min): Reduces sparse updates into a variable reference using the `min` operation.

[`scatter_mul(...)`](./tf/scatter_mul): Multiplies sparse updates into a variable reference.

[`scatter_nd(...)`](./tf/scatter_nd): Scatter `updates` into a new tensor according to `indices`.

[`scatter_nd_add(...)`](./tf/scatter_nd_add): Applies sparse addition to individual values or slices in a Variable.

[`scatter_nd_sub(...)`](./tf/scatter_nd_sub): Applies sparse subtraction to individual values or slices in a Variable.

[`scatter_nd_update(...)`](./tf/scatter_nd_update): Applies sparse `updates` to individual values or slices in a Variable.

[`scatter_sub(...)`](./tf/scatter_sub): Subtracts sparse updates to a variable reference.

[`scatter_update(...)`](./tf/scatter_update): Applies sparse updates to a variable reference.

[`searchsorted(...)`](./tf/searchsorted): Searches input tensor for values on the innermost dimension.

[`segment_max(...)`](./tf/math/segment_max): Computes the maximum along segments of a tensor.

[`segment_mean(...)`](./tf/math/segment_mean): Computes the mean along segments of a tensor.

[`segment_min(...)`](./tf/math/segment_min): Computes the minimum along segments of a tensor.

[`segment_prod(...)`](./tf/math/segment_prod): Computes the product along segments of a tensor.

[`segment_sum(...)`](./tf/math/segment_sum): Computes the sum along segments of a tensor.

[`self_adjoint_eig(...)`](./tf/linalg/eigh): Computes the eigen decomposition of a batch of self-adjoint matrices.

[`self_adjoint_eigvals(...)`](./tf/linalg/eigvalsh): Computes the eigenvalues of one or more self-adjoint matrices.

[`sequence_mask(...)`](./tf/sequence_mask): Returns a mask tensor representing the first N positions of each cell.

[`serialize_many_sparse(...)`](./tf/io/serialize_many_sparse): Serialize `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor`.

[`serialize_sparse(...)`](./tf/io/serialize_sparse): Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

[`serialize_tensor(...)`](./tf/io/serialize_tensor): Transforms a Tensor into a serialized TensorProto proto.

[`set_random_seed(...)`](./tf/random/set_random_seed): Sets the graph-level random seed for the default graph.

[`setdiff1d(...)`](./tf/setdiff1d): Computes the difference between two lists of numbers or strings.

[`shape(...)`](./tf/shape): Returns the shape of a tensor.

[`shape_n(...)`](./tf/shape_n): Returns shape of tensors.

[`sigmoid(...)`](./tf/math/sigmoid): Computes sigmoid of `x` element-wise.

[`sign(...)`](./tf/math/sign): Returns an element-wise indication of the sign of a number.

[`sin(...)`](./tf/math/sin): Computes sine of x element-wise.

[`sinh(...)`](./tf/math/sinh): Computes hyperbolic sine of x element-wise.

[`size(...)`](./tf/size): Returns the size of a tensor.

[`slice(...)`](./tf/slice): Extracts a slice from a tensor.

[`sort(...)`](./tf/sort): Sorts a tensor.

[`space_to_batch(...)`](./tf/nn/space_to_batch): SpaceToBatch for 4-D tensors of type T.

[`space_to_batch_nd(...)`](./tf/space_to_batch_nd): SpaceToBatch for N-D tensors of type T.

[`space_to_depth(...)`](./tf/nn/space_to_depth): SpaceToDepth for tensors of type T.

[`sparse_add(...)`](./tf/sparse/add): Adds two tensors, at least one of each is a `SparseTensor`. (deprecated arguments)

[`sparse_concat(...)`](./tf/sparse/concat): Concatenates a list of `SparseTensor` along the specified dimension. (deprecated arguments)

[`sparse_fill_empty_rows(...)`](./tf/sparse/fill_empty_rows): Fills empty rows in the input 2-D `SparseTensor` with a default value.

[`sparse_mask(...)`](./tf/sparse/mask): Masks elements of `IndexedSlices`.

[`sparse_matmul(...)`](./tf/sparse_matmul): Multiply matrix "a" by matrix "b".

[`sparse_maximum(...)`](./tf/sparse/maximum): Returns the element-wise max of two SparseTensors.

[`sparse_merge(...)`](./tf/sparse/merge): Combines a batch of feature ids and values into a single `SparseTensor`. (deprecated)

[`sparse_minimum(...)`](./tf/sparse/minimum): Returns the element-wise min of two SparseTensors.

[`sparse_placeholder(...)`](./tf/sparse/placeholder): Inserts a placeholder for a sparse tensor that will be always fed.

[`sparse_reduce_max(...)`](./tf/sparse/reduce_max): Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments) (deprecated arguments)

[`sparse_reduce_max_sparse(...)`](./tf/sparse/reduce_max_sparse): Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

[`sparse_reduce_sum(...)`](./tf/sparse/reduce_sum): Computes the sum of elements across dimensions of a SparseTensor. (deprecated arguments) (deprecated arguments)

[`sparse_reduce_sum_sparse(...)`](./tf/sparse/reduce_sum_sparse): Computes the sum of elements across dimensions of a SparseTensor. (deprecated arguments)

[`sparse_reorder(...)`](./tf/sparse/reorder): Reorders a `SparseTensor` into the canonical, row-major ordering.

[`sparse_reset_shape(...)`](./tf/sparse/reset_shape): Resets the shape of a `SparseTensor` with indices and values unchanged.

[`sparse_reshape(...)`](./tf/sparse/reshape): Reshapes a `SparseTensor` to represent values in a new dense shape.

[`sparse_retain(...)`](./tf/sparse/retain): Retains specified non-empty values within a `SparseTensor`.

[`sparse_segment_mean(...)`](./tf/sparse/segment_mean): Computes the mean along sparse segments of a tensor.

[`sparse_segment_sqrt_n(...)`](./tf/sparse/segment_sqrt_n): Computes the sum along sparse segments of a tensor divided by the sqrt(N).

[`sparse_segment_sum(...)`](./tf/sparse/segment_sum): Computes the sum along sparse segments of a tensor.

[`sparse_slice(...)`](./tf/sparse/slice): Slice a `SparseTensor` based on the `start` and `size.

[`sparse_softmax(...)`](./tf/sparse/softmax): Applies softmax to a batched N-D `SparseTensor`.

[`sparse_split(...)`](./tf/sparse/split): Split a `SparseTensor` into `num_split` tensors along `axis`. (deprecated arguments)

[`sparse_tensor_dense_matmul(...)`](./tf/sparse/sparse_dense_matmul): Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

[`sparse_tensor_to_dense(...)`](./tf/sparse/to_dense): Converts a `SparseTensor` into a dense tensor.

[`sparse_to_dense(...)`](./tf/sparse_to_dense): Converts a sparse representation into a dense tensor. (deprecated)

[`sparse_to_indicator(...)`](./tf/sparse/to_indicator): Converts a `SparseTensor` of ids into a dense bool indicator tensor.

[`sparse_transpose(...)`](./tf/sparse/transpose): Transposes a `SparseTensor`

[`split(...)`](./tf/split): Splits a tensor into sub tensors.

[`sqrt(...)`](./tf/math/sqrt): Computes square root of x element-wise.

[`square(...)`](./tf/math/square): Computes square of x element-wise.

[`squared_difference(...)`](./tf/math/squared_difference): Returns (x - y)(x - y) element-wise.

[`squeeze(...)`](./tf/squeeze): Removes dimensions of size 1 from the shape of a tensor. (deprecated arguments)

[`stack(...)`](./tf/stack): Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor.

[`stop_gradient(...)`](./tf/stop_gradient): Stops gradient computation.

[`strided_slice(...)`](./tf/strided_slice): Extracts a strided slice of a tensor (generalized python array indexing).

[`string_join(...)`](./tf/strings/join): Joins the strings in the given list of string tensors into one tensor;

[`string_split(...)`](./tf/string_split): Split elements of `source` based on `delimiter`. (deprecated arguments)

[`string_strip(...)`](./tf/strings/strip): Strip leading and trailing whitespaces from the Tensor.

[`string_to_hash_bucket(...)`](./tf/strings/to_hash_bucket): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_hash_bucket_fast(...)`](./tf/strings/to_hash_bucket_fast): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_hash_bucket_strong(...)`](./tf/strings/to_hash_bucket_strong): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`string_to_number(...)`](./tf/strings/to_number): Converts each string in the input Tensor to the specified numeric type.

[`substr(...)`](./tf/substr): Return substrings from `Tensor` of strings.

[`subtract(...)`](./tf/math/subtract): Returns x - y element-wise.

[`svd(...)`](./tf/linalg/svd): Computes the singular value decompositions of one or more matrices.

[`switch_case(...)`](./tf/switch_case): Create a switch/case operation, i.e. an integer-indexed conditional.

[`tables_initializer(...)`](./tf/initializers/tables_initializer): Returns an Op that initializes all tables of the default graph.

[`tan(...)`](./tf/math/tan): Computes tan of x element-wise.

[`tanh(...)`](./tf/math/tanh): Computes hyperbolic tangent of `x` element-wise.

[`tensor_scatter_add(...)`](./tf/tensor_scatter_nd_add): Adds sparse `updates` to an existing tensor according to `indices`.

[`tensor_scatter_nd_add(...)`](./tf/tensor_scatter_nd_add): Adds sparse `updates` to an existing tensor according to `indices`.

[`tensor_scatter_nd_sub(...)`](./tf/tensor_scatter_nd_sub): Subtracts sparse `updates` from an existing tensor according to `indices`.

[`tensor_scatter_nd_update(...)`](./tf/tensor_scatter_nd_update): Scatter `updates` into an existing tensor according to `indices`.

[`tensor_scatter_sub(...)`](./tf/tensor_scatter_nd_sub): Subtracts sparse `updates` from an existing tensor according to `indices`.

[`tensor_scatter_update(...)`](./tf/tensor_scatter_nd_update): Scatter `updates` into an existing tensor according to `indices`.

[`tensordot(...)`](./tf/tensordot): Tensor contraction of a and b along specified axes and outer product.

[`tile(...)`](./tf/tile): Constructs a tensor by tiling a given tensor.

[`timestamp(...)`](./tf/timestamp): Provides the time since epoch in seconds.

[`to_bfloat16(...)`](./tf/to_bfloat16): Casts a tensor to type `bfloat16`. (deprecated)

[`to_complex128(...)`](./tf/to_complex128): Casts a tensor to type `complex128`. (deprecated)

[`to_complex64(...)`](./tf/to_complex64): Casts a tensor to type `complex64`. (deprecated)

[`to_double(...)`](./tf/to_double): Casts a tensor to type `float64`. (deprecated)

[`to_float(...)`](./tf/to_float): Casts a tensor to type `float32`. (deprecated)

[`to_int32(...)`](./tf/to_int32): Casts a tensor to type `int32`. (deprecated)

[`to_int64(...)`](./tf/to_int64): Casts a tensor to type `int64`. (deprecated)

[`trace(...)`](./tf/linalg/trace): Compute the trace of a tensor `x`.

[`trainable_variables(...)`](./tf/trainable_variables): Returns all variables created with `trainable=True`.

[`transpose(...)`](./tf/transpose): Transposes `a`.

[`truediv(...)`](./tf/math/truediv): Divides x / y elementwise (using Python 3 division operator semantics).

[`truncated_normal(...)`](./tf/random/truncated_normal): Outputs random values from a truncated normal distribution.

[`truncatediv(...)`](./tf/truncatediv): Returns x / y element-wise for integer types.

[`truncatemod(...)`](./tf/truncatemod): Returns element-wise remainder of division. This emulates C semantics in that

[`tuple(...)`](./tf/tuple): Group tensors together.

[`unique(...)`](./tf/unique): Finds unique elements in a 1-D tensor.

[`unique_with_counts(...)`](./tf/unique_with_counts): Finds unique elements in a 1-D tensor.

[`unravel_index(...)`](./tf/unravel_index): Converts an array of flat indices into a tuple of coordinate arrays.

[`unsorted_segment_max(...)`](./tf/math/unsorted_segment_max): Computes the maximum along segments of a tensor.

[`unsorted_segment_mean(...)`](./tf/math/unsorted_segment_mean): Computes the mean along segments of a tensor.

[`unsorted_segment_min(...)`](./tf/math/unsorted_segment_min): Computes the minimum along segments of a tensor.

[`unsorted_segment_prod(...)`](./tf/math/unsorted_segment_prod): Computes the product along segments of a tensor.

[`unsorted_segment_sqrt_n(...)`](./tf/math/unsorted_segment_sqrt_n): Computes the sum along segments of a tensor divided by the sqrt(N).

[`unsorted_segment_sum(...)`](./tf/math/unsorted_segment_sum): Computes the sum along segments of a tensor.

[`unstack(...)`](./tf/unstack): Unpacks the given dimension of a rank-`R` tensor into rank-`(R-1)` tensors.

[`variable_axis_size_partitioner(...)`](./tf/variable_axis_size_partitioner): Get a partitioner for VariableScope to keep shards below `max_shard_bytes`.

[`variable_creator_scope(...)`](./tf/variable_creator_scope): Scope which defines a variable creation function to be used by variable().

[`variable_op_scope(...)`](./tf/variable_op_scope): Deprecated: context manager for defining an op that creates variables.

[`variables_initializer(...)`](./tf/initializers/variables): Returns an Op that initializes a list of variables.

[`vectorized_map(...)`](./tf/vectorized_map): Parallel map on the list of tensors unpacked from `elems` on dimension 0.

[`verify_tensor_all_finite(...)`](./tf/debugging/assert_all_finite): Assert that the tensor does not contain any NaN's or Inf's.

[`where(...)`](./tf/where): Return the elements, either from `x` or `y`, depending on the `condition`. (deprecated)

[`where_v2(...)`](./tf/where_v2): Return the elements, either from `x` or `y`, depending on the `condition`.

[`while_loop(...)`](./tf/while_loop): Repeat `body` while the condition `cond` is true.

[`wrap_function(...)`](./tf/wrap_function): Wraps the TF 1.x function fn into a graph function.

[`write_file(...)`](./tf/io/write_file): Writes contents to the file at input filename. Creates file and recursively

[`zeros(...)`](./tf/zeros): Creates a tensor with all elements set to zero.

[`zeros_like(...)`](./tf/zeros_like): Creates a tensor with all elements set to zero.

[`zeta(...)`](./tf/math/zeta): Compute the Hurwitz zeta function \\(\zeta(x, q)\\).

## Other Members

* `AUTO_REUSE` <a id="AUTO_REUSE"></a>
* `COMPILER_VERSION = '7.3.1 20180303'` <a id="COMPILER_VERSION"></a>
* `CXX11_ABI_FLAG = 0` <a id="CXX11_ABI_FLAG"></a>
* `GIT_VERSION = 'v1.15.0-rc3-22-g590d6ee'` <a id="GIT_VERSION"></a>
* `GRAPH_DEF_VERSION = 134` <a id="GRAPH_DEF_VERSION"></a>
* `GRAPH_DEF_VERSION_MIN_CONSUMER = 0` <a id="GRAPH_DEF_VERSION_MIN_CONSUMER"></a>
* `GRAPH_DEF_VERSION_MIN_PRODUCER = 0` <a id="GRAPH_DEF_VERSION_MIN_PRODUCER"></a>
* `MONOLITHIC_BUILD = 0` <a id="MONOLITHIC_BUILD"></a>
* `QUANTIZED_DTYPES` <a id="QUANTIZED_DTYPES"></a>
* `VERSION = '1.15.0'` <a id="VERSION"></a>
* `__version__ = '1.15.0'` <a id="__version__"></a>
* `bfloat16` <a id="bfloat16"></a>
* `bool` <a id="bool"></a>
* `complex128` <a id="complex128"></a>
* `complex64` <a id="complex64"></a>
* `double` <a id="double"></a>
* `float16` <a id="float16"></a>
* `float32` <a id="float32"></a>
* `float64` <a id="float64"></a>
* `half` <a id="half"></a>
* `int16` <a id="int16"></a>
* `int32` <a id="int32"></a>
* `int64` <a id="int64"></a>
* `int8` <a id="int8"></a>
* `qint16` <a id="qint16"></a>
* `qint32` <a id="qint32"></a>
* `qint8` <a id="qint8"></a>
* `quint16` <a id="quint16"></a>
* `quint8` <a id="quint8"></a>
* `resource` <a id="resource"></a>
* `string` <a id="string"></a>
* `uint16` <a id="uint16"></a>
* `uint32` <a id="uint32"></a>
* `uint64` <a id="uint64"></a>
* `uint8` <a id="uint8"></a>
* `variant` <a id="variant"></a>
