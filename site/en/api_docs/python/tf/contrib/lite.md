page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.lite



Defined in [`tensorflow/contrib/lite/python/lite.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/lite/python/lite.py).

TensorFlow Lite tooling helper functionality.

EXPERIMENTAL: APIs here are unstable and likely to change without notice.



## Modules

[`constants`](../../tf/contrib/lite/constants) module: Constants for TFLite.

[`signature_constants`](../../tf/contrib/lite/signature_constants) module: Signature constants for SavedModel save and restore operations.

[`tag_constants`](../../tf/contrib/lite/tag_constants) module: Common tags used for graphs in SavedModel.

[`tf_graph_util`](../../tf/contrib/lite/tf_graph_util) module: Helpers to manipulate a tensor graph in python.

## Classes

[`class DecodeError`](../../tf/contrib/lite/DecodeError)

[`class Interpreter`](../../tf/contrib/lite/Interpreter): Interpreter inferace for TF-Lite Models.

[`class OpHint`](../../tf/contrib/lite/OpHint): A class that helps build tflite function invocations.

[`class TocoConverter`](../../tf/contrib/lite/TocoConverter): Convert a TensorFlow model into `output_format` using TOCO.

## Functions

[`build_toco_convert_protos(...)`](../../tf/contrib/lite/build_toco_convert_protos): Builds protocol buffers describing a conversion of a model using TOCO.

[`convert_op_hints_to_stubs(...)`](../../tf/contrib/lite/convert_op_hints_to_stubs): Converts a graphdef with LiteOp hints into stub operations.

[`freeze_saved_model(...)`](../../tf/contrib/lite/freeze_saved_model): Converts a SavedModel to a frozen graph.

[`get_tensors_from_tensor_names(...)`](../../tf/contrib/lite/get_tensors_from_tensor_names): Gets the Tensors associated with the `tensor_names` in the provided graph.

[`global_variables_initializer(...)`](../../tf/global_variables_initializer): Returns an Op that initializes global variables.

[`import_graph_def(...)`](../../tf/import_graph_def): Imports the graph from `graph_def` into the current default `Graph`. (deprecated arguments)

[`set_tensor_shapes(...)`](../../tf/contrib/lite/set_tensor_shapes): Sets Tensor shape for each tensor if the shape is defined.

[`tensor_name(...)`](../../tf/contrib/lite/tensor_name)

[`toco_convert(...)`](../../tf/contrib/lite/toco_convert): "Convert a model using TOCO.

[`toco_convert_protos(...)`](../../tf/contrib/lite/toco_convert_protos): Convert `input_data_str` according to model and toco parameters.

## Other Members

`PY3`

`absolute_import`

`division`

`print_function`

