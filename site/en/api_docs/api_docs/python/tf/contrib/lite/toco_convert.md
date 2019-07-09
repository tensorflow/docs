

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.toco_convert

``` python
tf.contrib.lite.toco_convert(
    input_data,
    input_tensors,
    output_tensors,
    *args,
    **kwargs
)
```



Defined in [`tensorflow/contrib/lite/python/convert.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/lite/python/convert.py).

"Convert a model using TOCO.

Typically this function is used to convert from TensorFlow GraphDef to TFLite.
Conversion can be customized by providing arguments that are forwarded to
`build_toco_convert_protos` (see documentation for details).

#### Args:

* <b>`input_data`</b>: Input data (i.e. often `sess.graph_def`),
* <b>`input_tensors`</b>: List of input tensors. Type and shape are computed using
    `foo.get_shape()` and `foo.dtype`.
* <b>`output_tensors`</b>: List of output tensors (only .name is used from this).
* <b>`*args`</b>: See `build_toco_convert_protos`,
* <b>`**kwargs`</b>: See `build_toco_convert_protos`.


#### Returns:

The converted data. For example if TFLite was the destination, then
this will be a tflite flatbuffer in a bytes array.


#### Raises:

Defined in `build_toco_convert_protos`.