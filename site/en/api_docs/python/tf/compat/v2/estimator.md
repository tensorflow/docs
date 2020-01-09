page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.estimator


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Estimator: High level tools for working with models.

<!-- Placeholder for "Used in" -->


## Modules

[`experimental`](../../../tf/estimator/experimental) module: Public API for tf.estimator.experimental namespace.

[`export`](../../../tf/estimator/export) module: All public utility methods for exporting Estimator to SavedModel.

## Classes

[`class BaselineClassifier`](../../../tf/estimator/BaselineClassifier): A classifier that can establish a simple baseline.

[`class BaselineEstimator`](../../../tf/estimator/BaselineEstimator): An estimator that can establish a simple baseline.

[`class BaselineRegressor`](../../../tf/estimator/BaselineRegressor): A regressor that can establish a simple baseline.

[`class BestExporter`](../../../tf/estimator/BestExporter): This class exports the serving graph and checkpoints of the best models.

[`class BinaryClassHead`](../../../tf/estimator/BinaryClassHead): Creates a `Head` for single label binary classification.

[`class BoostedTreesClassifier`](../../../tf/estimator/BoostedTreesClassifier): A Classifier for Tensorflow Boosted Trees models.

[`class BoostedTreesEstimator`](../../../tf/estimator/BoostedTreesEstimator): An Estimator for Tensorflow Boosted Trees models.

[`class BoostedTreesRegressor`](../../../tf/estimator/BoostedTreesRegressor): A Regressor for Tensorflow Boosted Trees models.

[`class CheckpointSaverHook`](../../../tf/estimator/CheckpointSaverHook): Saves checkpoints every N steps or seconds.

[`class CheckpointSaverListener`](../../../tf/estimator/CheckpointSaverListener): Interface for listeners that take action before or after checkpoint save.

[`class DNNClassifier`](../../../tf/estimator/DNNClassifier): A classifier for TensorFlow DNN models.

[`class DNNEstimator`](../../../tf/estimator/DNNEstimator): An estimator for TensorFlow DNN models with user-specified head.

[`class DNNLinearCombinedClassifier`](../../../tf/estimator/DNNLinearCombinedClassifier): An estimator for TensorFlow Linear and DNN joined classification models.

[`class DNNLinearCombinedEstimator`](../../../tf/estimator/DNNLinearCombinedEstimator): An estimator for TensorFlow Linear and DNN joined models with custom head.

[`class DNNLinearCombinedRegressor`](../../../tf/estimator/DNNLinearCombinedRegressor): An estimator for TensorFlow Linear and DNN joined models for regression.

[`class DNNRegressor`](../../../tf/estimator/DNNRegressor): A regressor for TensorFlow DNN models.

[`class Estimator`](../../../tf/estimator/Estimator): Estimator class to train and evaluate TensorFlow models.

[`class EstimatorSpec`](../../../tf/estimator/EstimatorSpec): Ops and objects returned from a `model_fn` and passed to an `Estimator`.

[`class EvalSpec`](../../../tf/estimator/EvalSpec): Configuration for the "eval" part for the `train_and_evaluate` call.

[`class Exporter`](../../../tf/estimator/Exporter): A class representing a type of model export.

[`class FeedFnHook`](../../../tf/estimator/FeedFnHook): Runs `feed_fn` and sets the `feed_dict` accordingly.

[`class FinalExporter`](../../../tf/estimator/FinalExporter): This class exports the serving graph and checkpoints at the end.

[`class FinalOpsHook`](../../../tf/estimator/FinalOpsHook): A hook which evaluates `Tensors` at the end of a session.

[`class GlobalStepWaiterHook`](../../../tf/estimator/GlobalStepWaiterHook): Delays execution until global step reaches `wait_until_step`.

[`class Head`](../../../tf/estimator/Head): Interface for the head/top of a model.

[`class LatestExporter`](../../../tf/estimator/LatestExporter): This class regularly exports the serving graph and checkpoints.

[`class LinearClassifier`](../../../tf/estimator/LinearClassifier): Linear classifier model.

[`class LinearEstimator`](../../../tf/estimator/LinearEstimator): An estimator for TensorFlow linear models with user-specified head.

[`class LinearRegressor`](../../../tf/estimator/LinearRegressor): An estimator for TensorFlow Linear regression problems.

[`class LoggingTensorHook`](../../../tf/estimator/LoggingTensorHook): Prints the given tensors every N local steps, every N seconds, or at end.

[`class LogisticRegressionHead`](../../../tf/estimator/LogisticRegressionHead): Creates a `Head` for logistic regression.

[`class ModeKeys`](../../../tf/estimator/ModeKeys): Standard names for Estimator model modes.

[`class MultiClassHead`](../../../tf/estimator/MultiClassHead): Creates a `Head` for multi class classification.

[`class MultiHead`](../../../tf/estimator/MultiHead): Creates a `Head` for multi-objective learning.

[`class MultiLabelHead`](../../../tf/estimator/MultiLabelHead): Creates a `Head` for multi-label classification.

[`class NanLossDuringTrainingError`](../../../tf/estimator/NanLossDuringTrainingError): Unspecified run-time error.

[`class NanTensorHook`](../../../tf/estimator/NanTensorHook): Monitors the loss tensor and stops training if loss is NaN.

[`class PoissonRegressionHead`](../../../tf/estimator/PoissonRegressionHead): Creates a `Head` for poisson regression using <a href="../../../tf/nn/log_poisson_loss"><code>tf.nn.log_poisson_loss</code></a>.

[`class ProfilerHook`](../../../tf/estimator/ProfilerHook): Captures CPU/GPU profiling information every N steps or seconds.

[`class RegressionHead`](../../../tf/estimator/RegressionHead): Creates a `Head` for regression using the `mean_squared_error` loss.

[`class RunConfig`](../../../tf/estimator/RunConfig): This class specifies the configurations for an `Estimator` run.

[`class SecondOrStepTimer`](../../../tf/estimator/SecondOrStepTimer): Timer that triggers at most once every N seconds or once every N steps.

[`class SessionRunArgs`](../../../tf/estimator/SessionRunArgs): Represents arguments to be added to a `Session.run()` call.

[`class SessionRunContext`](../../../tf/estimator/SessionRunContext): Provides information about the `session.run()` call being made.

[`class SessionRunHook`](../../../tf/estimator/SessionRunHook): Hook to extend calls to MonitoredSession.run().

[`class SessionRunValues`](../../../tf/estimator/SessionRunValues): Contains the results of `Session.run()`.

[`class StepCounterHook`](../../../tf/estimator/StepCounterHook): Hook that counts steps per second.

[`class StopAtStepHook`](../../../tf/estimator/StopAtStepHook): Hook that requests stop at a specified step.

[`class SummarySaverHook`](../../../tf/estimator/SummarySaverHook): Saves summaries every N steps.

[`class TrainSpec`](../../../tf/estimator/TrainSpec): Configuration for the "train" part for the `train_and_evaluate` call.

[`class VocabInfo`](../../../tf/estimator/VocabInfo): Vocabulary information for warm-starting.

[`class WarmStartSettings`](../../../tf/estimator/WarmStartSettings): Settings for warm-starting in `tf.estimator.Estimators`.

## Functions

[`add_metrics(...)`](../../../tf/estimator/add_metrics): Creates a new <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a> which has given metrics.

[`classifier_parse_example_spec(...)`](../../../tf/estimator/classifier_parse_example_spec): Generates parsing spec for tf.parse_example to be used with classifiers.

[`regressor_parse_example_spec(...)`](../../../tf/estimator/regressor_parse_example_spec): Generates parsing spec for tf.parse_example to be used with regressors.

[`train_and_evaluate(...)`](../../../tf/estimator/train_and_evaluate): Train and evaluate the `estimator`.
