description: Interface for the head/top of a model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.Head" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="create_estimator_spec"/>
<meta itemprop="property" content="loss"/>
<meta itemprop="property" content="metrics"/>
<meta itemprop="property" content="predictions"/>
<meta itemprop="property" content="update_metrics"/>
</div>

# tf.estimator.Head

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Interface for the head/top of a model.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.Head`</p>
</p>
</section>

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
  ```python
  def _my_dnn_model_fn(features, labels, mode, params, config=None):
    # Optionally your callers can pass head to model_fn as a param.
    head = tf.estimator.RegressionHead(...)

    feature_columns = tf.feature_column.numeric_column(...)
    feature_layer = tf.keras.layers.DenseFeatures(feature_columns)
    inputs = feature_layer(features)

    # Compute logits with tf.keras.layers API
    hidden_layer0 = tf.keras.layers.Dense(
        units=1000, activation="relu")(inputs)
    hidden_layer1 = tf.keras.layers.Dense(
        units=500, activation="relu")(hidden_layer0)
    logits = tf.keras.layers.Dense(
        units=head.logits_dimension, activation=None)(hidden_layer1)

    # Or use Keras model for logits computation
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(units=1000, activation="relu"))
    model.add(tf.keras.layers.Dense(units=500, activation="relu"))
    model.add(tf.keras.layers.Dense(
       units=head.logits_dimension, activation=None))
    logits = model(inputs)

    return head.create_estimator_spec(
        features=features,
        labels=labels,
        mode=mode,
        logits=logits,
        optimizer=optimizer)
  ```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`logits_dimension`
</td>
<td>
Size of the last dimension of the logits `Tensor`.

Often is the number of classes, labels, or real values to be predicted.
Typically, logits is of shape `[batch_size, logits_dimension]`.
</td>
</tr><tr>
<td>
`loss_reduction`
</td>
<td>
One of <a href="../../tf/keras/losses/Reduction.md"><code>tf.losses.Reduction</code></a>.

Describes how to reduce training loss over batch, such as mean or sum.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of this head.
</td>
</tr>
</table>



## Methods

<h3 id="create_estimator_spec"><code>create_estimator_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_estimator_spec(
    features, mode, logits, labels=None, optimizer=None, trainable_variables=None,
    train_op_fn=None, update_ops=None, regularization_losses=None
)
</code></pre>

Returns `EstimatorSpec` that a model_fn can return.

It is recommended to pass all args via name.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`features`
</td>
<td>
Input `dict` mapping string feature names to `Tensor` or
`SparseTensor` objects containing the values for that feature in a
minibatch. Often to be used to fetch example-weight tensor.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
Estimator's `ModeKeys`.
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
Logits `Tensor` to be used by the head.
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
Labels `Tensor`, or `dict` mapping string label names to `Tensor`
objects of the label values.
</td>
</tr><tr>
<td>
`optimizer`
</td>
<td>
An <a href="../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a> instance to optimize the
loss in TRAIN mode. Namely, sets `train_op = optimizer.get_updates(loss,
trainable_variables)`, which updates variables to minimize `loss`.
</td>
</tr><tr>
<td>
`trainable_variables`
</td>
<td>
A list or tuple of `Variable` objects to update to
minimize `loss`. In Tensorflow 1.x, by default these are the list of
variables collected in the graph under the key
`GraphKeys.TRAINABLE_VARIABLES`. As Tensorflow 2.x doesn't have
collections and GraphKeys, trainable_variables need to be passed
explicitly here.
</td>
</tr><tr>
<td>
`train_op_fn`
</td>
<td>
Function that takes a scalar loss `Tensor` and returns an op
to optimize the model with the loss in TRAIN mode. Used if `optimizer`
is `None`. Exactly one of `train_op_fn` and `optimizer` must be set in
TRAIN mode. By default, it is `None` in other modes. If you want to
optimize loss yourself, you can pass `lambda _: tf.no_op()` and then use
<a href="../../tf/estimator/EstimatorSpec.md#loss"><code>EstimatorSpec.loss</code></a> to compute and apply gradients.
</td>
</tr><tr>
<td>
`update_ops`
</td>
<td>
A list or tuple of update ops to be run at training time. For
example, layers such as BatchNormalization create mean and variance
update ops that need to be run at training time. In Tensorflow 1.x,
these are thrown into an UPDATE_OPS collection. As Tensorflow 2.x
doesn't have collections, update_ops need to be passed explicitly here.
</td>
</tr><tr>
<td>
`regularization_losses`
</td>
<td>
A list of additional scalar losses to be added to
the training loss, such as regularization losses.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`EstimatorSpec`.
</td>
</tr>

</table>



<h3 id="loss"><code>loss</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>loss(
    labels, logits, features=None, mode=None, regularization_losses=None
)
</code></pre>

Returns a loss `Tensor` from provided arguments.

Note that, the args of `features` and `mode` are most likely not used, but
some Head implementations may require them.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`labels`
</td>
<td>
Labels `Tensor`, or `dict` mapping string label names to `Tensor`
objects of the label values.
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
Logits `Tensor` to be used for loss construction.
</td>
</tr><tr>
<td>
`features`
</td>
<td>
Input `dict` mapping string feature names to `Tensor` or
`SparseTensor` objects containing the values for that feature in a
minibatch. Often to be used to fetch example-weight tensor.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
Estimator's `ModeKeys`. To be used in case loss calculation is
different in Train and Eval mode.
</td>
</tr><tr>
<td>
`regularization_losses`
</td>
<td>
A list of additional scalar losses to be added to
the training loss, such as regularization losses.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A scalar `Tensor` representing regularized training loss used in train and
eval.
</td>
</tr>

</table>



<h3 id="metrics"><code>metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>metrics(
    regularization_losses=None
)
</code></pre>

Returns a `dict` of metric objects.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`regularization_losses`
</td>
<td>
A list of additional scalar losses to be added to
the training loss, such as regularization losses.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `dict` of metrics keyed by string name. The value is an instance of
`Metric` class.
</td>
</tr>

</table>



<h3 id="predictions"><code>predictions</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>predictions(
    logits, keys=None
)
</code></pre>

Returns a `dict` of predictions from provided logits.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`logits`
</td>
<td>
Logits `Tensor` to be used for prediction construction.
</td>
</tr><tr>
<td>
`keys`
</td>
<td>
A list of `string` for prediction keys. Defaults to `None`, meaning
if not specified, predictions will be created for all the pre-defined
valid keys in the head.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `dict` of predicted `Tensor` keyed by prediction name.
</td>
</tr>

</table>



<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>update_metrics(
    eval_metrics, features, logits, labels, mode=None, regularization_losses=None
)
</code></pre>

Updates metric objects and returns a `dict` of the updated metrics.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`eval_metrics`
</td>
<td>
A `dict` of metrics to be updated.
</td>
</tr><tr>
<td>
`features`
</td>
<td>
Input `dict` mapping string feature names to `Tensor` or
`SparseTensor` objects containing the values for that feature in a
minibatch. Often to be used to fetch example-weight tensor.
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
logits `Tensor` to be used for metrics update.
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
Labels `Tensor`, or `dict` mapping string label names to `Tensor`
objects of the label values.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
Estimator's `ModeKeys`. In most cases, this arg is not used and can
be removed in the method implementation.
</td>
</tr><tr>
<td>
`regularization_losses`
</td>
<td>
A list of additional scalar losses to be added to
the training and evaluation loss, such as regularization losses.  Note
that, the `mode` arg is not used in the `tf.estimator.*Head`. If the
update of the metrics doesn't rely on `mode`, it can be safely ignored
in the method signature.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `dict` of updated metrics keyed by name. The value is an instance of
`Metric` class.
</td>
</tr>

</table>





