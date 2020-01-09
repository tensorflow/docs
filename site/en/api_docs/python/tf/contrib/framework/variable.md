page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.variable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L209-L281">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets an existing variable with these parameters or creates a new one.

``` python
tf.contrib.framework.variable(
    name,
    shape=None,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=True,
    collections=None,
    caching_device=None,
    device=None,
    partitioner=None,
    custom_getter=None,
    use_resource=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.VariableAggregation.NONE
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: the name of the new or existing variable.
* <b>`shape`</b>: shape of the new or existing variable.
* <b>`dtype`</b>: type of the new or existing variable (defaults to `DT_FLOAT`).
* <b>`initializer`</b>: initializer for the variable if one is created.
* <b>`regularizer`</b>: a (Tensor -> Tensor or None) function; the result of applying
  it on a newly created variable will be added to the collection
  GraphKeys.REGULARIZATION_LOSSES and can be used for regularization.
* <b>`trainable`</b>: If `True` also add the variable to the graph collection
  <a href="/api_docs/python/tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a> (see <a href="../../../tf/Variable"><code>tf.Variable</code></a>).
* <b>`collections`</b>: A list of collection names to which the Variable will be added.
  If None it would default to <a href="../../../tf/GraphKeys#GLOBAL_VARIABLES"><code>tf.GraphKeys.GLOBAL_VARIABLES</code></a>.
* <b>`caching_device`</b>: Optional device string or function describing where the
  Variable should be cached for reading.  Defaults to the Variable's device.
* <b>`device`</b>: Optional device to place the variable. It can be an string or a
  function that is called to get the device for the variable.
* <b>`partitioner`</b>: Optional callable that accepts a fully defined `TensorShape`
  and dtype of the `Variable` to be created, and returns a list of
  partitions for each axis (currently only one axis can be partitioned).
* <b>`custom_getter`</b>: Callable that allows overwriting the internal get_variable
  method and has to have the same signature.
* <b>`use_resource`</b>: If `True` use a ResourceVariable instead of a Variable.
* <b>`synchronization`</b>: Indicates when a distributed a variable will be aggregated.
  Accepted values are constants defined in the class
  <a href="../../../tf/VariableSynchronization"><code>tf.VariableSynchronization</code></a>. By default the synchronization is set to
  `AUTO` and the current `DistributionStrategy` chooses when to synchronize.
* <b>`aggregation`</b>: Indicates how a distributed variable will be aggregated.
  Accepted values are constants defined in the class
  <a href="../../../tf/VariableAggregation"><code>tf.VariableAggregation</code></a>.


#### Returns:

The created or existing variable.
