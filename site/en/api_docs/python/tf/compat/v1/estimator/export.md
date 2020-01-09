page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.estimator.export


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



All public utility methods for exporting Estimator to SavedModel.

<!-- Placeholder for "Used in" -->

This file includes functions and constants from core (model_utils) and export.py

## Classes

[`class ClassificationOutput`](../../../../tf/estimator/export/ClassificationOutput): Represents the output of a classification head.

[`class ExportOutput`](../../../../tf/estimator/export/ExportOutput): Represents an output of a model that can be served.

[`class PredictOutput`](../../../../tf/estimator/export/PredictOutput): Represents the output of a generic prediction head.

[`class RegressionOutput`](../../../../tf/estimator/export/RegressionOutput): Represents the output of a regression head.

[`class ServingInputReceiver`](../../../../tf/estimator/export/ServingInputReceiver): A return type for a serving_input_receiver_fn.

[`class TensorServingInputReceiver`](../../../../tf/estimator/export/TensorServingInputReceiver): A return type for a serving_input_receiver_fn.

## Functions

[`build_parsing_serving_input_receiver_fn(...)`](../../../../tf/estimator/export/build_parsing_serving_input_receiver_fn): Build a serving_input_receiver_fn expecting fed tf.Examples.

[`build_raw_serving_input_receiver_fn(...)`](../../../../tf/estimator/export/build_raw_serving_input_receiver_fn): Build a serving_input_receiver_fn expecting feature Tensors.
