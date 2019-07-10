page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_json_example

Convert JSON-encoded Example records to binary protocol buffer strings.

### Aliases:

* `tf.compat.v1.decode_json_example`
* `tf.compat.v1.io.decode_json_example`
* `tf.compat.v2.io.decode_json_example`
* `tf.decode_json_example`
* `tf.io.decode_json_example`

``` python
tf.io.decode_json_example(
    json_examples,
    name=None
)
```



Defined in generated file: `python/ops/gen_parsing_ops.py`.

<!-- Placeholder for "Used in" -->

This op translates a tensor containing Example records, encoded using
the [standard JSON
mapping](https://developers.google.com/protocol-buffers/docs/proto3#json),
into a tensor containing the same records encoded as binary protocol
buffers. The resulting tensor can then be fed to any of the other
Example-parsing ops.

#### Args:


* <b>`json_examples`</b>: A `Tensor` of type `string`.
  Each string is a JSON object serialized according to the JSON
  mapping of the Example proto.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
