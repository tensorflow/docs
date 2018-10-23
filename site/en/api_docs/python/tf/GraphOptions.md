


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.GraphOptions

### `class tf.GraphOptions`



## Properties

<h3 id="build_cost_model"><code>build_cost_model</code></h3>

Magic attribute generated for "build_cost_model" proto field.

<h3 id="build_cost_model_after"><code>build_cost_model_after</code></h3>

Magic attribute generated for "build_cost_model_after" proto field.

<h3 id="enable_bfloat16_sendrecv"><code>enable_bfloat16_sendrecv</code></h3>

Magic attribute generated for "enable_bfloat16_sendrecv" proto field.

<h3 id="enable_recv_scheduling"><code>enable_recv_scheduling</code></h3>

Magic attribute generated for "enable_recv_scheduling" proto field.

<h3 id="infer_shapes"><code>infer_shapes</code></h3>

Magic attribute generated for "infer_shapes" proto field.

<h3 id="optimizer_options"><code>optimizer_options</code></h3>

Magic attribute generated for "optimizer_options" proto field.

<h3 id="place_pruned_graph"><code>place_pruned_graph</code></h3>

Magic attribute generated for "place_pruned_graph" proto field.

<h3 id="timeline_step"><code>timeline_step</code></h3>

Magic attribute generated for "timeline_step" proto field.



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

<h3 id="BUILD_COST_MODEL_AFTER_FIELD_NUMBER"><code>BUILD_COST_MODEL_AFTER_FIELD_NUMBER</code></h3>

<h3 id="BUILD_COST_MODEL_FIELD_NUMBER"><code>BUILD_COST_MODEL_FIELD_NUMBER</code></h3>

<h3 id="DESCRIPTOR"><code>DESCRIPTOR</code></h3>

<h3 id="ENABLE_BFLOAT16_SENDRECV_FIELD_NUMBER"><code>ENABLE_BFLOAT16_SENDRECV_FIELD_NUMBER</code></h3>

<h3 id="ENABLE_RECV_SCHEDULING_FIELD_NUMBER"><code>ENABLE_RECV_SCHEDULING_FIELD_NUMBER</code></h3>

<h3 id="INFER_SHAPES_FIELD_NUMBER"><code>INFER_SHAPES_FIELD_NUMBER</code></h3>

<h3 id="OPTIMIZER_OPTIONS_FIELD_NUMBER"><code>OPTIMIZER_OPTIONS_FIELD_NUMBER</code></h3>

<h3 id="PLACE_PRUNED_GRAPH_FIELD_NUMBER"><code>PLACE_PRUNED_GRAPH_FIELD_NUMBER</code></h3>

<h3 id="TIMELINE_STEP_FIELD_NUMBER"><code>TIMELINE_STEP_FIELD_NUMBER</code></h3>



Defined in [`tensorflow/core/protobuf/config_pb2.py`](https://www.tensorflow.org/code/tensorflow/core/protobuf/config_pb2.py).

