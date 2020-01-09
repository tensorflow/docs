page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.summary


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorboard/tree/master/tensorboard/summary/_tf/summary/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Operations for writing summary data, for use in analysis and visualization.

<!-- Placeholder for "Used in" -->

The <a href="../../../tf/summary"><code>tf.summary</code></a> module provides APIs for writing summary data. This data can be
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

Example usage with <a href="../../../tf/function"><code>tf.function</code></a> graph execution:

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

[`experimental`](../../../tf/compat/v2/summary/experimental) module: Public API for tf.summary.experimental namespace.

## Classes

[`class SummaryWriter`](../../../tf/compat/v2/summary/SummaryWriter): Interface representing a stateful summary writer object.

## Functions

[`audio(...)`](../../../tf/compat/v2/summary/audio): Write an audio summary.

[`create_file_writer(...)`](../../../tf/compat/v2/summary/create_file_writer): Creates a summary file writer for the given log directory.

[`create_noop_writer(...)`](../../../tf/compat/v2/summary/create_noop_writer): Returns a summary writer that does nothing.

[`flush(...)`](../../../tf/compat/v2/summary/flush): Forces summary writer to send any buffered data to storage.

[`histogram(...)`](../../../tf/compat/v2/summary/histogram): Write a histogram summary.

[`image(...)`](../../../tf/compat/v2/summary/image): Write an image summary.

[`record_if(...)`](../../../tf/compat/v2/summary/record_if): Sets summary recording on or off per the provided boolean value.

[`scalar(...)`](../../../tf/compat/v2/summary/scalar): Write a scalar summary.

[`text(...)`](../../../tf/compat/v2/summary/text): Write a text summary.

[`trace_export(...)`](../../../tf/compat/v2/summary/trace_export): Stops and exports the active trace as a Summary and/or profile file.

[`trace_off(...)`](../../../tf/compat/v2/summary/trace_off): Stops the current trace and discards any collected information.

[`trace_on(...)`](../../../tf/compat/v2/summary/trace_on): Starts a trace to record computation graphs and profiling information.

[`write(...)`](../../../tf/compat/v2/summary/write): Writes a generic summary to the default SummaryWriter if one exists.
