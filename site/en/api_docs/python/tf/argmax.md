

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.argmax

``` python
argmax(
    input,
    axis=None,
    name=None,
    dimension=None,
    output_type=tf.int64
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Sequence Comparison and Indexing](../../../api_guides/python/math_ops#Sequence_Comparison_and_Indexing)

Returns the index with the largest value across axes of a tensor. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed in a future version.
Instructions for updating:
Use the `axis` argument instead

Note that in case of ties the identity of the return value is not guaranteed.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`, `uint32`, `uint64`, `bfloat16`.
* <b>`axis`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    int32 or int64, must be in the range `[-rank(input), rank(input))`.
    Describes which axis of the input Tensor to reduce across. For vectors,
    use axis = 0.
* <b>`output_type`</b>: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `output_type`.