page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.model_variable

Gets an existing model variable with these parameters or creates a new one.

``` python
tf.contrib.framework.model_variable(
    name,
    shape=None,
    dtype=tf.dtypes.float32,
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



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

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
  `GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../tf/Variable"><code>tf.Variable</code></a>).
* <b>`collections`</b>: A list of collection names to which the Variable will be added.
  Note that the variable is always also added to the
  `GraphKeys.GLOBAL_VARIABLES` and `GraphKeys.MODEL_VARIABLES` collections.
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
  If `synchronization` is set to `ON_READ`, `trainable` must not be set to
  `True`.
* <b>`aggregation`</b>: Indicates how a distributed variable will be aggregated.
  Accepted values are constants defined in the class
  <a href="../../../tf/VariableAggregation"><code>tf.VariableAggregation</code></a>.


#### Returns:

The created or existing variable.
