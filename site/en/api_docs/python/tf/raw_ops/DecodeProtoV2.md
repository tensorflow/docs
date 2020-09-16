description: The op extracts fields from a serialized protocol buffers message into tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.DecodeProtoV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.DecodeProtoV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



The op extracts fields from a serialized protocol buffers message into tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DecodeProtoV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DecodeProtoV2(
    bytes, message_type, field_names, output_types, descriptor_source='local://',
    message_format='binary', sanitize=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `decode_proto` op extracts fields from a serialized protocol buffers
message into tensors.  The fields in `field_names` are decoded and converted
to the corresponding `output_types` if possible.

A `message_type` name must be provided to give context for the field names.
The actual message descriptor can be looked up either in the linked-in
descriptor pool or a filename provided by the caller using the
`descriptor_source` attribute.

Each output tensor is a dense tensor. This means that it is padded to hold
the largest number of repeated elements seen in the input minibatch. (The
shape is also padded by one to prevent zero-sized dimensions). The actual
repeat counts for each example in the minibatch can be found in the `sizes`
output. In many cases the output of `decode_proto` is fed immediately into
tf.squeeze if missing values are not a concern. When using tf.squeeze, always
pass the squeeze dimension explicitly to avoid surprises.

For the most part, the mapping between Proto field types and TensorFlow dtypes
is straightforward. However, there are a few special cases:

- A proto field that contains a submessage or group can only be converted
to `DT_STRING` (the serialized submessage). This is to reduce the complexity
of the API. The resulting string can be used as input to another instance of
the decode_proto op.

- TensorFlow lacks support for unsigned integers. The ops represent uint64
types as a `DT_INT64` with the same twos-complement bit pattern (the obvious
way). Unsigned int32 values can be represented exactly by specifying type
`DT_INT64`, or using twos-complement if the caller specifies `DT_INT32` in
the `output_types` attribute.

Both binary and text proto serializations are supported, and can be
chosen using the `format` attribute.

The `descriptor_source` attribute selects the source of protocol
descriptors to consult when looking up `message_type`. This may be:

- An empty string  or "local://", in which case protocol descriptors are
created for C++ (not Python) proto definitions linked to the binary.

- A file, in which case protocol descriptors are created from the file,
which is expected to contain a `FileDescriptorSet` serialized as a string.
NOTE: You can build a `descriptor_source` file using the `--descriptor_set_out`
and `--include_imports` options to the protocol compiler `protoc`.

- A "bytes://<bytes>", in which protocol descriptors are created from `<bytes>`,
which is expected to be a `FileDescriptorSet` serialized as a string.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`bytes`
</td>
<td>
A `Tensor` of type `string`.
Tensor of serialized protos with shape `batch_shape`.
</td>
</tr><tr>
<td>
`message_type`
</td>
<td>
A `string`. Name of the proto message type to decode.
</td>
</tr><tr>
<td>
`field_names`
</td>
<td>
A list of `strings`.
List of strings containing proto field names. An extension field can be decoded
by using its full name, e.g. EXT_PACKAGE.EXT_FIELD_NAME.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes`.
List of TF types to use for the respective field in field_names.
</td>
</tr><tr>
<td>
`descriptor_source`
</td>
<td>
An optional `string`. Defaults to `"local://"`.
Either the special value `local://` or a path to a file containing
a serialized `FileDescriptorSet`.
</td>
</tr><tr>
<td>
`message_format`
</td>
<td>
An optional `string`. Defaults to `"binary"`.
Either `binary` or `text`.
</td>
</tr><tr>
<td>
`sanitize`
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether to sanitize the result or not.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple of `Tensor` objects (sizes, values).
</td>
</tr>
<tr>
<td>
`sizes`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A list of `Tensor` objects of type `output_types`.
</td>
</tr>
</table>

