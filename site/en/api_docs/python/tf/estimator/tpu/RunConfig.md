page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.tpu.RunConfig

## Class `RunConfig`

RunConfig with TPU support.

Inherits From: [`RunConfig`](../../../tf/estimator/RunConfig)

### Aliases:

* Class `tf.compat.v1.estimator.tpu.RunConfig`
* Class `tf.contrib.tpu.RunConfig`
* Class `tf.estimator.tpu.RunConfig`



Defined in [`python/estimator/tpu/tpu_config.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_config.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    tpu_config=None,
    evaluation_master=None,
    master=None,
    cluster=None,
    **kwargs
)
```

Constructs a RunConfig.


#### Args:


* <b>`tpu_config`</b>: the TPUConfig that specifies TPU-specific configuration.
* <b>`evaluation_master`</b>: a string. The address of the master to use for eval.
  Defaults to master if not set.
* <b>`master`</b>: a string. The address of the master to use for training.
* <b>`cluster`</b>: a ClusterResolver
* <b>`**kwargs`</b>: keyword config parameters.


#### Raises:


* <b>`ValueError`</b>: if cluster is not None and the provided session_config has a
  cluster_def already.



## Properties

<h3 id="cluster"><code>cluster</code></h3>




<h3 id="cluster_spec"><code>cluster_spec</code></h3>




<h3 id="device_fn"><code>device_fn</code></h3>

Returns the device_fn.

If device_fn is not `None`, it overrides the default
device function used in `Estimator`.
Otherwise the default one is used.

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




<h3 id="tf_random_seed"><code>tf_random_seed</code></h3>




<h3 id="tpu_config"><code>tpu_config</code></h3>




<h3 id="train_distribute"><code>train_distribute</code></h3>

Optional <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> for training.
    



## Methods

<h3 id="replace"><code>replace</code></h3>

``` python
replace(**kwargs)
```






