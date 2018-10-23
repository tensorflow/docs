

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.train.queue_runner



Defined in [`tensorflow/python/training/queue_runner.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/training/queue_runner.py).

Create threads to run multiple enqueue ops.

## Classes

[`class QueueRunner`](../../tf/train/QueueRunner): Holds a list of enqueue operations for a queue, each to be run in a thread.

## Functions

[`add_queue_runner(...)`](../../tf/train/add_queue_runner): Adds a `QueueRunner` to a collection in the graph.

[`start_queue_runners(...)`](../../tf/train/start_queue_runners): Starts all queue runners collected in the graph.

