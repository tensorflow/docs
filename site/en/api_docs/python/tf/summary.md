description: Operations for writing summary data, for use in analysis and visualization.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.summary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorboard/tree/master/tensorboard/summary/_tf/summary/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Operations for writing summary data, for use in analysis and visualization.


The <a href="../tf/summary.md"><code>tf.summary</code></a> module provides APIs for writing summary data. This data can be
visualized in TensorBoard, the visualization toolkit that comes with TensorFlow.
See the [TensorBoard website](https://www.tensorflow.org/tensorboard) for more
detailed tutorials about how to use these APIs, or some quick examples below.

Example usage with eager execution, the default in TF 2.0:

```python
writer = tf.summary.create_file_writer("/tmp/mylogs")
with writer.as_default():
  for step in range(100):
    # other model code would go here
    tf.summary.scalar("my_metric", 0.5, step=step)
    writer.flush()
```

Example usage with <a href="../tf/function.md"><code>tf.function</code></a> graph execution:

```python
writer = tf.summary.create_file_writer("/tmp/mylogs")

@tf.function
def my_func(step):
  # other model code would go here
  with writer.as_default():
    tf.summary.scalar("my_metric", 0.5, step=step)

for step in range(100):
  my_func(step)
  writer.flush()
```

Example usage with legacy TF 1.x graph execution:

```python
with tf.compat.v1.Graph().as_default():
  step = tf.Variable(0, dtype=tf.int64)
  step_update = step.assign_add(1)
  writer = tf.summary.create_file_writer("/tmp/mylogs")
  with writer.as_default():
    tf.summary.scalar("my_metric", 0.5, step=step)
  all_summary_ops = tf.compat.v1.summary.all_v2_summary_ops()
  writer_flush = writer.flush()

  sess = tf.compat.v1.Session()
  sess.run([writer.init(), step.initializer])
  for i in range(100):
    sess.run(all_summary_ops)
    sess.run(step_update)
    sess.run(writer_flush)
```

## Modules

[`experimental`](../tf/summary/experimental.md) module: Public API for tf.summary.experimental namespace.

## Classes

[`class SummaryWriter`](../tf/summary/SummaryWriter.md): Interface representing a stateful summary writer object.

## Functions

[`audio(...)`](../tf/summary/audio.md): Write an audio summary.

[`create_file_writer(...)`](../tf/summary/create_file_writer.md): Creates a summary file writer for the given log directory.

[`create_noop_writer(...)`](../tf/summary/create_noop_writer.md): Returns a summary writer that does nothing.

[`flush(...)`](../tf/summary/flush.md): Forces summary writer to send any buffered data to storage.

[`histogram(...)`](../tf/summary/histogram.md): Write a histogram summary.

[`image(...)`](../tf/summary/image.md): Write an image summary.

[`record_if(...)`](../tf/summary/record_if.md): Sets summary recording on or off per the provided boolean value.

[`scalar(...)`](../tf/summary/scalar.md): Write a scalar summary.

[`text(...)`](../tf/summary/text.md): Write a text summary.

[`trace_export(...)`](../tf/summary/trace_export.md): Stops and exports the active trace as a Summary and/or profile file.

[`trace_off(...)`](../tf/summary/trace_off.md): Stops the current trace and discards any collected information.

[`trace_on(...)`](../tf/summary/trace_on.md): Starts a trace to record computation graphs and profiling information.

[`write(...)`](../tf/summary/write.md): Writes a generic summary to the default SummaryWriter if one exists.

