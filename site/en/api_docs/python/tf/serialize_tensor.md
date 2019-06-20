page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.serialize_tensor

``` python
tf.serialize_tensor(
    tensor,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_parsing_ops.py`.

Transforms a Tensor into a serialized TensorProto proto.

#### Args:

* <b>`tensor`</b>: A `Tensor`. A Tensor of type `T`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.