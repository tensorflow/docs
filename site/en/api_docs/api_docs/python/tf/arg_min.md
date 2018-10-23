

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.arg_min

``` python
arg_min(
    input,
    dimension,
    output_type=None,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_math_ops.py`.

Returns the index with the smallest value across dimensions of a tensor. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `argmin` instead

Note that in case of ties the identity of the return value is not guaranteed.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
* <b>`dimension`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    int32 or int64, 0 <= dimension < rank(input).  Describes
    which dimension of the input Tensor to reduce across. For vectors,
    use dimension = 0.
* <b>`output_type`</b>: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `output_type`.