page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.f1_score


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/metrics/python/metrics/classification.py#L70-L185">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the approximately best F1-score across different thresholds.

``` python
tf.contrib.metrics.f1_score(
    labels,
    predictions,
    weights=None,
    num_thresholds=200,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The f1_score function applies a range of thresholds to the predictions to
convert them from [0, 1] to bool. Precision and recall are computed by
comparing them to the labels. The F1-Score is then defined as
2 * precision * recall / (precision + recall). The best one across the
thresholds is returned.

Disclaimer: In practice it may be desirable to choose the best threshold on
the validation set and evaluate the F1 score with this threshold on a
separate test set. Or it may be desirable to use a fixed threshold (e.g. 0.5).

This function internally creates four local variables, `true_positives`,
`true_negatives`, `false_positives` and `false_negatives` that are used to
compute the pairs of recall and precision values for a linearly spaced set of
thresholds from which the best f1-score is derived.

This value is ultimately returned as `f1-score`, an idempotent operation that
computes the F1-score (computed using the aforementioned variables). The
`num_thresholds` variable controls the degree of discretization with larger
numbers of thresholds more closely approximating the true best F1-score.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the F1-score.

Example usage with a custom estimator:
def model_fn(features, labels, mode):
  predictions = make_predictions(features)
  loss = make_loss(predictions, labels)
  train_op = tf.contrib.training.create_train_op(
        total_loss=loss,
        optimizer='Adam')
  eval_metric_ops = {'f1': f1_score(labels, predictions)}
  return tf.estimator.EstimatorSpec(
      mode=mode,
      predictions=predictions,
      loss=loss,
      train_op=train_op,
      eval_metric_ops=eval_metric_ops,
      export_outputs=export_outputs)
estimator = tf.estimator.Estimator(model_fn=model_fn)

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`labels`</b>: A `Tensor` whose shape matches `predictions`. Will be cast to
  `bool`.
* <b>`predictions`</b>: A floating point `Tensor` of arbitrary shape and whose values
  are in the range `[0, 1]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `labels` dimension).
* <b>`num_thresholds`</b>: The number of thresholds to use when discretizing the roc
  curve.
* <b>`metrics_collections`</b>: An optional list of collections that `f1_score` should
  be added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
  be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`f1_score`</b>: A scalar `Tensor` representing the current best f1-score across
  different thresholds.
* <b>`update_op`</b>: An operation that increments the `true_positives`,
  `true_negatives`, `false_positives` and `false_negatives` variables
  appropriately and whose value matches the `f1_score`.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  either `metrics_collections` or `updates_collections` are not a list or
  tuple.
