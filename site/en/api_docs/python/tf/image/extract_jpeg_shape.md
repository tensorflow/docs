

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.image.extract_jpeg_shape

``` python
tf.image.extract_jpeg_shape(
    contents,
    output_type=tf.int32,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_image_ops.py`.

Extract the shape information of a JPEG-encoded image.

This op only parses the image header, so it is much faster than DecodeJpeg.

#### Args:

* <b>`contents`</b>: A `Tensor` of type `string`. 0-D. The JPEG-encoded image.
* <b>`output_type`</b>: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int32`.
    (Optional) The output type of the operation (int32 or int64).
    Defaults to int32.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `output_type`.