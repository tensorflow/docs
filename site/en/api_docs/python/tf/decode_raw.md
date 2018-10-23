

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.decode_raw

``` python
tf.decode_raw(
    bytes,
    out_type,
    little_endian=True,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_parsing_ops.py`.

See the guides: [Inputs and Readers > Converting](../../../api_guides/python/io_ops#Converting), [Reading data > `QueueRunner`](../../../api_guides/python/reading_data#_QueueRunner_), [Strings > Conversion](../../../api_guides/python/string_ops#Conversion)

Reinterpret the bytes of a string as a vector of numbers.

#### Args:

* <b>`bytes`</b>: A `Tensor` of type `string`.
    All the elements must have the same length.
* <b>`out_type`</b>: A `tf.DType` from: `tf.half, tf.float32, tf.float64, tf.int32, tf.uint16, tf.uint8, tf.int16, tf.int8, tf.int64`.
* <b>`little_endian`</b>: An optional `bool`. Defaults to `True`.
    Whether the input `bytes` are in little-endian order.
    Ignored for `out_type` values that are stored in a single byte like
    `uint8`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `out_type`.