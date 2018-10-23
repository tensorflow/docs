

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.metrics.precision_recall_at_equal_thresholds

``` python
tf.contrib.metrics.precision_recall_at_equal_thresholds(
    labels,
    predictions,
    weights=None,
    num_thresholds=None,
    use_locking=None,
    name=None
)
```



Defined in [`tensorflow/contrib/metrics/python/ops/metric_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/metrics/python/ops/metric_ops.py).

A helper method for creating metrics related to precision-recall curves.

These values are true positives, false negatives, true negatives, false
positives, precision, and recall. This function returns a data structure that
contains ops within it.

Unlike _streaming_confusion_matrix_at_thresholds (which exhibits O(T * N)
space and run time), this op exhibits O(T + N) space and run time, where T is
the number of thresholds and N is the size of the predictions tensor. Hence,
it may be advantageous to use this function when `predictions` is big.

For instance, prefer this method for per-pixel classification tasks, for which
the predictions tensor may be very large.

Each number in `predictions`, a float in `[0, 1]`, is compared with its
corresponding label in `labels`, and counts as a single tp/fp/tn/fn value at
each threshold. This is then multiplied with `weights` which can be used to
reweight certain values, or more commonly used for masking values.

#### Args:

* <b>`labels`</b>: A bool `Tensor` whose shape matches `predictions`.
* <b>`predictions`</b>: A floating point `Tensor` of arbitrary shape and whose values
    are in the range `[0, 1]`.
* <b>`weights`</b>: Optional; If provided, a `Tensor` that has the same dtype as,
    and broadcastable to, `predictions`. This tensor is multiplied by counts.
* <b>`num_thresholds`</b>: Optional; Number of thresholds, evenly distributed in
    `[0, 1]`. Should be `>= 2`. Defaults to 201. Note that the number of bins
    is 1 less than `num_thresholds`. Using an even `num_thresholds` value
    instead of an odd one may yield unfriendly edges for bins.
* <b>`use_locking`</b>: Optional; If True, the op will be protected by a lock.
    Otherwise, the behavior is undefined, but may exhibit less contention.
    Defaults to True.
* <b>`name`</b>: Optional; variable_scope name. If not provided, the string
    'precision_recall_at_equal_threshold' is used.


#### Returns:

* <b>`result`</b>: A named tuple (See PrecisionRecallData within the implementation of
    this function) with properties that are variables of shape
    `[num_thresholds]`. The names of the properties are tp, fp, tn, fn,
    precision, recall, thresholds.
* <b>`update_op`</b>: An op that accumulates values.


#### Raises:

* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
    `weights` is not `None` and its shape doesn't match `predictions`, or if
    `includes` contains invalid keys.