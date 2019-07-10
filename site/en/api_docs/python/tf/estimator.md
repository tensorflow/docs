page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.estimator



### Aliases:

* Module `tf.compat.v1.estimator`
* Module `tf.estimator`



Defined in [`python/estimator/api/_v1/estimator/__init__.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/api/_v1/estimator/__init__.py).

<!-- Placeholder for "Used in" -->


## Modules

[`experimental`](../tf/estimator/experimental) module

[`export`](../tf/estimator/export) module

[`inputs`](../tf/estimator/inputs) module

[`tpu`](../tf/estimator/tpu) module

## Classes

[`class BaselineClassifier`](../tf/estimator/BaselineClassifier): A classifier that can establish a simple baseline.

[`class BaselineEstimator`](../tf/estimator/BaselineEstimator): An estimator that can establish a simple baseline.

[`class BaselineRegressor`](../tf/estimator/BaselineRegressor): A regressor that can establish a simple baseline.

[`class BestExporter`](../tf/estimator/BestExporter): This class exports the serving graph and checkpoints of the best models.

[`class BoostedTreesClassifier`](../tf/estimator/BoostedTreesClassifier): A Classifier for Tensorflow Boosted Trees models.

[`class BoostedTreesEstimator`](../tf/estimator/BoostedTreesEstimator): An Estimator for Tensorflow Boosted Trees models.

[`class BoostedTreesRegressor`](../tf/estimator/BoostedTreesRegressor): A Regressor for Tensorflow Boosted Trees models.

[`class CheckpointSaverHook`](../tf/train/CheckpointSaverHook): Saves checkpoints every N steps or seconds.

[`class CheckpointSaverListener`](../tf/train/CheckpointSaverListener): Interface for listeners that take action before or after checkpoint save.

[`class DNNClassifier`](../tf/estimator/DNNClassifier): A classifier for TensorFlow DNN models.

[`class DNNEstimator`](../tf/estimator/DNNEstimator): An estimator for TensorFlow DNN models with user-specified head.

[`class DNNLinearCombinedClassifier`](../tf/estimator/DNNLinearCombinedClassifier): An estimator for TensorFlow Linear and DNN joined classification models.

[`class DNNLinearCombinedEstimator`](../tf/estimator/DNNLinearCombinedEstimator): An estimator for TensorFlow Linear and DNN joined models with custom head.

[`class DNNLinearCombinedRegressor`](../tf/estimator/DNNLinearCombinedRegressor): An estimator for TensorFlow Linear and DNN joined models for regression.

[`class DNNRegressor`](../tf/estimator/DNNRegressor): A regressor for TensorFlow DNN models.

[`class Estimator`](../tf/estimator/Estimator): Estimator class to train and evaluate TensorFlow models.

[`class EstimatorSpec`](../tf/estimator/EstimatorSpec): Ops and objects returned from a `model_fn` and passed to an `Estimator`.

[`class EvalSpec`](../tf/estimator/EvalSpec): Configuration for the "eval" part for the `train_and_evaluate` call.

[`class Exporter`](../tf/estimator/Exporter): A class representing a type of model export.

[`class FeedFnHook`](../tf/train/FeedFnHook): Runs `feed_fn` and sets the `feed_dict` accordingly.

[`class FinalExporter`](../tf/estimator/FinalExporter): This class exports the serving graph and checkpoints at the end.

[`class FinalOpsHook`](../tf/train/FinalOpsHook): A hook which evaluates `Tensors` at the end of a session.

[`class GlobalStepWaiterHook`](../tf/train/GlobalStepWaiterHook): Delays execution until global step reaches `wait_until_step`.

[`class LatestExporter`](../tf/estimator/LatestExporter): This class regularly exports the serving graph and checkpoints.

[`class LinearClassifier`](../tf/estimator/LinearClassifier): Linear classifier model.

[`class LinearEstimator`](../tf/estimator/LinearEstimator): An estimator for TensorFlow linear models with user-specified head.

[`class LinearRegressor`](../tf/estimator/LinearRegressor): An estimator for TensorFlow Linear regression problems.

[`class LoggingTensorHook`](../tf/train/LoggingTensorHook): Prints the given tensors every N local steps, every N seconds, or at end.

[`class ModeKeys`](../tf/estimator/ModeKeys): Standard names for Estimator model modes.

[`class NanLossDuringTrainingError`](../tf/train/NanLossDuringTrainingError)

[`class NanTensorHook`](../tf/train/NanTensorHook): Monitors the loss tensor and stops training if loss is NaN.

[`class ProfilerHook`](../tf/train/ProfilerHook): Captures CPU/GPU profiling information every N steps or seconds.

[`class RunConfig`](../tf/estimator/RunConfig): This class specifies the configurations for an `Estimator` run.

[`class SecondOrStepTimer`](../tf/train/SecondOrStepTimer): Timer that triggers at most once every N seconds or once every N steps.

[`class SessionRunArgs`](../tf/train/SessionRunArgs): Represents arguments to be added to a <a href="../tf/InteractiveSession#run"><code>Session.run()</code></a> call.

[`class SessionRunContext`](../tf/train/SessionRunContext): Provides information about the `session.run()` call being made.

[`class SessionRunHook`](../tf/train/SessionRunHook): Hook to extend calls to MonitoredSession.run().

[`class SessionRunValues`](../tf/train/SessionRunValues): Contains the results of <a href="../tf/InteractiveSession#run"><code>Session.run()</code></a>.

[`class StepCounterHook`](../tf/train/StepCounterHook): Hook that counts steps per second.

[`class StopAtStepHook`](../tf/train/StopAtStepHook): Hook that requests stop at a specified step.

[`class SummarySaverHook`](../tf/train/SummarySaverHook): Saves summaries every N steps.

[`class TrainSpec`](../tf/estimator/TrainSpec): Configuration for the "train" part for the `train_and_evaluate` call.

[`class VocabInfo`](../tf/train/VocabInfo): Vocabulary information for warm-starting.

[`class WarmStartSettings`](../tf/estimator/WarmStartSettings): Settings for warm-starting in `tf.estimator.Estimators`.

## Functions

[`add_metrics(...)`](../tf/estimator/add_metrics): Creates a new <a href="../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a> which has given metrics.

[`classifier_parse_example_spec(...)`](../tf/estimator/classifier_parse_example_spec): Generates parsing spec for tf.parse_example to be used with classifiers.

[`regressor_parse_example_spec(...)`](../tf/estimator/regressor_parse_example_spec): Generates parsing spec for tf.parse_example to be used with regressors.

[`train_and_evaluate(...)`](../tf/estimator/train_and_evaluate): Train and evaluate the `estimator`.

