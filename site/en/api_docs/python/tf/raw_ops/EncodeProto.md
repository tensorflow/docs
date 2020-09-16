description: The op serializes protobuf messages provided in the input tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.EncodeProto" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.EncodeProto

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



The op serializes protobuf messages provided in the input tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.EncodeProto`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.EncodeProto(
    sizes, values, field_names, message_type, descriptor_source='local://',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The types of the tensors in `values` must match the schema for the fields
specified in `field_names`. All the tensors in `values` must have a common
shape prefix, *batch_shape*.

The `sizes` tensor specifies repeat counts for each field.  The repeat count
(last dimension) of a each tensor in `values` must be greater than or equal
to corresponding repeat count in `sizes`.

A `message_type` name must be provided to give context for the field names.
The actual message descriptor can be looked up either in the linked-in
descriptor pool or a filename provided by the caller using the
`descriptor_source` attribute.

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
`sizes`
</td>
<td>
A `Tensor` of type `int32`.
Tensor of int32 with shape `[batch_shape, len(field_names)]`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A list of `Tensor` objects.
List of tensors containing values for the corresponding field.
</td>
</tr><tr>
<td>
`field_names`
</td>
<td>
A list of `strings`.
List of strings containing proto field names.
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
`descriptor_source`
</td>
<td>
An optional `string`. Defaults to `"local://"`.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

