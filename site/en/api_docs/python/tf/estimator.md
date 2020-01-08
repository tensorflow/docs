page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.estimator



Defined in [`tensorflow/python/estimator/api/estimator/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/estimator/api/estimator/__init__.py).

Estimator: High level tools for working with models.

## Modules

[`export`](../tf/estimator/export) module: Utility methods for exporting Estimator.

[`inputs`](../tf/estimator/inputs) module: Utility methods to create simple input_fns.

## Classes

[`class BaselineClassifier`](../tf/estimator/BaselineClassifier): A classifier that can establish a simple baseline.

[`class BaselineRegressor`](../tf/estimator/BaselineRegressor): A regressor that can establish a simple baseline.

[`class BestExporter`](../tf/estimator/BestExporter): This class exports the serving graph and checkpoints of the best models.

[`class BoostedTreesClassifier`](../tf/estimator/BoostedTreesClassifier): A Classifier for Tensorflow Boosted Trees models.

[`class BoostedTreesRegressor`](../tf/estimator/BoostedTreesRegressor): A Regressor for Tensorflow Boosted Trees models.

[`class DNNClassifier`](../tf/estimator/DNNClassifier): A classifier for TensorFlow DNN models.

[`class DNNLinearCombinedClassifier`](../tf/estimator/DNNLinearCombinedClassifier): An estimator for TensorFlow Linear and DNN joined classification models.

[`class DNNLinearCombinedRegressor`](../tf/estimator/DNNLinearCombinedRegressor): An estimator for TensorFlow Linear and DNN joined models for regression.

[`class DNNRegressor`](../tf/estimator/DNNRegressor): A regressor for TensorFlow DNN models.

[`class Estimator`](../tf/estimator/Estimator): Estimator class to train and evaluate TensorFlow models.

[`class EstimatorSpec`](../tf/estimator/EstimatorSpec): Ops and objects returned from a `model_fn` and passed to an `Estimator`.

[`class EvalSpec`](../tf/estimator/EvalSpec): Configuration for the "eval" part for the `train_and_evaluate` call.

[`class Exporter`](../tf/estimator/Exporter): A class representing a type of model export.

[`class FinalExporter`](../tf/estimator/FinalExporter): This class exports the serving graph and checkpoints in the end.

[`class LatestExporter`](../tf/estimator/LatestExporter): This class regularly exports the serving graph and checkpoints.

[`class LinearClassifier`](../tf/estimator/LinearClassifier): Linear classifier model.

[`class LinearRegressor`](../tf/estimator/LinearRegressor): An estimator for TensorFlow Linear regression problems.

[`class ModeKeys`](../tf/estimator/ModeKeys): Standard names for model modes.

[`class RunConfig`](../tf/estimator/RunConfig): This class specifies the configurations for an `Estimator` run.

[`class TrainSpec`](../tf/estimator/TrainSpec): Configuration for the "train" part for the `train_and_evaluate` call.

[`class VocabInfo`](../tf/train/VocabInfo): Vocabulary information for warm-starting.

[`class WarmStartSettings`](../tf/estimator/WarmStartSettings): Settings for warm-starting in `tf.estimator.Estimators`.

## Functions

[`classifier_parse_example_spec(...)`](../tf/estimator/classifier_parse_example_spec): Generates parsing spec for tf.parse_example to be used with classifiers.

[`regressor_parse_example_spec(...)`](../tf/estimator/regressor_parse_example_spec): Generates parsing spec for tf.parse_example to be used with regressors.

[`train_and_evaluate(...)`](../tf/estimator/train_and_evaluate): Train and evaluate the `estimator`.

