description: Interface for listeners that take action before or after checkpoint save.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.CheckpointSaverListener" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="after_save"/>
<meta itemprop="property" content="before_save"/>
<meta itemprop="property" content="begin"/>
<meta itemprop="property" content="end"/>
</div>

# tf.estimator.CheckpointSaverListener

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/basic_session_run_hooks.py#L446-L509">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Interface for listeners that take action before or after checkpoint save.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.CheckpointSaverListener`, `tf.compat.v1.train.CheckpointSaverListener`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

`CheckpointSaverListener` triggers only in steps when `CheckpointSaverHook` is
triggered, and provides callbacks at the following points:
 - before using the session
 - before each call to `Saver.save()`
 - after each call to `Saver.save()`
 - at the end of session

To use a listener, implement a class and pass the listener to a
`CheckpointSaverHook`, as in this example:

```python
class ExampleCheckpointSaverListener(CheckpointSaverListener):
  def begin(self):
    # You can add ops to the graph here.
    print('Starting the session.')
    self.your_tensor = ...

  def before_save(self, session, global_step_value):
    print('About to write a checkpoint')

  def after_save(self, session, global_step_value):
    print('Done writing checkpoint.')
    if decided_to_stop_training():
      return True

  def end(self, session, global_step_value):
    print('Done with the session.')

...
listener = ExampleCheckpointSaverListener()
saver_hook = tf.estimator.CheckpointSaverHook(
    checkpoint_dir, listeners=[listener])
with
tf.compat.v1.train.MonitoredTrainingSession(chief_only_hooks=[saver_hook]):
  ...
```

A `CheckpointSaverListener` may simply take some action after every
checkpoint save. It is also possible for the listener to use its own schedule
to act less frequently, e.g. based on global_step_value. In this case,
implementors should implement the `end()` method to handle actions related to
the last checkpoint save. But the listener should not act twice if
`after_save()` already handled this last checkpoint save.

A `CheckpointSaverListener` can request training to be stopped, by returning
True in `after_save`. Please note that, in replicated distributed training
setting, only `chief` should use this behavior. Otherwise each worker will do
their own evaluation, which may be wasteful of resources.

## Methods

<h3 id="after_save"><code>after_save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/basic_session_run_hooks.py#L505-L506">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>after_save(
    session, global_step_value
)
</code></pre>




<h3 id="before_save"><code>before_save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/basic_session_run_hooks.py#L502-L503">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>before_save(
    session, global_step_value
)
</code></pre>




<h3 id="begin"><code>begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/basic_session_run_hooks.py#L499-L500">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>begin()
</code></pre>




<h3 id="end"><code>end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/basic_session_run_hooks.py#L508-L509">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end(
    session, global_step_value
)
</code></pre>






