page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.serialize_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/serialize_tensor">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_parsing_ops.py`



Transforms a Tensor into a serialized TensorProto proto.

### Aliases:

* <a href="/api_docs/python/tf/io/serialize_tensor"><code>tf.compat.v1.io.serialize_tensor</code></a>
* <a href="/api_docs/python/tf/io/serialize_tensor"><code>tf.compat.v1.serialize_tensor</code></a>
* <a href="/api_docs/python/tf/io/serialize_tensor"><code>tf.compat.v2.io.serialize_tensor</code></a>
* <a href="/api_docs/python/tf/io/serialize_tensor"><code>tf.serialize_tensor</code></a>


``` python
tf.io.serialize_tensor(
    tensor,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`tensor`</b>: A `Tensor`. A Tensor of type `T`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
