page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.PoissonRegressionHead


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `PoissonRegressionHead`

Creates a `Head` for poisson regression using <a href="../../tf/nn/log_poisson_loss"><code>tf.nn.log_poisson_loss</code></a>.

Inherits From: [`RegressionHead`](../../tf/estimator/RegressionHead)

### Aliases:

* Class `tf.compat.v1.estimator.PoissonRegressionHead`
* Class `tf.compat.v2.estimator.PoissonRegressionHead`


<!-- Placeholder for "Used in" -->

The loss is the weighted sum over all input dimensions. Namely, if the input
labels have shape `[batch_size, label_dimension]`, the loss is the weighted
sum over both `batch_size` and `label_dimension`.

The head expects `logits` with shape `[D0, D1, ... DN, label_dimension]`.
In many applications, the shape is `[batch_size, label_dimension]`.

The `labels` shape must match `logits`, namely
`[D0, D1, ... DN, label_dimension]`. If `label_dimension=1`, shape
`[D0, D1, ... DN]` is also supported.

If `weight_column` is specified, weights must be of shape
`[D0, D1, ... DN]`, `[D0, D1, ... DN, 1]` or
`[D0, D1, ... DN, label_dimension]`.

This is implemented as a generalized linear model, see
https://en.wikipedia.org/wiki/Generalized_linear_model.

The head can be used with a canned estimator. Example:

```python
my_head = tf.estimator.PoissonRegressionHead()
my_estimator = tf.estimator.DNNEstimator(
    head=my_head,
    hidden_units=...,
    feature_columns=...)
```

It can also be used with a custom `model_fn`. Example:

```python
def _my_model_fn(features, labels, mode):
  my_head = tf.estimator.PoissonRegressionHead()
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


* <b>`weight_column`</b>: A string or a `NumericColumn` created by
  <a href="../../tf/feature_column/numeric_column"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
  weights. It is used to down weight or boost examples during training. It
  will be multiplied by the loss of the example.
* <b>`label_dimension`</b>: Number of regression labels per example. This is the size
  of the last dimension of the labels `Tensor` (typically, this has shape
  `[batch_size, label_dimension]`).
* <b>`loss_reduction`</b>: One of <a href="../../tf/keras/losses/Reduction"><code>tf.losses.Reduction</code></a> except `NONE`. Decides how to
  reduce training loss over batch and label dimension. Defaults to
  `SUM_OVER_BATCH_SIZE`, namely weighted sum of losses divided by
  `batch size * label_dimension`.
* <b>`compute_full_loss`</b>: Whether to include the constant `log(z!)` term in
  computing the poisson loss. See <a href="../../tf/nn/log_poisson_loss"><code>tf.nn.log_poisson_loss</code></a> for the full
  documentation.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
  suffixed by `"/" + name`. Also used as `name_scope` when creating ops.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py">View source</a>

``` python
__init__(
    label_dimension=1,
    weight_column=None,
    loss_reduction=losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE,
    compute_full_loss=True,
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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py">View source</a>

``` python
loss(
    labels,
    logits,
    features=None,
    mode=None,
    regularization_losses=None
)
```

Return predictions based on keys. See `base_head.Head` for details.


<h3 id="metrics"><code>metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py">View source</a>

``` python
metrics(regularization_losses=None)
```

Creates metrics. See `base_head.Head` for details.


<h3 id="predictions"><code>predictions</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py">View source</a>

``` python
predictions(logits)
```

Return predictions based on keys.  See `base_head.Head` for details.


#### Args:


* <b>`logits`</b>: logits `Tensor` with shape `[D0, D1, ... DN, logits_dimension]`.
  For many applications, the shape is `[batch_size, logits_dimension]`.


#### Returns:

A dict of predictions.


<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py">View source</a>

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
