description: Public API for tf.estimator.experimental namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.experimental" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.estimator.experimental

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.estimator.experimental namespace.



## Classes

[`class InMemoryEvaluatorHook`](../../tf/estimator/experimental/InMemoryEvaluatorHook.md): Hook to run evaluation in training without a checkpoint.

[`class LinearSDCA`](../../tf/estimator/experimental/LinearSDCA.md): Stochastic Dual Coordinate Ascent helper for linear estimators.

[`class RNNClassifier`](../../tf/estimator/experimental/RNNClassifier.md): A classifier for TensorFlow RNN models.

[`class RNNEstimator`](../../tf/estimator/experimental/RNNEstimator.md): An Estimator for TensorFlow RNN models with user-specified head.

## Functions

[`build_raw_supervised_input_receiver_fn(...)`](../../tf/estimator/experimental/build_raw_supervised_input_receiver_fn.md): Build a supervised_input_receiver_fn for raw features and labels.

[`call_logit_fn(...)`](../../tf/estimator/experimental/call_logit_fn.md): Calls logit_fn (experimental).

[`make_early_stopping_hook(...)`](../../tf/estimator/experimental/make_early_stopping_hook.md): Creates early-stopping hook.

[`make_stop_at_checkpoint_step_hook(...)`](../../tf/estimator/experimental/make_stop_at_checkpoint_step_hook.md): Creates a proper StopAtCheckpointStepHook based on chief status.

[`stop_if_higher_hook(...)`](../../tf/estimator/experimental/stop_if_higher_hook.md): Creates hook to stop if the given metric is higher than the threshold.

[`stop_if_lower_hook(...)`](../../tf/estimator/experimental/stop_if_lower_hook.md): Creates hook to stop if the given metric is lower than the threshold.

[`stop_if_no_decrease_hook(...)`](../../tf/estimator/experimental/stop_if_no_decrease_hook.md): Creates hook to stop if metric does not decrease within given max steps.

[`stop_if_no_increase_hook(...)`](../../tf/estimator/experimental/stop_if_no_increase_hook.md): Creates hook to stop if metric does not increase within given max steps.

