

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.test.create_local_cluster

### `tf.test.create_local_cluster`

``` python
create_local_cluster(
    num_workers,
    num_ps,
    protocol='grpc'
)
```



Defined in [`tensorflow/python/framework/test_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/framework/test_util.py).

Create and start local servers and return the associated `Server` objects.

Example:

```python
workers, _ = tf.test.create_local_cluster(num_workers=2, num_ps=2)

worker_sessions = [tf.Session(w.target) for w in workers]

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
* <b>`protocol`</b>: Communication protocol.  Allowed values are documented in
    the documentation of `tf.train.Server`.


#### Returns:

  A tuple `(worker_servers, ps_servers)`.  `worker_servers` is a list
  of `num_workers` objects of type `tf.train.Server` (all running locally);
  and `ps_servers` is a list of `num_ps` objects of similar type.


#### Raises:

* <b>`ImportError`</b>: if portpicker module was not found at load time