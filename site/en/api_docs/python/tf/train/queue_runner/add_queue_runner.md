page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.queue_runner.add_queue_runner


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/queue_runner_impl.py#L394-L411">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds a `QueueRunner` to a collection in the graph. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/train/queue_runner/add_queue_runner"><code>tf.compat.v1.train.add_queue_runner</code></a>
* <a href="/api_docs/python/tf/train/queue_runner/add_queue_runner"><code>tf.compat.v1.train.queue_runner.add_queue_runner</code></a>
* <a href="/api_docs/python/tf/train/queue_runner/add_queue_runner"><code>tf.train.add_queue_runner</code></a>


``` python
tf.train.queue_runner.add_queue_runner(
    qr,
    collection=tf.GraphKeys.QUEUE_RUNNERS
)
```



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
