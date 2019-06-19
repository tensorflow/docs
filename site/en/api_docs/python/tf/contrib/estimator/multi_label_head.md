page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.multi_label_head

``` python
tf.contrib.estimator.multi_label_head(
    n_classes,
    weight_column=None,
    thresholds=None,
    label_vocabulary=None,
    loss_reduction=losses.Reduction.SUM_OVER_BATCH_SIZE,
    loss_fn=None,
    classes_for_class_based_metrics=None,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for multi-label classification.

Multi-label classification handles the case where each example may have zero
or more associated labels, from a discrete set. This is distinct from
`multi_class_head` which has exactly one label per example.

Uses `sigmoid_cross_entropy` loss average over classes and weighted sum over
the batch. Namely, if the input logits have shape `[batch_size, n_classes]`,
the loss is the average over `n_classes` and the weighted sum over
`batch_size`.

The head expects `logits` with shape `[D0, D1, ... DN, n_classes]`. In many
applications, the shape is `[batch_size, n_classes]`.

Labels can be:
* A multi-hot tensor of shape `[D0, D1, ... DN, n_classes]`
* An integer `SparseTensor` of class indices. The `dense_shape` must be
  `[D0, D1, ... DN, ?]` and the values within `[0, n_classes)`.
* If `label_vocabulary` is given, a string `SparseTensor`. The `dense_shape`
  must be `[D0, D1, ... DN, ?]` and the values within `label_vocabulary`.

If `weight_column` is specified, weights must be of shape
`[D0, D1, ... DN]`, or `[D0, D1, ... DN, 1]`.

Also supports custom `loss_fn`. `loss_fn` takes `(labels, logits)` or
`(labels, logits, features)` as arguments and returns unreduced loss with
shape `[D0, D1, ... DN, 1]`. `loss_fn` must support indicator `labels` with
shape `[D0, D1, ... DN, n_classes]`. Namely, the head applies
`label_vocabulary` to the input labels before passing them to `loss_fn`.

The head can be used with a canned estimator. Example:

```python
my_head = tf.contrib.estimator.multi_label_head(n_classes=3)
my_estimator = tf.contrib.estimator.DNNEstimator(
    head=my_head,
    hidden_units=...,
    feature_columns=...)
```

It can also be used with a custom `model_fn`. Example:

```python
def _my_model_fn(features, labels, mode):
  my_head = tf.contrib.estimator.multi_label_head(n_classes=3)
  logits = tf.keras.Model(...)(features)

  return my_head.create_estimator_spec(
      features=features,
      mode=mode,
      labels=labels,
      optimizer=tf.AdagradOptimizer(learning_rate=0.1),
      logits=logits)

my_estimator = tf.estimator.Estimator(model_fn=_my_model_fn)
```

#### Args:

* <b>`n_classes`</b>: Number of classes, must be greater than 1 (for 1 class, use
    `binary_classification_head`).
* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    <a href="../../../tf/feature_column/numeric_column"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.  Per-class weighting is
    not supported.
* <b>`thresholds`</b>: Iterable of floats in the range `(0, 1)`. Accuracy, precision
    and recall metrics are evaluated for each threshold value. The threshold
    is applied to the predicted probabilities, i.e. above the threshold is
    `true`, below is `false`.
* <b>`label_vocabulary`</b>: A list of strings represents possible label values. If it
    is not given, that means labels are already encoded as integer within
    [0, n_classes) or multi-hot Tensor. If given, labels must be SparseTensor
    string type and have any value in `label_vocabulary`. Also there will be
    errors if vocabulary is not provided and labels are string.
* <b>`loss_reduction`</b>: One of <a href="../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a> except `NONE`. Describes how to
    reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`, namely
    weighted sum of losses divided by batch size. See <a href="../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a>.
* <b>`loss_fn`</b>: Optional loss function.
* <b>`classes_for_class_based_metrics`</b>: List of integer class IDs or string class
    names for which per-class metrics are evaluated. If integers, all must be
    in the range `[0, n_classes - 1]`. If strings, all must be in
    `label_vocabulary`.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`. Also used as `name_scope` when creating ops.


#### Returns:

An instance of `_Head` for multi-label classification.


#### Raises:

* <b>`ValueError`</b>: if `n_classes`, `thresholds`, `loss_reduction`, `loss_fn` or
  `metric_class_ids` is invalid.