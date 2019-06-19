page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.toco_convert

``` python
tf.contrib.lite.toco_convert(
    input_data,
    input_tensors,
    output_tensors,
    inference_type=lite_constants.FLOAT,
    inference_input_type=None,
    input_format=lite_constants.TENSORFLOW_GRAPHDEF,
    output_format=lite_constants.TFLITE,
    quantized_input_stats=None,
    default_ranges_stats=None,
    drop_control_dependency=True,
    reorder_across_fake_quant=False,
    allow_custom_ops=False,
    change_concat_input_ranges=False
)
```



Defined in [`tensorflow/contrib/lite/python/convert.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/lite/python/convert.py).

Convert a model using TOCO from `input_format` to `output_format`.

Typically this is to convert from TensorFlow GraphDef to TFLite, in which
case the default `input_format` and `output_format` are sufficient.

#### Args:

* <b>`input_data`</b>: Input data (i.e. often `sess.graph_def`).
* <b>`input_tensors`</b>: List of input tensors. Type and shape are computed using
    `foo.get_shape()` and `foo.dtype`.
* <b>`output_tensors`</b>: List of output tensors (only .name is used from this).
* <b>`inference_type`</b>: Target data type of arrays in the output file. Currently
    must be `{FLOAT, QUANTIZED_UINT8}`.  (default FLOAT)
* <b>`inference_input_type`</b>: Target data type of input arrays. Allows for a
    different type for input arrays in the case of quantization. Currently
    must be `{FLOAT, QUANTIZED_UINT8}`. (default `inference_type`)
* <b>`input_format`</b>: Type of data to read Currently must be
    `{TENSORFLOW_GRAPHDEF}`. (default TENSORFLOW_GRAPHDEF)
* <b>`output_format`</b>: Output file format. Currently must be `{TFLITE,
    GRAPHVIZ_DOT}`. (default TFLITE)
* <b>`quantized_input_stats`</b>: Dict of strings representing input tensor names
    mapped to tuple of integers representing the mean and standard deviation
    of the training data (e.g., {"foo" : (0., 1.)}). Only need if
    `inference_type` is `QUANTIZED_UINT8`. (default None)
* <b>`default_ranges_stats`</b>: Tuple of integers representing (min, max) range values
    for all arrays without a specified range. Intended for experimenting with
    quantization via "dummy quantization". (default None)
* <b>`drop_control_dependency`</b>: Boolean indicating whether to drop control
    dependencies silently. This is due to TFLite not supporting control
    dependencies. (default True)
* <b>`reorder_across_fake_quant`</b>: Boolean indicating whether to reorder FakeQuant
    nodes in unexpected locations. Used when the location of the FakeQuant
    nodes is preventing graph transformations necessary to convert the graph.
    Results in a graph that differs from the quantized training graph,
    potentially causing differing arithmetic behavior. (default False)
* <b>`change_concat_input_ranges`</b>: Boolean to change behavior of min/max ranges for
    inputs and outputs of the concat operator for quantized models. Changes
    the ranges of concat operator overlap when true. (default False)
* <b>`allow_custom_ops`</b>: Boolean indicating whether to allow custom operations.
    When false any unknown operation is an error. When true, custom ops are
    created for any op that is unknown. The developer will need to provide
    these to the TensorFlow Lite runtime with a custom resolver.
    (default False)


#### Returns:

The converted data. For example if TFLite was the destination, then
this will be a tflite flatbuffer in a bytes array.


#### Raises:

* <b>`ValueError`</b>: If the input tensor type is unknown
* <b>`RuntimeError`</b>: If TOCO fails to convert (in which case the runtime error's
    error text will contain the TOCO error log)