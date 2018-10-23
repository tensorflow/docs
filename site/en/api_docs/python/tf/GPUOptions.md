


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.GPUOptions

### `class tf.GPUOptions`



## Properties

<h3 id="allocator_type"><code>allocator_type</code></h3>

Magic attribute generated for "allocator_type" proto field.

<h3 id="allow_growth"><code>allow_growth</code></h3>

Magic attribute generated for "allow_growth" proto field.

<h3 id="deferred_deletion_bytes"><code>deferred_deletion_bytes</code></h3>

Magic attribute generated for "deferred_deletion_bytes" proto field.

<h3 id="per_process_gpu_memory_fraction"><code>per_process_gpu_memory_fraction</code></h3>

Magic attribute generated for "per_process_gpu_memory_fraction" proto field.

<h3 id="visible_device_list"><code>visible_device_list</code></h3>

Magic attribute generated for "visible_device_list" proto field.



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

<h3 id="ALLOCATOR_TYPE_FIELD_NUMBER"><code>ALLOCATOR_TYPE_FIELD_NUMBER</code></h3>

<h3 id="ALLOW_GROWTH_FIELD_NUMBER"><code>ALLOW_GROWTH_FIELD_NUMBER</code></h3>

<h3 id="DEFERRED_DELETION_BYTES_FIELD_NUMBER"><code>DEFERRED_DELETION_BYTES_FIELD_NUMBER</code></h3>

<h3 id="DESCRIPTOR"><code>DESCRIPTOR</code></h3>

<h3 id="PER_PROCESS_GPU_MEMORY_FRACTION_FIELD_NUMBER"><code>PER_PROCESS_GPU_MEMORY_FRACTION_FIELD_NUMBER</code></h3>

<h3 id="VISIBLE_DEVICE_LIST_FIELD_NUMBER"><code>VISIBLE_DEVICE_LIST_FIELD_NUMBER</code></h3>



Defined in [`tensorflow/core/protobuf/config_pb2.py`](https://www.tensorflow.org/code/tensorflow/core/protobuf/config_pb2.py).

