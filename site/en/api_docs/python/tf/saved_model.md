page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.saved_model





Public API for tf.saved_model namespace.

## Modules

[`builder`](../tf/saved_model/builder) module: SavedModel builder.

[`constants`](../tf/saved_model/constants) module: Constants for SavedModel save and restore operations.

[`loader`](../tf/saved_model/loader) module: Loader functionality for SavedModel with hermetic, language-neutral exports.

[`main_op`](../tf/saved_model/main_op) module: SavedModel main op.

[`signature_constants`](../tf/saved_model/signature_constants) module: Signature constants for SavedModel save and restore operations.

[`signature_def_utils`](../tf/saved_model/signature_def_utils) module: SignatureDef utility functions.

[`tag_constants`](../tf/saved_model/tag_constants) module: Common tags used for graphs in SavedModel.

[`utils`](../tf/saved_model/utils) module: SavedModel utility functions.

## Classes

[`class Builder`](../tf/saved_model/Builder): Builds the `SavedModel` protocol buffer and saves variables and assets.

## Functions

[`build_signature_def(...)`](../tf/saved_model/build_signature_def): Utility function to build a SignatureDef protocol buffer.

[`build_tensor_info(...)`](../tf/saved_model/build_tensor_info): Utility function to build TensorInfo proto.

[`classification_signature_def(...)`](../tf/saved_model/classification_signature_def): Creates classification signature from given examples and predictions.

[`get_tensor_from_tensor_info(...)`](../tf/saved_model/get_tensor_from_tensor_info): Returns the Tensor or SparseTensor described by a TensorInfo proto.

[`is_valid_signature(...)`](../tf/saved_model/is_valid_signature): Determine whether a SignatureDef can be served by TensorFlow Serving.

[`load(...)`](../tf/saved_model/load): Loads the model from a SavedModel as specified by tags.

[`main_op_with_restore(...)`](../tf/saved_model/main_op_with_restore): Returns a main op to init variables, tables and restore the graph.

[`maybe_saved_model_directory(...)`](../tf/saved_model/maybe_saved_model_directory): Checks whether the provided export directory could contain a SavedModel.

[`predict_signature_def(...)`](../tf/saved_model/predict_signature_def): Creates prediction signature from given inputs and outputs.

[`regression_signature_def(...)`](../tf/saved_model/regression_signature_def): Creates regression signature from given examples and predictions.

[`simple_save(...)`](../tf/saved_model/simple_save): Convenience function to build a SavedModel suitable for serving.

