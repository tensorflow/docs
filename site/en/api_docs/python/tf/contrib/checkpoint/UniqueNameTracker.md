page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.UniqueNameTracker


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/checkpoint/python/containers.py#L24-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `UniqueNameTracker`

Adds dependencies on trackable objects with name hints.



<!-- Placeholder for "Used in" -->

Useful for creating dependencies with locally unique names.

#### Example usage:


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/checkpoint/python/containers.py#L44-L47">View source</a>

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




<h3 id="trainable"><code>trainable</code></h3>




<h3 id="trainable_variables"><code>trainable_variables</code></h3>




<h3 id="trainable_weights"><code>trainable_weights</code></h3>




<h3 id="updates"><code>updates</code></h3>

Aggregate updates from any `Layer` instances.


<h3 id="variables"><code>variables</code></h3>




<h3 id="weights"><code>weights</code></h3>






## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/tracking/data_structures.py#L247-L250">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="track"><code>track</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/checkpoint/python/containers.py#L53-L84">View source</a>

``` python
track(
    trackable,
    base_name
)
```

Add a dependency on `trackable`.


#### Args:


* <b>`trackable`</b>: An object to add a checkpoint dependency on.
* <b>`base_name`</b>: A name hint, which is uniquified to determine the dependency
  name.

#### Returns:

`trackable`, for chaining.


#### Raises:


* <b>`ValueError`</b>: If `trackable` is not a trackable object.
