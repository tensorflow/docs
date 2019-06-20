page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.estimator



Defined in [`tensorflow/contrib/estimator/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/estimator/__init__.py).

Experimental utilities re:tf.estimator.*.

## Classes

[`class BaselineEstimator`](../../tf/contrib/estimator/BaselineEstimator): An estimator that can establish a simple baseline.

[`class DNNEstimator`](../../tf/contrib/estimator/DNNEstimator): An estimator for TensorFlow DNN models with user-specified head.

[`class DNNLinearCombinedEstimator`](../../tf/contrib/estimator/DNNLinearCombinedEstimator): An estimator for TensorFlow Linear and DNN joined models with custom head.

[`class InMemoryEvaluatorHook`](../../tf/contrib/estimator/InMemoryEvaluatorHook): Hook to run evaluation in training without a checkpoint.

[`class LinearEstimator`](../../tf/contrib/estimator/LinearEstimator): An estimator for TensorFlow linear models with user-specified head.

[`class RNNClassifier`](../../tf/contrib/estimator/RNNClassifier): A classifier for TensorFlow RNN models.

[`class RNNEstimator`](../../tf/contrib/estimator/RNNEstimator): An Estimator for TensorFlow RNN models with user-specified head.

[`class TowerOptimizer`](../../tf/contrib/estimator/TowerOptimizer): Gathers gradients from all towers and reduces them in the last one.

## Functions

[`add_metrics(...)`](../../tf/contrib/estimator/add_metrics): Creates a new <a href="../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a> which has given metrics.

[`binary_classification_head(...)`](../../tf/contrib/estimator/binary_classification_head): Creates a `_Head` for single label binary classification.

[`boosted_trees_classifier_train_in_memory(...)`](../../tf/contrib/estimator/boosted_trees_classifier_train_in_memory): Trains a boosted tree classifier with in memory dataset.

[`boosted_trees_regressor_train_in_memory(...)`](../../tf/contrib/estimator/boosted_trees_regressor_train_in_memory): Trains a boosted tree regressor with in memory dataset.

[`call_logit_fn(...)`](../../tf/contrib/estimator/call_logit_fn): Calls logit_fn.

[`clip_gradients_by_norm(...)`](../../tf/contrib/estimator/clip_gradients_by_norm): Returns an optimizer which clips gradients before applying them.

[`dnn_logit_fn_builder(...)`](../../tf/contrib/estimator/dnn_logit_fn_builder): Function builder for a dnn logit_fn.

[`export_all_saved_models(...)`](../../tf/contrib/estimator/export_all_saved_models): Exports requested train/eval/predict graphs as separate SavedModels.

[`export_saved_model_for_mode(...)`](../../tf/contrib/estimator/export_saved_model_for_mode): Exports a single train/eval/predict graph as a SavedModel.

[`forward_features(...)`](../../tf/contrib/estimator/forward_features): Forward features to predictions dictionary.

[`linear_logit_fn_builder(...)`](../../tf/contrib/estimator/linear_logit_fn_builder): Function builder for a linear logit_fn.

[`logistic_regression_head(...)`](../../tf/contrib/estimator/logistic_regression_head): Creates a `_Head` for logistic regression.

[`make_early_stopping_hook(...)`](../../tf/contrib/estimator/make_early_stopping_hook): Creates early-stopping hook.

[`multi_class_head(...)`](../../tf/contrib/estimator/multi_class_head): Creates a `_Head` for multi class classification.

[`multi_head(...)`](../../tf/contrib/estimator/multi_head): Creates a `_Head` for multi-objective learning.

[`multi_label_head(...)`](../../tf/contrib/estimator/multi_label_head): Creates a `_Head` for multi-label classification.

[`poisson_regression_head(...)`](../../tf/contrib/estimator/poisson_regression_head): Creates a `_Head` for poisson regression using <a href="../../tf/nn/log_poisson_loss"><code>tf.nn.log_poisson_loss</code></a>.

[`read_eval_metrics(...)`](../../tf/contrib/estimator/read_eval_metrics): Helper to read eval metrics from eval summary files.

[`regression_head(...)`](../../tf/contrib/estimator/regression_head): Creates a `_Head` for regression using the `mean_squared_error` loss.

[`replicate_model_fn(...)`](../../tf/contrib/estimator/replicate_model_fn): Replicate `Estimator.model_fn` over GPUs. (deprecated)

[`stop_if_higher_hook(...)`](../../tf/contrib/estimator/stop_if_higher_hook): Creates hook to stop if the given metric is higher than the threshold.

[`stop_if_lower_hook(...)`](../../tf/contrib/estimator/stop_if_lower_hook): Creates hook to stop if the given metric is lower than the threshold.

[`stop_if_no_decrease_hook(...)`](../../tf/contrib/estimator/stop_if_no_decrease_hook): Creates hook to stop if metric does not decrease within given max steps.

[`stop_if_no_increase_hook(...)`](../../tf/contrib/estimator/stop_if_no_increase_hook): Creates hook to stop if metric does not increase within given max steps.

