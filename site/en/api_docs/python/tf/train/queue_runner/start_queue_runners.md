page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.queue_runner.start_queue_runners


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/queue_runner_impl.py#L414-L480">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Starts all queue runners collected in the graph. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/train/queue_runner/start_queue_runners"><code>tf.compat.v1.train.queue_runner.start_queue_runners</code></a>
* <a href="/api_docs/python/tf/train/queue_runner/start_queue_runners"><code>tf.compat.v1.train.start_queue_runners</code></a>
* <a href="/api_docs/python/tf/train/queue_runner/start_queue_runners"><code>tf.train.start_queue_runners</code></a>


``` python
tf.train.queue_runner.start_queue_runners(
    sess=None,
    coord=None,
    daemon=True,
    start=True,
    collection=tf.GraphKeys.QUEUE_RUNNERS
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
To construct input pipelines, use the <a href="../../../tf/data"><code>tf.data</code></a> module.

This is a companion method to `add_queue_runner()`.  It just starts
threads for all queue runners collected in the graph.  It returns
the list of all threads.

#### Args:


* <b>`sess`</b>: `Session` used to run the queue ops.  Defaults to the
  default session.
* <b>`coord`</b>: Optional `Coordinator` for coordinating the started threads.
* <b>`daemon`</b>: Whether the threads should be marked as `daemons`, meaning
  they don't block program exit.
* <b>`start`</b>: Set to `False` to only create the threads, not start them.
* <b>`collection`</b>: A `GraphKey` specifying the graph collection to
  get the queue runners from.  Defaults to <a href="../../../tf/GraphKeys#QUEUE_RUNNERS"><code>GraphKeys.QUEUE_RUNNERS</code></a>.


#### Raises:


* <b>`ValueError`</b>: if `sess` is None and there isn't any default session.
* <b>`TypeError`</b>: if `sess` is not a <a href="../../../tf/Session"><code>tf.compat.v1.Session</code></a> object.


#### Returns:

A list of threads.



#### Raises:


* <b>`RuntimeError`</b>: If called with eager execution enabled.
* <b>`ValueError`</b>: If called without a default <a href="../../../tf/Session"><code>tf.compat.v1.Session</code></a> registered.



#### Eager Compatibility
Not compatible with eager execution. To ingest data under eager execution,
use the <a href="../../../tf/data"><code>tf.data</code></a> API instead.
