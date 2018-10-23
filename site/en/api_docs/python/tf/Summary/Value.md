


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.Summary.Value

### `class tf.Summary.Value`
### `class tf.summary.Summary.Value`



## Properties

<h3 id="audio"><code>audio</code></h3>

Magic attribute generated for "audio" proto field.

<h3 id="histo"><code>histo</code></h3>

Magic attribute generated for "histo" proto field.

<h3 id="image"><code>image</code></h3>

Magic attribute generated for "image" proto field.

<h3 id="node_name"><code>node_name</code></h3>

Magic attribute generated for "node_name" proto field.

<h3 id="obsolete_old_style_histogram"><code>obsolete_old_style_histogram</code></h3>

Magic attribute generated for "obsolete_old_style_histogram" proto field.

<h3 id="simple_value"><code>simple_value</code></h3>

Magic attribute generated for "simple_value" proto field.

<h3 id="tag"><code>tag</code></h3>

Magic attribute generated for "tag" proto field.

<h3 id="tensor"><code>tensor</code></h3>

Magic attribute generated for "tensor" proto field.



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

<h3 id="AUDIO_FIELD_NUMBER"><code>AUDIO_FIELD_NUMBER</code></h3>

<h3 id="DESCRIPTOR"><code>DESCRIPTOR</code></h3>

<h3 id="HISTO_FIELD_NUMBER"><code>HISTO_FIELD_NUMBER</code></h3>

<h3 id="IMAGE_FIELD_NUMBER"><code>IMAGE_FIELD_NUMBER</code></h3>

<h3 id="NODE_NAME_FIELD_NUMBER"><code>NODE_NAME_FIELD_NUMBER</code></h3>

<h3 id="OBSOLETE_OLD_STYLE_HISTOGRAM_FIELD_NUMBER"><code>OBSOLETE_OLD_STYLE_HISTOGRAM_FIELD_NUMBER</code></h3>

<h3 id="SIMPLE_VALUE_FIELD_NUMBER"><code>SIMPLE_VALUE_FIELD_NUMBER</code></h3>

<h3 id="TAG_FIELD_NUMBER"><code>TAG_FIELD_NUMBER</code></h3>

<h3 id="TENSOR_FIELD_NUMBER"><code>TENSOR_FIELD_NUMBER</code></h3>



Defined in [`tensorflow/core/framework/summary_pb2.py`](https://www.tensorflow.org/code/tensorflow/core/framework/summary_pb2.py).

