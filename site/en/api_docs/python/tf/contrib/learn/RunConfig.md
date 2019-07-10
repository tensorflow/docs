page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.RunConfig

## Class `RunConfig`

This class specifies the configurations for an `Estimator` run.

Inherits From: [`RunConfig`](../../../tf/estimator/RunConfig)



Defined in [`contrib/learn/python/learn/estimators/run_config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/learn/python/learn/estimators/run_config.py).

<!-- Placeholder for "Used in" -->

This class is a deprecated implementation of <a href="../../../tf/estimator/RunConfig"><code>tf.estimator.RunConfig</code></a>
interface.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    master=None,
    num_cores=0,
    log_device_placement=False,
    gpu_memory_fraction=1,
    tf_random_seed=None,
    save_summary_steps=100,
    save_checkpoints_secs=_USE_DEFAULT,
    save_checkpoints_steps=None,
    keep_checkpoint_max=5,
    keep_checkpoint_every_n_hours=10000,
    log_step_count_steps=100,
    protocol=None,
    evaluation_master='',
    model_dir=None,
    session_config=None
)
```

Constructor. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
When switching to tf.estimator.Estimator, use tf.estimator.RunConfig instead.

The superclass `ClusterConfig` may set properties like `cluster_spec`,
`is_chief`, `master` (if `None` in the args), `num_ps_replicas`, `task_id`,
and `task_type` based on the `TF_CONFIG` environment variable. See
`ClusterConfig` for more details.

N.B.: If `save_checkpoints_steps` or `save_checkpoints_secs` is set,
`keep_checkpoint_max` might need to be adjusted accordingly, especially in
distributed training. For example, setting `save_checkpoints_secs` as 60
without adjusting `keep_checkpoint_max` (defaults to 5) leads to situation
that checkpoint would be garbage collected after 5 minutes. In distributed
training, the evaluation job starts asynchronously and might fail to load or
find the checkpoint due to race condition.

#### Args:


* <b>`master`</b>: TensorFlow master. Defaults to empty string for local.
* <b>`num_cores`</b>: Number of cores to be used. If 0, the system picks an
  appropriate number (default: 0).
* <b>`log_device_placement`</b>: Log the op placement to devices (default: False).
* <b>`gpu_memory_fraction`</b>: Fraction of GPU memory used by the process on
  each GPU uniformly on the same machine.
* <b>`tf_random_seed`</b>: Random seed for TensorFlow initializers.
  Setting this value allows consistency between reruns.
* <b>`save_summary_steps`</b>: Save summaries every this many steps.
* <b>`save_checkpoints_secs`</b>: Save checkpoints every this many seconds. Can not
    be specified with `save_checkpoints_steps`.
* <b>`save_checkpoints_steps`</b>: Save checkpoints every this many steps. Can not be
    specified with `save_checkpoints_secs`.
* <b>`keep_checkpoint_max`</b>: The maximum number of recent checkpoint files to
  keep. As new files are created, older files are deleted. If None or 0,
  all checkpoint files are kept. Defaults to 5 (that is, the 5 most recent
  checkpoint files are kept.)
* <b>`keep_checkpoint_every_n_hours`</b>: Number of hours between each checkpoint
  to be saved. The default value of 10,000 hours effectively disables
  the feature.
* <b>`log_step_count_steps`</b>: The frequency, in number of global steps, that the
  global step/sec will be logged during training.
* <b>`evaluation_master`</b>: the master on which to perform evaluation.
* <b>`model_dir`</b>: directory where model parameters, graph etc are saved. If
  `None`, will use `model_dir` property in `TF_CONFIG` environment
  variable. If both are set, must have same value. If both are `None`, see
  `Estimator` about where the model will be saved.
* <b>`session_config`</b>: a ConfigProto used to set session parameters, or None.
  Note - using this argument, it is easy to provide settings which break
  otherwise perfectly good models. Use with care.
* <b>`protocol`</b>: An optional argument which specifies the protocol used when
  starting server. None means default to grpc.



## Properties

<h3 id="cluster_spec"><code>cluster_spec</code></h3>




<h3 id="device_fn"><code>device_fn</code></h3>

Returns the device_fn.

If device_fn is not `None`, it overrides the default
device function used in `Estimator`.
Otherwise the default one is used.

<h3 id="environment"><code>environment</code></h3>




<h3 id="eval_distribute"><code>eval_distribute</code></h3>

Optional <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> for evaluation.
    

<h3 id="evaluation_master"><code>evaluation_master</code></h3>




<h3 id="experimental_max_worker_delay_secs"><code>experimental_max_worker_delay_secs</code></h3>




<h3 id="global_id_in_cluster"><code>global_id_in_cluster</code></h3>

The global id in the training cluster.

All global ids in the training cluster are assigned from an increasing
sequence of consecutive integers. The first id is 0.

Note: Task id (the property field `task_id`) is tracking the index of the
node among all nodes with the SAME task type. For example, given the cluster
definition as follows:

```
  cluster = {'chief': ['host0:2222'],
             'ps': ['host1:2222', 'host2:2222'],
             'worker': ['host3:2222', 'host4:2222', 'host5:2222']}
```

Nodes with task type `worker` can have id 0, 1, 2.  Nodes with task type
`ps` can have id, 0, 1. So, `task_id` is not unique, but the pair
(`task_type`, `task_id`) can uniquely determine a node in the cluster.

Global id, i.e., this field, is tracking the index of the node among ALL
nodes in the cluster. It is uniquely assigned.  For example, for the cluster
spec given above, the global ids are assigned as:

```
  task_type  | task_id  |  global_id
  --------------------------------
  chief      | 0        |  0
  worker     | 0        |  1
  worker     | 1        |  2
  worker     | 2        |  3
  ps         | 0        |  4
  ps         | 1        |  5
```

#### Returns:

An integer id.


<h3 id="is_chief"><code>is_chief</code></h3>




<h3 id="keep_checkpoint_every_n_hours"><code>keep_checkpoint_every_n_hours</code></h3>




<h3 id="keep_checkpoint_max"><code>keep_checkpoint_max</code></h3>




<h3 id="log_step_count_steps"><code>log_step_count_steps</code></h3>




<h3 id="master"><code>master</code></h3>




<h3 id="model_dir"><code>model_dir</code></h3>




<h3 id="num_ps_replicas"><code>num_ps_replicas</code></h3>




<h3 id="num_worker_replicas"><code>num_worker_replicas</code></h3>




<h3 id="protocol"><code>protocol</code></h3>

Returns the optional protocol value.


<h3 id="save_checkpoints_secs"><code>save_checkpoints_secs</code></h3>




<h3 id="save_checkpoints_steps"><code>save_checkpoints_steps</code></h3>




<h3 id="save_summary_steps"><code>save_summary_steps</code></h3>




<h3 id="service"><code>service</code></h3>

Returns the platform defined (in TF_CONFIG) service dict.


<h3 id="session_config"><code>session_config</code></h3>




<h3 id="task_id"><code>task_id</code></h3>




<h3 id="task_type"><code>task_type</code></h3>




<h3 id="tf_config"><code>tf_config</code></h3>




<h3 id="tf_random_seed"><code>tf_random_seed</code></h3>




<h3 id="train_distribute"><code>train_distribute</code></h3>

Optional <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> for training.
    



## Methods

<h3 id="get_task_id"><code>get_task_id</code></h3>

``` python
get_task_id()
```

Returns task index from `TF_CONFIG` environmental variable.

If you have a ClusterConfig instance, you can just access its task_id
property instead of calling this function and re-parsing the environmental
variable.

#### Returns:

`TF_CONFIG['task']['index']`. Defaults to 0.


<h3 id="replace"><code>replace</code></h3>

``` python
replace(**kwargs)
```

Returns a new instance of `RunConfig` replacing specified properties.

Only the properties in the following list are allowed to be replaced:

  - `model_dir`,
  - `tf_random_seed`,
  - `save_summary_steps`,
  - `save_checkpoints_steps`,
  - `save_checkpoints_secs`,
  - `session_config`,
  - `keep_checkpoint_max`,
  - `keep_checkpoint_every_n_hours`,
  - `log_step_count_steps`,
  - `train_distribute`,
  - `device_fn`,
  - `protocol`.
  - `eval_distribute`,
  - `experimental_distribute`,
  - `experimental_max_worker_delay_secs`,

In addition, either `save_checkpoints_steps` or `save_checkpoints_secs`
can be set (should not be both).

#### Args:


* <b>`**kwargs`</b>: keyword named properties with new values.


#### Raises:


* <b>`ValueError`</b>: If any property name in `kwargs` does not exist or is not
  allowed to be replaced, or both `save_checkpoints_steps` and
  `save_checkpoints_secs` are set.


#### Returns:

a new instance of `RunConfig`.


<h3 id="uid"><code>uid</code></h3>

``` python
uid(
    *args,
    **kwargs
)
```

Generates a 'Unique Identifier' based on all internal fields. (experimental)

Warning: THIS FUNCTION IS EXPERIMENTAL. It may change or be removed at any time, and without warning.

Caller should use the uid string to check `RunConfig` instance integrity
in one session use, but should not rely on the implementation details, which
is subject to change.

#### Args:


* <b>`whitelist`</b>: A list of the string names of the properties uid should not
  include. If `None`, defaults to `_DEFAULT_UID_WHITE_LIST`, which
  includes most properties user allowes to change.


#### Returns:

A uid string.




