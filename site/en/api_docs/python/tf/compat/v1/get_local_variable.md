description: Gets an existing *local* variable or creates a new one.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.get_local_variable" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.get_local_variable

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/variable_scope.py#L1704-L1740">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Gets an existing *local* variable or creates a new one.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.get_local_variable(
    name, shape=None, dtype=None, initializer=None, regularizer=None,
    trainable=(False), collections=None, caching_device=None, partitioner=None,
    validate_shape=(True), use_resource=None, custom_getter=None, constraint=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.compat.v1.VariableAggregation.NONE
)
</code></pre>



<!-- Placeholder for "Used in" -->

Behavior is the same as in `get_variable`, except that variables are
added to the `LOCAL_VARIABLES` collection and `trainable` is set to
`False`.
This function prefixes the name with the current variable scope
and performs reuse checks. See the
[Variable Scope How To](https://tensorflow.org/guide/variables)
for an extensive description of how reusing works. Here is a basic example:

```python
def foo():
  with tf.variable_scope("foo", reuse=tf.AUTO_REUSE):
    v = tf.get_variable("v", [1])
  return v

v1 = foo()  # Creates v.
v2 = foo()  # Gets the same, existing v.
assert v1 == v2
```

If initializer is `None` (the default), the default initializer passed in
the variable scope will be used. If that one is `None` too, a
`glorot_uniform_initializer` will be used. The initializer can also be
a Tensor, in which case the variable is initialized to this value and shape.

Similarly, if the regularizer is `None` (the default), the default regularizer
passed in the variable scope will be used (if that is `None` too,
then by default no regularization is performed).

If a partitioner is provided, a `PartitionedVariable` is returned.
Accessing this object as a `Tensor` returns the shards concatenated along
the partition axis.

Some useful partitioners are available.  See, e.g.,
`variable_axis_size_partitioner` and `min_max_variable_partitioner`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
The name of the new or existing variable.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Shape of the new or existing variable.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Type of the new or existing variable (defaults to `DT_FLOAT`).
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
Initializer for the variable if one is created. Can either be
an initializer object or a Tensor. If it's a Tensor, its shape must be known
unless validate_shape is False.
</td>
</tr><tr>
<td>
`regularizer`
</td>
<td>
A (Tensor -> Tensor or None) function; the result of
applying it on a newly created variable will be added to the collection
`tf.GraphKeys.REGULARIZATION_LOSSES` and can be used for regularization.
</td>
</tr><tr>
<td>
`collections`
</td>
<td>
List of graph collections keys to add the Variable to.
Defaults to `[GraphKeys.LOCAL_VARIABLES]` (see <a href="../../../tf/Variable.md"><code>tf.Variable</code></a>).
</td>
</tr><tr>
<td>
`caching_device`
</td>
<td>
Optional device string or function describing where the
Variable should be cached for reading.  Defaults to the Variable's
device.  If not `None`, caches on another device.  Typical use is to
cache on the device where the Ops using the Variable reside, to
deduplicate copying through `Switch` and other conditional statements.
</td>
</tr><tr>
<td>
`partitioner`
</td>
<td>
Optional callable that accepts a fully defined `TensorShape`
and `dtype` of the Variable to be created, and returns a list of
partitions for each axis (currently only one axis can be partitioned).
</td>
</tr><tr>
<td>
`validate_shape`
</td>
<td>
If False, allows the variable to be initialized with a
value of unknown shape. If True, the default, the shape of initial_value
must be known. For this to be used the initializer must be a Tensor and
not an initializer object.
</td>
</tr><tr>
<td>
`use_resource`
</td>
<td>
If False, creates a regular Variable. If true, creates an
experimental ResourceVariable instead with well-defined semantics.
Defaults to False (will later change to True). When eager execution is
enabled this argument is always forced to be True.
</td>
</tr><tr>
<td>
`custom_getter`
</td>
<td>
Callable that takes as a first argument the true getter, and
allows overwriting the internal get_variable method.
The signature of `custom_getter` should match that of this method,
but the most future-proof version will allow for changes:
`def custom_getter(getter, *args, **kwargs)`.  Direct access to
all `get_variable` parameters is also allowed:
`def custom_getter(getter, name, *args, **kwargs)`.  A simple identity
custom getter that simply creates variables with modified names is:
```python
def custom_getter(getter, name, *args, **kwargs):
return getter(name + '_suffix', *args, **kwargs)
```
</td>
</tr><tr>
<td>
`constraint`
</td>
<td>
An optional projection function to be applied to the variable
after being updated by an `Optimizer` (e.g. used to implement norm
constraints or value constraints for layer weights). The function must
take as input the unprojected Tensor representing the value of the
variable and return the Tensor for the projected value
(which must have the same shape). Constraints are not safe to
use when doing asynchronous distributed training.
</td>
</tr><tr>
<td>
`synchronization`
</td>
<td>
Indicates when a distributed a variable will be
aggregated. Accepted values are constants defined in the class
<a href="../../../tf/VariableSynchronization.md"><code>tf.VariableSynchronization</code></a>. By default the synchronization is set to
`AUTO` and the current `DistributionStrategy` chooses
when to synchronize.
</td>
</tr><tr>
<td>
`aggregation`
</td>
<td>
Indicates how a distributed variable will be aggregated.
Accepted values are constants defined in the class
<a href="../../../tf/VariableAggregation.md"><code>tf.VariableAggregation</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The created or existing `Variable` (or `PartitionedVariable`, if a
partitioner was used).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
when creating a new variable and shape is not declared,
when violating reuse during variable creation, or when `initializer` dtype
and `dtype` don't match. Reuse is set inside `variable_scope`.
</td>
</tr>
</table>

