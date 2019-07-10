page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.CheckpointManager

## Class `CheckpointManager`



### Aliases:

* Class `tf.contrib.checkpoint.CheckpointManager`
* Class `tf.train.CheckpointManager`



Defined in [`tensorflow/python/training/checkpoint_management.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/training/checkpoint_management.py).

Deletes old checkpoints.

Example usage:

```python
import tensorflow as tf
checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
manager = tf.contrib.checkpoint.CheckpointManager(
    checkpoint, directory="/tmp/model", max_to_keep=5)
status = checkpoint.restore(manager.latest_checkpoint)
while True:
  # train
  manager.save()
```

`CheckpointManager` preserves its own state across instantiations (see the
`__init__` documentation for details). Only one should be active in a
particular directory at a time.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    checkpoint,
    directory,
    max_to_keep,
    keep_checkpoint_every_n_hours=None
)
```

Configure a `CheckpointManager` for use in `directory`.

If a `CheckpointManager` was previously used in `directory`, its
state will be restored. This includes the list of managed checkpoints and
the timestamp bookkeeping necessary to support
`keep_checkpoint_every_n_hours`. The behavior of the new `CheckpointManager`
will be the same as the previous `CheckpointManager`, including cleaning up
existing checkpoints if appropriate.

Checkpoints are only considered for deletion just after a new checkpoint has
been added. At that point, `max_to_keep` checkpoints will remain in an
"active set". Once a checkpoint is preserved by
`keep_checkpoint_every_n_hours` it will not be deleted by this
`CheckpointManager` or any future `CheckpointManager` instantiated in
`directory` (regardless of the new setting of
`keep_checkpoint_every_n_hours`). The `max_to_keep` checkpoints in the
active set may be deleted by this `CheckpointManager` or a future
`CheckpointManager` instantiated in `directory` (subject to its
`max_to_keep` and `keep_checkpoint_every_n_hours` settings).

#### Args:

* <b>`checkpoint`</b>: The <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a> instance to save and manage
    checkpoints for.
* <b>`directory`</b>: The path to a directory in which to write checkpoints. A
    special file named "checkpoint" is also written to this directory (in a
    human-readable text format) which contains the state of the
    `CheckpointManager`.
* <b>`max_to_keep`</b>: An integer, the number of checkpoints to keep. Unless
    preserved by `keep_checkpoint_every_n_hours`, checkpoints will be
    deleted from the active set, oldest first, until only `max_to_keep`
    checkpoints remain. If `None`, no checkpoints are deleted and everything
    stays in the active set. Note that `max_to_keep=None` will keep all
    checkpoint paths in memory and in the checkpoint state protocol buffer
    on disk.
* <b>`keep_checkpoint_every_n_hours`</b>: Upon removal from the active set, a
    checkpoint will be preserved if it has been at least
    `keep_checkpoint_every_n_hours` since the last preserved checkpoint. The
    default setting of `None` does not preserve any checkpoints in this way.


#### Raises:

* <b>`ValueError`</b>: If `max_to_keep` is not a positive integer.



## Properties

<h3 id="checkpoints"><code>checkpoints</code></h3>

A list of managed checkpoints.

Note that checkpoints saved due to `keep_checkpoint_every_n_hours` will not
show up in this list (to avoid ever-growing filename lists).

#### Returns:

A list of filenames, sorted from oldest to newest.

<h3 id="latest_checkpoint"><code>latest_checkpoint</code></h3>

The prefix of the most recent checkpoint in `directory`.

Equivalent to `tf.train.latest_checkpoint(directory)` where `directory` is
the constructor argument to `CheckpointManager`.

Suitable for passing to <a href="../../tf/train/Checkpoint#restore"><code>tf.train.Checkpoint.restore</code></a> to resume training.

#### Returns:

The checkpoint prefix. If there are no checkpoints, returns `None`.



## Methods

<h3 id="save"><code>save</code></h3>

``` python
save(checkpoint_number=None)
```

Creates a new checkpoint and manages it.

#### Args:

* <b>`checkpoint_number`</b>: An optional integer, or an integer-dtype `Variable` or
    `Tensor`, used to number the checkpoint. If `None` (default),
    checkpoints are numbered using `checkpoint.save_counter`. Even if
    `checkpoint_number` is provided, `save_counter` is still incremented. A
    user-provided `checkpoint_number` is not incremented even if it is a
    `Variable`.


#### Returns:

The path to the new checkpoint. It is also recorded in the `checkpoints`
and `latest_checkpoint` properies.



