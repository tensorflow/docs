description: SignatureDef utility functions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.saved_model.signature_def_utils" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.saved_model.signature_def_utils

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



SignatureDef utility functions.


Utility functions for building and inspecting SignatureDef protos.

## Classes

[`class MethodNameUpdater`](../../../../tf/compat/v1/saved_model/signature_def_utils/MethodNameUpdater.md): Updates the method name(s) of the SavedModel stored in the given path.

## Functions

[`build_signature_def(...)`](../../../../tf/compat/v1/saved_model/build_signature_def.md): Utility function to build a SignatureDef protocol buffer.

[`classification_signature_def(...)`](../../../../tf/compat/v1/saved_model/classification_signature_def.md): Creates classification signature from given examples and predictions.

[`is_valid_signature(...)`](../../../../tf/compat/v1/saved_model/is_valid_signature.md): Determine whether a SignatureDef can be served by TensorFlow Serving.

[`predict_signature_def(...)`](../../../../tf/compat/v1/saved_model/predict_signature_def.md): Creates prediction signature from given inputs and outputs.

[`regression_signature_def(...)`](../../../../tf/compat/v1/saved_model/regression_signature_def.md): Creates regression signature from given examples and predictions.

