description: Public API for tf.saved_model namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.saved_model" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="ASSETS_DIRECTORY"/>
<meta itemprop="property" content="ASSETS_KEY"/>
<meta itemprop="property" content="CLASSIFY_INPUTS"/>
<meta itemprop="property" content="CLASSIFY_METHOD_NAME"/>
<meta itemprop="property" content="CLASSIFY_OUTPUT_CLASSES"/>
<meta itemprop="property" content="CLASSIFY_OUTPUT_SCORES"/>
<meta itemprop="property" content="DEBUG_DIRECTORY"/>
<meta itemprop="property" content="DEBUG_INFO_FILENAME_PB"/>
<meta itemprop="property" content="DEFAULT_SERVING_SIGNATURE_DEF_KEY"/>
<meta itemprop="property" content="GPU"/>
<meta itemprop="property" content="LEGACY_INIT_OP_KEY"/>
<meta itemprop="property" content="MAIN_OP_KEY"/>
<meta itemprop="property" content="PREDICT_INPUTS"/>
<meta itemprop="property" content="PREDICT_METHOD_NAME"/>
<meta itemprop="property" content="PREDICT_OUTPUTS"/>
<meta itemprop="property" content="REGRESS_INPUTS"/>
<meta itemprop="property" content="REGRESS_METHOD_NAME"/>
<meta itemprop="property" content="REGRESS_OUTPUTS"/>
<meta itemprop="property" content="SAVED_MODEL_FILENAME_PB"/>
<meta itemprop="property" content="SAVED_MODEL_FILENAME_PBTXT"/>
<meta itemprop="property" content="SAVED_MODEL_SCHEMA_VERSION"/>
<meta itemprop="property" content="SERVING"/>
<meta itemprop="property" content="TPU"/>
<meta itemprop="property" content="TRAINING"/>
<meta itemprop="property" content="VARIABLES_DIRECTORY"/>
<meta itemprop="property" content="VARIABLES_FILENAME"/>
</div>

# Module: tf.compat.v1.saved_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.saved_model namespace.



## Modules

[`builder`](../../../tf/compat/v1/saved_model/builder.md) module: SavedModel builder.

[`constants`](../../../tf/compat/v1/saved_model/constants.md) module: Constants for SavedModel save and restore operations.

[`experimental`](../../../tf/compat/v1/saved_model/experimental.md) module: Public API for tf.saved_model.experimental namespace.

[`loader`](../../../tf/compat/v1/saved_model/loader.md) module: Loader functionality for SavedModel with hermetic, language-neutral exports.

[`main_op`](../../../tf/compat/v1/saved_model/main_op.md) module: SavedModel main op.

[`signature_constants`](../../../tf/compat/v1/saved_model/signature_constants.md) module: Signature constants for SavedModel save and restore operations.

[`signature_def_utils`](../../../tf/compat/v1/saved_model/signature_def_utils.md) module: SignatureDef utility functions.

[`tag_constants`](../../../tf/compat/v1/saved_model/tag_constants.md) module: Common tags used for graphs in SavedModel.

[`utils`](../../../tf/compat/v1/saved_model/utils.md) module: SavedModel utility functions.

## Classes

[`class Asset`](../../../tf/saved_model/Asset.md): Represents a file asset to hermetically include in a SavedModel.

[`class Builder`](../../../tf/compat/v1/saved_model/Builder.md): Builds the `SavedModel` protocol buffer and saves variables and assets.

[`class SaveOptions`](../../../tf/saved_model/SaveOptions.md): Options for saving to SavedModel.

## Functions

[`build_signature_def(...)`](../../../tf/compat/v1/saved_model/build_signature_def.md): Utility function to build a SignatureDef protocol buffer.

[`build_tensor_info(...)`](../../../tf/compat/v1/saved_model/build_tensor_info.md): Utility function to build TensorInfo proto from a Tensor. (deprecated)

[`classification_signature_def(...)`](../../../tf/compat/v1/saved_model/classification_signature_def.md): Creates classification signature from given examples and predictions.

[`contains_saved_model(...)`](../../../tf/compat/v1/saved_model/contains_saved_model.md): Checks whether the provided export directory could contain a SavedModel.

[`get_tensor_from_tensor_info(...)`](../../../tf/compat/v1/saved_model/get_tensor_from_tensor_info.md): Returns the Tensor or CompositeTensor described by a TensorInfo proto. (deprecated)

[`is_valid_signature(...)`](../../../tf/compat/v1/saved_model/is_valid_signature.md): Determine whether a SignatureDef can be served by TensorFlow Serving.

[`load(...)`](../../../tf/compat/v1/saved_model/load.md): Loads the model from a SavedModel as specified by tags. (deprecated)

[`load_v2(...)`](../../../tf/saved_model/load.md): Load a SavedModel from `export_dir`.

[`main_op_with_restore(...)`](../../../tf/compat/v1/saved_model/main_op_with_restore.md): Returns a main op to init variables, tables and restore the graph. (deprecated)

[`maybe_saved_model_directory(...)`](../../../tf/compat/v1/saved_model/contains_saved_model.md): Checks whether the provided export directory could contain a SavedModel.

[`predict_signature_def(...)`](../../../tf/compat/v1/saved_model/predict_signature_def.md): Creates prediction signature from given inputs and outputs.

[`regression_signature_def(...)`](../../../tf/compat/v1/saved_model/regression_signature_def.md): Creates regression signature from given examples and predictions.

[`save(...)`](../../../tf/saved_model/save.md): Exports the Trackable object `obj` to [SavedModel format](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md).

[`simple_save(...)`](../../../tf/compat/v1/saved_model/simple_save.md): Convenience function to build a SavedModel suitable for serving. (deprecated)

## Other Members

* `ASSETS_DIRECTORY = 'assets'` <a id="ASSETS_DIRECTORY"></a>
* `ASSETS_KEY = 'saved_model_assets'` <a id="ASSETS_KEY"></a>
* `CLASSIFY_INPUTS = 'inputs'` <a id="CLASSIFY_INPUTS"></a>
* `CLASSIFY_METHOD_NAME = 'tensorflow/serving/classify'` <a id="CLASSIFY_METHOD_NAME"></a>
* `CLASSIFY_OUTPUT_CLASSES = 'classes'` <a id="CLASSIFY_OUTPUT_CLASSES"></a>
* `CLASSIFY_OUTPUT_SCORES = 'scores'` <a id="CLASSIFY_OUTPUT_SCORES"></a>
* `DEBUG_DIRECTORY = 'debug'` <a id="DEBUG_DIRECTORY"></a>
* `DEBUG_INFO_FILENAME_PB = 'saved_model_debug_info.pb'` <a id="DEBUG_INFO_FILENAME_PB"></a>
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
