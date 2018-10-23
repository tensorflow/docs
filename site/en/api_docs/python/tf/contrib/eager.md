

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.eager



Defined in [`tensorflow/contrib/eager/python/tfe.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/eager/python/tfe.py).

TensorFlow Eager execution prototype.

EXPERIMENTAL: APIs here are unstable and likely to change without notice.

To use, at program startup, call `tfe.enable_eager_execution()`.












## Modules

[`metrics`](../../tf/contrib/eager/metrics) module: Metrics namespace.

## Classes

[`class EagerVariableStore`](../../tf/contrib/eager/EagerVariableStore): Wrapper allowing functional layers to be used with eager execution.

[`class GradientTape`](../../tf/contrib/eager/GradientTape): Records operations to use to compute gradients.

[`class IsolateTest`](../../tf/contrib/eager/IsolateTest): A context manager which isolates resources in its block.

[`class Iterator`](../../tf/contrib/eager/Iterator): An iterator producing tf.Tensor objects from a tf.data.Dataset.

[`class Network`](../../tf/contrib/eager/Network): Represents the composition of a set of Layers.

[`class Saver`](../../tf/contrib/eager/Saver): A tf.train.Saver adapter for use when eager execution is enabled.

[`class Sequential`](../../tf/contrib/eager/Sequential): Represents a linear sequence of Layers or functions.

[`class Variable`](../../tf/contrib/eager/Variable): Variable based on resource handles.

## Functions

[`add_execution_callback(...)`](../../tf/contrib/eager/add_execution_callback): Add an execution callback to the default eager context.

[`clear_execution_callbacks(...)`](../../tf/contrib/eager/clear_execution_callbacks): Clear all execution callbacks from the default eager context.

[`custom_gradient(...)`](../../tf/contrib/eager/custom_gradient): Decorator to define a function with a custom gradient.

[`defun(...)`](../../tf/contrib/eager/defun): Decorator to compile func into graph_mode.

[`enable_eager_execution(...)`](../../tf/contrib/eager/enable_eager_execution): Enables, for the rest of the lifetime of this program, eager execution.

[`get_optimizer_variables(...)`](../../tf/contrib/eager/get_optimizer_variables): Returns a list of variables for the given `tf.train.Optimizer`.

[`gradients_function(...)`](../../tf/contrib/eager/gradients_function): Returns a function which differentiates f with respect to params.

[`implicit_gradients(...)`](../../tf/contrib/eager/implicit_gradients): Returns a function which differentiates f with respect to variables.

[`implicit_value_and_gradients(...)`](../../tf/contrib/eager/implicit_value_and_gradients): Returns a function which differentiates f with respect to variables.

[`in_eager_mode(...)`](../../tf/contrib/eager/in_eager_mode): Returns True if current thread is in EAGER mode for default context.

[`in_graph_mode(...)`](../../tf/contrib/eager/in_graph_mode): Returns True if current thread is in GRAPH mode for default context.

[`inf_callback(...)`](../../tf/contrib/eager/inf_callback): A specialization of `inf_nan_callback` that checks for `inf`s only.

[`inf_nan_callback(...)`](../../tf/contrib/eager/inf_nan_callback): An execution callback that checks for `inf`s and `nan`s in output tensors.

[`list_devices(...)`](../../tf/contrib/eager/list_devices): List the names of the available devices.

[`make_template(...)`](../../tf/contrib/eager/make_template): Make a template, optionally compiling func_ into a graph function.

[`nan_callback(...)`](../../tf/contrib/eager/nan_callback): A specialization of `inf_nan_callback` that checks for `nan`s only.

[`num_gpus(...)`](../../tf/contrib/eager/num_gpus): Get the number of available GPU devices.

[`py_func(...)`](../../tf/contrib/eager/py_func): Wraps a python function into a TensorFlow op.

[`restore_network_checkpoint(...)`](../../tf/contrib/eager/restore_network_checkpoint): Restore the Network from a checkpoint.

[`restore_variables_on_create(...)`](../../tf/contrib/eager/restore_variables_on_create): ContextManager that restores variables on creation.

[`run(...)`](../../tf/contrib/eager/run): Runs the program with an optional main function and argv list.

[`run_test_in_graph_and_eager_modes(...)`](../../tf/contrib/eager/run_test_in_graph_and_eager_modes): Runs the test in both graph and eager modes.

[`save_network_checkpoint(...)`](../../tf/contrib/eager/save_network_checkpoint): Save variables from the Network to a checkpoint.

[`seterr(...)`](../../tf/contrib/eager/seterr): Set how abnormal conditions are handled by the default eager context.

[`value_and_gradients_function(...)`](../../tf/contrib/eager/value_and_gradients_function): Returns a function that computes f and its derivative w.r.t. params.

## Other Members

`DEVICE_PLACEMENT_EXPLICIT`

`DEVICE_PLACEMENT_SILENT`

`DEVICE_PLACEMENT_WARN`

