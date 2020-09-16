description: Creates a Head for single label binary classification.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.BinaryClassHead" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_estimator_spec"/>
<meta itemprop="property" content="loss"/>
<meta itemprop="property" content="metrics"/>
<meta itemprop="property" content="predictions"/>
<meta itemprop="property" content="update_metrics"/>
</div>

# tf.estimator.BinaryClassHead

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/binary_class_head.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a `Head` for single label binary classification.

Inherits From: [`Head`](../../tf/estimator/Head.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.BinaryClassHead`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.BinaryClassHead(
    weight_column=None, thresholds=None, label_vocabulary=None,
    loss_reduction=losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE, loss_fn=None,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Uses `sigmoid_cross_entropy_with_logits` loss.

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
`(labels, logits, features, loss_reduction)` as arguments and returns loss
with shape `[D0, D1, ... DN, 1]`. `loss_fn` must support float `labels` with
shape `[D0, D1, ... DN, 1]`. Namely, the head applies `label_vocabulary` to
the input labels before passing them to `loss_fn`.

#### Usage:



```
>>> head = tf.estimator.BinaryClassHead()
>>> logits = np.array(((45,), (-41,),), dtype=np.float32)
>>> labels = np.array(((1,), (1,),), dtype=np.int32)
>>> features = {'x': np.array(((42,),), dtype=np.float32)}
>>> # expected_loss = sum(cross_entropy(labels, logits)) / batch_size
>>> #               = sum(0, 41) / 2 = 41 / 2 = 20.50
>>> loss = head.loss(labels, logits, features=features)
>>> print('{:.2f}'.format(loss.numpy()))
20.50
>>> eval_metrics = head.metrics()
>>> updated_metrics = head.update_metrics(
...   eval_metrics, features, logits, labels)
>>> for k in sorted(updated_metrics):
...  print('{} : {:.2f}'.format(k, updated_metrics[k].result().numpy()))
  accuracy : 0.50
  accuracy_baseline : 1.00
  auc : 0.00
  auc_precision_recall : 1.00
  average_loss : 20.50
  label/mean : 1.00
  precision : 1.00
  prediction/mean : 0.50
  recall : 0.50
>>> preds = head.predictions(logits)
>>> print(preds['logits'])
tf.Tensor(
  [[ 45.]
   [-41.]], shape=(2, 1), dtype=float32)
```

Usage with a canned estimator:

```python
my_head = tf.estimator.BinaryClassHead()
my_estimator = tf.estimator.DNNEstimator(
    head=my_head,
    hidden_units=...,
    feature_columns=...)
```

It can also be used with a custom `model_fn`. Example:

```python
def _my_model_fn(features, labels, mode):
  my_head = tf.estimator.BinaryClassHead()
  logits = tf.keras.Model(...)(features)

  return my_head.create_estimator_spec(
      features=features,
      mode=mode,
      labels=labels,
      optimizer=tf.keras.optimizers.Adagrad(lr=0.1),
      logits=logits)

my_estimator = tf.estimator.Estimator(model_fn=_my_model_fn)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`weight_column`
</td>
<td>
A string or a `NumericColumn` created by
<a href="../../tf/feature_column/numeric_column.md"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
weights. It is used to down weight or boost examples during training. It
will be multiplied by the loss of the example.
</td>
</tr><tr>
<td>
`thresholds`
</td>
<td>
Iterable of floats in the range `(0, 1)`. For binary
classification metrics such as precision and recall, an eval metric is
generated for each threshold value. This threshold is applied to the
logistic values to determine the binary classification (i.e., above the
threshold is `true`, below is `false`.
</td>
</tr><tr>
<td>
`label_vocabulary`
</td>
<td>
A list or tuple of strings representing possible label
values. If it is not given, that means labels are already encoded within
[0, 1]. If given, labels must be string type and have any value in
`label_vocabulary`. Note that errors will be raised if `label_vocabulary`
is not provided but labels are strings.
</td>
</tr><tr>
<td>
`loss_reduction`
</td>
<td>
One of <a href="../../tf/keras/losses/Reduction.md"><code>tf.losses.Reduction</code></a> except `NONE`. Decides how to
reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`, namely
weighted sum of losses divided by `batch size * label_dimension`.
</td>
</tr><tr>
<td>
`loss_fn`
</td>
<td>
Optional loss function.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name of the head. If provided, summary and metrics keys will be
suffixed by `"/" + name`. Also used as `name_scope` when creating ops.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`logits_dimension`
</td>
<td>
See `base_head.Head` for details.
</td>
</tr><tr>
<td>
`loss_reduction`
</td>
<td>
See `base_head.Head` for details.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
See `base_head.Head` for details.
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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/binary_class_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>loss(
    labels, logits, features=None, mode=None, regularization_losses=None
)
</code></pre>

Returns regularized training loss. See `base_head.Head` for details.


<h3 id="metrics"><code>metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/binary_class_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>metrics(
    regularization_losses=None
)
</code></pre>

Creates metrics. See `base_head.Head` for details.


<h3 id="predictions"><code>predictions</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/binary_class_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predictions(
    logits, keys=None
)
</code></pre>

Return predictions based on keys.

See `base_head.Head` for details.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`logits`
</td>
<td>
logits `Tensor` with shape `[D0, D1, ... DN, logits_dimension]`.
For many applications, the shape is `[batch_size, logits_dimension]`.
</td>
</tr><tr>
<td>
`keys`
</td>
<td>
a list or tuple of prediction keys. Each key can be either the class
variable of prediction_keys.PredictionKeys or its string value, such as:
prediction_keys.PredictionKeys.CLASSES or 'classes'. If not specified,
it will return the predictions for all valid keys.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict of predictions.
</td>
</tr>

</table>



<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/binary_class_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_metrics(
    eval_metrics, features, logits, labels, regularization_losses=None
)
</code></pre>

Updates eval metrics. See `base_head.Head` for details.




