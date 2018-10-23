

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.metrics



Defined in [`tensorflow/python/ops/metrics.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/metrics.py).

Evaluation-related metrics.


## Functions

[`accuracy(...)`](../tf/metrics/accuracy): Calculates how often `predictions` matches `labels`.

[`auc(...)`](../tf/metrics/auc): Computes the approximate AUC via a Riemann sum.

[`false_negatives(...)`](../tf/metrics/false_negatives): Computes the total number of false negatives.

[`false_positives(...)`](../tf/metrics/false_positives): Sum the weights of false positives.

[`mean(...)`](../tf/metrics/mean): Computes the (weighted) mean of the given values.

[`mean_absolute_error(...)`](../tf/metrics/mean_absolute_error): Computes the mean absolute error between the labels and predictions.

[`mean_cosine_distance(...)`](../tf/metrics/mean_cosine_distance): Computes the cosine distance between the labels and predictions.

[`mean_iou(...)`](../tf/metrics/mean_iou): Calculate per-step mean Intersection-Over-Union (mIOU).

[`mean_per_class_accuracy(...)`](../tf/metrics/mean_per_class_accuracy): Calculates the mean of the per-class accuracies.

[`mean_relative_error(...)`](../tf/metrics/mean_relative_error): Computes the mean relative error by normalizing with the given values.

[`mean_squared_error(...)`](../tf/metrics/mean_squared_error): Computes the mean squared error between the labels and predictions.

[`mean_tensor(...)`](../tf/metrics/mean_tensor): Computes the element-wise (weighted) mean of the given tensors.

[`percentage_below(...)`](../tf/metrics/percentage_below): Computes the percentage of values less than the given threshold.

[`precision(...)`](../tf/metrics/precision): Computes the precision of the predictions with respect to the labels.

[`precision_at_thresholds(...)`](../tf/metrics/precision_at_thresholds): Computes precision values for different `thresholds` on `predictions`.

[`recall(...)`](../tf/metrics/recall): Computes the recall of the predictions with respect to the labels.

[`recall_at_k(...)`](../tf/metrics/recall_at_k): Computes recall@k of the predictions with respect to sparse labels.

[`recall_at_thresholds(...)`](../tf/metrics/recall_at_thresholds): Computes various recall values for different `thresholds` on `predictions`.

[`root_mean_squared_error(...)`](../tf/metrics/root_mean_squared_error): Computes the root mean squared error between the labels and predictions.

[`sensitivity_at_specificity(...)`](../tf/metrics/sensitivity_at_specificity): Computes the specificity at a given sensitivity.

[`sparse_average_precision_at_k(...)`](../tf/metrics/sparse_average_precision_at_k): Computes average precision@k of predictions with respect to sparse labels.

[`sparse_precision_at_k(...)`](../tf/metrics/sparse_precision_at_k): Computes precision@k of the predictions with respect to sparse labels.

[`specificity_at_sensitivity(...)`](../tf/metrics/specificity_at_sensitivity): Computes the specificity at a given sensitivity.

[`true_positives(...)`](../tf/metrics/true_positives): Sum the weights of true_positives.

