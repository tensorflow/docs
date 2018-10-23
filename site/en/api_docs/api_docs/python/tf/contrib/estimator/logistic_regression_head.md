

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.logistic_regression_head

``` python
tf.contrib.estimator.logistic_regression_head(
    weight_column=None,
    loss_reduction=losses.Reduction.SUM_OVER_BATCH_SIZE,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for logistic regression.

Uses `sigmoid_cross_entropy_with_logits` loss, which is the same as
`binary_classification_head`. The differences compared to
`binary_classification_head` are:

* Does not support `label_vocabulary`. Instead, labels must be float in the
  range [0, 1].
* Does not calculate some metrics that do not make sense, such as AUC.
* In `PREDICT` mode, only returns logits and predictions
  (`=tf.sigmoid(logits)`), whereas `binary_classification_head` also returns
  probabilities, classes, and class_ids.
* Export output defaults to `RegressionOutput`, whereas
  `binary_classification_head` defaults to `PredictOutput`.

The head expects `logits` with shape `[D0, D1, ... DN, 1]`.
In many applications, the shape is `[batch_size, 1]`.

The `labels` shape must match `logits`, namely
`[D0, D1, ... DN]` or `[D0, D1, ... DN, 1]`.

If `weight_column` is specified, weights must be of shape
`[D0, D1, ... DN]` or `[D0, D1, ... DN, 1]`.

This is implemented as a generalized linear model, see
https://en.wikipedia.org/wiki/Generalized_linear_model.

The head can be used with a canned estimator. Example:

```python
my_head = tf.contrib.estimator.logistic_regression_head()
my_estimator = tf.contrib.estimator.DNNEstimator(
    head=my_head,
    hidden_units=...,
    feature_columns=...)
```

It can also be used with a custom `model_fn`. Example:

```python
def _my_model_fn(features, labels, mode):
  my_head = tf.contrib.estimator.logistic_regression_head()
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

* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    <a href="../../../tf/feature_column/numeric_column"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`loss_reduction`</b>: One of <a href="../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a> except `NONE`. Describes how to
    reduce training loss over batch and label dimension. Defaults to
    `SUM_OVER_BATCH_SIZE`, namely weighted sum of losses divided by
    `batch size * label_dimension`. See <a href="../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a>.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`. Also used as `name_scope` when creating ops.


#### Returns:

An instance of `_Head` for logistic regression.


#### Raises:

* <b>`ValueError`</b>: If `loss_reduction` is invalid.