description: Deletes old checkpoints.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.CheckpointManager" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="restore_or_initialize"/>
<meta itemprop="property" content="save"/>
</div>

# tf.train.CheckpointManager

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/checkpoint_management.py#L513-L852">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Deletes old checkpoints.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.CheckpointManager`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.train.CheckpointManager(
    checkpoint, directory, max_to_keep, keep_checkpoint_every_n_hours=None,
    checkpoint_name='ckpt', step_counter=None, checkpoint_interval=None,
    init_fn=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example usage:



```python
import tensorflow as tf
checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
manager = tf.train.CheckpointManager(
    checkpoint, directory="/tmp/model", max_to_keep=5)
status = checkpoint.restore(manager.latest_checkpoint)
while True:
  # train
  manager.save()
```

`CheckpointManager` preserves its own state across instantiations (see the
`__init__` documentation for details). Only one should be active in a
particular directory at a time.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`checkpoint`
</td>
<td>
The <a href="../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> instance to save and manage
checkpoints for.
</td>
</tr><tr>
<td>
`directory`
</td>
<td>
The path to a directory in which to write checkpoints. A
special file named "checkpoint" is also written to this directory (in a
human-readable text format) which contains the state of the
`CheckpointManager`.
</td>
</tr><tr>
<td>
`max_to_keep`
</td>
<td>
An integer, the number of checkpoints to keep. Unless
preserved by `keep_checkpoint_every_n_hours`, checkpoints will be
deleted from the active set, oldest first, until only `max_to_keep`
checkpoints remain. If `None`, no checkpoints are deleted and everything
stays in the active set. Note that `max_to_keep=None` will keep all
checkpoint paths in memory and in the checkpoint state protocol buffer
on disk.
</td>
</tr><tr>
<td>
`keep_checkpoint_every_n_hours`
</td>
<td>
Upon removal from the active set, a
checkpoint will be preserved if it has been at least
`keep_checkpoint_every_n_hours` since the last preserved checkpoint. The
default setting of `None` does not preserve any checkpoints in this way.
</td>
</tr><tr>
<td>
`checkpoint_name`
</td>
<td>
Custom name for the checkpoint file.
</td>
</tr><tr>
<td>
`step_counter`
</td>
<td>
A <a href="../../tf/Variable.md"><code>tf.Variable</code></a> instance for checking the current step
counter value, in case users want to save checkpoints every N steps.
</td>
</tr><tr>
<td>
`checkpoint_interval`
</td>
<td>
An integer, indicates the minimum step interval
between two checkpoints.
</td>
</tr><tr>
<td>
`init_fn`
</td>
<td>
Callable. A function to do customized intialization if no
checkpoints are in the directory.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `max_to_keep` is not a positive integer.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`checkpoint`
</td>
<td>
Returns the <a href="../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> object.
</td>
</tr><tr>
<td>
`checkpoint_interval`
</td>
<td>

</td>
</tr><tr>
<td>
`checkpoints`
</td>
<td>
A list of managed checkpoints.

Note that checkpoints saved due to `keep_checkpoint_every_n_hours` will not
show up in this list (to avoid ever-growing filename lists).
</td>
</tr><tr>
<td>
`directory`
</td>
<td>

</td>
</tr><tr>
<td>
`latest_checkpoint`
</td>
<td>
The prefix of the most recent checkpoint in `directory`.

Equivalent to <a href="../../tf/train/latest_checkpoint.md"><code>tf.train.latest_checkpoint(directory)</code></a> where `directory` is
the constructor argument to `CheckpointManager`.

Suitable for passing to <a href="../../tf/train/Checkpoint.md#restore"><code>tf.train.Checkpoint.restore</code></a> to resume training.
</td>
</tr>
</table>



## Methods

<h3 id="restore_or_initialize"><code>restore_or_initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/checkpoint_management.py#L826-L852">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>restore_or_initialize()
</code></pre>

Restore items in `checkpoint` from the latest checkpoint file.

This method will first try to restore from the most recent checkpoint in
`directory`. If no checkpoints exist in `directory`, and `init_fn` is
specified, this method will call `init_fn` to do customized
initialization. This can be used to support initialization from pretrained
models.

Note that unlike <a href="../../tf/train/Checkpoint.md#restore"><code>tf.train.Checkpoint.restore()</code></a>, this method doesn't return
a load status object that users can run assertions on
(e.g. assert_consumed()). Thus to run assertions, users should directly use
<a href="../../tf/train/Checkpoint.md#restore"><code>tf.train.Checkpoint.restore()</code></a> method.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The restored checkpoint path if the lastest checkpoint is found and
restored. Otherwise None.
</td>
</tr>

</table>



<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/checkpoint_management.py#L750-L824">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save(
    checkpoint_number=None, check_interval=(True)
)
</code></pre>

Creates a new checkpoint and manages it.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`checkpoint_number`
</td>
<td>
An optional integer, or an integer-dtype `Variable` or
`Tensor`, used to number the checkpoint. If `None` (default),
checkpoints are numbered using `checkpoint.save_counter`. Even if
`checkpoint_number` is provided, `save_counter` is still incremented. A
user-provided `checkpoint_number` is not incremented even if it is a
`Variable`.
</td>
</tr><tr>
<td>
`check_interval`
</td>
<td>
An optional boolean. The argument is only effective when
`checkpoint_interval` is passed into the manager. If `True`, the manager
will only save the checkpoint if the interval between checkpoints is
larger than `checkpoint_interval`. Otherwise it will always save the
checkpoint unless a checkpoint has already been saved for the current
step.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The path to the new checkpoint. It is also recorded in the `checkpoints`
and `latest_checkpoint` properties. `None` if no checkpoint is saved.
</td>
</tr>

</table>





