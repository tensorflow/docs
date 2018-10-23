


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.ConfigProto

### `class tf.ConfigProto`



## Child Classes
[`class DeviceCountEntry`](../tf/ConfigProto/DeviceCountEntry)

## Properties

<h3 id="allow_soft_placement"><code>allow_soft_placement</code></h3>

Magic attribute generated for "allow_soft_placement" proto field.

<h3 id="device_count"><code>device_count</code></h3>

Magic attribute generated for "device_count" proto field.

<h3 id="device_filters"><code>device_filters</code></h3>

Magic attribute generated for "device_filters" proto field.

<h3 id="gpu_options"><code>gpu_options</code></h3>

Magic attribute generated for "gpu_options" proto field.

<h3 id="graph_options"><code>graph_options</code></h3>

Magic attribute generated for "graph_options" proto field.

<h3 id="inter_op_parallelism_threads"><code>inter_op_parallelism_threads</code></h3>

Magic attribute generated for "inter_op_parallelism_threads" proto field.

<h3 id="intra_op_parallelism_threads"><code>intra_op_parallelism_threads</code></h3>

Magic attribute generated for "intra_op_parallelism_threads" proto field.

<h3 id="log_device_placement"><code>log_device_placement</code></h3>

Magic attribute generated for "log_device_placement" proto field.

<h3 id="operation_timeout_in_ms"><code>operation_timeout_in_ms</code></h3>

Magic attribute generated for "operation_timeout_in_ms" proto field.

<h3 id="placement_period"><code>placement_period</code></h3>

Magic attribute generated for "placement_period" proto field.

<h3 id="rpc_options"><code>rpc_options</code></h3>

Magic attribute generated for "rpc_options" proto field.

<h3 id="session_inter_op_thread_pool"><code>session_inter_op_thread_pool</code></h3>

Magic attribute generated for "session_inter_op_thread_pool" proto field.

<h3 id="use_per_session_threads"><code>use_per_session_threads</code></h3>

Magic attribute generated for "use_per_session_threads" proto field.



## Methods

<h3 id="ByteSize"><code>ByteSize()</code></h3>



<h3 id="Clear"><code>Clear()</code></h3>



<h3 id="ClearExtension"><code>ClearExtension(extension_handle)</code></h3>



<h3 id="ClearField"><code>ClearField(field_name)</code></h3>



<h3 id="CopyFrom"><code>CopyFrom(other_msg)</code></h3>

Copies the content of the specified message into the current message.

The method clears the current message and then merges the specified
message using MergeFrom.

#### Args:

* <b>`other_msg`</b>: Message to copy into the current one.

<h3 id="DiscardUnknownFields"><code>DiscardUnknownFields()</code></h3>



<h3 id="FindInitializationErrors"><code>FindInitializationErrors()</code></h3>

Finds required fields which are not initialized.

#### Returns:

  A list of strings.  Each string is a path to an uninitialized field from
  the top-level message, e.g. "foo.bar[5].baz".

<h3 id="FromString"><code>FromString(s)</code></h3>



<h3 id="HasExtension"><code>HasExtension(extension_handle)</code></h3>



<h3 id="HasField"><code>HasField(field_name)</code></h3>



<h3 id="IsInitialized"><code>IsInitialized(errors=None)</code></h3>

Checks if all required fields of a message are set.

#### Args:

* <b>`errors`</b>:  A list which, if provided, will be populated with the field
           paths of all missing required fields.


#### Returns:

  True iff the specified message has all required fields set.

<h3 id="ListFields"><code>ListFields()</code></h3>



<h3 id="MergeFrom"><code>MergeFrom(msg)</code></h3>



<h3 id="MergeFromString"><code>MergeFromString(serialized)</code></h3>



<h3 id="ParseFromString"><code>ParseFromString(serialized)</code></h3>

Parse serialized protocol buffer data into this message.

Like MergeFromString(), except we clear the object first and
do not return the value that MergeFromString returns.

<h3 id="RegisterExtension"><code>RegisterExtension(extension_handle)</code></h3>



<h3 id="SerializePartialToString"><code>SerializePartialToString()</code></h3>



<h3 id="SerializeToString"><code>SerializeToString()</code></h3>



<h3 id="SetInParent"><code>SetInParent()</code></h3>

Sets the _cached_byte_size_dirty bit to true,
and propagates this to our listener iff this was a state change.

<h3 id="WhichOneof"><code>WhichOneof(oneof_name)</code></h3>

Returns the name of the currently set field inside a oneof, or None.

<h3 id="__init__"><code>__init__(**kwargs)</code></h3>





## Class Members

<h3 id="ALLOW_SOFT_PLACEMENT_FIELD_NUMBER"><code>ALLOW_SOFT_PLACEMENT_FIELD_NUMBER</code></h3>

<h3 id="DESCRIPTOR"><code>DESCRIPTOR</code></h3>

<h3 id="DEVICE_COUNT_FIELD_NUMBER"><code>DEVICE_COUNT_FIELD_NUMBER</code></h3>

<h3 id="DEVICE_FILTERS_FIELD_NUMBER"><code>DEVICE_FILTERS_FIELD_NUMBER</code></h3>

<h3 id="GPU_OPTIONS_FIELD_NUMBER"><code>GPU_OPTIONS_FIELD_NUMBER</code></h3>

<h3 id="GRAPH_OPTIONS_FIELD_NUMBER"><code>GRAPH_OPTIONS_FIELD_NUMBER</code></h3>

<h3 id="INTER_OP_PARALLELISM_THREADS_FIELD_NUMBER"><code>INTER_OP_PARALLELISM_THREADS_FIELD_NUMBER</code></h3>

<h3 id="INTRA_OP_PARALLELISM_THREADS_FIELD_NUMBER"><code>INTRA_OP_PARALLELISM_THREADS_FIELD_NUMBER</code></h3>

<h3 id="LOG_DEVICE_PLACEMENT_FIELD_NUMBER"><code>LOG_DEVICE_PLACEMENT_FIELD_NUMBER</code></h3>

<h3 id="OPERATION_TIMEOUT_IN_MS_FIELD_NUMBER"><code>OPERATION_TIMEOUT_IN_MS_FIELD_NUMBER</code></h3>

<h3 id="PLACEMENT_PERIOD_FIELD_NUMBER"><code>PLACEMENT_PERIOD_FIELD_NUMBER</code></h3>

<h3 id="RPC_OPTIONS_FIELD_NUMBER"><code>RPC_OPTIONS_FIELD_NUMBER</code></h3>

<h3 id="SESSION_INTER_OP_THREAD_POOL_FIELD_NUMBER"><code>SESSION_INTER_OP_THREAD_POOL_FIELD_NUMBER</code></h3>

<h3 id="USE_PER_SESSION_THREADS_FIELD_NUMBER"><code>USE_PER_SESSION_THREADS_FIELD_NUMBER</code></h3>



Defined in [`tensorflow/core/protobuf/config_pb2.py`](https://www.tensorflow.org/code/tensorflow/core/protobuf/config_pb2.py).

