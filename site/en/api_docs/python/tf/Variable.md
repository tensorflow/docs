


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.Variable

### `class tf.Variable`

See the guide: [Variables > Variables](../../../api_guides/python/state_ops#Variables)

See the [Variables How To](../../../programmers_guide/variables) for a high
level overview.

A variable maintains state in the graph across calls to `run()`. You add a
variable to the graph by constructing an instance of the class `Variable`.

The `Variable()` constructor requires an initial value for the variable,
which can be a `Tensor` of any type and shape. The initial value defines the
type and shape of the variable. After construction, the type and shape of
the variable are fixed. The value can be changed using one of the assign
methods.

If you want to change the shape of a variable later you have to use an
`assign` Op with `validate_shape=False`.

Just like any `Tensor`, variables created with `Variable()` can be used as
inputs for other Ops in the graph. Additionally, all the operators
overloaded for the `Tensor` class are carried over to variables, so you can
also add nodes to the graph by just doing arithmetic on variables.

```python
import tensorflow as tf

# Create a variable.
w = tf.Variable(<initial-value>, name=<optional-name>)

# Use the variable in the graph like any Tensor.
y = tf.matmul(w, ...another variable or tensor...)

# The overloaded operators are available too.
z = tf.sigmoid(w + y)

# Assign a new value to the variable with `assign()` or a related method.
w.assign(w + 1.0)
w.assign_add(1.0)
```

When you launch the graph, variables have to be explicitly initialized before
you can run Ops that use their value. You can initialize a variable by
running its *initializer op*, restoring the variable from a save file, or
simply running an `assign` Op that assigns a value to the variable. In fact,
the variable *initializer op* is just an `assign` Op that assigns the
variable's initial value to the variable itself.

```python
# Launch the graph in a session.
with tf.Session() as sess:
    # Run the variable initializer.
    sess.run(w.initializer)
    # ...you now can run ops that use the value of 'w'...
```

The most common initialization pattern is to use the convenience function
`global_variables_initializer()` to add an Op to the graph that initializes
all the variables. You then run that Op after launching the graph.

```python
# Add an Op to initialize global variables.
init_op = tf.global_variables_initializer()

# Launch the graph in a session.
with tf.Session() as sess:
    # Run the Op that initializes global variables.
    sess.run(init_op)
    # ...you can now run any Op that uses variable values...
```

If you need to create a variable with an initial value dependent on another
variable, use the other variable's `initialized_value()`. This ensures that
variables are initialized in the right order.

All variables are automatically collected in the graph where they are
created. By default, the constructor adds the new variable to the graph
collection `GraphKeys.GLOBAL_VARIABLES`. The convenience function
`global_variables()` returns the contents of that collection.

When building a machine learning model it is often convenient to distinguish
between variables holding the trainable model parameters and other variables
such as a `global step` variable used to count training steps. To make this
easier, the variable constructor supports a `trainable=<bool>` parameter. If
`True`, the new variable is also added to the graph collection
`GraphKeys.TRAINABLE_VARIABLES`. The convenience function
`trainable_variables()` returns the contents of this collection. The
various `Optimizer` classes use this collection as the default list of
variables to optimize.

## Child Classes
[`class SaveSliceInfo`](../tf/Variable/SaveSliceInfo)

## Properties

<h3 id="device"><code>device</code></h3>

The device of this variable.

<h3 id="dtype"><code>dtype</code></h3>

The `DType` of this variable.

<h3 id="graph"><code>graph</code></h3>

The `Graph` of this variable.

<h3 id="initial_value"><code>initial_value</code></h3>

Returns the Tensor used as the initial value for the variable.

Note that this is different from `initialized_value()` which runs
the op that initializes the variable before returning its value.
This method returns the tensor that is used by the op that initializes
the variable.

#### Returns:

  A `Tensor`.

<h3 id="initializer"><code>initializer</code></h3>

The initializer operation for this variable.

<h3 id="name"><code>name</code></h3>

The name of this variable.

<h3 id="op"><code>op</code></h3>

The `Operation` of this variable.



## Methods

<h3 id="__init__"><code>__init__(initial_value=None, trainable=True, collections=None, validate_shape=True, caching_device=None, name=None, variable_def=None, dtype=None, expected_shape=None, import_scope=None)</code></h3>

Creates a new variable with value `initial_value`.

The new variable is added to the graph collections listed in `collections`,
which defaults to `[GraphKeys.GLOBAL_VARIABLES]`.

If `trainable` is `True` the variable is also added to the graph collection
`GraphKeys.TRAINABLE_VARIABLES`.

This constructor creates both a `variable` Op and an `assign` Op to set the
variable to its initial value.

#### Args:

* <b>`initial_value`</b>: A `Tensor`, or Python object convertible to a `Tensor`,
    which is the initial value for the Variable. The initial value must have
    a shape specified unless `validate_shape` is set to False. Can also be a
    callable with no argument that returns the initial value when called. In
    that case, `dtype` must be specified. (Note that initializer functions
    from init_ops.py must first be bound to a shape before being used here.)
* <b>`trainable`</b>: If `True`, the default, also adds the variable to the graph
    collection `GraphKeys.TRAINABLE_VARIABLES`. This collection is used as
    the default list of variables to use by the `Optimizer` classes.
* <b>`collections`</b>: List of graph collections keys. The new variable is added to
    these collections. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
* <b>`validate_shape`</b>: If `False`, allows the variable to be initialized with a
    value of unknown shape. If `True`, the default, the shape of
    `initial_value` must be known.
* <b>`caching_device`</b>: Optional device string describing where the Variable
    should be cached for reading.  Defaults to the Variable's device.
    If not `None`, caches on another device.  Typical use is to cache
    on the device where the Ops using the Variable reside, to deduplicate
    copying through `Switch` and other conditional statements.
* <b>`name`</b>: Optional name for the variable. Defaults to `'Variable'` and gets
    uniquified automatically.
* <b>`variable_def`</b>: `VariableDef` protocol buffer. If not `None`, recreates
    the Variable object with its contents. `variable_def` and the other
    arguments are mutually exclusive.
* <b>`dtype`</b>: If set, initial_value will be converted to the given type.
    If `None`, either the datatype will be kept (if `initial_value` is
    a Tensor), or `convert_to_tensor` will decide.
* <b>`expected_shape`</b>: A TensorShape. If set, initial_value is expected
    to have this shape.
* <b>`import_scope`</b>: Optional `string`. Name scope to add to the
    `Variable.` Only used when initializing from protocol buffer.


#### Raises:

* <b>`ValueError`</b>: If both `variable_def` and initial_value are specified.
* <b>`ValueError`</b>: If the initial value is not specified, or does not have a
    shape and `validate_shape` is `True`.

<h3 id="assign"><code>assign(value, use_locking=False)</code></h3>

Assigns a new value to the variable.

This is essentially a shortcut for `assign(self, value)`.

#### Args:

* <b>`value`</b>: A `Tensor`. The new value for this variable.
* <b>`use_locking`</b>: If `True`, use locking during the assignment.


#### Returns:

  A `Tensor` that will hold the new value of this variable after
  the assignment has completed.

<h3 id="assign_add"><code>assign_add(delta, use_locking=False)</code></h3>

Adds a value to this variable.

 This is essentially a shortcut for `assign_add(self, delta)`.

#### Args:

* <b>`delta`</b>: A `Tensor`. The value to add to this variable.
* <b>`use_locking`</b>: If `True`, use locking during the operation.


#### Returns:

  A `Tensor` that will hold the new value of this variable after
  the addition has completed.

<h3 id="assign_sub"><code>assign_sub(delta, use_locking=False)</code></h3>

Subtracts a value from this variable.

This is essentially a shortcut for `assign_sub(self, delta)`.

#### Args:

* <b>`delta`</b>: A `Tensor`. The value to subtract from this variable.
* <b>`use_locking`</b>: If `True`, use locking during the operation.


#### Returns:

  A `Tensor` that will hold the new value of this variable after
  the subtraction has completed.

<h3 id="count_up_to"><code>count_up_to(limit)</code></h3>

Increments this variable until it reaches `limit`.

When that Op is run it tries to increment the variable by `1`. If
incrementing the variable would bring it above `limit` then the Op raises
the exception `OutOfRangeError`.

If no error is raised, the Op outputs the value of the variable before
the increment.

This is essentially a shortcut for `count_up_to(self, limit)`.

#### Args:

* <b>`limit`</b>: value at which incrementing the variable raises an error.


#### Returns:

  A `Tensor` that will hold the variable value before the increment. If no
  other Op modifies this variable, the values produced will all be
  distinct.

<h3 id="eval"><code>eval(session=None)</code></h3>

In a session, computes and returns the value of this variable.

This is not a graph construction method, it does not add ops to the graph.

This convenience method requires a session where the graph
containing this variable has been launched. If no session is
passed, the default session is used.  See [`tf.Session`](../tf/Session) for more
information on launching a graph and on sessions.

```python
v = tf.Variable([1, 2])
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # Usage passing the session explicitly.
    print(v.eval(sess))
    # Usage with the default session.  The 'with' block
    # above makes 'sess' the default session.
    print(v.eval())
```

#### Args:

* <b>`session`</b>: The session to use to evaluate this variable. If
    none, the default session is used.


#### Returns:

  A numpy `ndarray` with a copy of the value of this variable.

<h3 id="from_proto"><code>from_proto(variable_def, import_scope=None)</code></h3>

Returns a `Variable` object created from `variable_def`.

<h3 id="get_shape"><code>get_shape()</code></h3>

The `TensorShape` of this variable.

#### Returns:

  A `TensorShape`.

<h3 id="initialized_value"><code>initialized_value()</code></h3>

Returns the value of the initialized variable.

You should use this instead of the variable itself to initialize another
variable with a value that depends on the value of this variable.

Beware of using initialized_value except during initialization:
initialized_value causes the Variable's initializer op to be run, so running
this op resets the variable to the initial value.

```python
# Initialize 'v' with a random tensor.
v = tf.Variable(tf.truncated_normal([10, 40]))
# Use `initialized_value` to guarantee that `v` has been
# initialized before its value is used to initialize `w`.
# The random values are picked only once.
w = tf.Variable(v.initialized_value() * 2.0)
```

#### Returns:

  A `Tensor` holding the value of this variable after its initializer
  has run.

<h3 id="load"><code>load(value, session=None)</code></h3>

Load new value into this variable

Writes new value to variable's memory. Doesn't add ops to the graph.

This convenience method requires a session where the graph
containing this variable has been launched. If no session is
passed, the default session is used.  See [`tf.Session`](../tf/Session) for more
information on launching a graph and on sessions.

```python
v = tf.Variable([1, 2])
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # Usage passing the session explicitly.
    v.load([2, 3], sess)
    print(v.eval(sess)) # prints [2 3]
    # Usage with the default session.  The 'with' block
    # above makes 'sess' the default session.
    v.load([3, 4], sess)
    print(v.eval()) # prints [3 4]
```

#### Args:

    value: New variable value
    session: The session to use to evaluate this variable. If
      none, the default session is used.


#### Raises:

    ValueError: Session is not passed and no default session

<h3 id="read_value"><code>read_value()</code></h3>

Returns the value of this variable, read in the current context.

Can be different from value() if it's on another device, with control
dependencies, etc.

#### Returns:

  A `Tensor` containing the value of the variable.

<h3 id="scatter_sub"><code>scatter_sub(sparse_delta, use_locking=False)</code></h3>

Subtracts `IndexedSlices` from this variable.

This is essentially a shortcut for `scatter_sub(self, sparse_delta.indices,
sparse_delta.values)`.

#### Args:

* <b>`sparse_delta`</b>: `IndexedSlices` to be subtracted from this variable.
* <b>`use_locking`</b>: If `True`, use locking during the operation.


#### Returns:

  A `Tensor` that will hold the new value of this variable after
  the scattered subtraction has completed.


#### Raises:

* <b>`ValueError`</b>: if `sparse_delta` is not an `IndexedSlices`.

<h3 id="set_shape"><code>set_shape(shape)</code></h3>

Overrides the shape for this variable.

#### Args:

* <b>`shape`</b>: the `TensorShape` representing the overridden shape.

<h3 id="to_proto"><code>to_proto(export_scope=None)</code></h3>

Converts a `Variable` to a `VariableDef` protocol buffer.

#### Args:

* <b>`export_scope`</b>: Optional `string`. Name scope to remove.


#### Returns:

  A `VariableDef` protocol buffer, or `None` if the `Variable` is not
  in the specified name scope.

<h3 id="value"><code>value()</code></h3>

Returns the last snapshot of this variable.

You usually do not need to call this method as all ops that need the value
of the variable call it automatically through a `convert_to_tensor()` call.

Returns a `Tensor` which holds the value of the variable.  You can not
assign a new value to this tensor as it is not a reference to the variable.

To avoid copies, if the consumer of the returned value is on the same device
as the variable, this actually returns the live value of the variable, not
a copy.  Updates to the variable are seen by the consumer.  If the consumer
is on a different device it will get a copy of the variable.

#### Returns:

  A `Tensor` containing the value of the variable.





Defined in [`tensorflow/python/ops/variables.py`](https://www.tensorflow.org/code/tensorflow/python/ops/variables.py).

