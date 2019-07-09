

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.checkpoint



Defined in [`tensorflow/contrib/checkpoint/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/checkpoint/__init__.py).

Tools for working with object-based checkpoints.

Visualization and inspection:

Managing dependencies:

Checkpointable data structures:

## Classes

[`class Checkpointable`](../../tf/contrib/checkpoint/Checkpointable): Manages dependencies on other objects.

[`class CheckpointableBase`](../../tf/contrib/checkpoint/CheckpointableBase): Base class for `Checkpointable` objects without automatic dependencies.

[`class CheckpointableObjectGraph`](../../tf/contrib/checkpoint/CheckpointableObjectGraph)

[`class List`](../../tf/contrib/checkpoint/List): An append-only sequence type which is checkpointable.

[`class Mapping`](../../tf/contrib/checkpoint/Mapping): An append-only checkpointable mapping data structure with string keys.

[`class NoDependency`](../../tf/contrib/checkpoint/NoDependency): Allows attribute assignment to `Checkpointable` objects with no dependency.

[`class UniqueNameTracker`](../../tf/contrib/checkpoint/UniqueNameTracker): Adds dependencies on checkpointable objects with name hints.

## Functions

[`capture_dependencies(...)`](../../tf/contrib/checkpoint/capture_dependencies): Capture variables created within this scope as `Template` dependencies.

[`dot_graph_from_checkpoint(...)`](../../tf/contrib/checkpoint/dot_graph_from_checkpoint): Visualizes an object-based checkpoint (from <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a>).

[`list_objects(...)`](../../tf/contrib/checkpoint/list_objects): Traverse the object graph and list all accessible objects.

[`object_metadata(...)`](../../tf/contrib/checkpoint/object_metadata): Retrieves information about the objects in a checkpoint.

[`split_dependency(...)`](../../tf/contrib/checkpoint/split_dependency): Creates multiple dependencies with a synchronized save/restore.

