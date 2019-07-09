page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.UniqueNameTracker

## Class `UniqueNameTracker`





Defined in [`tensorflow/contrib/checkpoint/python/containers.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/checkpoint/python/containers.py).

Adds dependencies on checkpointable objects with name hints.

Useful for creating dependencies with locally unique names.

Example usage:

```python
class SlotManager(tf.contrib.checkpoint.Checkpointable):

  def __init__(self):
    # Create a dependency named "slotdeps" on the container.
    self.slotdeps = tf.contrib.checkpoint.UniqueNameTracker()
    slotdeps = self.slotdeps
    slots = []
    slots.append(slotdeps.track(tf.Variable(3.), "x"))  # Named "x"
    slots.append(slotdeps.track(tf.Variable(4.), "y"))
    slots.append(slotdeps.track(tf.Variable(5.), "x"))  # Named "x_1"
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.



## Properties

<h3 id="layers"><code>layers</code></h3>



<h3 id="losses"><code>losses</code></h3>

Aggregate losses from any `Layer` instances.

<h3 id="non_trainable_variables"><code>non_trainable_variables</code></h3>



<h3 id="non_trainable_weights"><code>non_trainable_weights</code></h3>



<h3 id="trainable_variables"><code>trainable_variables</code></h3>



<h3 id="trainable_weights"><code>trainable_weights</code></h3>



<h3 id="updates"><code>updates</code></h3>

Aggregate updates from any `Layer` instances.

<h3 id="variables"><code>variables</code></h3>



<h3 id="weights"><code>weights</code></h3>





## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

Return self==value.

<h3 id="track"><code>track</code></h3>

``` python
track(
    checkpointable,
    base_name
)
```

Add a dependency on `checkpointable`.

#### Args:

* <b>`checkpointable`</b>: An object to add a checkpoint dependency on.
* <b>`base_name`</b>: A name hint, which is uniquified to determine the dependency
    name.

#### Returns:

`checkpointable`, for chaining.

#### Raises:

* <b>`ValueError`</b>: If `checkpointable` is not a checkpointable object.



