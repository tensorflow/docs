description: All public utility methods for exporting Estimator to SavedModel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.export" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.estimator.export

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



All public utility methods for exporting Estimator to SavedModel.


This file includes functions and constants from core (model_utils) and export.py

## Classes

[`class ClassificationOutput`](../../../../tf/estimator/export/ClassificationOutput.md): Represents the output of a classification head.

[`class ExportOutput`](../../../../tf/estimator/export/ExportOutput.md): Represents an output of a model that can be served.

[`class PredictOutput`](../../../../tf/estimator/export/PredictOutput.md): Represents the output of a generic prediction head.

[`class RegressionOutput`](../../../../tf/estimator/export/RegressionOutput.md): Represents the output of a regression head.

[`class ServingInputReceiver`](../../../../tf/estimator/export/ServingInputReceiver.md): A return type for a serving_input_receiver_fn.

[`class TensorServingInputReceiver`](../../../../tf/estimator/export/TensorServingInputReceiver.md): A return type for a serving_input_receiver_fn.

## Functions

[`build_parsing_serving_input_receiver_fn(...)`](../../../../tf/estimator/export/build_parsing_serving_input_receiver_fn.md): Build a serving_input_receiver_fn expecting fed tf.Examples.

[`build_raw_serving_input_receiver_fn(...)`](../../../../tf/estimator/export/build_raw_serving_input_receiver_fn.md): Build a serving_input_receiver_fn expecting feature Tensors.

