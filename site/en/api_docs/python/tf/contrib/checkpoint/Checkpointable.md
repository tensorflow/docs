page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.Checkpointable

## Class `Checkpointable`

Inherits From: [`CheckpointableBase`](../../../tf/contrib/checkpoint/CheckpointableBase)

### Aliases:

* Class `tf.contrib.checkpoint.Checkpointable`
* Class `tf.contrib.eager.Checkpointable`



Defined in [`tensorflow/python/training/checkpointable/tracking.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/training/checkpointable/tracking.py).

Manages dependencies on other objects.

`Checkpointable` objects may have dependencies: other `Checkpointable` objects
which should be saved if the object declaring the dependency is saved. A
correctly saveable program has a dependency graph such that if changing a
global variable affects an object (e.g. changes the behavior of any of its
methods) then there is a chain of dependencies from the influenced object to
the variable.

Dependency edges have names, and are created implicitly when a
`Checkpointable` object is assigned to an attribute of another
`Checkpointable` object. For example:

```
obj = Checkpointable()
obj.v = ResourceVariable(0.)
```

The `Checkpointable` object `obj` now has a dependency named "v" on a
variable.

`Checkpointable` objects may specify `Tensor`s to be saved and restored
directly (e.g. a `Variable` indicating how to save itself) rather than through
dependencies on other objects. See
`Checkpointable._gather_saveables_for_checkpoint` for details.

## Methods

<h3 id="__setattr__"><code>__setattr__</code></h3>

``` python
__setattr__(
    name,
    value
)
```

Support self.foo = checkpointable syntax.



