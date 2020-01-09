page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.NoDependency


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/tracking/data_structures.py#L41-L63">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `NoDependency`

Allows attribute assignment to `Trackable` objects with no dependency.



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
still track the `Layer` (so it will appear in <a href="/api_docs/python/tf/keras/Model#layers"><code>Model.layers</code></a>, and its
variables will appear in <a href="/api_docs/python/tf/keras/layers/Layer#variables"><code>Model.variables</code></a>).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/tracking/data_structures.py#L62-L63">View source</a>

``` python
__init__(value)
```

Initialize self.  See help(type(self)) for accurate signature.
