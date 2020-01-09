page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.saved_model


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/v1/saved_model">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Public API for tf.saved_model namespace.

<!-- Placeholder for "Used in" -->


## Modules

[`builder`](../../../tf/compat/v1/saved_model/builder) module: SavedModel builder.

[`constants`](../../../tf/compat/v1/saved_model/constants) module: Constants for SavedModel save and restore operations.

[`experimental`](../../../tf/compat/v1/saved_model/experimental) module: Public API for tf.saved_model.experimental namespace.

[`loader`](../../../tf/compat/v1/saved_model/loader) module: Loader functionality for SavedModel with hermetic, language-neutral exports.

[`main_op`](../../../tf/compat/v1/saved_model/main_op) module: SavedModel main op.

[`signature_constants`](../../../tf/compat/v1/saved_model/signature_constants) module: Signature constants for SavedModel save and restore operations.

[`signature_def_utils`](../../../tf/compat/v1/saved_model/signature_def_utils) module: SignatureDef utility functions.

[`tag_constants`](../../../tf/compat/v1/saved_model/tag_constants) module: Common tags used for graphs in SavedModel.

[`utils`](../../../tf/compat/v1/saved_model/utils) module: SavedModel utility functions.

## Classes

[`class Builder`](../../../tf/saved_model/Builder): Builds the `SavedModel` protocol buffer and saves variables and assets.

## Functions

[`build_signature_def(...)`](../../../tf/saved_model/build_signature_def): Utility function to build a SignatureDef protocol buffer.

[`build_tensor_info(...)`](../../../tf/saved_model/build_tensor_info): Utility function to build TensorInfo proto from a Tensor. (deprecated)

[`classification_signature_def(...)`](../../../tf/saved_model/classification_signature_def): Creates classification signature from given examples and predictions.

[`contains_saved_model(...)`](../../../tf/saved_model/contains_saved_model): Checks whether the provided export directory could contain a SavedModel.

[`get_tensor_from_tensor_info(...)`](../../../tf/saved_model/get_tensor_from_tensor_info): Returns the Tensor or CompositeTensor described by a TensorInfo proto. (deprecated)

[`is_valid_signature(...)`](../../../tf/saved_model/is_valid_signature): Determine whether a SignatureDef can be served by TensorFlow Serving.

[`load(...)`](../../../tf/saved_model/load): Loads the model from a SavedModel as specified by tags. (deprecated)

[`load_v2(...)`](../../../tf/saved_model/load_v2): Load a SavedModel from `export_dir`.

[`main_op_with_restore(...)`](../../../tf/saved_model/main_op_with_restore): Returns a main op to init variables, tables and restore the graph. (deprecated)

[`maybe_saved_model_directory(...)`](../../../tf/saved_model/contains_saved_model): Checks whether the provided export directory could contain a SavedModel.

[`predict_signature_def(...)`](../../../tf/saved_model/predict_signature_def): Creates prediction signature from given inputs and outputs.

[`regression_signature_def(...)`](../../../tf/saved_model/regression_signature_def): Creates regression signature from given examples and predictions.

[`save(...)`](../../../tf/saved_model/save): Exports the Trackable object `obj` to [SavedModel format](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md).

[`simple_save(...)`](../../../tf/saved_model/simple_save): Convenience function to build a SavedModel suitable for serving. (deprecated)

## Other Members

* `ASSETS_DIRECTORY = 'assets'` <a id="ASSETS_DIRECTORY"></a>
* `ASSETS_KEY = 'saved_model_assets'` <a id="ASSETS_KEY"></a>
* `CLASSIFY_INPUTS = 'inputs'` <a id="CLASSIFY_INPUTS"></a>
* `CLASSIFY_METHOD_NAME = 'tensorflow/serving/classify'` <a id="CLASSIFY_METHOD_NAME"></a>
* `CLASSIFY_OUTPUT_CLASSES = 'classes'` <a id="CLASSIFY_OUTPUT_CLASSES"></a>
* `CLASSIFY_OUTPUT_SCORES = 'scores'` <a id="CLASSIFY_OUTPUT_SCORES"></a>
* `DEFAULT_SERVING_SIGNATURE_DEF_KEY = 'serving_default'` <a id="DEFAULT_SERVING_SIGNATURE_DEF_KEY"></a>
* `GPU = 'gpu'` <a id="GPU"></a>
* `LEGACY_INIT_OP_KEY = 'legacy_init_op'` <a id="LEGACY_INIT_OP_KEY"></a>
* `MAIN_OP_KEY = 'saved_model_main_op'` <a id="MAIN_OP_KEY"></a>
* `PREDICT_INPUTS = 'inputs'` <a id="PREDICT_INPUTS"></a>
* `PREDICT_METHOD_NAME = 'tensorflow/serving/predict'` <a id="PREDICT_METHOD_NAME"></a>
* `PREDICT_OUTPUTS = 'outputs'` <a id="PREDICT_OUTPUTS"></a>
* `REGRESS_INPUTS = 'inputs'` <a id="REGRESS_INPUTS"></a>
* `REGRESS_METHOD_NAME = 'tensorflow/serving/regress'` <a id="REGRESS_METHOD_NAME"></a>
* `REGRESS_OUTPUTS = 'outputs'` <a id="REGRESS_OUTPUTS"></a>
* `SAVED_MODEL_FILENAME_PB = 'saved_model.pb'` <a id="SAVED_MODEL_FILENAME_PB"></a>
* `SAVED_MODEL_FILENAME_PBTXT = 'saved_model.pbtxt'` <a id="SAVED_MODEL_FILENAME_PBTXT"></a>
* `SAVED_MODEL_SCHEMA_VERSION = 1` <a id="SAVED_MODEL_SCHEMA_VERSION"></a>
* `SERVING = 'serve'` <a id="SERVING"></a>
* `TPU = 'tpu'` <a id="TPU"></a>
* `TRAINING = 'train'` <a id="TRAINING"></a>
* `VARIABLES_DIRECTORY = 'variables'` <a id="VARIABLES_DIRECTORY"></a>
* `VARIABLES_FILENAME = 'variables'` <a id="VARIABLES_FILENAME"></a>
