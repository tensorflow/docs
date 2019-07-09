page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.CheckpointableSaver

## Class `CheckpointableSaver`





Defined in [`tensorflow/python/training/checkpointable/util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/training/checkpointable/util.py).

Saves and restores a `Checkpointable` object and its dependencies.

See `Checkpointable` for details of dependency management. `Saver` wraps
<a href="../../../tf/train/Saver"><code>tf.train.Saver</code></a> for saving, including extra information about the graph of
dependencies between Python objects. When restoring, it uses this information
about the save-time dependency graph to more robustly match objects with their
checkpointed values. When executing eagerly, it supports restoring variables
on object creation (see `Saver.restore`).

Values in a checkpoint are mapped to `Checkpointable` Python objects
(`Variable`s, `Optimizer`s, `Layer`s) based on the names provided when the
checkpoint was written. To avoid breaking existing checkpoints when modifying
a class, dependency names (the names of attributes to which `Checkpointable`
objects are assigned) may not change. These names are local to objects, in
contrast to the `Variable.name`-based save/restore from <a href="../../../tf/train/Saver"><code>tf.train.Saver</code></a>, and
so allow additional program transformations.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(root_checkpointable)
```

Configure saving.

#### Args:

* <b>`root_checkpointable`</b>: The root of the object graph to save/restore. This
    object and all of its dependencies are saved in the checkpoint. When
    restoring, objects are matched and restored starting from this root.



## Methods

<h3 id="restore"><code>restore</code></h3>

``` python
restore(save_path)
```

Restore a training checkpoint.

Restores `root_checkpointable` and any objects that it tracks
(transitive). Either assigns values immediately if variables to restore have
been created already, or defers restoration until the variables are
created. Dependencies added to the `root_checkpointable` passed to the
constructor after this call will be matched if they have a corresponding
object in the checkpoint.

When building a graph, restorations are added to the graph but not run.

To disallow deferred loading, assert immediately that all checkpointed
variables have been matched to variable objects:

```python
saver = Saver(root)
saver.restore(path).assert_consumed()
```

An exception will be raised unless every object was matched and its
variables already exist.

When graph building, `assert_consumed()` indicates that all of the restore
ops which will be created for this checkpoint have been created. They can be
run via the `run_restore_ops()` function of the status object:

```python
saver.restore(path).assert_consumed().run_restore_ops()
```

If the checkpoint has not been consumed completely, then the list of restore
ops will grow as more objects are added to the dependency graph.

Name-based <a href="../../../tf/train/Saver"><code>tf.train.Saver</code></a> checkpoints can be loaded using this
method. There is no deferred loading, and names are used to match
variables. No restore ops are created/run until `run_restore_ops()` or
`initialize_or_restore()` are called on the returned status object, even
when executing eagerly. Re-encode name-based checkpoints using this
object-based `Saver.save` as soon as possible.

#### Args:

* <b>`save_path`</b>: The path to the checkpoint, as returned by `save` or
    <a href="../../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint</code></a>. If None (as when there is no latest
    checkpoint for <a href="../../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint</code></a> to return), returns an
    object which may run initializers for objects in the dependency
    graph. If the checkpoint was written by the name-based <a href="../../../tf/train/Saver"><code>tf.train.Saver</code></a>,
    names are used to match variables.


#### Returns:

A load status object, which can be used to make assertions about the
status of checkpoint restoration and run initialization/restore ops
(of type `CheckpointLoadStatus`, or `InitializationOnlyStatus` if
`save_path` is `None`).

If `save_path` points to a name-based checkpoint, a `NameBasedSaverStatus`
object is returned which runs restore ops from a name-based saver.

<h3 id="save"><code>save</code></h3>

``` python
save(
    file_prefix,
    checkpoint_number=None,
    session=None
)
```

Save a training checkpoint.

The saved checkpoint includes variables created by this object and any
Checkpointable objects it depends on at the time `Saver.save()` is called.

#### Args:

* <b>`file_prefix`</b>: A prefix to use for the checkpoint filenames
    (/path/to/directory/and_a_prefix). Names are generated based on this
    prefix and `checkpoint_number`, if provided.
* <b>`checkpoint_number`</b>: An integer variable or Tensor, used to number
    checkpoints. Typically this value is saved along with other variables in
    training checkpoints, which will happen automatically if it was created
    by `root_checkpointable` or one of its dependencies (via
    `Checkpointable._add_variable`).
* <b>`session`</b>: The session to evaluate variables in. Ignored when executing
    eagerly. If not provided when graph building, the default session is
    used.


#### Returns:

The full path to the checkpoint.



