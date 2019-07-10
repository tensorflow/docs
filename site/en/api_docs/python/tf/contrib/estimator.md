page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.estimator

estimator python module.



Defined in [`contrib/estimator/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/estimator/__init__.py).

<!-- Placeholder for "Used in" -->

Importing from tensorflow.python.estimator
is unsupported and will soon break!

## Classes

[`class RNNClassifier`](../../tf/contrib/estimator/RNNClassifier): A classifier for TensorFlow RNN models.

[`class RNNEstimator`](../../tf/contrib/estimator/RNNEstimator): An Estimator for TensorFlow RNN models with user-specified head.

[`class SavedModelEstimator`](../../tf/contrib/estimator/SavedModelEstimator): Create an Estimator from a SavedModel.

[`class TowerOptimizer`](../../tf/contrib/estimator/TowerOptimizer): Gathers gradients from all towers and reduces them in the last one.

## Functions

[`DNNClassifierWithLayerAnnotations(...)`](../../tf/contrib/estimator/DNNClassifierWithLayerAnnotations): A classifier for TensorFlow DNN models with layer annotations.

[`DNNRegressorWithLayerAnnotations(...)`](../../tf/contrib/estimator/DNNRegressorWithLayerAnnotations): A regressor for TensorFlow DNN models with layer annotations.

[`add_metrics(...)`](../../tf/contrib/estimator/add_metrics): Creates a new <a href="../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a> which has given metrics.

[`binary_classification_head(...)`](../../tf/contrib/estimator/binary_classification_head): Creates a `_Head` for single label binary classification.

[`boosted_trees_classifier_train_in_memory(...)`](../../tf/contrib/estimator/boosted_trees_classifier_train_in_memory): Trains a boosted tree classifier with in memory dataset.

[`boosted_trees_regressor_train_in_memory(...)`](../../tf/contrib/estimator/boosted_trees_regressor_train_in_memory): Trains a boosted tree regressor with in memory dataset.

[`build_raw_supervised_input_receiver_fn(...)`](../../tf/contrib/estimator/build_raw_supervised_input_receiver_fn): Build a supervised_input_receiver_fn for raw features and labels.

[`build_supervised_input_receiver_fn_from_input_fn(...)`](../../tf/contrib/estimator/build_supervised_input_receiver_fn_from_input_fn): Get a function that returns a SupervisedInputReceiver matching an input_fn.

[`call_logit_fn(...)`](../../tf/contrib/estimator/call_logit_fn): Calls logit_fn.

[`clip_gradients_by_norm(...)`](../../tf/contrib/estimator/clip_gradients_by_norm): Returns an optimizer which clips gradients before applying them.

[`dnn_logit_fn_builder(...)`](../../tf/contrib/estimator/dnn_logit_fn_builder): Function builder for a dnn logit_fn.

[`export_all_saved_models(...)`](../../tf/contrib/estimator/export_all_saved_models): Exports requested train/eval/predict graphs as separate SavedModels. (deprecated)

[`export_saved_model_for_mode(...)`](../../tf/contrib/estimator/export_saved_model_for_mode): Exports a single train/eval/predict graph as a SavedModel. (deprecated)

[`forward_features(...)`](../../tf/contrib/estimator/forward_features): Forward features to predictions dictionary.

[`linear_logit_fn_builder(...)`](../../tf/contrib/estimator/linear_logit_fn_builder): Function builder for a linear logit_fn.

[`logistic_regression_head(...)`](../../tf/contrib/estimator/logistic_regression_head): Creates a `_Head` for logistic regression.

[`multi_class_head(...)`](../../tf/contrib/estimator/multi_class_head): Creates a `_Head` for multi class classification.

[`multi_head(...)`](../../tf/contrib/estimator/multi_head): Creates a `_Head` for multi-objective learning.

[`multi_label_head(...)`](../../tf/contrib/estimator/multi_label_head): Creates a `_Head` for multi-label classification.

[`poisson_regression_head(...)`](../../tf/contrib/estimator/poisson_regression_head): Creates a `_Head` for poisson regression using <a href="../../tf/nn/log_poisson_loss"><code>tf.nn.log_poisson_loss</code></a>.

[`regression_head(...)`](../../tf/contrib/estimator/regression_head): Creates a `_Head` for regression using the `mean_squared_error` loss.

[`replicate_model_fn(...)`](../../tf/contrib/estimator/replicate_model_fn): Replicate `Estimator.model_fn` over GPUs. (deprecated)

