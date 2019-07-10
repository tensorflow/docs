page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.encode_proto

The op serializes protobuf messages provided in the input tensors.

### Aliases:

* `tf.compat.v1.io.encode_proto`
* `tf.compat.v2.io.encode_proto`
* `tf.contrib.proto.encode_proto`
* `tf.io.encode_proto`

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



Defined in generated file: `python/ops/gen_encode_proto_ops.py`.

<!-- Placeholder for "Used in" -->

The types of the tensors in `values` must match the schema for the
fields specified in `field_names`. All the tensors in `values` must
have a common shape prefix, *batch_shape*.

The `sizes` tensor specifies repeat counts for each field.  The repeat
count (last dimension) of a each tensor in `values` must be greater
than or equal to corresponding repeat count in `sizes`.

A `message_type` name must be provided to give context for the field
names. The actual message descriptor can be looked up either in the
linked-in descriptor pool or a filename provided by the caller using
the `descriptor_source` attribute.

The `descriptor_source` attribute selects a source of protocol
descriptors to consult when looking up `message_type`. This may be a
filename containing a serialized `FileDescriptorSet` message,
or the special value `local://`, in which case only descriptors linked
into the code will be searched; the filename can be on any filesystem
accessible to TensorFlow.

You can build a `descriptor_source` file using the `--descriptor_set_out`
and `--include_imports` options to the protocol compiler `protoc`.

The `local://` database only covers descriptors linked into the
code via C++ libraries, not Python imports. You can link in a proto descriptor
by creating a cc_library target with alwayslink=1.

There are a few special cases in the value mapping:

Submessage and group fields must be pre-serialized as TensorFlow strings.

TensorFlow lacks support for unsigned int64s, so they must be
represented as <a href="../../tf#int64"><code>tf.int64</code></a> with the same twos-complement bit pattern
(the obvious way).

Unsigned int32 values can be represented exactly with <a href="../../tf#int64"><code>tf.int64</code></a>, or
with sign wrapping if the input is of type <a href="../../tf#int32"><code>tf.int32</code></a>.

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
