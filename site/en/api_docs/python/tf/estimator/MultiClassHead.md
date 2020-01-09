page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.MultiClassHead


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_class_head.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MultiClassHead`

Creates a `Head` for multi class classification.

Inherits From: [`Head`](../../tf/estimator/Head)

### Aliases:

* Class `tf.compat.v1.estimator.MultiClassHead`
* Class `tf.compat.v2.estimator.MultiClassHead`


<!-- Placeholder for "Used in" -->

Uses `sparse_softmax_cross_entropy` loss.

The head expects `logits` with shape `[D0, D1, ... DN, n_classes]`.
In many applications, the shape is `[batch_size, n_classes]`.

`labels` must be a dense `Tensor` with shape matching `logits`, namely
`[D0, D1, ... DN, 1]`. If `label_vocabulary` given, `labels` must be a string
`Tensor` with values from the vocabulary. If `label_vocabulary` is not given,
`labels` must be an integer `Tensor` with values specifying the class index.

If `weight_column` is specified, weights must be of shape
`[D0, D1, ... DN]`, or `[D0, D1, ... DN, 1]`.

The loss is the weighted sum over the input dimensions. Namely, if the input
labels have shape `[batch_size, 1]`, the loss is the weighted sum over
`batch_size`.

Also supports custom `loss_fn`. `loss_fn` takes `(labels, logits)` or
`(labels, logits, features, loss_reduction)` as arguments and returns
unreduced loss with shape `[D0, D1, ... DN, 1]`. `loss_fn` must support
integer `labels` with shape `[D0, D1, ... DN, 1]`. Namely, the head applies
`label_vocabulary` to the input labels before passing them to `loss_fn`.

The head can be used with a canned estimator. Example:

```python
my_head = tf.estimator.MultiClassHead(n_classes=3)
my_estimator = tf.estimator.DNNEstimator(
    head=my_head,
    hidden_units=...,
    feature_columns=...)
```

It can also be used with a custom `model_fn`. Example:

```python
def _my_model_fn(features, labels, mode):
  my_head = tf.estimator.MultiClassHead(n_classes=3)
  logits = tf.keras.Model(...)(features)

  return my_head.create_estimator_spec(
      features=features,
      mode=mode,
      labels=labels,
      optimizer=tf.keras.optimizers.Adagrad(lr=0.1),
      logits=logits)

my_estimator = tf.estimator.Estimator(model_fn=_my_model_fn)
```

#### Args:


* <b>`n_classes`</b>: Number of classes, must be greater than 2 (for 2 classes, use
  `BinaryClassHead`).
* <b>`weight_column`</b>: A string or a `NumericColumn` created by
  <a href="../../tf/feature_column/numeric_column"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
  weights. It is used to down weight or boost examples during training. It
  will be multiplied by the loss of the example.
* <b>`label_vocabulary`</b>: A list or tuple of strings representing possible label
  values. If it is not given, that means labels are already encoded as an
  integer within [0, n_classes). If given, labels must be of string type and
  have any value in `label_vocabulary`. Note that errors will be raised if
  `label_vocabulary` is not provided but labels are strings. If both
  `n_classes` and `label_vocabulary` are provided, `label_vocabulary` should
  contain exactly `n_classes` items.
* <b>`loss_reduction`</b>: One of <a href="../../tf/keras/losses/Reduction"><code>tf.losses.Reduction</code></a> except `NONE`. Decides how to
  reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`, namely
  weighted sum of losses divided by `batch size * label_dimension`.
* <b>`loss_fn`</b>: Optional loss function.
* <b>`name`</b>: Name of the head. If provided, summary and metrics keys will be
  suffixed by `"/" + name`. Also used as `name_scope` when creating ops.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_class_head.py">View source</a>

``` python
__init__(
    n_classes,
    weight_column=None,
    label_vocabulary=None,
    loss_reduction=losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE,
    loss_fn=None,
    name=None
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="logits_dimension"><code>logits_dimension</code></h3>

See `base_head.Head` for details.


<h3 id="loss_reduction"><code>loss_reduction</code></h3>

See `base_head.Head` for details.


<h3 id="name"><code>name</code></h3>

See `base_head.Head` for details.




## Methods

<h3 id="create_estimator_spec"><code>create_estimator_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

``` python
create_estimator_spec(
    features,
    mode,
    logits,
    labels=None,
    optimizer=None,
    trainable_variables=None,
    train_op_fn=None,
    update_ops=None,
    regularization_losses=None
)
```

Returns `EstimatorSpec` that a model_fn can return.

It is recommended to pass all args via name.

#### Args:


* <b>`features`</b>: Input `dict` mapping string feature names to `Tensor` or
  `SparseTensor` objects containing the values for that feature in a
  minibatch. Often to be used to fetch example-weight tensor.
* <b>`mode`</b>: Estimator's `ModeKeys`.
* <b>`logits`</b>: Logits `Tensor` to be used by the head.
* <b>`labels`</b>: Labels `Tensor`, or `dict` mapping string label names to `Tensor`
  objects of the label values.
* <b>`optimizer`</b>: An <a href="../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a> instance to optimize the
  loss in TRAIN mode. Namely, sets `train_op = optimizer.get_updates(loss,
  trainable_variables)`, which updates variables to minimize `loss`.
* <b>`trainable_variables`</b>: A list or tuple of `Variable` objects to update to
  minimize `loss`. In Tensorflow 1.x, by default these are the list of
  variables collected in the graph under the key
  `GraphKeys.TRAINABLE_VARIABLES`. As Tensorflow 2.x doesn't have
  collections and GraphKeys, trainable_variables need to be passed
  explicitly here.
* <b>`train_op_fn`</b>: Function that takes a scalar loss `Tensor` and returns an op
  to optimize the model with the loss in TRAIN mode. Used if `optimizer`
  is `None`. Exactly one of `train_op_fn` and `optimizer` must be set in
  TRAIN mode. By default, it is `None` in other modes. If you want to
  optimize loss yourself, you can pass `lambda _: tf.no_op()` and then use
  <a href="../../tf/estimator/EstimatorSpec#loss"><code>EstimatorSpec.loss</code></a> to compute and apply gradients.
* <b>`update_ops`</b>: A list or tuple of update ops to be run at training time. For
  example, layers such as BatchNormalization create mean and variance
  update ops that need to be run at training time. In Tensorflow 1.x,
  these are thrown into an UPDATE_OPS collection. As Tensorflow 2.x
  doesn't have collections, update_ops need to be passed explicitly here.
* <b>`regularization_losses`</b>: A list of additional scalar losses to be added to
  the training loss, such as regularization losses.


#### Returns:

`EstimatorSpec`.


<h3 id="loss"><code>loss</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_class_head.py">View source</a>

``` python
loss(
    labels,
    logits,
    features=None,
    mode=None,
    regularization_losses=None
)
```

Returns regularized training loss. See `base_head.Head` for details.


<h3 id="metrics"><code>metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_class_head.py">View source</a>

``` python
metrics(regularization_losses=None)
```

Creates metrics. See `base_head.Head` for details.


<h3 id="predictions"><code>predictions</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_class_head.py">View source</a>

``` python
predictions(
    logits,
    keys=None
)
```

Return predictions based on keys. See `base_head.Head` for details.


#### Args:


* <b>`logits`</b>: logits `Tensor` with shape `[D0, D1, ... DN, logits_dimension]`.
  For many applications, the shape is `[batch_size, logits_dimension]`.
* <b>`keys`</b>: a list or tuple of prediction keys. Each key can be either the class
  variable of prediction_keys.PredictionKeys or its string value, such as:
  prediction_keys.PredictionKeys.CLASSES or 'classes'. If not specified,
  it will return the predictions for all valid keys.


#### Returns:

A dict of predictions.


<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_class_head.py">View source</a>

``` python
update_metrics(
    eval_metrics,
    features,
    logits,
    labels,
    regularization_losses=None
)
```

Updates eval metrics. See `base_head.Head` for details.
