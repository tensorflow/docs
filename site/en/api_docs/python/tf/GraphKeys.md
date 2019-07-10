page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.GraphKeys

## Class `GraphKeys`

Standard names to use for graph collections.



### Aliases:

* Class `tf.GraphKeys`
* Class `tf.compat.v1.GraphKeys`



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->

The standard library uses various well-known names to collect and
retrieve values associated with a graph. For example, the
`tf.Optimizer` subclasses default to optimizing the variables
collected under <a href="../tf/GraphKeys#TRAINABLE_VARIABLES"><code>tf.GraphKeys.TRAINABLE_VARIABLES</code></a> if none is
specified, but it is also possible to pass an explicit list of
variables.

The following standard keys are defined:

* `GLOBAL_VARIABLES`: the default collection of `Variable` objects, shared
  across distributed environment (model variables are subset of these). See
  <a href="../tf/global_variables"><code>tf.compat.v1.global_variables</code></a>
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
  <a href="../tf/trainable_variables"><code>tf.compat.v1.trainable_variables</code></a>
  for more details.
* `SUMMARIES`: the summary `Tensor` objects that have been created in the
  graph. See
  <a href="../tf/summary/merge_all"><code>tf.compat.v1.summary.merge_all</code></a>
  for more details.
* `QUEUE_RUNNERS`: the `QueueRunner` objects that are used to
  produce input for a computation. See
  <a href="../tf/train/queue_runner/start_queue_runners"><code>tf.compat.v1.train.start_queue_runners</code></a>
  for more details.
* `MOVING_AVERAGE_VARIABLES`: the subset of `Variable` objects that will also
  keep moving averages.  See
  <a href="../tf/moving_average_variables"><code>tf.compat.v1.moving_average_variables</code></a>
  for more details.
* `REGULARIZATION_LOSSES`: regularization losses collected during graph
  construction.

The following standard keys are _defined_, but their collections are **not**
automatically populated as many of the others are:

* `WEIGHTS`
* `BIASES`
* `ACTIVATIONS`

## Class Members

* `ACTIVATIONS = 'activations'` <a id="ACTIVATIONS"></a>
* `ASSET_FILEPATHS = 'asset_filepaths'` <a id="ASSET_FILEPATHS"></a>
* `BIASES = 'biases'` <a id="BIASES"></a>
* `CONCATENATED_VARIABLES = 'concatenated_variables'` <a id="CONCATENATED_VARIABLES"></a>
* `COND_CONTEXT = 'cond_context'` <a id="COND_CONTEXT"></a>
* `EVAL_STEP = 'eval_step'` <a id="EVAL_STEP"></a>
* `GLOBAL_STEP = 'global_step'` <a id="GLOBAL_STEP"></a>
* `GLOBAL_VARIABLES = 'variables'` <a id="GLOBAL_VARIABLES"></a>
* `INIT_OP = 'init_op'` <a id="INIT_OP"></a>
* `LOCAL_INIT_OP = 'local_init_op'` <a id="LOCAL_INIT_OP"></a>
* `LOCAL_RESOURCES = 'local_resources'` <a id="LOCAL_RESOURCES"></a>
* `LOCAL_VARIABLES = 'local_variables'` <a id="LOCAL_VARIABLES"></a>
* `LOSSES = 'losses'` <a id="LOSSES"></a>
* `METRIC_VARIABLES = 'metric_variables'` <a id="METRIC_VARIABLES"></a>
* `MODEL_VARIABLES = 'model_variables'` <a id="MODEL_VARIABLES"></a>
* `MOVING_AVERAGE_VARIABLES = 'moving_average_variables'` <a id="MOVING_AVERAGE_VARIABLES"></a>
* `QUEUE_RUNNERS = 'queue_runners'` <a id="QUEUE_RUNNERS"></a>
* `READY_FOR_LOCAL_INIT_OP = 'ready_for_local_init_op'` <a id="READY_FOR_LOCAL_INIT_OP"></a>
* `READY_OP = 'ready_op'` <a id="READY_OP"></a>
* `REGULARIZATION_LOSSES = 'regularization_losses'` <a id="REGULARIZATION_LOSSES"></a>
* `RESOURCES = 'resources'` <a id="RESOURCES"></a>
* `SAVEABLE_OBJECTS = 'saveable_objects'` <a id="SAVEABLE_OBJECTS"></a>
* `SAVERS = 'savers'` <a id="SAVERS"></a>
* `SUMMARIES = 'summaries'` <a id="SUMMARIES"></a>
* `SUMMARY_OP = 'summary_op'` <a id="SUMMARY_OP"></a>
* `TABLE_INITIALIZERS = 'table_initializer'` <a id="TABLE_INITIALIZERS"></a>
* `TRAINABLE_RESOURCE_VARIABLES = 'trainable_resource_variables'` <a id="TRAINABLE_RESOURCE_VARIABLES"></a>
* `TRAINABLE_VARIABLES = 'trainable_variables'` <a id="TRAINABLE_VARIABLES"></a>
* `TRAIN_OP = 'train_op'` <a id="TRAIN_OP"></a>
* `UPDATE_OPS = 'update_ops'` <a id="UPDATE_OPS"></a>
* `VARIABLES = 'variables'` <a id="VARIABLES"></a>
* `WEIGHTS = 'weights'` <a id="WEIGHTS"></a>
* `WHILE_CONTEXT = 'while_context'` <a id="WHILE_CONTEXT"></a>
