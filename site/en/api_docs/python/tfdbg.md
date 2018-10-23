


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tfdbg

### Module `tfdbg`

Public Python API of TensorFlow Debugger (tfdbg).

See the [TensorFlow Debugger](../../api_guides/python/tfdbg) guide.


## Members

[`class DebugDumpDir`](./tfdbg/DebugDumpDir): Data set from a debug-dump directory on filesystem.

[`class DebugTensorDatum`](./tfdbg/DebugTensorDatum): A single tensor dumped by TensorFlow Debugger (tfdbg).

[`class DumpingDebugHook`](./tfdbg/DumpingDebugHook): A debugger hook that dumps debug data to filesystem.

[`class DumpingDebugWrapperSession`](./tfdbg/DumpingDebugWrapperSession): Debug Session wrapper that dumps debug data to filesystem.

[`class LocalCLIDebugHook`](./tfdbg/LocalCLIDebugHook): Command-line-interface debugger hook.

[`class LocalCLIDebugWrapperSession`](./tfdbg/LocalCLIDebugWrapperSession): Concrete subclass of BaseDebugWrapperSession implementing a local CLI.

Constant absolute_import

[`add_debug_tensor_watch(...)`](./tfdbg/add_debug_tensor_watch): Add watch on a `Tensor` to `RunOptions`.

[`cli`](./tfdbg/cli) module

Constant division

[`has_inf_or_nan(...)`](./tfdbg/has_inf_or_nan): A predicate for whether a tensor consists of any bad numerical values.

[`lib`](./tfdbg/lib) module

[`load_tensor_from_event_file(...)`](./tfdbg/load_tensor_from_event_file): Load a tensor from an event file.

Constant print_function

[`watch_graph(...)`](./tfdbg/watch_graph): Add debug watches to `RunOptions` for a TensorFlow graph.

[`watch_graph_with_blacklists(...)`](./tfdbg/watch_graph_with_blacklists): Add debug tensor watches, blacklisting nodes and op types.

[`wrappers`](./tfdbg/wrappers) module

Defined in [`tensorflow/python/debug/__init__.py`](https://www.tensorflow.org/code/tensorflow/python/debug/__init__.py).

