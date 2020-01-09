page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_proto


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/decode_proto">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_decode_proto_ops.py`



The op extracts fields from a serialized protocol buffers message into tensors.

### Aliases:

* <a href="/api_docs/python/tf/io/decode_proto"><code>tf.compat.v1.io.decode_proto</code></a>
* <a href="/api_docs/python/tf/io/decode_proto"><code>tf.compat.v2.io.decode_proto</code></a>
* <a href="/api_docs/python/tf/io/decode_proto"><code>tf.contrib.proto.decode_proto</code></a>


``` python
tf.io.decode_proto(
    bytes,
    message_type,
    field_names,
    output_types,
    descriptor_source='local://',
    message_format='binary',
    sanitize=False,
    name=None
)
```



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

#### Args:


* <b>`bytes`</b>: A `Tensor` of type `string`.
  Tensor of serialized protos with shape `batch_shape`.
* <b>`message_type`</b>: A `string`. Name of the proto message type to decode.
* <b>`field_names`</b>: A list of `strings`.
  List of strings containing proto field names. An extension field can be decoded
  by using its full name, e.g. EXT_PACKAGE.EXT_FIELD_NAME.
* <b>`output_types`</b>: A list of `tf.DTypes`.
  List of TF types to use for the respective field in field_names.
* <b>`descriptor_source`</b>: An optional `string`. Defaults to `"local://"`.
  Either the special value `local://` or a path to a file containing
  a serialized `FileDescriptorSet`.
* <b>`message_format`</b>: An optional `string`. Defaults to `"binary"`.
  Either `binary` or `text`.
* <b>`sanitize`</b>: An optional `bool`. Defaults to `False`.
  Whether to sanitize the result or not.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (sizes, values).


* <b>`sizes`</b>: A `Tensor` of type `int32`.
* <b>`values`</b>: A list of `Tensor` objects of type `output_types`.
