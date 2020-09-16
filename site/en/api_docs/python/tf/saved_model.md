description: Public API for tf.saved_model namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.saved_model" />
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

# Module: tf.saved_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.saved_model namespace.



## Classes

[`class Asset`](../tf/saved_model/Asset.md): Represents a file asset to hermetically include in a SavedModel.

[`class SaveOptions`](../tf/saved_model/SaveOptions.md): Options for saving to SavedModel.

## Functions

[`contains_saved_model(...)`](../tf/saved_model/contains_saved_model.md): Checks whether the provided export directory could contain a SavedModel.

[`load(...)`](../tf/saved_model/load.md): Load a SavedModel from `export_dir`.

[`save(...)`](../tf/saved_model/save.md): Exports the Trackable object `obj` to [SavedModel format](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md).

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
