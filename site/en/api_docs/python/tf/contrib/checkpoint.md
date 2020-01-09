page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.checkpoint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/checkpoint/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Tools for working with object-based checkpoints.

<!-- Placeholder for "Used in" -->

Visualization and inspection:

#### Managing dependencies:



Trackable data structures:

#### Checkpoint management:



Saving and restoring Python state:

## Classes

[`class CheckpointManager`](../../tf/train/CheckpointManager): Deletes old checkpoints.

[`class Checkpointable`](../../tf/contrib/checkpoint/Checkpointable): Manages dependencies on other objects.

[`class CheckpointableBase`](../../tf/contrib/checkpoint/CheckpointableBase): Base class for `Trackable` objects without automatic dependencies.

[`class CheckpointableObjectGraph`](../../tf/contrib/checkpoint/CheckpointableObjectGraph): A ProtocolMessage

[`class List`](../../tf/contrib/checkpoint/List): An append-only sequence type which is trackable.

[`class Mapping`](../../tf/contrib/checkpoint/Mapping): An append-only trackable mapping data structure with string keys.

[`class NoDependency`](../../tf/contrib/checkpoint/NoDependency): Allows attribute assignment to `Trackable` objects with no dependency.

[`class NumpyState`](../../tf/contrib/checkpoint/NumpyState): A trackable object whose NumPy array attributes are saved/restored.

[`class PythonStateWrapper`](../../tf/train/experimental/PythonState): A mixin for putting Python state in an object-based checkpoint.

[`class UniqueNameTracker`](../../tf/contrib/checkpoint/UniqueNameTracker): Adds dependencies on trackable objects with name hints.

## Functions

[`capture_dependencies(...)`](../../tf/contrib/checkpoint/capture_dependencies): Capture variables created within this scope as `Template` dependencies.

[`dot_graph_from_checkpoint(...)`](../../tf/contrib/checkpoint/dot_graph_from_checkpoint): Visualizes an object-based checkpoint (from <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a>).

[`list_objects(...)`](../../tf/contrib/checkpoint/list_objects): Traverse the object graph and list all accessible objects.

[`object_metadata(...)`](../../tf/contrib/checkpoint/object_metadata): Retrieves information about the objects in a checkpoint.

[`split_dependency(...)`](../../tf/contrib/checkpoint/split_dependency): Creates multiple dependencies with a synchronized save/restore.
