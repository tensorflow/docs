

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.bitcast

``` python
bitcast(
    input,
    type,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_array_ops.py`.

See the guide: [Tensor Transformations > Casting](../../../api_guides/python/array_ops#Casting)

Bitcasts a tensor from one type to another without copying data.

Given a tensor `input`, this operation returns a tensor that has the same buffer
data as `input` with datatype `type`.

If the input datatype `T` is larger than the output datatype `type` then the
shape changes from [...] to [..., sizeof(`T`)/sizeof(`type`)].

If `T` is smaller than `type`, the operator requires that the rightmost
dimension be equal to sizeof(`type`)/sizeof(`T`). The shape then goes from
[..., sizeof(`type`)/sizeof(`T`)] to [...].

*NOTE*: Bitcast is implemented as a low-level cast, so machines with different
endian orderings will give different results.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int8`, `int16`, `complex64`, `complex128`, `qint8`, `quint8`, `qint16`, `quint16`, `qint32`, `half`.
* <b>`type`</b>: A `tf.DType` from: `tf.bfloat16, tf.float32, tf.float64, tf.int64, tf.int32, tf.uint8, tf.uint16, tf.int8, tf.int16, tf.complex64, tf.complex128, tf.qint8, tf.quint8, tf.qint16, tf.quint16, tf.qint32, tf.half`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `type`.