description: Creates a Head for multi-objective learning.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.MultiHead" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_estimator_spec"/>
<meta itemprop="property" content="loss"/>
<meta itemprop="property" content="metrics"/>
<meta itemprop="property" content="predictions"/>
<meta itemprop="property" content="update_metrics"/>
</div>

# tf.estimator.MultiHead

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a `Head` for multi-objective learning.

Inherits From: [`Head`](../../tf/estimator/Head.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.MultiHead`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.MultiHead(
    heads, head_weights=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class merges the output of multiple `Head` objects. Specifically:

* For training, sums losses of each head, calls `train_op_fn` with this
  final loss.
* For eval, merges metrics by adding `head.name` suffix to the keys in eval
  metrics, such as `precision/head1.name`, `precision/head2.name`.
* For prediction, merges predictions and updates keys in prediction dict to a
  2-tuple, `(head.name, prediction_key)`. Merges `export_outputs` such that
  by default the first head is served.

#### Usage:



```
>>> head1 = tf.estimator.MultiLabelHead(n_classes=2, name='head1')
>>> head2 = tf.estimator.MultiLabelHead(n_classes=3, name='head2')
>>> multi_head = tf.estimator.MultiHead([head1, head2])
>>> logits = {
...    'head1': np.array([[-10., 10.], [-15., 10.]], dtype=np.float32),
...    'head2': np.array([[20., -20., 20.], [-30., 20., -20.]],
...    dtype=np.float32),}
>>> labels = {
...    'head1': np.array([[1, 0], [1, 1]], dtype=np.int64),
...    'head2': np.array([[0, 1, 0], [1, 1, 0]], dtype=np.int64),}
>>> features = {'x': np.array(((42,),), dtype=np.float32)}
>>> # For large logits, sigmoid cross entropy loss is approximated as:
>>> # loss = labels * (logits < 0) * (-logits) +
>>> #        (1 - labels) * (logits > 0) * logits =>
>>> # head1: expected_unweighted_loss = [[10., 10.], [15., 0.]]
>>> # loss1 = ((10 + 10) / 2 + (15 + 0) / 2) / 2 = 8.75
>>> # head2: expected_unweighted_loss = [[20., 20., 20.], [30., 0., 0]]
>>> # loss2 = ((20 + 20 + 20) / 3 + (30 + 0 + 0) / 3) / 2 = 15.00
>>> # loss = loss1 + loss2 = 8.75 + 15.00 = 23.75
>>> loss = multi_head.loss(labels, logits, features=features)
>>> print('{:.2f}'.format(loss.numpy()))
23.75
>>> eval_metrics = multi_head.metrics()
>>> updated_metrics = multi_head.update_metrics(
...   eval_metrics, features, logits, labels)
>>> for k in sorted(updated_metrics):
...  print('{} : {:.2f}'.format(k, updated_metrics[k].result().numpy()))
auc/head1 : 0.17
auc/head2 : 0.33
auc_precision_recall/head1 : 0.60
auc_precision_recall/head2 : 0.40
average_loss/head1 : 8.75
average_loss/head2 : 15.00
loss/head1 : 8.75
loss/head2 : 15.00
>>> preds = multi_head.predictions(logits)
>>> print(preds[('head1', 'logits')])
tf.Tensor(
  [[-10.  10.]
   [-15.  10.]], shape=(2, 2), dtype=float32)
```

Usage with a canned estimator:

```python
# In `input_fn`, specify labels as a dict keyed by head name:
def input_fn():
  features = ...
  labels1 = ...
  labels2 = ...
  return features, {'head1.name': labels1, 'head2.name': labels2}

# In `model_fn`, specify logits as a dict keyed by head name:
def model_fn(features, labels, mode):
  # Create simple heads and specify head name.
  head1 = tf.estimator.MultiClassHead(n_classes=3, name='head1')
  head2 = tf.estimator.BinaryClassHead(name='head2')
  # Create MultiHead from two simple heads.
  head = tf.estimator.MultiHead([head1, head2])
  # Create logits for each head, and combine them into a dict.
  logits1, logits2 = logit_fn()
  logits = {'head1.name': logits1, 'head2.name': logits2}
  # Return the merged EstimatorSpec
  return head.create_estimator_spec(..., logits=logits, ...)

# Create an estimator with this model_fn.
estimator = tf.estimator.Estimator(model_fn=model_fn)
estimator.train(input_fn=input_fn)
```

Also supports `logits` as a `Tensor` of shape
`[D0, D1, ... DN, logits_dimension]`. It will split the `Tensor` along the
last dimension and distribute it appropriately among the heads. E.g.:

```python
# Input logits.
logits = np.array([[-1., 1., 2., -2., 2.], [-1.5, 1., -3., 2., -2.]],
                  dtype=np.float32)
# Suppose head1 and head2 have the following logits dimension.
head1.logits_dimension = 2
head2.logits_dimension = 3
# After splitting, the result will be:
logits_dict = {'head1_name': [[-1., 1.], [-1.5, 1.]],
               'head2_name':  [[2., -2., 2.], [-3., 2., -2.]]}
```

#### Usage:



```python
def model_fn(features, labels, mode):
  # Create simple heads and specify head name.
  head1 = tf.estimator.MultiClassHead(n_classes=3, name='head1')
  head2 = tf.estimator.BinaryClassHead(name='head2')
  # Create multi-head from two simple heads.
  head = tf.estimator.MultiHead([head1, head2])
  # Create logits for the multihead. The result of logits is a `Tensor`.
  logits = logit_fn(logits_dimension=head.logits_dimension)
  # Return the merged EstimatorSpec
  return head.create_estimator_spec(..., logits=logits, ...)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`heads`
</td>
<td>
List or tuple of `Head` instances. All heads must have `name`
specified. The first head in the list is the default used at serving time.
</td>
</tr><tr>
<td>
`head_weights`
</td>
<td>
Optional list of weights, same length as `heads`. Used when
merging losses to calculate the weighted sum of losses from each head. If
`None`, all losses are weighted equally.
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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_estimator_spec(
    features, mode, logits, labels=None, optimizer=None, trainable_variables=None,
    train_op_fn=None, update_ops=None, regularization_losses=None
)
</code></pre>

Returns a `model_fn.EstimatorSpec`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`features`
</td>
<td>
Input `dict` of `Tensor` or `SparseTensor` objects.
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
Input `dict` keyed by head name, or logits `Tensor` with shape
`[D0, D1, ... DN, logits_dimension]`. For many applications, the
`Tensor` shape is `[batch_size, logits_dimension]`. If logits is a
`Tensor`, it  will split the `Tensor` along the last dimension and
distribute it appropriately among the heads. Check `MultiHead` for
examples.
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
Input `dict` keyed by head name. For each head, the label value
can be integer or string `Tensor` with shape matching its corresponding
`logits`.`labels` is a required argument when `mode` equals `TRAIN` or
`EVAL`.
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
Function that takes a scalar loss `Tensor` and returns
`train_op`. Used if `optimizer` is `None`.
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
the training loss, such as regularization losses. These losses are
usually expressed as a batch average, so for best results, in each head,
users need to use the default `loss_reduction=SUM_OVER_BATCH_SIZE` to
avoid scaling errors.  Compared to the regularization losses for each
head, this loss is to regularize the merged loss of all heads in multi
head, and will be added to the overall training loss of multi head.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `model_fn.EstimatorSpec` instance.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If both `train_op_fn` and `optimizer` are `None` in TRAIN
mode, or if both are set.
If `mode` is not in Estimator's `ModeKeys`.
</td>
</tr>
</table>



<h3 id="loss"><code>loss</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>loss(
    labels, logits, features=None, mode=None, regularization_losses=None
)
</code></pre>

Returns regularized training loss. See `base_head.Head` for details.


<h3 id="metrics"><code>metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>metrics(
    regularization_losses=None
)
</code></pre>

Creates metrics. See `base_head.Head` for details.


<h3 id="predictions"><code>predictions</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predictions(
    logits, keys=None
)
</code></pre>

Create predictions. See `base_head.Head` for details.


<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_metrics(
    eval_metrics, features, logits, labels, regularization_losses=None
)
</code></pre>

Updates eval metrics. See `base_head.Head` for details.




