page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.MultiHead


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/estimator/MultiHead">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MultiHead`

Creates a `Head` for multi-objective learning.

Inherits From: [`Head`](../../tf/estimator/Head)

### Aliases:

* Class <a href="/api_docs/python/tf/estimator/MultiHead"><code>tf.compat.v1.estimator.MultiHead</code></a>
* Class <a href="/api_docs/python/tf/estimator/MultiHead"><code>tf.compat.v2.estimator.MultiHead</code></a>


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
# Input logits.
# logits = np.array([[-1., 1., 2., -2., 2.], [-1.5, 1., -3., 2., -2.]],
                    dtype=np.float32)
# Suppose head1.logits_dimension = 2 and head2.logits_dimension = 3. After
# splitting, the result is:
# logits_dict = {'head1_name': [[-1., 1.], [-1.5, 1.]],
                 'head2_name':  [[2., -2., 2.], [-3., 2., -2.]]}
Usage:

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

#### Args:


* <b>`heads`</b>: List or tuple of `Head` instances. All heads must have `name`
  specified. The first head in the list is the default used at serving time.
* <b>`head_weights`</b>: Optional list of weights, same length as `heads`. Used when
  merging losses to calculate the weighted sum of losses from each head. If
  `None`, all losses are weighted equally.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

``` python
__init__(
    heads,
    head_weights=None
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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

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

Returns a `model_fn.EstimatorSpec`.


#### Args:


* <b>`features`</b>: Input `dict` of `Tensor` or `SparseTensor` objects.
* <b>`mode`</b>: Estimator's `ModeKeys`.
* <b>`logits`</b>: Input `dict` keyed by head name, or logits `Tensor` with shape
  `[D0, D1, ... DN, logits_dimension]`. For many applications, the
  `Tensor` shape is `[batch_size, logits_dimension]`. If logits is a
  `Tensor`, it  will split the `Tensor` along the last dimension and
  distribute it appropriately among the heads. Check `MultiHead` for
  examples.
* <b>`labels`</b>: Input `dict` keyed by head name. For each head, the label value
  can be integer or string `Tensor` with shape matching its corresponding
  `logits`.`labels` is a required argument when `mode` equals `TRAIN` or
  `EVAL`.
* <b>`optimizer`</b>: An <a href="../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a> instance to optimize the
  loss in TRAIN mode. Namely, sets `train_op = optimizer.get_updates(loss,
  trainable_variables)`, which updates variables to minimize `loss`.
* <b>`trainable_variables`</b>: A list or tuple of `Variable` objects to update to
  minimize `loss`. In Tensorflow 1.x, by default these are the list of
  variables collected in the graph under the key
  <a href="../../tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a>. As Tensorflow 2.x doesn't have
  collections and GraphKeys, trainable_variables need to be passed
  explicitly here.
* <b>`train_op_fn`</b>: Function that takes a scalar loss `Tensor` and returns
  `train_op`. Used if `optimizer` is `None`.
* <b>`update_ops`</b>: A list or tuple of update ops to be run at training time. For
  example, layers such as BatchNormalization create mean and variance
  update ops that need to be run at training time. In Tensorflow 1.x,
  these are thrown into an UPDATE_OPS collection. As Tensorflow 2.x
  doesn't have collections, update_ops need to be passed explicitly here.
* <b>`regularization_losses`</b>: A list of additional scalar losses to be added to
  the training loss, such as regularization losses. These losses are
  usually expressed as a batch average, so for best results, in each head,
  users need to use the default `loss_reduction=SUM_OVER_BATCH_SIZE` to
  avoid scaling errors.  Compared to the regularization losses for each
  head, this loss is to regularize the merged loss of all heads in multi
  head, and will be added to the overall training loss of multi head.


#### Returns:

A `model_fn.EstimatorSpec` instance.



#### Raises:


* <b>`ValueError`</b>: If both `train_op_fn` and `optimizer` are `None` in TRAIN
mode, or if both are set.
If `mode` is not in Estimator's `ModeKeys`.

<h3 id="loss"><code>loss</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

``` python
metrics(regularization_losses=None)
```

Creates metrics. See `base_head.Head` for details.


<h3 id="predictions"><code>predictions</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

``` python
predictions(
    logits,
    keys=None
)
```

Create predictions. See `base_head.Head` for details.


<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/multi_head.py">View source</a>

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
