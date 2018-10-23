

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.Checkpoint

## Class `Checkpoint`

Inherits From: [`Checkpointable`](../../../tf/contrib/eager/Checkpointable)



Defined in [`tensorflow/contrib/eager/python/checkpointable_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/eager/python/checkpointable_utils.py).

A utility class which groups `Checkpointable` objects.

Accepts arbitrary keyword arguments to its constructor and saves those values
with a checkpoint. Maintains a `save_counter` for numbering checkpoints.

Example usage:

```python
import tensorflow as tf
import tensorflow.contrib.eager as tfe
import os

checkpoint_directory = "/tmp/training_checkpoints"
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

root = tfe.Checkpoint(optimizer=optimizer, model=model)
root.restore(tf.train.latest_checkpoint(checkpoint_directory))
for _ in range(num_training_steps):
  optimizer.minimize( ... )
root.save(file_prefix=checkpoint_prefix)
```

For more manual control over saving, use `tfe.CheckpointableSaver` directly.

#### Attributes:

* <b>`save_counter`</b>: Incremented when `save()` is called. Used to number
    checkpoints.

## Properties

<h3 id="save_counter"><code>save_counter</code></h3>

An integer variable which starts at zero and is incremented on save.

Used to number checkpoints.

#### Returns:

The save counter variable.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(**kwargs)
```

Group objects into a training checkpoint.

#### Args:

* <b>`**kwargs`</b>: Keyword arguments are set as attributes of this object, and are
    saved with the checkpoint. Attribute values must derive from
    `CheckpointableBase`.

#### Raises:

* <b>`ValueError`</b>: If objects in `kwargs` are not Checkpointable.

<h3 id="__setattr__"><code>__setattr__</code></h3>

``` python
__setattr__(
    name,
    value
)
```

Support self.foo = checkpointable syntax.

<h3 id="restore"><code>restore</code></h3>

``` python
restore(save_path)
```

Restore a checkpoint. Wraps `tfe.CheckpointableSaver.restore`.

<h3 id="save"><code>save</code></h3>

``` python
save(
    file_prefix,
    session=None
)
```

Save a checkpoint. Wraps `tfe.CheckpointableSaver.save`.



