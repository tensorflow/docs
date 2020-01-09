page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_raw

### Aliases:

* `tf.decode_raw`
* `tf.io.decode_raw`

``` python
tf.io.decode_raw(
    bytes,
    out_type,
    little_endian=True,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_parsing_ops.py`.

See the guides: [Inputs and Readers > Converting](../../../../api_guides/python/io_ops#Converting), [Reading data > `QueueRunner`](../../../../api_guides/python/reading_data#_QueueRunner_)

Reinterpret the bytes of a string as a vector of numbers.

#### Args:

* <b>`bytes`</b>: A `Tensor` of type `string`.
    All the elements must have the same length.
* <b>`out_type`</b>: A <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.half, tf.float32, tf.float64, tf.int32, tf.uint16, tf.uint8, tf.int16, tf.int8, tf.int64`.
* <b>`little_endian`</b>: An optional `bool`. Defaults to `True`.
    Whether the input `bytes` are in little-endian order.
    Ignored for `out_type` values that are stored in a single byte like
    `uint8`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `out_type`.