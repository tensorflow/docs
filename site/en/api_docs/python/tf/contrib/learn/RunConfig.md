


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.RunConfig

### `class tf.contrib.learn.RunConfig`

See the guide: [Learn (contrib) > Graph actions](../../../../../api_guides/python/contrib.learn#Graph_actions)

This class specifies the configurations for an `Estimator` run.

If you're a Google-internal user using command line flags with
`learn_runner.py` (for instance, to do distributed training or to use
parameter servers), you probably want to use `learn_runner.EstimatorConfig`
instead.

## Properties

<h3 id="cluster_spec"><code>cluster_spec</code></h3>



<h3 id="environment"><code>environment</code></h3>



<h3 id="evaluation_master"><code>evaluation_master</code></h3>



<h3 id="is_chief"><code>is_chief</code></h3>



<h3 id="keep_checkpoint_every_n_hours"><code>keep_checkpoint_every_n_hours</code></h3>



<h3 id="keep_checkpoint_max"><code>keep_checkpoint_max</code></h3>



<h3 id="master"><code>master</code></h3>



<h3 id="num_ps_replicas"><code>num_ps_replicas</code></h3>



<h3 id="save_checkpoints_secs"><code>save_checkpoints_secs</code></h3>



<h3 id="save_checkpoints_steps"><code>save_checkpoints_steps</code></h3>



<h3 id="save_summary_steps"><code>save_summary_steps</code></h3>



<h3 id="task_id"><code>task_id</code></h3>



<h3 id="task_type"><code>task_type</code></h3>



<h3 id="tf_config"><code>tf_config</code></h3>



<h3 id="tf_random_seed"><code>tf_random_seed</code></h3>





## Methods

<h3 id="__init__"><code>__init__(master=None, num_cores=0, log_device_placement=False, gpu_memory_fraction=1, tf_random_seed=None, save_summary_steps=100, save_checkpoints_secs=600, save_checkpoints_steps=None, keep_checkpoint_max=5, keep_checkpoint_every_n_hours=10000, evaluation_master='')</code></h3>

Constructor.

Note that the superclass `ClusterConfig` may set properties like
`cluster_spec`, `is_chief`, `master` (if `None` in the args),
`num_ps_replicas`, `task_id`, and `task_type` based on the `TF_CONFIG`
environment variable. See `ClusterConfig` for more details.

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
* <b>`evaluation_master`</b>: the master on which to perform evaluation.

<h3 id="get_task_id"><code>get_task_id()</code></h3>

Returns task index from `TF_CONFIG` environmental variable.

If you have a ClusterConfig instance, you can just access its task_id
property instead of calling this function and re-parsing the environmental
variable.

#### Returns:

  `TF_CONFIG['task']['index']`. Defaults to 0.





Defined in [`tensorflow/contrib/learn/python/learn/estimators/run_config.py`](https://www.tensorflow.org/code/tensorflow/contrib/learn/python/learn/estimators/run_config.py).

