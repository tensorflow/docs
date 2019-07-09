page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.GraphKeys

## Class `GraphKeys`





Defined in [`tensorflow/python/framework/ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/framework/ops.py).

Standard names to use for graph collections.

The standard library uses various well-known names to collect and
retrieve values associated with a graph. For example, the
`tf.Optimizer` subclasses default to optimizing the variables
collected under <a href="../tf/GraphKeys#TRAINABLE_VARIABLES"><code>tf.GraphKeys.TRAINABLE_VARIABLES</code></a> if none is
specified, but it is also possible to pass an explicit list of
variables.

The following standard keys are defined:

* `GLOBAL_VARIABLES`: the default collection of `Variable` objects, shared
  across distributed environment (model variables are subset of these). See
  <a href="../tf/global_variables"><code>tf.global_variables</code></a>
  for more details.
  Commonly, all `TRAINABLE_VARIABLES` variables will be in `MODEL_VARIABLES`,
  and all `MODEL_VARIABLES` variables will be in `GLOBAL_VARIABLES`.
* `LOCAL_VARIABLES`: the subset of `Variable` objects that are local to each
  machine. Usually used for temporarily variables, like counters.
  Note: use <a href="../tf/contrib/framework/local_variable"><code>tf.contrib.framework.local_variable</code></a> to add to this collection.
* `MODEL_VARIABLES`: the subset of `Variable` objects that are used in the
  model for inference (feed forward). Note: use
  <a href="../tf/contrib/framework/model_variable"><code>tf.contrib.framework.model_variable</code></a> to add to this collection.
* `TRAINABLE_VARIABLES`: the subset of `Variable` objects that will
  be trained by an optimizer. See
  <a href="../tf/trainable_variables"><code>tf.trainable_variables</code></a>
  for more details.
* `SUMMARIES`: the summary `Tensor` objects that have been created in the
  graph. See
  <a href="../tf/summary/merge_all"><code>tf.summary.merge_all</code></a>
  for more details.
* `QUEUE_RUNNERS`: the `QueueRunner` objects that are used to
  produce input for a computation. See
  <a href="../tf/train/queue_runner/start_queue_runners"><code>tf.train.start_queue_runners</code></a>
  for more details.
* `MOVING_AVERAGE_VARIABLES`: the subset of `Variable` objects that will also
  keep moving averages.  See
  <a href="../tf/moving_average_variables"><code>tf.moving_average_variables</code></a>
  for more details.
* `REGULARIZATION_LOSSES`: regularization losses collected during graph
  construction.

The following standard keys are _defined_, but their collections are **not**
automatically populated as many of the others are:

* `WEIGHTS`
* `BIASES`
* `ACTIVATIONS`

## Class Members

<h3 id="ACTIVATIONS"><code>ACTIVATIONS</code></h3>

<h3 id="ASSET_FILEPATHS"><code>ASSET_FILEPATHS</code></h3>

<h3 id="BIASES"><code>BIASES</code></h3>

<h3 id="CONCATENATED_VARIABLES"><code>CONCATENATED_VARIABLES</code></h3>

<h3 id="COND_CONTEXT"><code>COND_CONTEXT</code></h3>

<h3 id="EVAL_STEP"><code>EVAL_STEP</code></h3>

<h3 id="GLOBAL_STEP"><code>GLOBAL_STEP</code></h3>

<h3 id="GLOBAL_VARIABLES"><code>GLOBAL_VARIABLES</code></h3>

<h3 id="INIT_OP"><code>INIT_OP</code></h3>

<h3 id="LOCAL_INIT_OP"><code>LOCAL_INIT_OP</code></h3>

<h3 id="LOCAL_RESOURCES"><code>LOCAL_RESOURCES</code></h3>

<h3 id="LOCAL_VARIABLES"><code>LOCAL_VARIABLES</code></h3>

<h3 id="LOSSES"><code>LOSSES</code></h3>

<h3 id="METRIC_VARIABLES"><code>METRIC_VARIABLES</code></h3>

<h3 id="MODEL_VARIABLES"><code>MODEL_VARIABLES</code></h3>

<h3 id="MOVING_AVERAGE_VARIABLES"><code>MOVING_AVERAGE_VARIABLES</code></h3>

<h3 id="QUEUE_RUNNERS"><code>QUEUE_RUNNERS</code></h3>

<h3 id="READY_FOR_LOCAL_INIT_OP"><code>READY_FOR_LOCAL_INIT_OP</code></h3>

<h3 id="READY_OP"><code>READY_OP</code></h3>

<h3 id="REGULARIZATION_LOSSES"><code>REGULARIZATION_LOSSES</code></h3>

<h3 id="RESOURCES"><code>RESOURCES</code></h3>

<h3 id="SAVEABLE_OBJECTS"><code>SAVEABLE_OBJECTS</code></h3>

<h3 id="SAVERS"><code>SAVERS</code></h3>

<h3 id="SUMMARIES"><code>SUMMARIES</code></h3>

<h3 id="SUMMARY_OP"><code>SUMMARY_OP</code></h3>

<h3 id="TABLE_INITIALIZERS"><code>TABLE_INITIALIZERS</code></h3>

<h3 id="TRAINABLE_RESOURCE_VARIABLES"><code>TRAINABLE_RESOURCE_VARIABLES</code></h3>

<h3 id="TRAINABLE_VARIABLES"><code>TRAINABLE_VARIABLES</code></h3>

<h3 id="TRAIN_OP"><code>TRAIN_OP</code></h3>

<h3 id="UPDATE_OPS"><code>UPDATE_OPS</code></h3>

<h3 id="VARIABLES"><code>VARIABLES</code></h3>

<h3 id="WEIGHTS"><code>WEIGHTS</code></h3>

<h3 id="WHILE_CONTEXT"><code>WHILE_CONTEXT</code></h3>

