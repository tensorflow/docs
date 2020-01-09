page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.parse_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/parse_tensor">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_parsing_ops.py`



Transforms a serialized tensorflow.TensorProto proto into a Tensor.

### Aliases:

* <a href="/api_docs/python/tf/io/parse_tensor"><code>tf.compat.v1.io.parse_tensor</code></a>
* <a href="/api_docs/python/tf/io/parse_tensor"><code>tf.compat.v1.parse_tensor</code></a>
* <a href="/api_docs/python/tf/io/parse_tensor"><code>tf.compat.v2.io.parse_tensor</code></a>
* <a href="/api_docs/python/tf/io/parse_tensor"><code>tf.parse_tensor</code></a>


``` python
tf.io.parse_tensor(
    serialized,
    out_type,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`serialized`</b>: A `Tensor` of type `string`.
  A scalar string containing a serialized TensorProto proto.
* <b>`out_type`</b>: A <a href="../../tf/dtypes/DType"><code>tf.DType</code></a>.
  The type of the serialized tensor.  The provided type must match the
  type of the serialized tensor and no implicit conversion will take place.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `out_type`.
