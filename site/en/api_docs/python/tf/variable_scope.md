page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.variable_scope

## Class `variable_scope`





Defined in [`tensorflow/python/ops/variable_scope.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/variable_scope.py).

A context manager for defining ops that creates variables (layers).

This context manager validates that the (optional) `values` are from the same
graph, ensures that graph is the default graph, and pushes a name scope and a
variable scope.

If `name_or_scope` is not None, it is used as is. If `name_or_scope` is None,
then `default_name` is used.  In that case, if the same name has been
previously used in the same scope, it will be made unique by appending `_N`
to it.

Variable scope allows you to create new variables and to share already created
ones while providing checks to not create or share by accident. For details,
see the [Variable Scope How To](https://tensorflow.org/guide/variables), here
we present only a few basic examples.

Simple example of how to create a new variable:

```python
with tf.variable_scope("foo"):
    with tf.variable_scope("bar"):
        v = tf.get_variable("v", [1])
        assert v.name == "foo/bar/v:0"
```

Simple example of how to reenter a premade variable scope safely:

```python
with tf.variable_scope("foo") as vs:
  pass

# Re-enter the variable scope.
with tf.variable_scope(vs,
                       auxiliary_name_scope=False) as vs1:
  # Restore the original name_scope.
  with tf.name_scope(vs1.original_name_scope):
      v = tf.get_variable("v", [1])
      assert v.name == "foo/v:0"
      c = tf.constant([1], name="c")
      assert c.name == "foo/c:0"
```

Basic example of sharing a variable AUTO_REUSE:

```python
def foo():
  with tf.variable_scope("foo", reuse=tf.AUTO_REUSE):
    v = tf.get_variable("v", [1])
  return v

v1 = foo()  # Creates v.
v2 = foo()  # Gets the same, existing v.
assert v1 == v2
```

Basic example of sharing a variable with reuse=True:

```python
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
with tf.variable_scope("foo", reuse=True):
    v1 = tf.get_variable("v", [1])
assert v1 == v
```

Sharing a variable by capturing a scope and setting reuse:

```python
with tf.variable_scope("foo") as scope:
    v = tf.get_variable("v", [1])
    scope.reuse_variables()
    v1 = tf.get_variable("v", [1])
assert v1 == v
```

To prevent accidental sharing of variables, we raise an exception when getting
an existing variable in a non-reusing scope.

```python
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
    v1 = tf.get_variable("v", [1])
    #  Raises ValueError("... v already exists ...").
```

Similarly, we raise an exception when trying to get a variable that does not
exist in reuse mode.

```python
with tf.variable_scope("foo", reuse=True):
    v = tf.get_variable("v", [1])
    #  Raises ValueError("... v does not exists ...").
```

Note that the `reuse` flag is inherited: if we open a reusing scope, then all
its sub-scopes become reusing as well.

A note about name scoping: Setting `reuse` does not impact the naming of other
ops such as mult. See related discussion on
[github#6189](https://github.com/tensorflow/tensorflow/issues/6189)

Note that up to and including version 1.0, it was allowed (though explicitly
discouraged) to pass False to the reuse argument, yielding undocumented
behaviour slightly different from None. Starting at 1.1.0 passing None and
False as reuse has exactly the same effect.

A note about using variable scopes in multi-threaded environment: Variable
scopes are thread local, so one thread will not see another thread's current
scope. Also, when using `default_name`, unique scopes names are also generated
only on a per thread basis. If the same name was used within a different
thread, that doesn't prevent a new thread from creating the same scope.
However, the underlying variable store is shared across threads (within the
same graph). As such, if another thread tries to create a new variable with
the same name as a variable created by a previous thread, it will fail unless
reuse is True.

Further, each thread starts with an empty variable scope. So if you wish to
preserve name prefixes from a scope from the main thread, you should capture
the main thread's scope and re-enter it in each thread. For e.g.

```
main_thread_scope = variable_scope.get_variable_scope()

# Thread's target function:
def thread_target_fn(captured_scope):
  with variable_scope.variable_scope(captured_scope):
    # .... regular code for this thread


thread = threading.Thread(target=thread_target_fn, args=(main_thread_scope,))
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name_or_scope,
    default_name=None,
    values=None,
    initializer=None,
    regularizer=None,
    caching_device=None,
    partitioner=None,
    custom_getter=None,
    reuse=None,
    dtype=None,
    use_resource=None,
    constraint=None,
    auxiliary_name_scope=True
)
```

Initialize the context manager.

#### Args:

* <b>`name_or_scope`</b>: `string` or `VariableScope`: the scope to open.
* <b>`default_name`</b>: The default name to use if the `name_or_scope` argument is
    `None`, this name will be uniquified. If name_or_scope is provided it
    won't be used and therefore it is not required and can be None.
* <b>`values`</b>: The list of `Tensor` arguments that are passed to the op function.
* <b>`initializer`</b>: default initializer for variables within this scope.
* <b>`regularizer`</b>: default regularizer for variables within this scope.
* <b>`caching_device`</b>: default caching device for variables within this scope.
* <b>`partitioner`</b>: default partitioner for variables within this scope.
* <b>`custom_getter`</b>: default custom getter for variables within this scope.
* <b>`reuse`</b>: `True`, None, or tf.AUTO_REUSE; if `True`, we go into reuse mode
    for this scope as well as all sub-scopes; if tf.AUTO_REUSE, we create
    variables if they do not exist, and return them otherwise; if None, we
    inherit the parent scope's reuse flag. When eager execution is enabled,
    new variables are always created unless an EagerVariableStore or
    template is currently active.
* <b>`dtype`</b>: type of variables created in this scope (defaults to the type
    in the passed scope, or inherited from parent scope).
* <b>`use_resource`</b>: If False, all variables will be regular Variables. If True,
    experimental ResourceVariables with well-defined semantics will be used
    instead. Defaults to False (will later change to True). When eager
    execution is enabled this argument is always forced to be True.
* <b>`constraint`</b>: An optional projection function to be applied to the variable
    after being updated by an `Optimizer` (e.g. used to implement norm
    constraints or value constraints for layer weights). The function must
    take as input the unprojected Tensor representing the value of the
    variable and return the Tensor for the projected value
    (which must have the same shape). Constraints are not safe to
    use when doing asynchronous distributed training.
* <b>`auxiliary_name_scope`</b>: If `True`, we create an auxiliary name scope with
    the scope. If `False`, we don't create it. Note that the argument is
    not inherited, and it only takes effect for once when creating. You
    should only use it for re-entering a premade variable scope.


#### Returns:

A scope that can be captured and reused.


#### Raises:

* <b>`ValueError`</b>: when trying to reuse within a create scope, or create within
    a reuse scope.
* <b>`TypeError`</b>: when the types of some arguments are not appropriate.



## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```



<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    type_arg,
    value_arg,
    traceback_arg
)
```





