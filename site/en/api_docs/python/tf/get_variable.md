page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_variable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variable_scope.py#L1468-L1500">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets an existing variable with these parameters or create a new one.

### Aliases:

* <a href="/api_docs/python/tf/get_variable"><code>tf.compat.v1.get_variable</code></a>


``` python
tf.get_variable(
    name,
    shape=None,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=None,
    collections=None,
    caching_device=None,
    partitioner=None,
    validate_shape=True,
    use_resource=None,
    custom_getter=None,
    constraint=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.VariableAggregation.NONE
)
```



<!-- Placeholder for "Used in" -->

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

#### Args:


* <b>`name`</b>: The name of the new or existing variable.
* <b>`shape`</b>: Shape of the new or existing variable.
* <b>`dtype`</b>: Type of the new or existing variable (defaults to `DT_FLOAT`).
* <b>`initializer`</b>: Initializer for the variable if one is created. Can either be
  an initializer object or a Tensor. If it's a Tensor, its shape must be known
  unless validate_shape is False.
* <b>`regularizer`</b>: A (Tensor -> Tensor or None) function; the result of
  applying it on a newly created variable will be added to the collection
  <a href="../tf/GraphKeys#REGULARIZATION_LOSSES"><code>tf.GraphKeys.REGULARIZATION_LOSSES</code></a> and can be used for regularization.
* <b>`trainable`</b>: If `True` also add the variable to the graph collection
  <a href="../tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a> (see <a href="../tf/Variable"><code>tf.Variable</code></a>).
* <b>`collections`</b>: List of graph collections keys to add the Variable to.
  Defaults to `[GraphKeys.GLOBAL_VARIABLES]` (see <a href="../tf/Variable"><code>tf.Variable</code></a>).
* <b>`caching_device`</b>: Optional device string or function describing where the
  Variable should be cached for reading.  Defaults to the Variable's
  device.  If not `None`, caches on another device.  Typical use is to
  cache on the device where the Ops using the Variable reside, to
  deduplicate copying through `Switch` and other conditional statements.
* <b>`partitioner`</b>: Optional callable that accepts a fully defined `TensorShape`
  and `dtype` of the Variable to be created, and returns a list of
  partitions for each axis (currently only one axis can be partitioned).
* <b>`validate_shape`</b>: If False, allows the variable to be initialized with a
    value of unknown shape. If True, the default, the shape of initial_value
    must be known. For this to be used the initializer must be a Tensor and
    not an initializer object.
* <b>`use_resource`</b>: If False, creates a regular Variable. If true, creates an
  experimental ResourceVariable instead with well-defined semantics.
  Defaults to False (will later change to True). When eager execution is
  enabled this argument is always forced to be True.
* <b>`custom_getter`</b>: Callable that takes as a first argument the true getter, and
  allows overwriting the internal get_variable method.
  The signature of `custom_getter` should match that of this method,
  but the most future-proof version will allow for changes:
  `def custom_getter(getter, *args, **kwargs)`.  Direct access to
  all `get_variable` parameters is also allowed:
  `def custom_getter(getter, name, *args, **kwargs)`.  A simple identity
  custom getter that simply creates variables with modified names is:

>     def custom_getter(getter, name, *args, **kwargs):
>       return getter(name + '_suffix', *args, **kwargs)
* <b>`constraint`</b>: An optional projection function to be applied to the variable
  after being updated by an `Optimizer` (e.g. used to implement norm
  constraints or value constraints for layer weights). The function must
  take as input the unprojected Tensor representing the value of the
  variable and return the Tensor for the projected value
  (which must have the same shape). Constraints are not safe to
  use when doing asynchronous distributed training.
* <b>`synchronization`</b>: Indicates when a distributed a variable will be
  aggregated. Accepted values are constants defined in the class
  <a href="../tf/VariableSynchronization"><code>tf.VariableSynchronization</code></a>. By default the synchronization is set to
  `AUTO` and the current `DistributionStrategy` chooses
  when to synchronize.
* <b>`aggregation`</b>: Indicates how a distributed variable will be aggregated.
  Accepted values are constants defined in the class
  <a href="../tf/VariableAggregation"><code>tf.VariableAggregation</code></a>.


#### Returns:

The created or existing `Variable` (or `PartitionedVariable`, if a
partitioner was used).



#### Raises:


* <b>`ValueError`</b>: when creating a new variable and shape is not declared,
  when violating reuse during variable creation, or when `initializer` dtype
  and `dtype` don't match. Reuse is set inside `variable_scope`.
