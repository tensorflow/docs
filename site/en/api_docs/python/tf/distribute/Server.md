page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.Server

## Class `Server`

An in-process TensorFlow server, for use in distributed training.



### Aliases:

* Class `tf.compat.v1.distribute.Server`
* Class `tf.compat.v1.train.Server`
* Class `tf.compat.v2.distribute.Server`
* Class `tf.distribute.Server`
* Class `tf.train.Server`



Defined in [`python/training/server_lib.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/server_lib.py).

<!-- Placeholder for "Used in" -->

A <a href="../../tf/distribute/Server"><code>tf.distribute.Server</code></a> instance encapsulates a set of devices and a
<a href="../../tf/Session"><code>tf.compat.v1.Session</code></a> target that
can participate in distributed training. A server belongs to a
cluster (specified by a <a href="../../tf/train/ClusterSpec"><code>tf.train.ClusterSpec</code></a>), and
corresponds to a particular task in a named job. The server can
communicate with any other server in the same cluster.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    server_or_cluster_def,
    job_name=None,
    task_index=None,
    protocol=None,
    config=None,
    start=True
)
```

Creates a new server with the given definition.

The `job_name`, `task_index`, and `protocol` arguments are optional, and
override any information provided in `server_or_cluster_def`.

#### Args:


* <b>`server_or_cluster_def`</b>: A <a href="../../tf/train/ServerDef"><code>tf.train.ServerDef</code></a> or <a href="../../tf/train/ClusterDef"><code>tf.train.ClusterDef</code></a>
  protocol buffer, or a <a href="../../tf/train/ClusterSpec"><code>tf.train.ClusterSpec</code></a> object, describing the
  server to be created and/or the cluster of which it is a member.
* <b>`job_name`</b>: (Optional.) Specifies the name of the job of which the server is
  a member. Defaults to the value in `server_or_cluster_def`, if
  specified.
* <b>`task_index`</b>: (Optional.) Specifies the task index of the server in its job.
  Defaults to the value in `server_or_cluster_def`, if specified.
  Otherwise defaults to 0 if the server's job has only one task.
* <b>`protocol`</b>: (Optional.) Specifies the protocol to be used by the server.
  Acceptable values include `"grpc", "grpc+verbs"`. Defaults to the value
  in `server_or_cluster_def`, if specified. Otherwise defaults to
  `"grpc"`.
* <b>`config`</b>: (Options.) A <a href="../../tf/ConfigProto"><code>tf.compat.v1.ConfigProto</code></a> that specifies default
  configuration options for all sessions that run on this server.
* <b>`start`</b>: (Optional.) Boolean, indicating whether to start the server after
  creating it. Defaults to `True`.


#### Raises:


* <b>`tf.errors.OpError`</b>: Or one of its subclasses if an error occurs while
  creating the TensorFlow server.



## Properties

<h3 id="server_def"><code>server_def</code></h3>

Returns the <a href="../../tf/train/ServerDef"><code>tf.train.ServerDef</code></a> for this server.


#### Returns:

A <a href="../../tf/train/ServerDef"><code>tf.train.ServerDef</code></a> protocol buffer that describes the configuration
of this server.


<h3 id="target"><code>target</code></h3>

Returns the target for a <a href="../../tf/Session"><code>tf.compat.v1.Session</code></a> to connect to this server.

To create a
<a href="../../tf/Session"><code>tf.compat.v1.Session</code></a> that
connects to this server, use the following snippet:

```python
server = tf.distribute.Server(...)
with tf.compat.v1.Session(server.target):
  # ...
```

#### Returns:

A string containing a session target for this server.




## Methods

<h3 id="create_local_server"><code>create_local_server</code></h3>

``` python
@staticmethod
create_local_server(
    config=None,
    start=True
)
```

Creates a new single-process cluster running on the local host.

This method is a convenience wrapper for creating a
<a href="../../tf/distribute/Server"><code>tf.distribute.Server</code></a> with a <a href="../../tf/train/ServerDef"><code>tf.train.ServerDef</code></a> that specifies a
single-process cluster containing a single task in a job called
`"local"`.

#### Args:


* <b>`config`</b>: (Options.) A <a href="../../tf/ConfigProto"><code>tf.compat.v1.ConfigProto</code></a> that specifies default
  configuration options for all sessions that run on this server.
* <b>`start`</b>: (Optional.) Boolean, indicating whether to start the server after
  creating it. Defaults to `True`.


#### Returns:

A local <a href="../../tf/distribute/Server"><code>tf.distribute.Server</code></a>.


<h3 id="join"><code>join</code></h3>

``` python
join()
```

Blocks until the server has shut down.

This method currently blocks forever.

#### Raises:


* <b>`tf.errors.OpError`</b>: Or one of its subclasses if an error occurs while
  joining the TensorFlow server.

<h3 id="start"><code>start</code></h3>

``` python
start()
```

Starts this server.


#### Raises:


* <b>`tf.errors.OpError`</b>: Or one of its subclasses if an error occurs while
  starting the TensorFlow server.



