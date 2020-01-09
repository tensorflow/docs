page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.create_local_cluster


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/test/create_local_cluster">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/test_util.py#L2947-L3034">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create and start local servers and return the associated `Server` objects.

### Aliases:

* <a href="/api_docs/python/tf/test/create_local_cluster"><code>tf.compat.v1.test.create_local_cluster</code></a>
* <a href="/api_docs/python/tf/test/create_local_cluster"><code>tf.compat.v2.test.create_local_cluster</code></a>


``` python
tf.test.create_local_cluster(
    num_workers,
    num_ps,
    protocol='grpc',
    worker_config=None,
    ps_config=None
)
```



<!-- Placeholder for "Used in" -->

"PS" stands for "parameter server": a task responsible for storing and
updating the model's parameters. Other tasks send updates to these parameters
as they work on optimizing the parameters. This particular division of labor
between tasks is not required, but is common for distributed training.

Read more at https://www.tensorflow.org/guide/extend/architecture

![components](https://www.tensorflow.org/images/diag1.svg "components")


Figure illustrates the interaction of these components.
"/job:worker/task:0" and "/job:ps/task:0" are both tasks with worker services.


#### Example:


```python
workers, _ = tf.test.create_local_cluster(num_workers=2, num_ps=2)

worker_sessions = [tf.compat.v1.Session(w.target) for w in workers]

with tf.device("/job:ps/task:0"):
  ...
with tf.device("/job:ps/task:1"):
  ...
with tf.device("/job:worker/task:0"):
  ...
with tf.device("/job:worker/task:1"):
  ...

worker_sessions[0].run(...)
```

#### Args:


* <b>`num_workers`</b>: Number of worker servers to start.
* <b>`num_ps`</b>: Number of PS servers to start.
* <b>`protocol`</b>: Communication protocol. Allowed values are documented in the
  documentation of <a href="../../tf/distribute/Server"><code>tf.distribute.Server</code></a>.
* <b>`worker_config`</b>: (optional) <a href="../../tf/ConfigProto"><code>tf.ConfigProto</code></a> to initialize workers. Can be
  used to instantiate multiple devices etc.
* <b>`ps_config`</b>: (optional) <a href="../../tf/ConfigProto"><code>tf.ConfigProto</code></a> to initialize PS servers.


#### Returns:

A tuple `(worker_servers, ps_servers)`.  `worker_servers` is a list
of `num_workers` objects of type <a href="../../tf/distribute/Server"><code>tf.distribute.Server</code></a> (all running
locally);
and `ps_servers` is a list of `num_ps` objects of similar type.



#### Raises:


* <b>`ImportError`</b>: if portpicker module was not found at load time
