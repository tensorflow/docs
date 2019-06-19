page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.checkpoint



Defined in [`tensorflow/contrib/checkpoint/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/checkpoint/__init__.py).

Tools for working with object-based checkpoints.

Visualization and inspection:

Managing dependencies:

Checkpointable data structures:

## Classes

[`class Checkpointable`](../../tf/contrib/checkpoint/Checkpointable): Manages dependencies on other objects.

[`class CheckpointableObjectGraph`](../../tf/contrib/checkpoint/CheckpointableObjectGraph)

[`class List`](../../tf/contrib/checkpoint/List): An append-only sequence type which is checkpointable.

[`class Mapping`](../../tf/contrib/checkpoint/Mapping): An append-only checkpointable mapping data structure with string keys.

[`class NoDependency`](../../tf/contrib/checkpoint/NoDependency): Allows attribute assignment to `Checkpointable` objects with no dependency.

[`class UniqueNameTracker`](../../tf/contrib/checkpoint/UniqueNameTracker): Adds dependencies on checkpointable objects with name hints.

## Functions

[`dot_graph_from_checkpoint(...)`](../../tf/contrib/checkpoint/dot_graph_from_checkpoint): Visualizes an object-based checkpoint (from <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a>).

[`object_metadata(...)`](../../tf/contrib/checkpoint/object_metadata): Retrieves information about the objects in a checkpoint.

[`split_dependency(...)`](../../tf/contrib/checkpoint/split_dependency): Creates multiple dependencies with a synchronized save/restore.

