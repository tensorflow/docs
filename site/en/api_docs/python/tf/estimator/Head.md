page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.Head


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Head`

Interface for the head/top of a model.



### Aliases:

* Class `tf.compat.v1.estimator.Head`
* Class `tf.compat.v2.estimator.Head`


<!-- Placeholder for "Used in" -->

Head sits on top of the model network and handles computing the outputs of
the network. Given logits (or output of a hidden layer), a Head knows how to
compute predictions, loss, train_op, metrics and export outputs. It is meant
to:

1. Simplify writing model_fn and to make model_fn more configurable for
   Estimator.
2. Simpilfy creating loss and metrics for the train and test loop in Eager
   execution.
3. Support wide range of machine learning models. Since most heads can work
   with logits, they can support DNN, RNN, Wide, Wide&Deep,
   Global objectives, Gradient boosted trees and many other types
   of machine learning models.

#### Common usage:


Here is simplified model_fn to build a DNN regression model.

>     def _my_dnn_model_fn(features, labels, mode, params, config=None):
>       # Optionally your callers can pass head to model_fn as a param.
>       head = tf.estimator.RegressionHead(...)
>     
>       # TODO(b/117839674): update feature_column
>       inputs = tf.feature_column.input_layer(features, ...)
>     
>       # Compute logits with tf.keras.layers API
>       hidden_layer0 = tf.keras.layers.Dense(
>           units=1000, activation="relu")(inputs)
>       hidden_layer1 = tf.keras.layers.Dense(
>           units=500, activation="relu")(hidden_layer0)
>       logits = tf.keras.layers.Dense(
>           units=head.logits_dimension, activation=None)(hidden_layer1)
>     
>       # Or use Keras model for logits computation
>       model = tf.keras.Sequential()
>       model.add(tf.keras.layers.Dense(units=1000, activation="relu"))
>       model.add(tf.keras.layers.Dense(units=500, activation="relu"))
>       model.add(tf.keras.layers.Dense(
>          units=head.logits_dimension, activation=None))
>       logits = model(inputs)
>     
>       return head.create_estimator_spec(
>           features=features,
>           labels=labels,
>           mode=mode,
>           logits=logits,
>           optimizer=optimizer)

## Properties

<h3 id="logits_dimension"><code>logits_dimension</code></h3>

Size of the last dimension of the logits `Tensor`.

Often is the number of classes, labels, or real values to be predicted.
Typically, logits is of shape `[batch_size, logits_dimension]`.

#### Returns:

The expected size of the `logits` tensor.


<h3 id="loss_reduction"><code>loss_reduction</code></h3>

One of <a href="../../tf/keras/losses/Reduction"><code>tf.losses.Reduction</code></a>.

Describes how to reduce training loss over batch, such as mean or sum.

#### Returns:

The type of loss reduction used in the head.


<h3 id="name"><code>name</code></h3>

The name of this head.


#### Returns:

A string.




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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

``` python
loss(
    labels,
    logits,
    features=None,
    mode=None,
    regularization_losses=None
)
```

Returns a loss `Tensor` from provided arguments.

Note that, the args of `features` and `mode` are most likely not used, but
some Head implementations may require them.

#### Args:


* <b>`labels`</b>: Labels `Tensor`, or `dict` mapping string label names to `Tensor`
  objects of the label values.
* <b>`logits`</b>: Logits `Tensor` to be used for loss construction.
* <b>`features`</b>: Input `dict` mapping string feature names to `Tensor` or
  `SparseTensor` objects containing the values for that feature in a
  minibatch. Often to be used to fetch example-weight tensor.
* <b>`mode`</b>: Estimator's `ModeKeys`. To be used in case loss calculation is
  different in Train and Eval mode.
* <b>`regularization_losses`</b>: A list of additional scalar losses to be added to
  the training loss, such as regularization losses.


#### Returns:

A scalar `Tensor` representing regularized training loss used in train and
eval.


<h3 id="metrics"><code>metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

``` python
metrics(regularization_losses=None)
```

Returns a `dict` of metric objects.


#### Args:


* <b>`regularization_losses`</b>: A list of additional scalar losses to be added to
  the training loss, such as regularization losses.


#### Returns:

A `dict` of metrics keyed by string name. The value is an instance of
`Metric` class.


<h3 id="predictions"><code>predictions</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

``` python
predictions(
    logits,
    keys=None
)
```

Returns a `dict` of predictions from provided logits.


#### Args:


* <b>`logits`</b>: Logits `Tensor` to be used for prediction construction.
* <b>`keys`</b>: A list of `string` for prediction keys. Defaults to `None`, meaning
  if not specified, predictions will be created for all the pre-defined
  valid keys in the head.


#### Returns:

A `dict` of predicted `Tensor` keyed by prediction name.


<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

``` python
update_metrics(
    eval_metrics,
    features,
    logits,
    labels,
    mode=None,
    regularization_losses=None
)
```

Updates metric objects and returns a `dict` of the updated metrics.


#### Args:


* <b>`eval_metrics`</b>: A `dict` of metrics to be updated.
* <b>`features`</b>: Input `dict` mapping string feature names to `Tensor` or
  `SparseTensor` objects containing the values for that feature in a
  minibatch. Often to be used to fetch example-weight tensor.
* <b>`logits`</b>: logits `Tensor` to be used for metrics update.
* <b>`labels`</b>: Labels `Tensor`, or `dict` mapping string label names to `Tensor`
  objects of the label values.
* <b>`mode`</b>: Estimator's `ModeKeys`.
* <b>`regularization_losses`</b>: A list of additional scalar losses to be added to
  the training and evaluation loss, such as regularization losses.


#### Returns:

A `dict` of updated metrics keyed by name. The value is an instance of
`Metric` class.
