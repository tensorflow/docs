page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_json_example


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/decode_json_example">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_parsing_ops.py`



Convert JSON-encoded Example records to binary protocol buffer strings.

### Aliases:

* <a href="/api_docs/python/tf/io/decode_json_example"><code>tf.compat.v1.decode_json_example</code></a>
* <a href="/api_docs/python/tf/io/decode_json_example"><code>tf.compat.v1.io.decode_json_example</code></a>
* <a href="/api_docs/python/tf/io/decode_json_example"><code>tf.compat.v2.io.decode_json_example</code></a>
* <a href="/api_docs/python/tf/io/decode_json_example"><code>tf.decode_json_example</code></a>


``` python
tf.io.decode_json_example(
    json_examples,
    name=None
)
```



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
