

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.metrics



Defined in [`tensorflow/contrib/metrics/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/metrics/__init__.py).

Ops for evaluation metrics and summary statistics.

See the [Metrics (contrib)](../../../../api_guides/python/contrib.metrics) guide.


## Functions

[`accuracy(...)`](../../tf/contrib/metrics/accuracy): Computes the percentage of times that predictions matches labels.

[`aggregate_metric_map(...)`](../../tf/contrib/metrics/aggregate_metric_map): Aggregates the metric names to tuple dictionary.

[`aggregate_metrics(...)`](../../tf/contrib/metrics/aggregate_metrics): Aggregates the metric value tensors and update ops into two lists.

[`auc_using_histogram(...)`](../../tf/contrib/metrics/auc_using_histogram): AUC computed by maintaining histograms.

[`confusion_matrix(...)`](../../tf/contrib/metrics/confusion_matrix): Deprecated. Use tf.confusion_matrix instead.

[`set_difference(...)`](../../tf/sets/set_difference): Compute set difference of elements in last dimension of `a` and `b`.

[`set_intersection(...)`](../../tf/sets/set_intersection): Compute set intersection of elements in last dimension of `a` and `b`.

[`set_size(...)`](../../tf/sets/set_size): Compute number of unique elements along last dimension of `a`.

[`set_union(...)`](../../tf/sets/set_union): Compute set union of elements in last dimension of `a` and `b`.

[`streaming_accuracy(...)`](../../tf/contrib/metrics/streaming_accuracy): Calculates how often `predictions` matches `labels`.

[`streaming_auc(...)`](../../tf/contrib/metrics/streaming_auc): Computes the approximate AUC via a Riemann sum.

[`streaming_concat(...)`](../../tf/contrib/metrics/streaming_concat): Concatenate values along an axis across batches.

[`streaming_covariance(...)`](../../tf/contrib/metrics/streaming_covariance): Computes the unbiased sample covariance between `predictions` and `labels`.

[`streaming_curve_points(...)`](../../tf/contrib/metrics/streaming_curve_points): Computes curve (ROC or PR) values for a prespecified number of points.

[`streaming_false_negatives(...)`](../../tf/contrib/metrics/streaming_false_negatives): Computes the total number of false negatives.

[`streaming_false_negatives_at_thresholds(...)`](../../tf/contrib/metrics/streaming_false_negatives_at_thresholds)

[`streaming_false_positives(...)`](../../tf/contrib/metrics/streaming_false_positives): Sum the weights of false positives.

[`streaming_false_positives_at_thresholds(...)`](../../tf/contrib/metrics/streaming_false_positives_at_thresholds)

[`streaming_mean(...)`](../../tf/contrib/metrics/streaming_mean): Computes the (weighted) mean of the given values.

[`streaming_mean_absolute_error(...)`](../../tf/contrib/metrics/streaming_mean_absolute_error): Computes the mean absolute error between the labels and predictions.

[`streaming_mean_cosine_distance(...)`](../../tf/contrib/metrics/streaming_mean_cosine_distance): Computes the cosine distance between the labels and predictions.

[`streaming_mean_iou(...)`](../../tf/contrib/metrics/streaming_mean_iou): Calculate per-step mean Intersection-Over-Union (mIOU).

[`streaming_mean_relative_error(...)`](../../tf/contrib/metrics/streaming_mean_relative_error): Computes the mean relative error by normalizing with the given values.

[`streaming_mean_squared_error(...)`](../../tf/contrib/metrics/streaming_mean_squared_error): Computes the mean squared error between the labels and predictions.

[`streaming_mean_tensor(...)`](../../tf/contrib/metrics/streaming_mean_tensor): Computes the element-wise (weighted) mean of the given tensors.

[`streaming_pearson_correlation(...)`](../../tf/contrib/metrics/streaming_pearson_correlation): Computes Pearson correlation coefficient between `predictions`, `labels`.

[`streaming_percentage_less(...)`](../../tf/contrib/metrics/streaming_percentage_less): Computes the percentage of values less than the given threshold.

[`streaming_precision(...)`](../../tf/contrib/metrics/streaming_precision): Computes the precision of the predictions with respect to the labels.

[`streaming_precision_at_thresholds(...)`](../../tf/contrib/metrics/streaming_precision_at_thresholds): Computes precision values for different `thresholds` on `predictions`.

[`streaming_recall(...)`](../../tf/contrib/metrics/streaming_recall): Computes the recall of the predictions with respect to the labels.

[`streaming_recall_at_k(...)`](../../tf/contrib/metrics/streaming_recall_at_k): Computes the recall@k of the predictions with respect to dense labels. (deprecated)

[`streaming_recall_at_thresholds(...)`](../../tf/contrib/metrics/streaming_recall_at_thresholds): Computes various recall values for different `thresholds` on `predictions`.

[`streaming_root_mean_squared_error(...)`](../../tf/contrib/metrics/streaming_root_mean_squared_error): Computes the root mean squared error between the labels and predictions.

[`streaming_sensitivity_at_specificity(...)`](../../tf/contrib/metrics/streaming_sensitivity_at_specificity): Computes the specificity at a given sensitivity.

[`streaming_sparse_average_precision_at_k(...)`](../../tf/contrib/metrics/streaming_sparse_average_precision_at_k): Computes average precision@k of predictions with respect to sparse labels.

[`streaming_sparse_average_precision_at_top_k(...)`](../../tf/contrib/metrics/streaming_sparse_average_precision_at_top_k): Computes average precision@k of predictions with respect to sparse labels.

[`streaming_sparse_precision_at_k(...)`](../../tf/contrib/metrics/streaming_sparse_precision_at_k): Computes precision@k of the predictions with respect to sparse labels.

[`streaming_sparse_precision_at_top_k(...)`](../../tf/contrib/metrics/streaming_sparse_precision_at_top_k): Computes precision@k of top-k predictions with respect to sparse labels.

[`streaming_sparse_recall_at_k(...)`](../../tf/contrib/metrics/streaming_sparse_recall_at_k): Computes recall@k of the predictions with respect to sparse labels.

[`streaming_specificity_at_sensitivity(...)`](../../tf/contrib/metrics/streaming_specificity_at_sensitivity): Computes the specificity at a given sensitivity.

[`streaming_true_negatives(...)`](../../tf/contrib/metrics/streaming_true_negatives): Sum the weights of true_negatives.

[`streaming_true_negatives_at_thresholds(...)`](../../tf/contrib/metrics/streaming_true_negatives_at_thresholds)

[`streaming_true_positives(...)`](../../tf/contrib/metrics/streaming_true_positives): Sum the weights of true_positives.

[`streaming_true_positives_at_thresholds(...)`](../../tf/contrib/metrics/streaming_true_positives_at_thresholds)

