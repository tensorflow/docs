page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.eager



Defined in [`tensorflow/contrib/eager/python/tfe.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/eager/python/tfe.py).

TensorFlow Eager execution prototype.

EXPERIMENTAL: APIs here are unstable and likely to change without notice.

To use, at program startup, call `tfe.enable_eager_execution()`.













## Modules

[`metrics`](../../tf/contrib/eager/metrics) module: Metrics namespace.

## Classes

[`class Checkpoint`](../../tf/train/Checkpoint): Groups checkpointable objects, saving and restoring them.

[`class Checkpointable`](../../tf/contrib/checkpoint/Checkpointable): Manages dependencies on other objects.

[`class CheckpointableSaver`](../../tf/contrib/eager/CheckpointableSaver): Saves and restores a `Checkpointable` object and its dependencies.

[`class EagerVariableStore`](../../tf/contrib/eager/EagerVariableStore): Wrapper allowing functional layers to be used with eager execution.

[`class GradientTape`](../../tf/GradientTape): Record operations for automatic differentiation.

[`class Iterator`](../../tf/contrib/eager/Iterator): An iterator producing tf.Tensor objects from a tf.data.Dataset.

[`class Network`](../../tf/contrib/eager/Network): Represents the composition of a set of Layers.

[`class Saver`](../../tf/contrib/eager/Saver): A tf.train.Saver adapter for use when eager execution is enabled.

[`class Sequential`](../../tf/contrib/eager/Sequential): Represents a linear sequence of Layers or functions.

[`class Variable`](../../tf/contrib/eager/Variable): Variable based on resource handles.

## Functions

[`add_execution_callback(...)`](../../tf/contrib/eager/add_execution_callback): Add an execution callback to the default eager context.

[`async_clear_error(...)`](../../tf/contrib/eager/async_clear_error): Clears errors raised during ASYNC execution mode.

[`async_wait(...)`](../../tf/contrib/eager/async_wait): Waits for ops dispatched in ASYNC mode to finish.

[`clear_execution_callbacks(...)`](../../tf/contrib/eager/clear_execution_callbacks): Clear all execution callbacks from the default eager context.

[`custom_gradient(...)`](../../tf/custom_gradient): Decorator to define a function with a custom gradient.

[`defun(...)`](../../tf/contrib/eager/defun): Compiles a Python function into a callable TensorFlow graph.

[`enable_eager_execution(...)`](../../tf/enable_eager_execution): Enables eager execution for the lifetime of this program.

[`executing_eagerly(...)`](../../tf/executing_eagerly): Returns True if the current thread has eager execution enabled.

[`execution_mode(...)`](../../tf/contrib/eager/execution_mode): Context manager for setting execution mode for current thread.

[`get_optimizer_variables(...)`](../../tf/contrib/eager/get_optimizer_variables): Returns a list of variables for the given <a href="../../tf/train/Optimizer"><code>tf.train.Optimizer</code></a>.

[`gradients_function(...)`](../../tf/contrib/eager/gradients_function): Returns a function which differentiates f with respect to params.

[`implicit_gradients(...)`](../../tf/contrib/eager/implicit_gradients): Returns a function which differentiates f with respect to variables.

[`implicit_value_and_gradients(...)`](../../tf/contrib/eager/implicit_value_and_gradients): Returns a function which differentiates f with respect to variables.

[`in_eager_mode(...)`](../../tf/executing_eagerly): Returns True if the current thread has eager execution enabled.

[`inf_callback(...)`](../../tf/contrib/eager/inf_callback): A specialization of `inf_nan_callback` that checks for `inf`s only.

[`inf_nan_callback(...)`](../../tf/contrib/eager/inf_nan_callback): An execution callback that checks for `inf`s and `nan`s in output tensors.

[`list_devices(...)`](../../tf/contrib/eager/list_devices): List the names of the available devices.

[`make_template(...)`](../../tf/contrib/eager/make_template): Make a template, optionally compiling func_ into a graph function.

[`nan_callback(...)`](../../tf/contrib/eager/nan_callback): A specialization of `inf_nan_callback` that checks for `nan`s only.

[`num_gpus(...)`](../../tf/contrib/eager/num_gpus): Get the number of available GPU devices.

[`py_func(...)`](../../tf/contrib/eager/py_func): Wraps a python function into a TensorFlow op that executes it eagerly.

[`restore_network_checkpoint(...)`](../../tf/contrib/eager/restore_network_checkpoint): Restore the Network from a checkpoint. (deprecated)

[`restore_variables_on_create(...)`](../../tf/contrib/eager/restore_variables_on_create): ContextManager that restores variables on creation.

[`run(...)`](../../tf/contrib/eager/run): Runs the program with an optional main function and argv list.

[`run_all_tests_in_graph_and_eager_modes(...)`](../../tf/contrib/eager/run_all_tests_in_graph_and_eager_modes): Execute all test methods in the given class with and without eager.

[`run_test_in_graph_and_eager_modes(...)`](../../tf/contrib/eager/run_test_in_graph_and_eager_modes): Execute the decorated test with and without enabling eager execution.

[`save_network_checkpoint(...)`](../../tf/contrib/eager/save_network_checkpoint): Save variables from the Network to a checkpoint. (deprecated)

[`set_execution_mode(...)`](../../tf/contrib/eager/set_execution_mode): Sets execution mode for the current thread.

[`seterr(...)`](../../tf/contrib/eager/seterr): Set how abnormal conditions are handled by the default eager context.

[`value_and_gradients_function(...)`](../../tf/contrib/eager/value_and_gradients_function): Returns a function that computes f and its derivative w.r.t. params.

## Other Members

`ASYNC`

`DEVICE_PLACEMENT_EXPLICIT`

`DEVICE_PLACEMENT_SILENT`

`DEVICE_PLACEMENT_WARN`

`SYNC`

