page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.metrics

Ops for evaluation metrics and summary statistics.



Defined in [`contrib/metrics/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/metrics/__init__.py).

<!-- Placeholder for "Used in" -->

See the
[Contrib Metrics](https://tensorflow.org/api_guides/python/contrib.metrics)
guide.


## Functions

[`accuracy(...)`](../../tf/contrib/metrics/accuracy): Computes the percentage of times that predictions matches labels.

[`aggregate_metric_map(...)`](../../tf/contrib/metrics/aggregate_metric_map): Aggregates the metric names to tuple dictionary.

[`aggregate_metrics(...)`](../../tf/contrib/metrics/aggregate_metrics): Aggregates the metric value tensors and update ops into two lists.

[`auc_using_histogram(...)`](../../tf/contrib/metrics/auc_using_histogram): AUC computed by maintaining histograms.

[`auc_with_confidence_intervals(...)`](../../tf/contrib/metrics/auc_with_confidence_intervals): Computes the AUC and asymptotic normally distributed confidence interval.

[`cohen_kappa(...)`](../../tf/contrib/metrics/cohen_kappa): Calculates Cohen's kappa.

[`confusion_matrix(...)`](../../tf/contrib/metrics/confusion_matrix): Deprecated. Use tf.math.confusion_matrix instead.

[`count(...)`](../../tf/contrib/metrics/count): Computes the number of examples, or sum of `weights`.

[`f1_score(...)`](../../tf/contrib/metrics/f1_score): Computes the approximately best F1-score across different thresholds.

[`precision_at_recall(...)`](../../tf/contrib/metrics/precision_at_recall): Computes the precision at a given recall.

[`precision_recall_at_equal_thresholds(...)`](../../tf/contrib/metrics/precision_recall_at_equal_thresholds): A helper method for creating metrics related to precision-recall curves.

[`recall_at_precision(...)`](../../tf/contrib/metrics/recall_at_precision): Computes `recall` at `precision`.

[`set_difference(...)`](../../tf/sets/difference): Compute set difference of elements in last dimension of `a` and `b`.

[`set_intersection(...)`](../../tf/sets/intersection): Compute set intersection of elements in last dimension of `a` and `b`.

[`set_size(...)`](../../tf/sets/size): Compute number of unique elements along last dimension of `a`.

[`set_union(...)`](../../tf/sets/union): Compute set union of elements in last dimension of `a` and `b`.

[`sparse_recall_at_top_k(...)`](../../tf/contrib/metrics/sparse_recall_at_top_k): Computes recall@k of top-k predictions with respect to sparse labels.

[`streaming_accuracy(...)`](../../tf/contrib/metrics/streaming_accuracy): Calculates how often `predictions` matches `labels`. (deprecated)

[`streaming_auc(...)`](../../tf/contrib/metrics/streaming_auc): Computes the approximate AUC via a Riemann sum. (deprecated)

[`streaming_concat(...)`](../../tf/contrib/metrics/streaming_concat): Concatenate values along an axis across batches.

[`streaming_covariance(...)`](../../tf/contrib/metrics/streaming_covariance): Computes the unbiased sample covariance between `predictions` and `labels`.

[`streaming_curve_points(...)`](../../tf/contrib/metrics/streaming_curve_points): Computes curve (ROC or PR) values for a prespecified number of points.

[`streaming_dynamic_auc(...)`](../../tf/contrib/metrics/streaming_dynamic_auc): Computes the apporixmate AUC by a Riemann sum with data-derived thresholds.

[`streaming_false_negative_rate(...)`](../../tf/contrib/metrics/streaming_false_negative_rate): Computes the false negative rate of predictions with respect to labels.

[`streaming_false_negative_rate_at_thresholds(...)`](../../tf/contrib/metrics/streaming_false_negative_rate_at_thresholds): Computes various fnr values for different `thresholds` on `predictions`.

[`streaming_false_negatives(...)`](../../tf/contrib/metrics/streaming_false_negatives): Computes the total number of false negatives. (deprecated)

[`streaming_false_negatives_at_thresholds(...)`](../../tf/contrib/metrics/streaming_false_negatives_at_thresholds)

[`streaming_false_positive_rate(...)`](../../tf/contrib/metrics/streaming_false_positive_rate): Computes the false positive rate of predictions with respect to labels.

[`streaming_false_positive_rate_at_thresholds(...)`](../../tf/contrib/metrics/streaming_false_positive_rate_at_thresholds): Computes various fpr values for different `thresholds` on `predictions`.

[`streaming_false_positives(...)`](../../tf/contrib/metrics/streaming_false_positives): Sum the weights of false positives. (deprecated)

[`streaming_false_positives_at_thresholds(...)`](../../tf/contrib/metrics/streaming_false_positives_at_thresholds)

[`streaming_mean(...)`](../../tf/contrib/metrics/streaming_mean): Computes the (weighted) mean of the given values. (deprecated)

[`streaming_mean_absolute_error(...)`](../../tf/contrib/metrics/streaming_mean_absolute_error): Computes the mean absolute error between the labels and predictions. (deprecated)

[`streaming_mean_cosine_distance(...)`](../../tf/contrib/metrics/streaming_mean_cosine_distance): Computes the cosine distance between the labels and predictions.

[`streaming_mean_iou(...)`](../../tf/contrib/metrics/streaming_mean_iou): Calculate per-step mean Intersection-Over-Union (mIOU).

[`streaming_mean_relative_error(...)`](../../tf/contrib/metrics/streaming_mean_relative_error): Computes the mean relative error by normalizing with the given values.

[`streaming_mean_squared_error(...)`](../../tf/contrib/metrics/streaming_mean_squared_error): Computes the mean squared error between the labels and predictions. (deprecated)

[`streaming_mean_tensor(...)`](../../tf/contrib/metrics/streaming_mean_tensor): Computes the element-wise (weighted) mean of the given tensors. (deprecated)

[`streaming_pearson_correlation(...)`](../../tf/contrib/metrics/streaming_pearson_correlation): Computes Pearson correlation coefficient between `predictions`, `labels`.

[`streaming_percentage_less(...)`](../../tf/contrib/metrics/streaming_percentage_less): Computes the percentage of values less than the given threshold.

[`streaming_precision(...)`](../../tf/contrib/metrics/streaming_precision): Computes the precision of the predictions with respect to the labels. (deprecated)

[`streaming_precision_at_thresholds(...)`](../../tf/contrib/metrics/streaming_precision_at_thresholds): Computes precision values for different `thresholds` on `predictions`. (deprecated)

[`streaming_recall(...)`](../../tf/contrib/metrics/streaming_recall): Computes the recall of the predictions with respect to the labels. (deprecated)

[`streaming_recall_at_k(...)`](../../tf/contrib/metrics/streaming_recall_at_k): Computes the recall@k of the predictions with respect to dense labels. (deprecated)

[`streaming_recall_at_thresholds(...)`](../../tf/contrib/metrics/streaming_recall_at_thresholds): Computes various recall values for different `thresholds` on `predictions`. (deprecated)

[`streaming_root_mean_squared_error(...)`](../../tf/contrib/metrics/streaming_root_mean_squared_error): Computes the root mean squared error between the labels and predictions. (deprecated)

[`streaming_sensitivity_at_specificity(...)`](../../tf/contrib/metrics/streaming_sensitivity_at_specificity): Computes the sensitivity at a given specificity.

[`streaming_sparse_average_precision_at_k(...)`](../../tf/contrib/metrics/streaming_sparse_average_precision_at_k): Computes average precision@k of predictions with respect to sparse labels.

[`streaming_sparse_average_precision_at_top_k(...)`](../../tf/contrib/metrics/streaming_sparse_average_precision_at_top_k): Computes average precision@k of predictions with respect to sparse labels.

[`streaming_sparse_precision_at_k(...)`](../../tf/contrib/metrics/streaming_sparse_precision_at_k): Computes precision@k of the predictions with respect to sparse labels.

[`streaming_sparse_precision_at_top_k(...)`](../../tf/contrib/metrics/streaming_sparse_precision_at_top_k): Computes precision@k of top-k predictions with respect to sparse labels.

[`streaming_sparse_recall_at_k(...)`](../../tf/contrib/metrics/streaming_sparse_recall_at_k): Computes recall@k of the predictions with respect to sparse labels.

[`streaming_specificity_at_sensitivity(...)`](../../tf/contrib/metrics/streaming_specificity_at_sensitivity): Computes the specificity at a given sensitivity.

[`streaming_true_negatives(...)`](../../tf/contrib/metrics/streaming_true_negatives): Sum the weights of true_negatives. (deprecated)

[`streaming_true_negatives_at_thresholds(...)`](../../tf/contrib/metrics/streaming_true_negatives_at_thresholds)

[`streaming_true_positives(...)`](../../tf/contrib/metrics/streaming_true_positives): Sum the weights of true_positives. (deprecated)

[`streaming_true_positives_at_thresholds(...)`](../../tf/contrib/metrics/streaming_true_positives_at_thresholds)

