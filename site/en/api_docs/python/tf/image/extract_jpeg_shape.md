page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.extract_jpeg_shape

``` python
tf.image.extract_jpeg_shape(
    contents,
    output_type=tf.int32,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_image_ops.py`.

Extract the shape information of a JPEG-encoded image.

This op only parses the image header, so it is much faster than DecodeJpeg.

#### Args:

* <b>`contents`</b>: A `Tensor` of type `string`. 0-D. The JPEG-encoded image.
* <b>`output_type`</b>: An optional <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf#int32"><code>tf.int32</code></a>.
    (Optional) The output type of the operation (int32 or int64).
    Defaults to int32.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `output_type`.