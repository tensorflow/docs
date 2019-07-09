

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.Checkpoint

## Class `Checkpoint`

Inherits From: [`Checkpointable`](../../tf/contrib/checkpoint/Checkpointable)

### Aliases:

* Class `tf.contrib.eager.Checkpoint`
* Class `tf.train.Checkpoint`



Defined in [`tensorflow/python/training/checkpointable/util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/training/checkpointable/util.py).

Groups checkpointable objects, saving and restoring them.

`Checkpoint`'s constructor accepts keyword arguments whose values are types
that contain checkpointable state, such as <a href="../../tf/train/Optimizer"><code>tf.train.Optimizer</code></a>
implementations, <a href="../../tf/Variable"><code>tf.Variable</code></a>, `tf.keras.Layer` implementations, or
<a href="../../tf/keras/Model"><code>tf.keras.Model</code></a> implementations. It saves these values with a checkpoint, and
maintains a `save_counter` for numbering checkpoints.

Example usage when graph building:

```python
import tensorflow as tf
import os

checkpoint_directory = "/tmp/training_checkpoints"
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_directory))
train_op = optimizer.minimize( ... )
status.assert_consumed()  # Optional sanity checks.
with tf.Session() as session:
  # Use the Session to restore variables, or initialize them if
  # tf.train.latest_checkpoint returned None.
  status.initialize_or_restore(session)
  for _ in range(num_training_steps):
    session.run(train_op)
  checkpoint.save(file_prefix=checkpoint_prefix)
```

Example usage with eager execution enabled:

```python
import tensorflow as tf
import os

tf.enable_eager_execution()

checkpoint_directory = "/tmp/training_checkpoints"
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_directory))
for _ in range(num_training_steps):
  optimizer.minimize( ... )  # Variables will be restored on creation.
status.assert_consumed()  # Optional sanity checks.
checkpoint.save(file_prefix=checkpoint_prefix)
```

`Checkpoint.save` and `Checkpoint.restore` write and read object-based
checkpoints, in contrast to <a href="../../tf/train/Saver"><code>tf.train.Saver</code></a> which writes and reads
`variable.name` based checkpoints. Object-based checkpointing saves a graph of
dependencies between Python objects (`Layer`s, `Optimizer`s, `Variable`s,
etc.) with named edges, and this graph is used to match variables when
restoring a checkpoint. It can be more robust to changes in the Python
program, and helps to support restore-on-create for variables when executing
eagerly. Prefer <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a> over <a href="../../tf/train/Saver"><code>tf.train.Saver</code></a> for new code.

`Checkpoint` objects have dependencies on the objects passed as keyword
arguments to their constructors, and each dependency is given a name that is
identical to the name of the keyword argument for which it was created.
TensorFlow classes like `Layer`s and `Optimizer`s will automatically add
dependencies on their variables (e.g. "kernel" and "bias" for
<a href="../../tf/keras/layers/Dense"><code>tf.keras.layers.Dense</code></a>). Inheriting from <a href="../../tf/keras/Model"><code>tf.keras.Model</code></a> makes managing
dependencies easy in user-defined classes, since `Model` hooks into attribute
assignment. For example:

```python
class Regress(tf.keras.Model):

  def __init__(self):
    super(Regress, self).__init__()
    self.input_transform = tf.keras.layers.Dense(10)
    # ...

  def call(self, inputs):
    x = self.input_transform(inputs)
    # ...
```

This `Model` has a dependency named "input_transform" on its `Dense` layer,
which in turn depends on its variables. As a result, saving an instance of
`Regress` using <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a> will also save all the variables created
by the `Dense` layer.

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
    saved with the checkpoint. Values must be checkpointable objects.

#### Raises:

* <b>`ValueError`</b>: If objects in `kwargs` are not checkpointable.

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

Restore a training checkpoint.

Restores this `Checkpoint` and any objects it depends on.

When executing eagerly, either assigns values immediately if variables to
restore have been created already, or defers restoration until the variables
are created. Dependencies added after this call will be matched if they have
a corresponding object in the checkpoint (the restore request will queue in
any checkpointable object waiting for the expected dependency to be added).

When graph building, restoration ops are added to the graph but not run
immediately.

To ensure that loading is complete and no more assignments will take place,
use the `assert_consumed()` method of the status object returned by
`restore`:

```python
checkpoint = tf.train.Checkpoint( ... )
checkpoint.restore(path).assert_consumed()
```

An exception will be raised if any Python objects in the dependency graph
were not found in the checkpoint, or if any checkpointed values do not have
a matching Python object.

When graph building, `assert_consumed()` indicates that all of the restore
ops that will be created for this checkpoint have been created. They can be
run via the `run_restore_ops()` method of the status object:

```python
checkpoint.restore(path).assert_consumed().run_restore_ops()
```

If the checkpoint has not been consumed completely, then the list of restore
ops will grow as more objects are added to the dependency graph.

Name-based <a href="../../tf/train/Saver"><code>tf.train.Saver</code></a> checkpoints can be loaded using this
method. Names are used to match variables. No restore ops are created/run
until `run_restore_ops()` or `initialize_or_restore()` are called on the
returned status object when graph building, but there is restore-on-creation
when executing eagerly. Re-encode name-based checkpoints using
<a href="../../tf/train/Checkpoint#save"><code>tf.train.Checkpoint.save</code></a> as soon as possible.

#### Args:

* <b>`save_path`</b>: The path to the checkpoint, as returned by `save` or
    <a href="../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint</code></a>. If None (as when there is no latest
    checkpoint for <a href="../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint</code></a> to return), returns an
    object which may run initializers for objects in the dependency
    graph. If the checkpoint was written by the name-based <a href="../../tf/train/Saver"><code>tf.train.Saver</code></a>,
    names are used to match variables.


#### Returns:

A load status object, which can be used to make assertions about the
status of a checkpoint restoration and run initialization/restore ops.

The returned status object has the following methods:
- `assert_consumed()`:
    Raises an exception if any variables/objects are unmatched: either
    checkpointed values which don't have a matching Python object or
    Python objects in the dependency graph with no values in the
    checkpoint. This method returns the status object, and so may be
    chained with `initialize_or_restore` or `run_restore_ops`.
- `initialize_or_restore(session=None)`:
    When graph building, runs variable initializers if `save_path` is
    `None`, but otherwise runs restore operations. If no `session` is
    explicitly specified, the default session is used. No effect when
    executing eagerly (variables are initialized or restored eagerly).
- `run_restore_ops(session=None)`:
    When graph building, runs restore operations. If no `session` is
    explicitly specified, the default session is used. No effect when
    executing eagerly (restore operations are run eagerly). May only be
    called when `save_path` is not `None`.

<h3 id="save"><code>save</code></h3>

``` python
save(
    file_prefix,
    session=None
)
```

Save a training checkpoint.

The saved checkpoint includes variables created by this object and any
checkpointable objects it depends on at the time `Checkpoint.save()` is
called.

#### Args:

* <b>`file_prefix`</b>: A prefix to use for the checkpoint filenames
    (/path/to/directory/and_a_prefix). Names are generated based on this
    prefix and `Checkpoint.save_counter`.
* <b>`session`</b>: The session to evaluate variables in. Ignored when executing
    eagerly. If not provided when graph building, the default session is
    used.


#### Returns:

The full path to the checkpoint.



