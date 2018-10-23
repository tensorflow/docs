

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.summary



Defined in [`tensorflow/contrib/summary/summary.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/summary/summary.py).

TensorFlow Summary API v2.

The operations in this package are safe to use with eager execution turned on or
off. It has a more flexible API that allows summaries to be written directly
from ops to places other than event log files, rather than propagating protos
from <a href="../../tf/summary/merge_all"><code>tf.summary.merge_all</code></a> to <a href="../../tf/summary/FileWriter"><code>tf.summary.FileWriter</code></a>.

To use with eager execution enabled, write your code as follows:

```python
global_step = tf.train.get_or_create_global_step()
summary_writer = tf.contrib.summary.create_file_writer(
    train_dir, flush_millis=10000)
with summary_writer.as_default(), tf.contrib.summary.always_record_summaries():
  # model code goes here
  # and in it call
  tf.contrib.summary.scalar("loss", my_loss)
  # In this case every call to tf.contrib.summary.scalar will generate a record
  # ...
```

To use it with graph execution, write your code as follows:

```python
global_step = tf.train.get_or_create_global_step()
summary_writer = tf.contrib.summary.create_file_writer(
    train_dir, flush_millis=10000)
with summary_writer.as_default(), tf.contrib.summary.always_record_summaries():
  # model definition code goes here
  # and in it call
  tf.contrib.summary.scalar("loss", my_loss)
  # In this case every call to tf.contrib.summary.scalar will generate an op,
  # note the need to run tf.contrib.summary.all_summary_ops() to make sure these
  # ops get executed.
  # ...
  train_op = ....

with tf.Session(...) as sess:
  tf.global_variables_initializer().run()
  tf.contrib.summary.initialize(graph=tf.get_default_graph())
  # ...
  while not_done_training:
    sess.run([train_op, tf.contrib.summary.all_summary_ops()])
    # ...
```

## Classes

[`class SummaryWriter`](../../tf/contrib/summary/SummaryWriter): Encapsulates a stateful summary writer resource.

## Functions

[`all_summary_ops(...)`](../../tf/contrib/summary/all_summary_ops): Graph-mode only. Returns all summary ops.

[`always_record_summaries(...)`](../../tf/contrib/summary/always_record_summaries): Sets the should_record_summaries Tensor to always true.

[`audio(...)`](../../tf/contrib/summary/audio): Writes an audio summary if possible.

[`create_db_writer(...)`](../../tf/contrib/summary/create_db_writer): Creates a summary database writer in the current context.

[`create_file_writer(...)`](../../tf/contrib/summary/create_file_writer): Creates a summary file writer in the current context under the given name.

[`create_summary_file_writer(...)`](../../tf/contrib/summary/create_summary_file_writer): Please use <a href="../../tf/contrib/summary/create_file_writer"><code>tf.contrib.summary.create_file_writer</code></a>.

[`eval_dir(...)`](../../tf/contrib/summary/eval_dir): Construct a logdir for an eval summary writer.

[`flush(...)`](../../tf/contrib/summary/flush): Forces summary writer to send any buffered data to storage.

[`generic(...)`](../../tf/contrib/summary/generic): Writes a tensor summary if possible.

[`graph(...)`](../../tf/contrib/summary/graph): Writes a TensorFlow graph to the summary interface.

[`histogram(...)`](../../tf/contrib/summary/histogram): Writes a histogram summary if possible.

[`image(...)`](../../tf/contrib/summary/image): Writes an image summary if possible.

[`import_event(...)`](../../tf/contrib/summary/import_event): Writes a <a href="../../tf/Event"><code>tf.Event</code></a> binary proto.

[`initialize(...)`](../../tf/contrib/summary/initialize): Initializes summary writing for graph execution mode.

[`never_record_summaries(...)`](../../tf/contrib/summary/never_record_summaries): Sets the should_record_summaries Tensor to always false.

[`record_summaries_every_n_global_steps(...)`](../../tf/contrib/summary/record_summaries_every_n_global_steps): Sets the should_record_summaries Tensor to true if global_step % n == 0.

[`scalar(...)`](../../tf/contrib/summary/scalar): Writes a scalar summary if possible.

[`should_record_summaries(...)`](../../tf/contrib/summary/should_record_summaries): Returns boolean Tensor which is true if summaries should be recorded.

[`summary_writer_initializer_op(...)`](../../tf/contrib/summary/summary_writer_initializer_op): Graph-mode only. Returns the list of ops to create all summary writers.

## Other Members

`absolute_import`

`division`

`print_function`

