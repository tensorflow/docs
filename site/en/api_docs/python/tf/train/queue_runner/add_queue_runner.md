page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.queue_runner.add_queue_runner

Adds a `QueueRunner` to a collection in the graph. (deprecated)

### Aliases:

* `tf.compat.v1.train.add_queue_runner`
* `tf.compat.v1.train.queue_runner.add_queue_runner`
* `tf.train.add_queue_runner`
* `tf.train.queue_runner.add_queue_runner`

``` python
tf.train.queue_runner.add_queue_runner(
    qr,
    collection=tf.GraphKeys.QUEUE_RUNNERS
)
```



Defined in [`python/training/queue_runner_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/queue_runner_impl.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
To construct input pipelines, use the <a href="../../../tf/data"><code>tf.data</code></a> module.

When building a complex model that uses many queues it is often difficult to
gather all the queue runners that need to be run.  This convenience function
allows you to add a queue runner to a well known collection in the graph.

The companion method `start_queue_runners()` can be used to start threads for
all the collected queue runners.

#### Args:


* <b>`qr`</b>: A `QueueRunner`.
* <b>`collection`</b>: A `GraphKey` specifying the graph collection to add
  the queue runner to.  Defaults to <a href="../../../tf/GraphKeys#QUEUE_RUNNERS"><code>GraphKeys.QUEUE_RUNNERS</code></a>.