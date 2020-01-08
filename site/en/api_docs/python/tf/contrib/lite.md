page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.lite



Defined in [`tensorflow/contrib/lite/python/lite.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/lite/python/lite.py).

TensorFlow Lite tooling helper functionality.

EXPERIMENTAL: APIs here are unstable and likely to change without notice.



## Modules

[`constants`](../../tf/contrib/lite/constants) module: Constants for TFLite.

## Classes

[`class ConverterMode`](../../tf/contrib/lite/ConverterMode): Enum class defining the converters available to generate TFLite models.

[`class DecodeError`](../../tf/contrib/lite/DecodeError)

[`class Interpreter`](../../tf/contrib/lite/Interpreter): Interpreter inferace for TF-Lite Models.

[`class OpHint`](../../tf/contrib/lite/OpHint): A class that helps build tflite function invocations.

[`class TFLiteConverter`](../../tf/contrib/lite/TFLiteConverter): Convert a TensorFlow model into `output_format` using TOCO.

[`class TocoConverter`](../../tf/contrib/lite/TocoConverter): Convert a TensorFlow model into `output_format` using TOCO.

## Functions

[`build_toco_convert_protos(...)`](../../tf/contrib/lite/build_toco_convert_protos): Builds protocol buffers describing a conversion of a model using TOCO.

[`convert_op_hints_to_stubs(...)`](../../tf/contrib/lite/convert_op_hints_to_stubs): Converts a graphdef with LiteOp hints into stub operations.

[`toco_convert(...)`](../../tf/contrib/lite/toco_convert): Convert a model using TOCO. (deprecated)

[`toco_convert_protos(...)`](../../tf/contrib/lite/toco_convert_protos): Convert `input_data_str` according to model and toco parameters.

## Other Members

<h3 id="PY3"><code>PY3</code></h3>

<h3 id="absolute_import"><code>absolute_import</code></h3>

<h3 id="division"><code>division</code></h3>

<h3 id="print_function"><code>print_function</code></h3>

