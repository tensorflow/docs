page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.proto.decode_proto

``` python
tf.contrib.proto.decode_proto(
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



Defined in generated file: `tensorflow/contrib/proto/python/ops/gen_decode_proto_op.py`.

TODO: add doc.

#### Args:

* <b>`bytes`</b>: A `Tensor` of type `string`.
* <b>`message_type`</b>: A `string`.
* <b>`field_names`</b>: A list of `strings`.
* <b>`output_types`</b>: A list of `tf.DTypes`.
* <b>`descriptor_source`</b>: An optional `string`. Defaults to `"local://"`.
* <b>`message_format`</b>: An optional `string`. Defaults to `"binary"`.
* <b>`sanitize`</b>: An optional `bool`. Defaults to `False`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (sizes, values).

* <b>`sizes`</b>: A `Tensor` of type `int32`.
* <b>`values`</b>: A list of `Tensor` objects of type `output_types`.