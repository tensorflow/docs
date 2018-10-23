

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tfdbg.DebugTensorDatum

## Class `DebugTensorDatum`





Defined in [`tensorflow/python/debug/lib/debug_data.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/debug/lib/debug_data.py).

See the guide: [TensorFlow Debugger > Classes for debug-dump data and directories](../../../api_guides/python/tfdbg#Classes_for_debug_dump_data_and_directories)

A single tensor dumped by TensorFlow Debugger (tfdbg).

Contains metadata about the dumped tensor, including `timestamp`,
`node_name`, `output_slot`, `debug_op`, and path to the dump file
(`file_path`).

This type does not hold the generally space-expensive tensor value (numpy
array). Instead, it points to the file from which the tensor value can be
loaded (with the `get_tensor` method) if needed.

## Properties

<h3 id="debug_op"><code>debug_op</code></h3>

Name of the debug op.

#### Returns:

  (`str`) debug op name (e.g., `DebugIdentity`).

<h3 id="device_name"><code>device_name</code></h3>

Name of the device that the tensor belongs to.

#### Returns:

  (`str`) device name.

<h3 id="dump_size_bytes"><code>dump_size_bytes</code></h3>

Size of the dump file.

Unit: byte.

#### Returns:

  If the dump file exists, size of the dump file, in bytes.
  If the dump file does not exist, None.

<h3 id="extended_timestamp"><code>extended_timestamp</code></h3>

Extended timestamp, possibly with an index suffix.

The index suffix, e.g., "-1", is for disambiguating multiple dumps of the
same tensor with the same timestamp, which can occur if the dumping events
are spaced by shorter than the temporal resolution of the timestamps.

#### Returns:

  (`str`) The extended timestamp.

<h3 id="file_path"><code>file_path</code></h3>

Path to the file which stores the value of the dumped tensor.

<h3 id="node_name"><code>node_name</code></h3>

Name of the node from which the tensor value was dumped.

#### Returns:

  (`str`) name of the node watched by the debug op.

<h3 id="output_slot"><code>output_slot</code></h3>

Output slot index from which the tensor value was dumped.

#### Returns:

  (`int`) output slot index watched by the debug op.

<h3 id="tensor_name"><code>tensor_name</code></h3>

Name of the tensor watched by the debug op.

#### Returns:

  (`str`) `Tensor` name, in the form of `node_name`:`output_slot`

<h3 id="timestamp"><code>timestamp</code></h3>

Timestamp of when this tensor value was dumped.

#### Returns:

  (`int`) The timestamp in microseconds.

<h3 id="watch_key"><code>watch_key</code></h3>

Watch key identities a debug watch on a tensor.

#### Returns:

  (`str`) A watch key, in the form of `tensor_name`:`debug_op`.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    dump_root,
    debug_dump_rel_path
)
```

`DebugTensorDatum` constructor.

#### Args:

* <b>`dump_root`</b>: (`str`) Debug dump root directory. This path should not include
    the path component that represents the device name (see also below).
* <b>`debug_dump_rel_path`</b>: (`str`) Path to a debug dump file, relative to the
    `dump_root`. The first item of this relative path is assumed to be
    a path representing the name of the device that the Tensor belongs to.
    See `device_path_to_device_name` for more details on the device path.
    For example, suppose the debug dump root
    directory is `/tmp/tfdbg_1` and the dump file is at
    `/tmp/tfdbg_1/<device_path>/>ns_1/node_a_0_DebugIdentity_123456789`,
    then the value of the debug_dump_rel_path should be
    `<device_path>/ns_1/node_a_0_DebugIdenity_1234456789`.


#### Raises:

* <b>`ValueError`</b>: If the base file name of the dump file does not conform to
    the dump file naming pattern:
    `node_name`_`output_slot`_`debug_op`_`timestamp`

<h3 id="get_tensor"><code>get_tensor</code></h3>

``` python
get_tensor()
```

Get tensor from the dump (`Event`) file.

#### Returns:

  The tensor loaded from the dump (`Event`) file.



