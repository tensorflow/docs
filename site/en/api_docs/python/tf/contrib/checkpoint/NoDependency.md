page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.NoDependency

## Class `NoDependency`

Allows attribute assignment to `Trackable` objects with no dependency.





Defined in [`python/training/tracking/data_structures.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/tracking/data_structures.py).

<!-- Placeholder for "Used in" -->


#### Example usage:


```python
obj = Trackable()
obj.has_dependency = tf.Variable(0., name="dep")
obj.no_dependency = NoDependency(tf.Variable(1., name="nodep"))
assert obj.no_dependency.name == "nodep:0"
```

`obj` in this example has a dependency on the variable "dep", and both
attributes contain un-wrapped `Variable` objects.

`NoDependency` also works with <a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a>, but only for checkpoint
dependencies: wrapping a `Layer` in `NoDependency` will assign the (unwrapped)
`Layer` to the attribute without a checkpoint dependency, but the `Model` will
still track the `Layer` (so it will appear in `Model.layers`, and its
variables will appear in `Model.variables`).

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(value)
```






