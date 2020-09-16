description: Evaluation-related metrics.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.metrics

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Evaluation-related metrics.



## Functions

[`accuracy(...)`](../../../tf/compat/v1/metrics/accuracy.md): Calculates how often `predictions` matches `labels`.

[`auc(...)`](../../../tf/compat/v1/metrics/auc.md): Computes the approximate AUC via a Riemann sum. (deprecated)

[`average_precision_at_k(...)`](../../../tf/compat/v1/metrics/average_precision_at_k.md): Computes average precision@k of predictions with respect to sparse labels.

[`false_negatives(...)`](../../../tf/compat/v1/metrics/false_negatives.md): Computes the total number of false negatives.

[`false_negatives_at_thresholds(...)`](../../../tf/compat/v1/metrics/false_negatives_at_thresholds.md): Computes false negatives at provided threshold values.

[`false_positives(...)`](../../../tf/compat/v1/metrics/false_positives.md): Sum the weights of false positives.

[`false_positives_at_thresholds(...)`](../../../tf/compat/v1/metrics/false_positives_at_thresholds.md): Computes false positives at provided threshold values.

[`mean(...)`](../../../tf/compat/v1/metrics/mean.md): Computes the (weighted) mean of the given values.

[`mean_absolute_error(...)`](../../../tf/compat/v1/metrics/mean_absolute_error.md): Computes the mean absolute error between the labels and predictions.

[`mean_cosine_distance(...)`](../../../tf/compat/v1/metrics/mean_cosine_distance.md): Computes the cosine distance between the labels and predictions.

[`mean_iou(...)`](../../../tf/compat/v1/metrics/mean_iou.md): Calculate per-step mean Intersection-Over-Union (mIOU).

[`mean_per_class_accuracy(...)`](../../../tf/compat/v1/metrics/mean_per_class_accuracy.md): Calculates the mean of the per-class accuracies.

[`mean_relative_error(...)`](../../../tf/compat/v1/metrics/mean_relative_error.md): Computes the mean relative error by normalizing with the given values.

[`mean_squared_error(...)`](../../../tf/compat/v1/metrics/mean_squared_error.md): Computes the mean squared error between the labels and predictions.

[`mean_tensor(...)`](../../../tf/compat/v1/metrics/mean_tensor.md): Computes the element-wise (weighted) mean of the given tensors.

[`percentage_below(...)`](../../../tf/compat/v1/metrics/percentage_below.md): Computes the percentage of values less than the given threshold.

[`precision(...)`](../../../tf/compat/v1/metrics/precision.md): Computes the precision of the predictions with respect to the labels.

[`precision_at_k(...)`](../../../tf/compat/v1/metrics/precision_at_k.md): Computes precision@k of the predictions with respect to sparse labels.

[`precision_at_thresholds(...)`](../../../tf/compat/v1/metrics/precision_at_thresholds.md): Computes precision values for different `thresholds` on `predictions`.

[`precision_at_top_k(...)`](../../../tf/compat/v1/metrics/precision_at_top_k.md): Computes precision@k of the predictions with respect to sparse labels.

[`recall(...)`](../../../tf/compat/v1/metrics/recall.md): Computes the recall of the predictions with respect to the labels.

[`recall_at_k(...)`](../../../tf/compat/v1/metrics/recall_at_k.md): Computes recall@k of the predictions with respect to sparse labels.

[`recall_at_thresholds(...)`](../../../tf/compat/v1/metrics/recall_at_thresholds.md): Computes various recall values for different `thresholds` on `predictions`.

[`recall_at_top_k(...)`](../../../tf/compat/v1/metrics/recall_at_top_k.md): Computes recall@k of top-k predictions with respect to sparse labels.

[`root_mean_squared_error(...)`](../../../tf/compat/v1/metrics/root_mean_squared_error.md): Computes the root mean squared error between the labels and predictions.

[`sensitivity_at_specificity(...)`](../../../tf/compat/v1/metrics/sensitivity_at_specificity.md): Computes the specificity at a given sensitivity.

[`sparse_average_precision_at_k(...)`](../../../tf/compat/v1/metrics/sparse_average_precision_at_k.md): Renamed to `average_precision_at_k`, please use that method instead. (deprecated)

[`sparse_precision_at_k(...)`](../../../tf/compat/v1/metrics/sparse_precision_at_k.md): Renamed to `precision_at_k`, please use that method instead. (deprecated)

[`specificity_at_sensitivity(...)`](../../../tf/compat/v1/metrics/specificity_at_sensitivity.md): Computes the specificity at a given sensitivity.

[`true_negatives(...)`](../../../tf/compat/v1/metrics/true_negatives.md): Sum the weights of true_negatives.

[`true_negatives_at_thresholds(...)`](../../../tf/compat/v1/metrics/true_negatives_at_thresholds.md): Computes true negatives at provided threshold values.

[`true_positives(...)`](../../../tf/compat/v1/metrics/true_positives.md): Sum the weights of true_positives.

[`true_positives_at_thresholds(...)`](../../../tf/compat/v1/metrics/true_positives_at_thresholds.md): Computes true positives at provided threshold values.

