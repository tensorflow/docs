

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.parse_tensor

``` python
parse_tensor(
    serialized,
    out_type,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_parsing_ops.py`.

See the guide: [Inputs and Readers > Converting](../../../api_guides/python/io_ops#Converting)

Transforms a serialized tensorflow.TensorProto proto into a Tensor.

#### Args:

* <b>`serialized`</b>: A `Tensor` of type `string`.
    A scalar string containing a serialized TensorProto proto.
* <b>`out_type`</b>: A `tf.DType`.
    The type of the serialized tensor.  The provided type must match the
    type of the serialized tensor and no implicit conversion will take place.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `out_type`. A Tensor of type `out_type`.