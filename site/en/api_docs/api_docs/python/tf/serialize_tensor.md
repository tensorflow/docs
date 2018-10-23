

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.serialize_tensor

``` python
serialize_tensor(
    tensor,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_parsing_ops.py`.

Transforms a Tensor into a serialized TensorProto proto.

#### Args:

* <b>`tensor`</b>: A `Tensor`. A Tensor of type `T`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
A serialized TensorProto proto of the input tensor.