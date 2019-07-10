page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.Checkpointable

## Class `Checkpointable`

Manages dependencies on other objects.

Inherits From: [`CheckpointableBase`](../../../tf/contrib/checkpoint/CheckpointableBase)

### Aliases:

* Class `tf.contrib.checkpoint.Checkpointable`
* Class `tf.contrib.eager.Checkpointable`



Defined in [`python/training/tracking/tracking.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/tracking/tracking.py).

<!-- Placeholder for "Used in" -->

`Trackable` objects may have dependencies: other `Trackable` objects
which should be saved if the object declaring the dependency is saved. A
correctly saveable program has a dependency graph such that if changing a
global variable affects an object (e.g. changes the behavior of any of its
methods) then there is a chain of dependencies from the influenced object to
the variable.

Dependency edges have names, and are created implicitly when a
`Trackable` object is assigned to an attribute of another
`Trackable` object. For example:

```
obj = Trackable()
obj.v = ResourceVariable(0.)
```

The `Trackable` object `obj` now has a dependency named "v" on a
variable.

`Trackable` objects may specify `Tensor`s to be saved and restored
directly (e.g. a `Variable` indicating how to save itself) rather than through
dependencies on other objects. See
`Trackable._gather_saveables_for_checkpoint` for details.

