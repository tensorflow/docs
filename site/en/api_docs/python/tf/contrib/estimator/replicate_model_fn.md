page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.replicate_model_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/contrib/estimator/python/estimator/replicate_model_fn.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Replicate <a href="/api_docs/python/tf/estimator/Estimator#model_fn"><code>Estimator.model_fn</code></a> over GPUs. (deprecated)

``` python
tf.contrib.estimator.replicate_model_fn(
    model_fn,
    loss_reduction=losses.Reduction.SUM_BY_NONZERO_WEIGHTS,
    devices=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-05-31.
Instructions for updating:
Please use <a href="../../../tf/contrib/distribute/MirroredStrategy"><code>tf.contrib.distribute.MirroredStrategy</code></a> instead.

The given `model_fn` specifies a single forward pass of a model.  To replicate
such a model over GPUs, each GPU gets its own instance of the forward pass
(a.k.a. a tower).  The input features and labels get sharded into the chunks
that correspond to the number of GPUs.  Each tower computes a loss based
on its input.  For each such loss, gradients are computed.  After that, the
available losses are aggregated to form aggregated loss.  Available
gradients are summed.  Then, they update weights using the specified
optimizer.

If `devices` are `None`, then all available GPUs are going to be used for
replication.  If no GPUs are available, then the model is going to be
placed on the CPU.

Two modes of local replication over available GPUs are supported:
  1)  If exactly 1 GPU is detected, then variables and operations are placed
      onto the GPU.
  2)  If more than 1 GPU is detected, then variables are going to be placed on
      the CPU.  Replicas of operations are placed on each individual GPU.

Here is an example of how one might use their `model_fn` to run over GPUs:

>        ...
>        def model_fn(...):  # See `model_fn` in `Estimator`.
>          loss = ...
>          optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
>          optimizer = tf.contrib.estimator.TowerOptimizer(optimizer)
>          if mode == tf.estimator.ModeKeys.TRAIN:
>            #  See the section below on `EstimatorSpec.train_op`.
>            return EstimatorSpec(mode=mode, loss=loss,
>                                 train_op=optimizer.minimize(loss))
>     
>          #  No change for `ModeKeys.EVAL` or `ModeKeys.PREDICT`.
>          return EstimatorSpec(...)
>        ...
>        classifier = tf.estimator.Estimator(
>          model_fn=tf.contrib.estimator.replicate_model_fn(model_fn))

Please see `DNNClassifierIntegrationTest` for an example with a canned
Estimator.

On <a href="/api_docs/python/tf/estimator/EstimatorSpec#train_op"><code>EstimatorSpec.train_op</code></a>:
`model_fn` returns <a href="/api_docs/python/tf/estimator/EstimatorSpec#train_op"><code>EstimatorSpec.train_op</code></a> for
`tf.estimator.GraphKeys.TRAIN`. It is typically derived using an optimizer.
Towers are expected to populate it in the same way.  Gradients from all towers
are reduced and applied in the last tower.  To achieve that in the case of
multiple towers, `TowerOptimizer` needs to be used.  See `TowerOptimizer`.

On sharding input features and labels:
Input features and labels are split for consumption by each tower. They are
split across the dimension 0.  Features and labels need to be batch major.

On reduction algorithms:
Certain algorithms were chosen for aggregating results of computations on
multiple towers:
  - Losses from all towers are reduced according to `loss_reduction`.
  - Gradients from all towers are reduced according to `loss_reduction`
    for each trainable variable.
  - `eval_metrics_ops` are reduced per metric using `reduce_mean`.
  - <a href="/api_docs/python/tf/estimator/EstimatorSpec#predictions"><code>EstimatorSpec.predictions</code></a> and <a href="/api_docs/python/tf/estimator/EstimatorSpec#export_outputs"><code>EstimatorSpec.export_outputs</code></a> are
    reduced using concatenation.
  - For all other fields of `EstimatorSpec` the values of the first tower
    are taken.

On distribution of variables:
Variables are not duplicated between towers.  Instead, they are placed on a
single device as defined above and shared across towers.

#### On overhead:


If only one device is specified, then aggregation of loss and gradients
doesn't happen. Replication consists of placing `model_fn` onto the
specified device.

On current limitations:
  - `predictions` are not supported for <a href="/api_docs/python/tf/estimator/ModeKeys#EVAL"><code>ModeKeys.EVAL</code></a>.  They are required
     for <a href="../../../tf/contrib/estimator/add_metrics"><code>tf.contrib.estimator.add_metrics</code></a>.

#### Args:


* <b>`model_fn`</b>: `model_fn` as defined in `Estimator`.  See the section above about
  the train_op argument of `EstimatorSpec`.
* <b>`loss_reduction`</b>: controls whether losses are summed or averaged.
* <b>`devices`</b>: Optional list of devices to replicate the model across.  This
  argument can be used to replicate only on the subset of available GPUs.
  If `None`, then all available GPUs are going to be used for replication.
  If no GPUs are available, then the model is going to be placed on the CPU.


#### Raises:


* <b>`ValueError`</b>: if there is no `loss_reduction` or if TowerOptimizer is
  mis-used.


#### Returns:

A replicated version of the supplied `model_fn`. Returned function that
  conforms to the requirements of `Estimator`'s `model_fn` and can be used
  instead of the supplied `model_fn`.
