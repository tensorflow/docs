


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.Event

### `class tf.Event`
### `class tf.summary.Event`



## Properties

<h3 id="file_version"><code>file_version</code></h3>

Magic attribute generated for "file_version" proto field.

<h3 id="graph_def"><code>graph_def</code></h3>

Magic attribute generated for "graph_def" proto field.

<h3 id="log_message"><code>log_message</code></h3>

Magic attribute generated for "log_message" proto field.

<h3 id="meta_graph_def"><code>meta_graph_def</code></h3>

Magic attribute generated for "meta_graph_def" proto field.

<h3 id="session_log"><code>session_log</code></h3>

Magic attribute generated for "session_log" proto field.

<h3 id="step"><code>step</code></h3>

Magic attribute generated for "step" proto field.

<h3 id="summary"><code>summary</code></h3>

Magic attribute generated for "summary" proto field.

<h3 id="tagged_run_metadata"><code>tagged_run_metadata</code></h3>

Magic attribute generated for "tagged_run_metadata" proto field.

<h3 id="wall_time"><code>wall_time</code></h3>

Magic attribute generated for "wall_time" proto field.



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

<h3 id="DESCRIPTOR"><code>DESCRIPTOR</code></h3>

<h3 id="FILE_VERSION_FIELD_NUMBER"><code>FILE_VERSION_FIELD_NUMBER</code></h3>

<h3 id="GRAPH_DEF_FIELD_NUMBER"><code>GRAPH_DEF_FIELD_NUMBER</code></h3>

<h3 id="LOG_MESSAGE_FIELD_NUMBER"><code>LOG_MESSAGE_FIELD_NUMBER</code></h3>

<h3 id="META_GRAPH_DEF_FIELD_NUMBER"><code>META_GRAPH_DEF_FIELD_NUMBER</code></h3>

<h3 id="SESSION_LOG_FIELD_NUMBER"><code>SESSION_LOG_FIELD_NUMBER</code></h3>

<h3 id="STEP_FIELD_NUMBER"><code>STEP_FIELD_NUMBER</code></h3>

<h3 id="SUMMARY_FIELD_NUMBER"><code>SUMMARY_FIELD_NUMBER</code></h3>

<h3 id="TAGGED_RUN_METADATA_FIELD_NUMBER"><code>TAGGED_RUN_METADATA_FIELD_NUMBER</code></h3>

<h3 id="WALL_TIME_FIELD_NUMBER"><code>WALL_TIME_FIELD_NUMBER</code></h3>



Defined in [`tensorflow/core/util/event_pb2.py`](https://www.tensorflow.org/code/tensorflow/core/util/event_pb2.py).

