page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.ElasticAverageCustomGetter

## Class `ElasticAverageCustomGetter`

Custom_getter class is used to do:





Defined in [`contrib/opt/python/training/elastic_average_optimizer.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/opt/python/training/elastic_average_optimizer.py).

<!-- Placeholder for "Used in" -->

1. Change trainable variables to local collection and place them at worker
  device
2. Generate global variables(global center variables)
3. Generate local variables(local center variables) which record the global
  variables and place them at worker device
  Notice that the class should be used with tf.replica_device_setter,
  so that the global center variables and global step variable can be placed
  at ps device. Besides, use 'tf.compat.v1.get_variable' instead of
  'tf.Variable' to
  use this custom getter.

For example,
ea_custom_getter = ElasticAverageCustomGetter(worker_device)
with tf.device(
  tf.compat.v1.train.replica_device_setter(
    worker_device=worker_device,
    ps_device="/job:ps",
    cluster=cluster)),
  tf.compat.v1.variable_scope('',custom_getter=ea_custom_getter):
  ...
  create your model here
  ...
  with tf.device(worker_device):
    opt = tf.compat.v1.train.MomentumOptimizer(...)
    optimizer = ElasticAverageOptimizer(
          opt,
          num_worker=2,
          moving_rate=0.01, # or use default value
          communication_period=20,
          ea_custom_getter=ea_custom_getter)
    ...
    train_op = optimizer.apply_gradients(
      grads_vars,
      global_step=global_step)
  ...
  hooks = [optimizer.make_session_run_hook(is_chief, task_index)]
  ...
  with tf.compat.v1.train.MonitoredTrainingSession(master=server.target,
                                         is_chief=is_chief,
                                         checkpoint_dir=("...),
                                         save_checkpoint_secs=600,
                                         hooks=hooks) as mon_sess:

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(worker_device)
```

Create a new `ElasticAverageCustomGetter`.


#### Args:


* <b>`worker_device`</b>: String.  Name of the `worker` job.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    getter,
    name,
    trainable,
    collections,
    *args,
    **kwargs
)
```






