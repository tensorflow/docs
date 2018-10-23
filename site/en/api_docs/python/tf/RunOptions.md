


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.RunOptions

### `class tf.RunOptions`



## Properties

<h3 id="debug_options"><code>debug_options</code></h3>

Magic attribute generated for "debug_options" proto field.

<h3 id="inter_op_thread_pool"><code>inter_op_thread_pool</code></h3>

Magic attribute generated for "inter_op_thread_pool" proto field.

<h3 id="output_partition_graphs"><code>output_partition_graphs</code></h3>

Magic attribute generated for "output_partition_graphs" proto field.

<h3 id="timeout_in_ms"><code>timeout_in_ms</code></h3>

Magic attribute generated for "timeout_in_ms" proto field.

<h3 id="trace_level"><code>trace_level</code></h3>

Magic attribute generated for "trace_level" proto field.



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

<h3 id="DEBUG_OPTIONS_FIELD_NUMBER"><code>DEBUG_OPTIONS_FIELD_NUMBER</code></h3>

<h3 id="DESCRIPTOR"><code>DESCRIPTOR</code></h3>

<h3 id="FULL_TRACE"><code>FULL_TRACE</code></h3>

<h3 id="HARDWARE_TRACE"><code>HARDWARE_TRACE</code></h3>

<h3 id="INTER_OP_THREAD_POOL_FIELD_NUMBER"><code>INTER_OP_THREAD_POOL_FIELD_NUMBER</code></h3>

<h3 id="NO_TRACE"><code>NO_TRACE</code></h3>

<h3 id="OUTPUT_PARTITION_GRAPHS_FIELD_NUMBER"><code>OUTPUT_PARTITION_GRAPHS_FIELD_NUMBER</code></h3>

<h3 id="SOFTWARE_TRACE"><code>SOFTWARE_TRACE</code></h3>

<h3 id="TIMEOUT_IN_MS_FIELD_NUMBER"><code>TIMEOUT_IN_MS_FIELD_NUMBER</code></h3>

<h3 id="TRACE_LEVEL_FIELD_NUMBER"><code>TRACE_LEVEL_FIELD_NUMBER</code></h3>

<h3 id="TraceLevel"><code>TraceLevel</code></h3>



Defined in [`tensorflow/core/protobuf/config_pb2.py`](https://www.tensorflow.org/code/tensorflow/core/protobuf/config_pb2.py).

