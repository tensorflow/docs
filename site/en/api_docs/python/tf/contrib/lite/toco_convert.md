

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.lite.toco_convert

``` python
tf.contrib.lite.toco_convert(
    input_data,
    input_tensors,
    output_tensors,
    inference_type=FLOAT,
    input_format=TENSORFLOW_GRAPHDEF,
    output_format=TFLITE,
    quantized_input_stats=None,
    drop_control_dependency=True
)
```



Defined in [`tensorflow/contrib/lite/python/lite.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/lite/python/lite.py).

Convert a model using TOCO from `input_format` to `output_format`.

Typically this is to convert from TensorFlow GraphDef to TFLite, in which
case the default `input_format` and `output_format` are sufficient.

#### Args:

* <b>`input_data`</b>: Input data (i.e. often `sess.graph_def`).
* <b>`input_tensors`</b>: List of input tensors. Type and shape are computed using
    `foo.get_shape()` and `foo.dtype`.
* <b>`output_tensors`</b>: List of output tensors (only .name is used from this).
* <b>`inference_type`</b>: Currently must be `{FLOAT, QUANTIZED_UINT8}`.
* <b>`input_format`</b>: Type of data to read (currently must be TENSORFLOW_GRAPHDEF).
* <b>`output_format`</b>: Type of data to write (currently must be TFLITE or
    GRAPHVIZ_DOT)
* <b>`quantized_input_stats`</b>: For each member of input_tensors the mean and
    std deviation of training data. Only needed if `inference_type` is
    `QUANTIZED_UINT8`.
* <b>`drop_control_dependency`</b>: Drops control dependencies silently. This is due
    to tf lite not supporting control dependencies.


#### Returns:

The converted data. For example if tflite was the destination, then
this will be a tflite flatbuffer in a bytes array.


#### Raises:

* <b>`ValueError`</b>: If the input tensor type is unknown
* <b>`RuntimeError`</b>: If TOCO fails to convert (in which case the runtime error's
    error text will contain the TOCO error log)