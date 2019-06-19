page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.variable

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
    use_resource=None
)
```



Defined in [`tensorflow/contrib/framework/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/framework/python/ops/variables.py).

See the guide: [Framework (contrib) > Variables](../../../../../api_guides/python/contrib.framework#Variables)

Gets an existing variable with these parameters or creates a new one.

#### Args:

* <b>`name`</b>: the name of the new or existing variable.
* <b>`shape`</b>: shape of the new or existing variable.
* <b>`dtype`</b>: type of the new or existing variable (defaults to `DT_FLOAT`).
* <b>`initializer`</b>: initializer for the variable if one is created.
* <b>`regularizer`</b>: a (Tensor -> Tensor or None) function; the result of
      applying it on a newly created variable will be added to the collection
      GraphKeys.REGULARIZATION_LOSSES and can be used for regularization.
* <b>`trainable`</b>: If `True` also add the variable to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../tf/Variable"><code>tf.Variable</code></a>).
* <b>`collections`</b>: A list of collection names to which the Variable will be added.
    If None it would default to <a href="../../../tf/GraphKeys#GLOBAL_VARIABLES"><code>tf.GraphKeys.GLOBAL_VARIABLES</code></a>.
* <b>`caching_device`</b>: Optional device string or function describing where the
      Variable should be cached for reading.  Defaults to the Variable's
      device.
* <b>`device`</b>: Optional device to place the variable. It can be an string or a
    function that is called to get the device for the variable.
* <b>`partitioner`</b>: Optional callable that accepts a fully defined `TensorShape`
    and dtype of the `Variable` to be created, and returns a list of
    partitions for each axis (currently only one axis can be partitioned).
* <b>`custom_getter`</b>: Callable that allows overwriting the internal
    get_variable method and has to have the same signature.
* <b>`use_resource`</b>: If `True` use a ResourceVariable instead of a Variable.


#### Returns:

The created or existing variable.