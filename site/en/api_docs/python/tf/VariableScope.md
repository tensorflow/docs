


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.VariableScope

### `class tf.VariableScope`

See the guide: [Variables > Sharing Variables](../../../api_guides/python/state_ops#Sharing_Variables)

Variable scope object to carry defaults to provide to `get_variable`.

Many of the arguments we need for `get_variable` in a variable store are most
easily handled with a context. This object is used for the defaults.

#### Attributes:

* <b>`name`</b>: name of the current scope, used as prefix in get_variable.
* <b>`initializer`</b>: default initializer passed to get_variable.
* <b>`regularizer`</b>: default regularizer passed to get_variable.
* <b>`reuse`</b>: Boolean or None, setting the reuse in get_variable.
* <b>`caching_device`</b>: string, callable, or None: the caching device passed to
    get_variable.
* <b>`partitioner`</b>: callable or `None`: the partitioner passed to `get_variable`.
* <b>`custom_getter`</b>: default custom getter passed to get_variable.
* <b>`name_scope`</b>: The name passed to `tf.name_scope`.
* <b>`dtype`</b>: default type passed to get_variable (defaults to DT_FLOAT).

## Properties

<h3 id="caching_device"><code>caching_device</code></h3>



<h3 id="custom_getter"><code>custom_getter</code></h3>



<h3 id="dtype"><code>dtype</code></h3>



<h3 id="initializer"><code>initializer</code></h3>



<h3 id="name"><code>name</code></h3>



<h3 id="original_name_scope"><code>original_name_scope</code></h3>



<h3 id="partitioner"><code>partitioner</code></h3>



<h3 id="regularizer"><code>regularizer</code></h3>



<h3 id="reuse"><code>reuse</code></h3>





## Methods

<h3 id="__init__"><code>__init__(reuse, name='', initializer=None, regularizer=None, caching_device=None, partitioner=None, custom_getter=None, name_scope='', dtype=tf.float32)</code></h3>

Creates a new VariableScope with the given properties.

<h3 id="get_variable"><code>get_variable(var_store, name, shape=None, dtype=None, initializer=None, regularizer=None, trainable=True, collections=None, caching_device=None, partitioner=None, validate_shape=True, custom_getter=None)</code></h3>

Gets an existing variable with this name or create a new one.

<h3 id="reuse_variables"><code>reuse_variables()</code></h3>

Reuse variables in this scope.

<h3 id="set_caching_device"><code>set_caching_device(caching_device)</code></h3>

Set caching_device for this scope.

<h3 id="set_custom_getter"><code>set_custom_getter(custom_getter)</code></h3>

Set custom getter for this scope.

<h3 id="set_dtype"><code>set_dtype(dtype)</code></h3>

Set data type for this scope.

<h3 id="set_initializer"><code>set_initializer(initializer)</code></h3>

Set initializer for this scope.

<h3 id="set_partitioner"><code>set_partitioner(partitioner)</code></h3>

Set partitioner for this scope.

<h3 id="set_regularizer"><code>set_regularizer(regularizer)</code></h3>

Set regularizer for this scope.





Defined in [`tensorflow/python/ops/variable_scope.py`](https://www.tensorflow.org/code/tensorflow/python/ops/variable_scope.py).

