

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.binary_classification_head

``` python
tf.contrib.estimator.binary_classification_head(
    weight_column=None,
    thresholds=None,
    label_vocabulary=None,
    loss_reduction=losses.Reduction.SUM_OVER_BATCH_SIZE,
    loss_fn=None,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for single label binary classification.

This head uses `sigmoid_cross_entropy_with_logits` loss.

The head expects `logits` with shape `[D0, D1, ... DN, 1]`.
In many applications, the shape is `[batch_size, 1]`.

`labels` must be a dense `Tensor` with shape matching `logits`, namely
`[D0, D1, ... DN, 1]`. If `label_vocabulary` given, `labels` must be a string
`Tensor` with values from the vocabulary. If `label_vocabulary` is not given,
`labels` must be float `Tensor` with values in the interval `[0, 1]`.

If `weight_column` is specified, weights must be of shape
`[D0, D1, ... DN]`, or `[D0, D1, ... DN, 1]`.

The loss is the weighted sum over the input dimensions. Namely, if the input
labels have shape `[batch_size, 1]`, the loss is the weighted sum over
`batch_size`.

Also supports custom `loss_fn`. `loss_fn` takes `(labels, logits)` or
`(labels, logits, features)` as arguments and returns unreduced loss with
shape `[D0, D1, ... DN, 1]`. `loss_fn` must support float `labels` with
shape `[D0, D1, ... DN, 1]`. Namely, the head applies `label_vocabulary` to
the input labels before passing them to `loss_fn`.

The head can be used with a canned estimator. Example:

```python
my_head = tf.contrib.estimator.binary_classification_head()
my_estimator = tf.contrib.estimator.DNNEstimator(
    head=my_head,
    hidden_units=...,
    feature_columns=...)
```

It can also be used with a custom `model_fn`. Example:

```python
def _my_model_fn(features, labels, mode):
  my_head = tf.contrib.estimator.binary_classification_head()
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
* <b>`thresholds`</b>: Iterable of floats in the range `(0, 1)`. For binary
    classification metrics such as precision and recall, an eval metric is
    generated for each threshold value. This threshold is applied to the
    logistic values to determine the binary classification (i.e., above the
    threshold is `true`, below is `false`.
* <b>`label_vocabulary`</b>: A list or tuple of strings representing possible label
    values. If it is not given, labels must be float with values within
    [0, 1]. If given, labels must be string type and have any value in
    `label_vocabulary`. Note that errors will be raised if `label_vocabulary`
    is not provided but labels are strings.
* <b>`loss_reduction`</b>: One of <a href="../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a> except `NONE`. Describes how to
    reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`, namely
    weighted sum of losses divided by batch size. See <a href="../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a>.
* <b>`loss_fn`</b>: Optional loss function.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`. Also used as `name_scope` when creating ops.


#### Returns:

An instance of `_Head` for binary classification.


#### Raises:

* <b>`ValueError`</b>: If `thresholds` contains a value outside of `(0, 1)`.
* <b>`ValueError`</b>: If `loss_reduction` is invalid.