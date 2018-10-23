

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.estimator.export



Defined in [`tensorflow/python/estimator/export/export_lib.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/estimator/export/export_lib.py).

Utility methods for exporting Estimator.

## Classes

[`class ClassificationOutput`](../../tf/estimator/export/ClassificationOutput): Represents the output of a classification head.

[`class ExportOutput`](../../tf/estimator/export/ExportOutput): Represents an output of a model that can be served.

[`class PredictOutput`](../../tf/estimator/export/PredictOutput): Represents the output of a generic prediction head.

[`class RegressionOutput`](../../tf/estimator/export/RegressionOutput): Represents the output of a regression head.

[`class ServingInputReceiver`](../../tf/estimator/export/ServingInputReceiver): A return type for a serving_input_receiver_fn.

## Functions

[`build_parsing_serving_input_receiver_fn(...)`](../../tf/estimator/export/build_parsing_serving_input_receiver_fn): Build a serving_input_receiver_fn expecting fed tf.Examples.

[`build_raw_serving_input_receiver_fn(...)`](../../tf/estimator/export/build_raw_serving_input_receiver_fn): Build a serving_input_receiver_fn expecting feature Tensors.

