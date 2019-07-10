page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.variable_creator_scope

``` python
tf.variable_creator_scope(variable_creator)
```



Defined in [`tensorflow/python/ops/variable_scope.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/variable_scope.py).

Scope which defines a variable creation function to be used by variable().

variable_creator is expected to be a function with the following signature:

```
  def variable_creator(next_creator, **kwargs)
```

The creator is supposed to eventually call the next_creator to create a
variable if it does want to create a variable and not call Variable or
ResourceVariable directly. This helps make creators composable. A creator may
choose to create multiple variables, return already existing variables, or
simply register that a variable was created and defer to the next creators in
line. Creators can also modify the keyword arguments seen by the next
creators.

Custom getters in the variable scope will eventually resolve down to these
custom creators when they do create variables.

The valid keyword arguments in kwds are:
    initial_value: A `Tensor`, or Python object convertible to a `Tensor`,
      which is the initial value for the Variable. The initial value must have
      a shape specified unless `validate_shape` is set to False. Can also be a
      callable with no argument that returns the initial value when called. In
      that case, `dtype` must be specified. (Note that initializer functions
      from init_ops.py must first be bound to a shape before being used here.)
    trainable: If `True`, the default, also adds the variable to the graph
      collection `GraphKeys.TRAINABLE_VARIABLES`. This collection is used as
      the default list of variables to use by the `Optimizer` classes.
      `trainable` defaults to `True` unless `synchronization` is
      set to `ON_READ`.
    collections: List of graph collections keys. The new variable is added to
      these collections. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
    validate_shape: If `False`, allows the variable to be initialized with a
      value of unknown shape. If `True`, the default, the shape of
      `initial_value` must be known.
    caching_device: Optional device string describing where the Variable
      should be cached for reading.  Defaults to the Variable's device.
      If not `None`, caches on another device.  Typical use is to cache
      on the device where the Ops using the Variable reside, to deduplicate
      copying through `Switch` and other conditional statements.
    name: Optional name for the variable. Defaults to `'Variable'` and gets
      uniquified automatically.
    dtype: If set, initial_value will be converted to the given type.
      If `None`, either the datatype will be kept (if `initial_value` is
      a Tensor), or `convert_to_tensor` will decide.
    constraint: A constraint function to be applied to the variable after
      updates by some algorithms.
    use_resource: if True, a ResourceVariable is always created.
    synchronization: Indicates when a distributed a variable will be
      aggregated. Accepted values are constants defined in the class
      <a href="../tf/VariableSynchronization"><code>tf.VariableSynchronization</code></a>. By default the synchronization is set to
      `AUTO` and the current `DistributionStrategy` chooses
      when to synchronize. If `synchronization` is set to `ON_READ`,
      `trainable` must not be set to `True`.
    aggregation: Indicates how a distributed variable will be aggregated.
      Accepted values are constants defined in the class
      <a href="../tf/VariableAggregation"><code>tf.VariableAggregation</code></a>.

This set may grow over time, so it's important the signature of creators is as
mentioned above.

#### Args:

* <b>`variable_creator`</b>: the passed creator


#### Yields:

A scope in which the creator is active