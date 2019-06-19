page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.proto.encode_proto

``` python
tf.contrib.proto.encode_proto(
    sizes,
    values,
    field_names,
    message_type,
    descriptor_source='local://',
    name=None
)
```



Defined in generated file: `tensorflow/contrib/proto/python/ops/gen_encode_proto_op.py`.

TODO: add doc.

#### Args:

* <b>`sizes`</b>: A `Tensor` of type `int32`.
* <b>`values`</b>: A list of `Tensor` objects.
* <b>`field_names`</b>: A list of `strings`.
* <b>`message_type`</b>: A `string`.
* <b>`descriptor_source`</b>: An optional `string`. Defaults to `"local://"`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.