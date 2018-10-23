

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.add_queue_runner

### Aliases:

* `tf.train.add_queue_runner`
* `tf.train.queue_runner.add_queue_runner`

``` python
tf.train.add_queue_runner(
    qr,
    collection=tf.GraphKeys.QUEUE_RUNNERS
)
```



Defined in [`tensorflow/python/training/queue_runner_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/training/queue_runner_impl.py).

See the guides: [Reading data > `QueueRunner`](../../../../api_guides/python/reading_data#_QueueRunner_), [Training > Coordinator and QueueRunner](../../../../api_guides/python/train#Coordinator_and_QueueRunner)

Adds a `QueueRunner` to a collection in the graph.

When building a complex model that uses many queues it is often difficult to
gather all the queue runners that need to be run.  This convenience function
allows you to add a queue runner to a well known collection in the graph.

The companion method `start_queue_runners()` can be used to start threads for
all the collected queue runners.

#### Args:

* <b>`qr`</b>: A `QueueRunner`.
* <b>`collection`</b>: A `GraphKey` specifying the graph collection to add
    the queue runner to.  Defaults to `GraphKeys.QUEUE_RUNNERS`.