page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.eager

TensorFlow Eager execution prototype.



Defined in [`contrib/eager/python/tfe.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/eager/python/tfe.py).

<!-- Placeholder for "Used in" -->

EXPERIMENTAL: APIs here are unstable and likely to change without notice.

To use, at program startup, call <a href="../../tf/enable_eager_execution"><code>tf.compat.v1.enable_eager_execution()</code></a>.















## Modules

[`metrics`](../../tf/contrib/eager/metrics) module: Metrics namespace.

## Classes

[`class Checkpoint`](../../tf/train/Checkpoint): Groups trackable objects, saving and restoring them.

[`class Checkpointable`](../../tf/contrib/checkpoint/Checkpointable): Manages dependencies on other objects.

[`class EagerVariableStore`](../../tf/contrib/eager/EagerVariableStore): Wrapper allowing functional layers to be used with eager execution.

[`class ExecutionCallback`](../../tf/contrib/eager/ExecutionCallback): Valid callback actions.

[`class GradientTape`](../../tf/GradientTape): Record operations for automatic differentiation.

[`class Iterator`](../../tf/contrib/eager/Iterator): An iterator producing tf.Tensor objects from a tf.data.Dataset.

[`class Network`](../../tf/contrib/eager/Network): Represents the composition of a set of Layers.

[`class Saver`](../../tf/contrib/eager/Saver): A tf.compat.v1.train.Saver adapter for use when eager execution is enabled.

[`class Sequential`](../../tf/contrib/eager/Sequential): Represents a linear sequence of Layers or functions.

[`class TensorSpec`](../../tf/TensorSpec): Describes a tf.Tensor.

[`class Variable`](../../tf/contrib/eager/Variable): Variable based on resource handles.

## Functions

[`add_execution_callback(...)`](../../tf/contrib/eager/add_execution_callback): Add an execution callback to the default eager context.

[`async_clear_error(...)`](../../tf/contrib/eager/async_clear_error): Clears errors raised during ASYNC execution mode.

[`async_wait(...)`](../../tf/contrib/eager/async_wait): Waits for ops dispatched in ASYNC mode to finish.

[`clear_execution_callbacks(...)`](../../tf/contrib/eager/clear_execution_callbacks): Clear all execution callbacks from the default eager context.

[`connect_to_remote_host(...)`](../../tf/config/experimental_connect_to_host): Connects to a single machine to enable remote execution on it.

[`custom_gradient(...)`](../../tf/custom_gradient): Decorator to define a function with a custom gradient.

[`defun(...)`](../../tf/contrib/eager/defun): Compiles a Python function into a callable TensorFlow graph.

[`enable_eager_execution(...)`](../../tf/enable_eager_execution): Enables eager execution for the lifetime of this program.

[`enable_remote_eager_execution(...)`](../../tf/contrib/eager/enable_remote_eager_execution): Enables eager execution for the lifetime of this program.

[`errstate(...)`](../../tf/contrib/eager/errstate): Context manager setting error state.

[`executing_eagerly(...)`](../../tf/executing_eagerly): Returns True if the current thread has eager execution enabled.

[`execution_mode(...)`](../../tf/contrib/eager/execution_mode): Context manager for setting execution mode for current thread.

[`function(...)`](../../tf/function): Creates a callable TensorFlow graph from a Python function.

[`get_optimizer_variables(...)`](../../tf/contrib/eager/get_optimizer_variables): Returns a list of variables for the given <a href="../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>.

[`gradients_function(...)`](../../tf/contrib/eager/gradients_function): Returns a function which differentiates f with respect to params.

[`implicit_gradients(...)`](../../tf/contrib/eager/implicit_gradients): Returns a function which differentiates f with respect to variables.

[`implicit_value_and_gradients(...)`](../../tf/contrib/eager/implicit_value_and_gradients): Returns a function which differentiates f with respect to variables.

[`in_eager_mode(...)`](../../tf/executing_eagerly): Returns True if the current thread has eager execution enabled.

[`inf_callback(...)`](../../tf/contrib/eager/inf_callback): A specialization of `inf_nan_callback` that checks for `inf`s only.

[`inf_nan_callback(...)`](../../tf/contrib/eager/inf_nan_callback): An execution callback that checks for `inf`s and `nan`s in output tensors.

[`list_devices(...)`](../../tf/config/experimental_list_devices): List the names of the available devices.

[`make_template(...)`](../../tf/contrib/eager/make_template): Make a template, optionally compiling func_ into a graph function.

[`nan_callback(...)`](../../tf/contrib/eager/nan_callback): A specialization of `inf_nan_callback` that checks for `nan`s only.

[`num_gpus(...)`](../../tf/contrib/eager/num_gpus): Get the number of available GPU devices.

[`py_func(...)`](../../tf/py_function): Wraps a python function into a TensorFlow op that executes it eagerly.

[`restore_network_checkpoint(...)`](../../tf/contrib/eager/restore_network_checkpoint): Restore the Network from a checkpoint. (deprecated)

[`restore_variables_on_create(...)`](../../tf/contrib/eager/restore_variables_on_create): ContextManager that restores variables on creation.

[`run(...)`](../../tf/contrib/eager/run): Runs the program with an optional main function and argv list.

[`run_all_tests_in_graph_and_eager_modes(...)`](../../tf/contrib/eager/run_all_tests_in_graph_and_eager_modes): Execute all test methods in the given class with and without eager.

[`run_test_in_graph_and_eager_modes(...)`](../../tf/contrib/eager/run_test_in_graph_and_eager_modes): Execute the decorated test with and without enabling eager execution.

[`save_network_checkpoint(...)`](../../tf/contrib/eager/save_network_checkpoint): Save variables from the Network to a checkpoint. (deprecated)

[`set_execution_mode(...)`](../../tf/contrib/eager/set_execution_mode): Sets execution mode for the current thread.

[`set_server_def(...)`](../../tf/contrib/eager/set_server_def)

[`seterr(...)`](../../tf/contrib/eager/seterr): Set how abnormal conditions are handled by the default eager context.

[`value_and_gradients_function(...)`](../../tf/contrib/eager/value_and_gradients_function): Returns a function that computes f and its derivative w.r.t. params.

## Other Members

* `ASYNC = 1` <a id="ASYNC"></a>
* `DEVICE_PLACEMENT_EXPLICIT = 0` <a id="DEVICE_PLACEMENT_EXPLICIT"></a>
* `DEVICE_PLACEMENT_SILENT = 2` <a id="DEVICE_PLACEMENT_SILENT"></a>
* `DEVICE_PLACEMENT_WARN = 1` <a id="DEVICE_PLACEMENT_WARN"></a>
* `SYNC = 0` <a id="SYNC"></a>
