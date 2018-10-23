

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.DebugDumpDir

## Class `DebugDumpDir`





Defined in [`tensorflow/python/debug/lib/debug_data.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/debug/lib/debug_data.py).

See the guide: [TensorFlow Debugger > Classes for debug-dump data and directories](../../../api_guides/python/tfdbg#Classes_for_debug_dump_data_and_directories)

Data set from a debug-dump directory on filesystem.

An instance of `DebugDumpDir` contains all `DebugTensorDatum` instances
in a tfdbg dump root directory.

## Properties

<h3 id="core_metadata"><code>core_metadata</code></h3>

Metadata about the `Session.run()` call from the core runtime.

Of the three counters available in the return value, `global_step` is
supplied by the caller of the debugged `Session.run()`, while
`session_run_index` and `executor_step_index` are determined by the state
of the core runtime, automatically. For the same fetch list, feed keys and
debug tensor watch options, the same executor will be used and
`executor_step_index` should increase by one at a time. However, runs with
different fetch lists, feed keys and debug_tensor watch options that all
share the same `Session` object can lead to gaps in `session_run_index`.

#### Returns:

If core metadata are loaded, a `namedtuple` with the fields:
  `global_step`: A global step count supplied by the caller of
    `Session.run()`. It is optional to the caller. If the caller did not
    supply this parameter, its value will be -1.
  `session_run_index`: A sorted index for Run() calls to the underlying
    TensorFlow `Session` object.
  `executor_step_index`: A counter for invocations of a given runtime
    executor. The same executor is re-used for the same fetched tensors,
    target nodes, input feed keys and debug tensor watch options.
  `input_names`: Names of the input (feed) Tensors.
  `output_names`: Names of the output (fetched) Tensors.
  `target_nodes`: Names of the target nodes.
If the core metadata have not been loaded, `None`.
If more than one core metadata files exist, return a list of the
  `nametuple` described above.

<h3 id="dumped_tensor_data"><code>dumped_tensor_data</code></h3>

Retrieve dumped tensor data.

<h3 id="python_graph"><code>python_graph</code></h3>

Get the Python graph.

#### Returns:

If the Python graph has been set, returns a <a href="../tf/Graph"><code>tf.Graph</code></a> object. Otherwise,
returns None.

<h3 id="run_feed_keys_info"><code>run_feed_keys_info</code></h3>

Get a str representation of the feed_dict used in the Session.run() call.

#### Returns:

If the information is available from one `Session.run` call, a `str`
  obtained from `repr(feed_dict)`.
If the information is available from multiple `Session.run` calls, a
  `list` of `str` obtained from `repr(feed_dict)`.
If the information is not available, `None`.

<h3 id="run_fetches_info"><code>run_fetches_info</code></h3>

Get a str representation of the fetches used in the Session.run() call.

#### Returns:

If the information is available from one `Session.run` call, a `str`
  obtained from `repr(fetches)`.
If the information is available from multiple `Session.run` calls, a
  `list` of `str` from `repr(fetches)`.
If the information is not available, `None`.

<h3 id="size"><code>size</code></h3>

Total number of dumped tensors in the dump root directory.

#### Returns:

(`int`) The total number of dumped tensors in the dump root directory.

<h3 id="t0"><code>t0</code></h3>

Absolute timestamp of the first dumped tensor across all devices.

#### Returns:

(`int`) absolute timestamp of the first dumped tensor, in microseconds.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    dump_root,
    partition_graphs=None,
    validate=True
)
```

`DebugDumpDir` constructor.

#### Args:

* <b>`dump_root`</b>: (`str`) path to the dump root directory.
* <b>`partition_graphs`</b>: A repeated field of GraphDefs representing the
      partition graphs executed by the TensorFlow runtime.
* <b>`validate`</b>: (`bool`) whether the dump files are to be validated against the
      partition graphs.


#### Raises:

* <b>`IOError`</b>: If dump_root does not exist as a directory.
* <b>`ValueError`</b>: If more than one core metadata file is found under the dump
    root directory.

<h3 id="debug_watch_keys"><code>debug_watch_keys</code></h3>

``` python
debug_watch_keys(
    node_name,
    device_name=None
)
```

Get all tensor watch keys of given node according to partition graphs.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    node_name exists on only one device, this argument is optional.


#### Returns:

(`list` of `str`) all debug tensor watch keys. Returns an empty list if
  the node name does not correspond to any debug watch keys.


#### Raises:

`LookupError`: If debug watch information has not been loaded from
  partition graphs yet.

<h3 id="devices"><code>devices</code></h3>

``` python
devices()
```

Get the list of device names.

#### Returns:

(`list` of `str`) names of the devices.

<h3 id="find"><code>find</code></h3>

``` python
find(
    predicate,
    first_n=0,
    device_name=None,
    exclude_node_names=None
)
```

Find dumped tensor data by a certain predicate.

#### Args:

* <b>`predicate`</b>: A callable that takes two input arguments:

    ```python
    def predicate(debug_tensor_datum, tensor):
      # returns a bool
    ```

    where `debug_tensor_datum` is an instance of `DebugTensorDatum`, which
    carries the metadata, such as the `Tensor`'s node name, output slot
    timestamp, debug op name, etc.; and `tensor` is the dumped tensor value
    as a `numpy.ndarray`.
* <b>`first_n`</b>: (`int`) return only the first n `DebugTensotDatum` instances (in
    time order) for which the predicate returns True. To return all the
    `DebugTensotDatum` instances, let first_n be <= 0.
* <b>`device_name`</b>: optional device name.
* <b>`exclude_node_names`</b>: Optional regular expression to exclude nodes with
    names matching the regular expression.


#### Returns:

A list of all `DebugTensorDatum` objects in this `DebugDumpDir` object
 for which predicate returns True, sorted in ascending order of the
 timestamp.

<h3 id="find_some_path"><code>find_some_path</code></h3>

``` python
find_some_path(
    src_node_name,
    dst_node_name,
    include_control=True,
    include_reversed_ref=False,
    device_name=None
)
```

Find a path between a source node and a destination node.

Limitation: the source and destination are required to be on the same
device, i.e., this method does not yet take into account Send/Recv nodes
across devices.

TODO(cais): Make this method work across device edges by tracing Send/Recv
  nodes.

#### Args:

* <b>`src_node_name`</b>: (`str`) name of the source node or name of an output tensor
    of the node.
* <b>`dst_node_name`</b>: (`str`) name of the destination node or name of an output
    tensor of the node.
* <b>`include_control`</b>: (`bool`) whrther control edges are considered in the
    graph tracing.
* <b>`include_reversed_ref`</b>: Whether a ref input, say from A to B, is to be also
    considered as an input from B to A. The rationale is that ref inputs
    generally let the recipient (e.g., B in this case) mutate the value of
    the source (e.g., A in this case). So the reverse direction of the ref
    edge reflects the direction of information flow.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    node_name exists on only one device, this argument is optional.


#### Returns:

A path from the src_node_name to dst_node_name, as a `list` of `str`, if
it exists. The list includes src_node_name as the first item and
dst_node_name as the last.
If such a path does not exist, `None`.


#### Raises:

* <b>`ValueError`</b>: If the source and destination nodes are not on the same
    device.

<h3 id="get_dump_sizes_bytes"><code>get_dump_sizes_bytes</code></h3>

``` python
get_dump_sizes_bytes(
    node_name,
    output_slot,
    debug_op,
    device_name=None
)
```

Get the sizes of the dump files for a debug-dumped tensor.

Unit of the file size: byte.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node that the tensor is produced by.
* <b>`output_slot`</b>: (`int`) output slot index of tensor.
* <b>`debug_op`</b>: (`str`) name of the debug op.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    the specified debug_watch_key exists on only one device, this argument
    is optional.


#### Returns:

(`list` of `int`): list of dump file sizes in bytes.


#### Raises:

* <b>`WatchKeyDoesNotExistInDebugDumpDirError`</b>: If the tensor watch key does not
    exist in the debug dump data.

<h3 id="get_rel_timestamps"><code>get_rel_timestamps</code></h3>

``` python
get_rel_timestamps(
    node_name,
    output_slot,
    debug_op,
    device_name=None
)
```

Get the relative timestamp from for a debug-dumped tensor.

Relative timestamp means (absolute timestamp - `t0`), where `t0` is the
absolute timestamp of the first dumped tensor in the dump root. The tensor
may be dumped multiple times in the dump root directory, so a list of
relative timestamps (`numpy.ndarray`) is returned.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node that the tensor is produced by.
* <b>`output_slot`</b>: (`int`) output slot index of tensor.
* <b>`debug_op`</b>: (`str`) name of the debug op.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    the specified debug_watch_key exists on only one device, this argument
    is optional.


#### Returns:

(`list` of `int`) list of relative timestamps.


#### Raises:

* <b>`WatchKeyDoesNotExistInDebugDumpDirError`</b>: If the tensor watch key does not
    exist in the debug dump data.

<h3 id="get_tensor_file_paths"><code>get_tensor_file_paths</code></h3>

``` python
get_tensor_file_paths(
    node_name,
    output_slot,
    debug_op,
    device_name=None
)
```

Get the file paths from a debug-dumped tensor.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node that the tensor is produced by.
* <b>`output_slot`</b>: (`int`) output slot index of tensor.
* <b>`debug_op`</b>: (`str`) name of the debug op.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    the specified debug_watch_key exists on only one device, this argument
    is optional.


#### Returns:

List of file path(s) loaded. This is a list because each debugged tensor
  may be dumped multiple times.


#### Raises:

* <b>`WatchKeyDoesNotExistInDebugDumpDirError`</b>: If the tensor does not exist in
    the debug-dump data.

<h3 id="get_tensors"><code>get_tensors</code></h3>

``` python
get_tensors(
    node_name,
    output_slot,
    debug_op,
    device_name=None
)
```

Get the tensor value from for a debug-dumped tensor.

The tensor may be dumped multiple times in the dump root directory, so a
list of tensors (`numpy.ndarray`) is returned.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node that the tensor is produced by.
* <b>`output_slot`</b>: (`int`) output slot index of tensor.
* <b>`debug_op`</b>: (`str`) name of the debug op.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    the specified debug_watch_key exists on only one device, this argument
    is optional.


#### Returns:

List of tensors (`numpy.ndarray`) loaded from the debug-dump file(s).


#### Raises:

* <b>`WatchKeyDoesNotExistInDebugDumpDirError`</b>: If the tensor does not exist in
    the debug-dump data.

<h3 id="loaded_partition_graphs"><code>loaded_partition_graphs</code></h3>

``` python
loaded_partition_graphs()
```

Test whether partition graphs have been loaded.

<h3 id="node_attributes"><code>node_attributes</code></h3>

``` python
node_attributes(
    node_name,
    device_name=None
)
```

Get the attributes of a node.

#### Args:

* <b>`node_name`</b>: Name of the node in question.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    node_name exists on only one device, this argument is optional.


#### Returns:

Attributes of the node.


#### Raises:

* <b>`LookupError`</b>: If no partition graphs have been loaded.

<h3 id="node_device"><code>node_device</code></h3>

``` python
node_device(node_name)
```

Get the names of the devices that has nodes of the specified name.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node.


#### Returns:

(`str` or `list` of `str`) name of the device(s) on which the node of the
  given name is found. Returns a `str` if there is only one such device,
  otherwise return a `list` of `str`.


#### Raises:

* <b>`LookupError`</b>: If node inputs and control inputs have not been loaded
     from partition graphs yet.
* <b>`ValueError`</b>: If the node does not exist in partition graphs.

<h3 id="node_exists"><code>node_exists</code></h3>

``` python
node_exists(
    node_name,
    device_name=None
)
```

Test if a node exists in the partition graphs.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node to be checked.
* <b>`device_name`</b>: optional device name. If None, will search for the node
    on all available devices. Otherwise, search for the node only on
    the given device.


#### Returns:

A boolean indicating whether the node exists.


#### Raises:

* <b>`LookupError`</b>: If no partition graphs have been loaded yet.
* <b>`ValueError`</b>: If device_name is specified but cannot be found.

<h3 id="node_inputs"><code>node_inputs</code></h3>

``` python
node_inputs(
    node_name,
    is_control=False,
    device_name=None
)
```

Get the inputs of given node according to partition graphs.

#### Args:

* <b>`node_name`</b>: Name of the node.
* <b>`is_control`</b>: (`bool`) Whether control inputs, rather than non-control
    inputs, are to be returned.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    node_name exists on only one device, this argument is optional.


#### Returns:

(`list` of `str`) inputs to the node, as a list of node names.


#### Raises:

* <b>`LookupError`</b>: If node inputs and control inputs have not been loaded
     from partition graphs yet.

<h3 id="node_op_type"><code>node_op_type</code></h3>

``` python
node_op_type(
    node_name,
    device_name=None
)
```

Get the op type of given node.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    node_name exists on only one device, this argument is optional.


#### Returns:

(`str`) op type of the node.


#### Raises:

* <b>`LookupError`</b>: If node op types have not been loaded
     from partition graphs yet.

<h3 id="node_recipients"><code>node_recipients</code></h3>

``` python
node_recipients(
    node_name,
    is_control=False,
    device_name=None
)
```

Get recipient of the given node's output according to partition graphs.

#### Args:

* <b>`node_name`</b>: (`str`) name of the node.
* <b>`is_control`</b>: (`bool`) whether control outputs, rather than non-control
    outputs, are to be returned.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    node_name exists on only one device, this argument is optional.


#### Returns:

(`list` of `str`) all inputs to the node, as a list of node names.


#### Raises:

* <b>`LookupError`</b>: If node inputs and control inputs have not been loaded
     from partition graphs yet.

<h3 id="node_traceback"><code>node_traceback</code></h3>

``` python
node_traceback(element_name)
```

Try to retrieve the Python traceback of node's construction.

#### Args:

* <b>`element_name`</b>: (`str`) Name of a graph element (node or tensor).


#### Returns:

(list) The traceback list object as returned by the `extract_trace`
  method of Python's traceback module.


#### Raises:

* <b>`LookupError`</b>: If Python graph is not available for traceback lookup.
* <b>`KeyError`</b>: If the node cannot be found in the Python graph loaded.

<h3 id="nodes"><code>nodes</code></h3>

``` python
nodes(device_name=None)
```

Get a list of all nodes from the partition graphs.

#### Args:

* <b>`device_name`</b>: (`str`) name of device. If None, all nodes from all available
    devices will be included.


#### Returns:

All nodes' names, as a list of str.


#### Raises:

* <b>`LookupError`</b>: If no partition graphs have been loaded.
* <b>`ValueError`</b>: If specified node name does not exist.

<h3 id="partition_graphs"><code>partition_graphs</code></h3>

``` python
partition_graphs()
```

Get the partition graphs.

#### Returns:

Partition graphs as a list of GraphDef.


#### Raises:

* <b>`LookupError`</b>: If no partition graphs have been loaded.

<h3 id="reconstructed_non_debug_partition_graphs"><code>reconstructed_non_debug_partition_graphs</code></h3>

``` python
reconstructed_non_debug_partition_graphs()
```

Reconstruct partition graphs with the debugger-inserted ops stripped.

The reconstructed partition graphs are identical to the original (i.e.,
non-debugger-decorated) partition graphs except in the following respects:
  1) The exact names of the runtime-inserted internal nodes may differ.
     These include _Send, _Recv, _HostSend, _HostRecv, _Retval ops.
  2) As a consequence of 1, the nodes that receive input directly from such
     send- and recv-type ops will have different input names.
  3) The parallel_iteration attribute of while-loop Enter ops are set to 1.

#### Returns:

A dict mapping device names (`str`s) to reconstructed <a href="../tf/GraphDef"><code>tf.GraphDef</code></a>s.

<h3 id="set_python_graph"><code>set_python_graph</code></h3>

``` python
set_python_graph(python_graph)
```

Provide Python `Graph` object to the wrapper.

Unlike the partition graphs, which are protobuf `GraphDef` objects, `Graph`
is a Python object and carries additional information such as the traceback
of the construction of the nodes in the graph.

#### Args:

* <b>`python_graph`</b>: (ops.Graph) The Python Graph object.

<h3 id="transitive_inputs"><code>transitive_inputs</code></h3>

``` python
transitive_inputs(
    node_name,
    include_control=True,
    include_reversed_ref=False,
    device_name=None
)
```

Get the transitive inputs of given node according to partition graphs.

#### Args:

* <b>`node_name`</b>: Name of the node.
* <b>`include_control`</b>: Include control inputs (True by default).
* <b>`include_reversed_ref`</b>: Whether a ref input, say from A to B, is to be also
    considered as an input from B to A. The rationale is that ref inputs
    generally let the recipient (e.g., B in this case) mutate the value of
    the source (e.g., A in this case). So the reverse direction of the ref
    edge reflects the direction of information flow.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    node_name exists on only one device, this argument is optional.


#### Returns:

(`list` of `str`) all transitive inputs to the node, as a list of node
  names.


#### Raises:

* <b>`LookupError`</b>: If node inputs and control inputs have not been loaded
     from partition graphs yet.

<h3 id="watch_key_to_data"><code>watch_key_to_data</code></h3>

``` python
watch_key_to_data(
    debug_watch_key,
    device_name=None
)
```

Get all `DebugTensorDatum` instances corresponding to a debug watch key.

#### Args:

* <b>`debug_watch_key`</b>: (`str`) debug watch key.
* <b>`device_name`</b>: (`str`) name of the device. If there is only one device or if
    the specified debug_watch_key exists on only one device, this argument
    is optional.


#### Returns:

A list of `DebugTensorDatum` instances that correspond to the debug watch
key. If the watch key does not exist, returns an empty list.


#### Raises:

* <b>`ValueError`</b>: If there are multiple devices that have the debug_watch_key,
    but device_name is not specified.



