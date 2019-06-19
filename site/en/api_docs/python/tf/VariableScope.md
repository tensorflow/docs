page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.VariableScope

## Class `VariableScope`





Defined in [`tensorflow/python/ops/variable_scope.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/variable_scope.py).

See the guide: [Variables > Sharing Variables](../../../api_guides/python/state_ops#Sharing_Variables)

Variable scope object to carry defaults to provide to `get_variable`.

Many of the arguments we need for `get_variable` in a variable store are most
easily handled with a context. This object is used for the defaults.

#### Attributes:

* <b>`name`</b>: name of the current scope, used as prefix in get_variable.
* <b>`initializer`</b>: default initializer passed to get_variable.
* <b>`regularizer`</b>: default regularizer passed to get_variable.
* <b>`reuse`</b>: Boolean, None, or tf.AUTO_REUSE, setting the reuse in
    get_variable. When eager execution is enabled this argument is always
    forced to be False.
* <b>`caching_device`</b>: string, callable, or None: the caching device passed to
    get_variable.
* <b>`partitioner`</b>: callable or `None`: the partitioner passed to `get_variable`.
* <b>`custom_getter`</b>: default custom getter passed to get_variable.
* <b>`name_scope`</b>: The name passed to <a href="../tf/name_scope"><code>tf.name_scope</code></a>.
* <b>`dtype`</b>: default type passed to get_variable (defaults to DT_FLOAT).
* <b>`use_resource`</b>: if False, create a normal Variable; if True create an
    experimental ResourceVariable with well-defined semantics. Defaults
    to False (will later change to True). When eager execution is enabled
    this argument is always forced to be True.
* <b>`constraint`</b>: An optional projection function to be applied to the variable
    after being updated by an `Optimizer` (e.g. used to implement norm
    constraints or value constraints for layer weights). The function must
    take as input the unprojected Tensor representing the value of the
    variable and return the Tensor for the projected value
    (which must have the same shape). Constraints are not safe to
    use when doing asynchronous distributed training.

## Properties

<h3 id="caching_device"><code>caching_device</code></h3>



<h3 id="constraint"><code>constraint</code></h3>



<h3 id="custom_getter"><code>custom_getter</code></h3>



<h3 id="dtype"><code>dtype</code></h3>



<h3 id="initializer"><code>initializer</code></h3>



<h3 id="name"><code>name</code></h3>



<h3 id="original_name_scope"><code>original_name_scope</code></h3>



<h3 id="partitioner"><code>partitioner</code></h3>



<h3 id="regularizer"><code>regularizer</code></h3>



<h3 id="reuse"><code>reuse</code></h3>



<h3 id="use_resource"><code>use_resource</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    reuse,
    name='',
    initializer=None,
    regularizer=None,
    caching_device=None,
    partitioner=None,
    custom_getter=None,
    name_scope='',
    dtype=tf.float32,
    use_resource=None,
    constraint=None
)
```

Creates a new VariableScope with the given properties.

<h3 id="get_collection"><code>get_collection</code></h3>

``` python
get_collection(name)
```

Get this scope's variables.

<h3 id="get_variable"><code>get_variable</code></h3>

``` python
get_variable(
    var_store,
    name,
    shape=None,
    dtype=None,
    initializer=None,
    regularizer=None,
    reuse=None,
    trainable=True,
    collections=None,
    caching_device=None,
    partitioner=None,
    validate_shape=True,
    use_resource=None,
    custom_getter=None,
    constraint=None
)
```

Gets an existing variable with this name or create a new one.

<h3 id="global_variables"><code>global_variables</code></h3>

``` python
global_variables()
```

Get this scope's global variables.

<h3 id="local_variables"><code>local_variables</code></h3>

``` python
local_variables()
```

Get this scope's local variables.

<h3 id="reuse_variables"><code>reuse_variables</code></h3>

``` python
reuse_variables()
```

Reuse variables in this scope.

<h3 id="set_caching_device"><code>set_caching_device</code></h3>

``` python
set_caching_device(caching_device)
```

Set caching_device for this scope.

<h3 id="set_custom_getter"><code>set_custom_getter</code></h3>

``` python
set_custom_getter(custom_getter)
```

Set custom getter for this scope.

<h3 id="set_dtype"><code>set_dtype</code></h3>

``` python
set_dtype(dtype)
```

Set data type for this scope.

<h3 id="set_initializer"><code>set_initializer</code></h3>

``` python
set_initializer(initializer)
```

Set initializer for this scope.

<h3 id="set_partitioner"><code>set_partitioner</code></h3>

``` python
set_partitioner(partitioner)
```

Set partitioner for this scope.

<h3 id="set_regularizer"><code>set_regularizer</code></h3>

``` python
set_regularizer(regularizer)
```

Set regularizer for this scope.

<h3 id="set_use_resource"><code>set_use_resource</code></h3>

``` python
set_use_resource(use_resource)
```

Sets whether to use ResourceVariables for this scope.

<h3 id="trainable_variables"><code>trainable_variables</code></h3>

``` python
trainable_variables()
```

Get this scope's trainable variables.



