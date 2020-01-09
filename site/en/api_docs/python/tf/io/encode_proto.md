page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.encode_proto


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/encode_proto">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_encode_proto_ops.py`



The op serializes protobuf messages provided in the input tensors.

### Aliases:

* <a href="/api_docs/python/tf/io/encode_proto"><code>tf.compat.v1.io.encode_proto</code></a>
* <a href="/api_docs/python/tf/io/encode_proto"><code>tf.compat.v2.io.encode_proto</code></a>
* <a href="/api_docs/python/tf/io/encode_proto"><code>tf.contrib.proto.encode_proto</code></a>


``` python
tf.io.encode_proto(
    sizes,
    values,
    field_names,
    message_type,
    descriptor_source='local://',
    name=None
)
```



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

#### Args:


* <b>`sizes`</b>: A `Tensor` of type `int32`.
  Tensor of int32 with shape `[batch_shape, len(field_names)]`.
* <b>`values`</b>: A list of `Tensor` objects.
  List of tensors containing values for the corresponding field.
* <b>`field_names`</b>: A list of `strings`.
  List of strings containing proto field names.
* <b>`message_type`</b>: A `string`. Name of the proto message type to decode.
* <b>`descriptor_source`</b>: An optional `string`. Defaults to `"local://"`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
