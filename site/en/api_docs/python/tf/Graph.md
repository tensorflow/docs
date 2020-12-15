description: A TensorFlow computation, represented as a dataflow graph.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.Graph" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_to_collection"/>
<meta itemprop="property" content="add_to_collections"/>
<meta itemprop="property" content="as_default"/>
<meta itemprop="property" content="as_graph_def"/>
<meta itemprop="property" content="as_graph_element"/>
<meta itemprop="property" content="clear_collection"/>
<meta itemprop="property" content="colocate_with"/>
<meta itemprop="property" content="container"/>
<meta itemprop="property" content="control_dependencies"/>
<meta itemprop="property" content="create_op"/>
<meta itemprop="property" content="device"/>
<meta itemprop="property" content="finalize"/>
<meta itemprop="property" content="get_all_collection_keys"/>
<meta itemprop="property" content="get_collection"/>
<meta itemprop="property" content="get_collection_ref"/>
<meta itemprop="property" content="get_name_scope"/>
<meta itemprop="property" content="get_operation_by_name"/>
<meta itemprop="property" content="get_operations"/>
<meta itemprop="property" content="get_tensor_by_name"/>
<meta itemprop="property" content="gradient_override_map"/>
<meta itemprop="property" content="is_feedable"/>
<meta itemprop="property" content="is_fetchable"/>
<meta itemprop="property" content="name_scope"/>
<meta itemprop="property" content="prevent_feeding"/>
<meta itemprop="property" content="prevent_fetching"/>
<meta itemprop="property" content="switch_to_thread_local"/>
<meta itemprop="property" content="unique_name"/>
</div>

# tf.Graph

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L2869-L5195">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A TensorFlow computation, represented as a dataflow graph.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.Graph`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.Graph()
</code></pre>



<!-- Placeholder for "Used in" -->

Graphs are used by <a href="../tf/function.md"><code>tf.function</code></a>s to represent the function's computations.
Each graph contains a set of <a href="../tf/Operation.md"><code>tf.Operation</code></a> objects, which represent units of
computation; and <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> objects, which represent the units of data that
flow between operations.

### Using graphs directly (deprecated)

A <a href="../tf/Graph.md"><code>tf.Graph</code></a> can be constructed and used directly without a <a href="../tf/function.md"><code>tf.function</code></a>, as
was required in TensorFlow 1, but this is deprecated and it is recommended to
use a <a href="../tf/function.md"><code>tf.function</code></a> instead. If a graph is directly used, other deprecated
TensorFlow 1 classes are also required to execute the graph, such as a
<a href="../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a>.

A default graph can be registered with the <a href="../tf/Graph.md#as_default"><code>tf.Graph.as_default</code></a> context
manager. Then, operations will be added to the graph instead of being executed
eagerly. For example:

```python
g = tf.Graph()
with g.as_default():
  # Define operations and tensors in `g`.
  c = tf.constant(30.0)
  assert c.graph is g
```

<a href="../tf/compat/v1/get_default_graph.md"><code>tf.compat.v1.get_default_graph()</code></a> can be used to obtain the default graph.

Important note: This class *is not* thread-safe for graph construction. All
operations should be created from a single thread, or external
synchronization must be provided. Unless otherwise specified, all methods
are not thread-safe.

A `Graph` instance supports an arbitrary number of "collections"
that are identified by name. For convenience when building a large
graph, collections can store groups of related objects: for
example, the <a href="../tf/Variable.md"><code>tf.Variable</code></a> uses a collection (named
`tf.GraphKeys.GLOBAL_VARIABLES`) for
all variables that are created during the construction of a graph. The caller
may define additional collections by specifying a new name.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`building_function`
</td>
<td>
Returns True iff this graph represents a function.
</td>
</tr><tr>
<td>
`collections`
</td>
<td>
Returns the names of the collections known to this graph.
</td>
</tr><tr>
<td>
`finalized`
</td>
<td>
True if this graph has been finalized.
</td>
</tr><tr>
<td>
`graph_def_versions`
</td>
<td>
The GraphDef version information of this graph.

For details on the meaning of each version, see
[`GraphDef`](https://www.tensorflow.org/code/tensorflow/core/framework/graph.proto).
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
The graph-level random seed of this graph.
</td>
</tr><tr>
<td>
`version`
</td>
<td>
Returns a version number that increases as ops are added to the graph.

Note that this is unrelated to the
<a href="../tf/Graph.md#graph_def_versions"><code>tf.Graph.graph_def_versions</code></a>.
</td>
</tr>
</table>



## Methods

<h3 id="add_to_collection"><code>add_to_collection</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3989-L4005">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_to_collection(
    name, value
)
</code></pre>

Stores `value` in the collection with the given `name`.

Note that collections are not sets, so it is possible to add a value to
a collection several times.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The key for the collection. The `GraphKeys` class contains many
standard names for collections.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
The value to add to the collection.
</td>
</tr>
</table>



<h3 id="add_to_collections"><code>add_to_collections</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4007-L4026">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_to_collections(
    names, value
)
</code></pre>

Stores `value` in the collections given by `names`.

Note that collections are not sets, so it is possible to add a value to
a collection several times. This function makes sure that duplicates in
`names` are ignored, but it will not check for pre-existing membership of
`value` in any of the collections in `names`.

`names` can be any iterable, but if `names` is a string, it is treated as a
single collection name.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`names`
</td>
<td>
The keys for the collections to add to. The `GraphKeys` class
contains many standard names for collections.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
The value to add to the collections.
</td>
</tr>
</table>



<h3 id="as_default"><code>as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3942-L3982">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_default()
</code></pre>

Returns a context manager that makes this `Graph` the default graph.

This method should be used if you want to create multiple graphs
in the same process. For convenience, a global default graph is
provided, and all ops will be added to this graph if you do not
create a new graph explicitly.

Use this method with the `with` keyword to specify that ops created within
the scope of a block should be added to this graph. In this case, once
the scope of the `with` is exited, the previous default graph is set again
as default. There is a stack, so it's ok to have multiple nested levels
of `as_default` calls.

The default graph is a property of the current thread. If you
create a new thread, and wish to use the default graph in that
thread, you must explicitly add a `with g.as_default():` in that
thread's function.

The following code examples are equivalent:

```python
# 1. Using Graph.as_default():
g = tf.Graph()
with g.as_default():
  c = tf.constant(5.0)
  assert c.graph is g

# 2. Constructing and making default:
with tf.Graph().as_default() as g:
  c = tf.constant(5.0)
  assert c.graph is g
```

If eager execution is enabled ops created under this context manager will be
added to the graph instead of executed eagerly.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager for using this graph as the default graph.
</td>
</tr>

</table>



<h3 id="as_graph_def"><code>as_graph_def</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3319-L3346">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_graph_def(
    from_version=None, add_shapes=(False)
)
</code></pre>

Returns a serialized `GraphDef` representation of this graph.

The serialized `GraphDef` can be imported into another `Graph`
(using <a href="../tf/graph_util/import_graph_def.md"><code>tf.import_graph_def</code></a>) or used with the
[C++ Session API](../../api_docs/cc/index.md).

This method is thread-safe.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`from_version`
</td>
<td>
Optional.  If this is set, returns a `GraphDef` containing
only the nodes that were added to this graph since its `version`
property had the given value.
</td>
</tr><tr>
<td>
`add_shapes`
</td>
<td>
If true, adds an "_output_shapes" list attr to each node with
the inferred shapes of each of its outputs.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A
[`GraphDef`](https://www.tensorflow.org/code/tensorflow/core/framework/graph.proto)
protocol buffer.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the `graph_def` would be too large.
</td>
</tr>
</table>



<h3 id="as_graph_element"><code>as_graph_element</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3692-L3726">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_graph_element(
    obj, allow_tensor=(True), allow_operation=(True)
)
</code></pre>

Returns the object referred to by `obj`, as an `Operation` or `Tensor`.

This function validates that `obj` represents an element of this
graph, and gives an informative error message if it is not.

This function is the canonical way to get/validate an object of
one of the allowed types from an external argument reference in the
Session API.

This method may be called concurrently from multiple threads.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`obj`
</td>
<td>
A `Tensor`, an `Operation`, or the name of a tensor or operation. Can
also be any object with an `_as_graph_element()` method that returns a
value of one of these types. Note: `_as_graph_element` will be called
inside the graph's lock and so may not modify the graph.
</td>
</tr><tr>
<td>
`allow_tensor`
</td>
<td>
If true, `obj` may refer to a `Tensor`.
</td>
</tr><tr>
<td>
`allow_operation`
</td>
<td>
If true, `obj` may refer to an `Operation`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The `Tensor` or `Operation` in the Graph corresponding to `obj`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `obj` is not a type we support attempting to convert
to types.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `obj` is of an appropriate type but invalid. For
example, an invalid string.
</td>
</tr><tr>
<td>
`KeyError`
</td>
<td>
If `obj` is not an object in the graph.
</td>
</tr>
</table>



<h3 id="clear_collection"><code>clear_collection</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4098-L4108">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>clear_collection(
    name
)
</code></pre>

Clears all values in a collection.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The key for the collection. The `GraphKeys` class contains many
standard names for collections.
</td>
</tr>
</table>



<h3 id="colocate_with"><code>colocate_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4348-L4425">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>colocate_with(
    op, ignore_existing=(False)
)
</code></pre>

Returns a context manager that specifies an op to colocate with.

Note: this function is not for public use, only for internal libraries.

#### For example:



```python
a = tf.Variable([1.0])
with g.colocate_with(a):
  b = tf.constant(1.0)
  c = tf.add(a, b)
```

`b` and `c` will always be colocated with `a`, no matter where `a`
is eventually placed.

**NOTE** Using a colocation scope resets any existing device constraints.

If `op` is `None` then `ignore_existing` must be `True` and the new
scope resets all colocation and device constraints.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`op`
</td>
<td>
The op to colocate all created ops with, or `None`.
</td>
</tr><tr>
<td>
`ignore_existing`
</td>
<td>
If true, only applies colocation of this op within the
context, rather than applying all colocation properties on the stack.
If `op` is `None`, this value must be `True`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if op is None but ignore_existing is False.
</td>
</tr>
</table>



#### Yields:

A context manager that specifies the op with which to colocate
newly created ops.


<h3 id="container"><code>container</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4531-L4581">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>container(
    container_name
)
</code></pre>

Returns a context manager that specifies the resource container to use.

Stateful operations, such as variables and queues, can maintain their
states on devices so that they can be shared by multiple processes.
A resource container is a string name under which these stateful
operations are tracked. These resources can be released or cleared
with `tf.Session.reset()`.

#### For example:



```python
with g.container('experiment0'):
  # All stateful Operations constructed in this context will be placed
  # in resource container "experiment0".
  v1 = tf.Variable([1.0])
  v2 = tf.Variable([2.0])
  with g.container("experiment1"):
    # All stateful Operations constructed in this context will be
    # placed in resource container "experiment1".
    v3 = tf.Variable([3.0])
    q1 = tf.queue.FIFOQueue(10, tf.float32)
  # All stateful Operations constructed in this context will be
  # be created in the "experiment0".
  v4 = tf.Variable([4.0])
  q1 = tf.queue.FIFOQueue(20, tf.float32)
  with g.container(""):
    # All stateful Operations constructed in this context will be
    # be placed in the default resource container.
    v5 = tf.Variable([5.0])
    q3 = tf.queue.FIFOQueue(30, tf.float32)

# Resets container "experiment0", after which the state of v1, v2, v4, q1
# will become undefined (such as uninitialized).
tf.Session.reset(target, ["experiment0"])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`container_name`
</td>
<td>
container name string.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager for defining resource containers for stateful ops,
yields the container name.
</td>
</tr>

</table>



<h3 id="control_dependencies"><code>control_dependencies</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4712-L4823">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>control_dependencies(
    control_inputs
)
</code></pre>

Returns a context manager that specifies control dependencies.

Use with the `with` keyword to specify that all operations constructed
within the context should have control dependencies on
`control_inputs`. For example:

```python
with g.control_dependencies([a, b, c]):
  # `d` and `e` will only run after `a`, `b`, and `c` have executed.
  d = ...
  e = ...
```

Multiple calls to `control_dependencies()` can be nested, and in
that case a new `Operation` will have control dependencies on the union
of `control_inputs` from all active contexts.

```python
with g.control_dependencies([a, b]):
  # Ops constructed here run after `a` and `b`.
  with g.control_dependencies([c, d]):
    # Ops constructed here run after `a`, `b`, `c`, and `d`.
```

You can pass None to clear the control dependencies:

```python
with g.control_dependencies([a, b]):
  # Ops constructed here run after `a` and `b`.
  with g.control_dependencies(None):
    # Ops constructed here run normally, not waiting for either `a` or `b`.
    with g.control_dependencies([c, d]):
      # Ops constructed here run after `c` and `d`, also not waiting
      # for either `a` or `b`.
```

*N.B.* The control dependencies context applies *only* to ops that
are constructed within the context. Merely using an op or tensor
in the context does not add a control dependency. The following
example illustrates this point:

```python
# WRONG
def my_func(pred, tensor):
  t = tf.matmul(tensor, tensor)
  with tf.control_dependencies([pred]):
    # The matmul op is created outside the context, so no control
    # dependency will be added.
    return t

# RIGHT
def my_func(pred, tensor):
  with tf.control_dependencies([pred]):
    # The matmul op is created in the context, so a control dependency
    # will be added.
    return tf.matmul(tensor, tensor)
```

Also note that though execution of ops created under this scope will trigger
execution of the dependencies, the ops created under this scope might still
be pruned from a normal tensorflow graph. For example, in the following
snippet of code the dependencies are never executed:

```python
  loss = model.loss()
  with tf.control_dependencies(dependencies):
    loss = loss + tf.constant(1)  # note: dependencies ignored in the
                                  # backward pass
  return tf.gradients(loss, model.variables)
```

This is because evaluating the gradient graph does not require evaluating
the constant(1) op created in the forward pass.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`control_inputs`
</td>
<td>
A list of `Operation` or `Tensor` objects which must be
executed or computed before running the operations defined in the
context.  Can also be `None` to clear the control dependencies.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager that specifies control dependencies for all
operations constructed within the context.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `control_inputs` is not a list of `Operation` or
`Tensor` objects.
</td>
</tr>
</table>



<h3 id="create_op"><code>create_op</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3411-L3467">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_op(
    op_type, inputs, dtypes=None, input_types=None, name=None, attrs=None,
    op_def=None, compute_shapes=(True), compute_device=(True)
)
</code></pre>

Creates an `Operation` in this graph. (deprecated arguments)

Warning: SOME ARGUMENTS ARE DEPRECATED: `(compute_shapes)`. They will be removed in a future version.
Instructions for updating:
Shapes are always computed; don't use the compute_shapes as it has no effect.

This is a low-level interface for creating an `Operation`. Most
programs will not call this method directly, and instead use the
Python op constructors, such as <a href="../tf/constant.md"><code>tf.constant()</code></a>, which add ops to
the default graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`op_type`
</td>
<td>
The `Operation` type to create. This corresponds to the
`OpDef.name` field for the proto that defines the operation.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A list of `Tensor` objects that will be inputs to the `Operation`.
</td>
</tr><tr>
<td>
`dtypes`
</td>
<td>
(Optional) A list of `DType` objects that will be the types of the
tensors that the operation produces.
</td>
</tr><tr>
<td>
`input_types`
</td>
<td>
(Optional.) A list of `DType`s that will be the types of the
tensors that the operation consumes. By default, uses the base `DType`
of each input in `inputs`. Operations that expect reference-typed inputs
must specify `input_types` explicitly.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional.) A string name for the operation. If not specified, a
name is generated based on `op_type`.
</td>
</tr><tr>
<td>
`attrs`
</td>
<td>
(Optional.) A dictionary where the key is the attribute name (a
string) and the value is the respective `attr` attribute of the
`NodeDef` proto that will represent the operation (an `AttrValue`
proto).
</td>
</tr><tr>
<td>
`op_def`
</td>
<td>
(Optional.) The `OpDef` proto that describes the `op_type` that
the operation will have.
</td>
</tr><tr>
<td>
`compute_shapes`
</td>
<td>
(Optional.) Deprecated. Has no effect (shapes are always
computed).
</td>
</tr><tr>
<td>
`compute_device`
</td>
<td>
(Optional.) If True, device functions will be executed to
compute the device property of the Operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if any of the inputs is not a `Tensor`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if colocation conflicts with existing device assignment.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Operation` object.
</td>
</tr>

</table>



<h3 id="device"><code>device</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4434-L4503">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>device(
    device_name_or_function
)
</code></pre>

Returns a context manager that specifies the default device to use.

The `device_name_or_function` argument may either be a device name
string, a device function, or None:

* If it is a device name string, all operations constructed in
  this context will be assigned to the device with that name, unless
  overridden by a nested `device()` context.
* If it is a function, it will be treated as a function from
  Operation objects to device name strings, and invoked each time
  a new Operation is created. The Operation will be assigned to
  the device with the returned name.
* If it is None, all `device()` invocations from the enclosing context
  will be ignored.

For information about the valid syntax of device name strings, see
the documentation in
[`DeviceNameUtils`](https://www.tensorflow.org/code/tensorflow/core/util/device_name_utils.h).

#### For example:



```python
with g.device('/device:GPU:0'):
  # All operations constructed in this context will be placed
  # on GPU 0.
  with g.device(None):
    # All operations constructed in this context will have no
    # assigned device.

# Defines a function from `Operation` to device string.
def matmul_on_gpu(n):
  if n.type == "MatMul":
    return "/device:GPU:0"
  else:
    return "/cpu:0"

with g.device(matmul_on_gpu):
  # All operations of type "MatMul" constructed in this context
  # will be placed on GPU 0; all other operations will be placed
  # on CPU 0.
```

**N.B.** The device scope may be overridden by op wrappers or
other library code. For example, a variable assignment op
`v.assign()` must be colocated with the <a href="../tf/Variable.md"><code>tf.Variable</code></a> `v`, and
incompatible device scopes will be ignored.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`device_name_or_function`
</td>
<td>
The device name or function to use in the
context.
</td>
</tr>
</table>



#### Yields:

A context manager that specifies the default device to use for newly
created ops.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If device scopes are not properly nested.
</td>
</tr>
</table>



<h3 id="finalize"><code>finalize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3177-L3185">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>finalize()
</code></pre>

Finalizes this graph, making it read-only.

After calling `g.finalize()`, no new operations can be added to
`g`.  This method is used to ensure that no operations are added
to a graph when it is shared between multiple threads, for example
when using a <a href="../tf/compat/v1/train/QueueRunner.md"><code>tf.compat.v1.train.QueueRunner</code></a>.

<h3 id="get_all_collection_keys"><code>get_all_collection_keys</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4093-L4096">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_all_collection_keys()
</code></pre>

Returns a list of collections used in this graph.


<h3 id="get_collection"><code>get_collection</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4053-L4091">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_collection(
    name, scope=None
)
</code></pre>

Returns a list of values in the collection with the given `name`.

This is different from `get_collection_ref()` which always returns the
actual collection list if it exists in that it returns a new list each time
it is called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The key for the collection. For example, the `GraphKeys` class
contains many standard names for collections.
</td>
</tr><tr>
<td>
`scope`
</td>
<td>
(Optional.) A string. If supplied, the resulting list is filtered
to include only items whose `name` attribute matches `scope` using
`re.match`. Items without a `name` attribute are never returned if a
scope is supplied. The choice of `re.match` means that a `scope` without
special tokens filters by prefix.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The list of values in the collection with the given `name`, or
an empty list if no value has been added to that collection. The
list contains the values in the order under which they were
collected.
</td>
</tr>

</table>



<h3 id="get_collection_ref"><code>get_collection_ref</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4028-L4051">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_collection_ref(
    name
)
</code></pre>

Returns a list of values in the collection with the given `name`.

If the collection exists, this returns the list itself, which can
be modified in place to change the collection.  If the collection does
not exist, it is created as an empty list and the list is returned.

This is different from `get_collection()` which always returns a copy of
the collection list if it exists and never creates an empty collection.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The key for the collection. For example, the `GraphKeys` class
contains many standard names for collections.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The list of values in the collection with the given `name`, or an empty
list if no value has been added to that collection.
</td>
</tr>

</table>



<h3 id="get_name_scope"><code>get_name_scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4314-L4329">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_name_scope()
</code></pre>

Returns the current name scope.


#### For example:



```python
with tf.name_scope('scope1'):
  with tf.name_scope('scope2'):
    print(tf.compat.v1.get_default_graph().get_name_scope())
```
would print the string `scope1/scope2`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A string representing the current name scope.
</td>
</tr>

</table>



<h3 id="get_operation_by_name"><code>get_operation_by_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3835-L3854">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_operation_by_name(
    name
)
</code></pre>

Returns the `Operation` with the given `name`.

This method may be called concurrently from multiple threads.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The name of the `Operation` to return.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The `Operation` with the given `name`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `name` is not a string.
</td>
</tr><tr>
<td>
`KeyError`
</td>
<td>
If `name` does not correspond to an operation in this graph.
</td>
</tr>
</table>



<h3 id="get_operations"><code>get_operations</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3817-L3833">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_operations()
</code></pre>

Return the list of operations in the graph.

You can modify the operations in place, but modifications
to the list such as inserts/delete have no effect on the
list of operations known to the graph.

This method may be called concurrently from multiple threads.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of Operations.
</td>
</tr>

</table>



<h3 id="get_tensor_by_name"><code>get_tensor_by_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L3883-L3902">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_tensor_by_name(
    name
)
</code></pre>

Returns the `Tensor` with the given `name`.

This method may be called concurrently from multiple threads.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The name of the `Tensor` to return.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The `Tensor` with the given `name`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `name` is not a string.
</td>
</tr><tr>
<td>
`KeyError`
</td>
<td>
If `name` does not correspond to a tensor in this graph.
</td>
</tr>
</table>



<h3 id="gradient_override_map"><code>gradient_override_map</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4965-L5024">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>gradient_override_map(
    op_type_map
)
</code></pre>

EXPERIMENTAL: A context manager for overriding gradient functions.

This context manager can be used to override the gradient function
that will be used for ops within the scope of the context.

#### For example:



```python
@tf.RegisterGradient("CustomSquare")
def _custom_square_grad(op, grad):
  # ...

with tf.Graph().as_default() as g:
  c = tf.constant(5.0)
  s_1 = tf.square(c)  # Uses the default gradient for tf.square.
  with g.gradient_override_map({"Square": "CustomSquare"}):
    s_2 = tf.square(s_2)  # Uses _custom_square_grad to compute the
                          # gradient of s_2.
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`op_type_map`
</td>
<td>
A dictionary mapping op type strings to alternative op type
strings.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager that sets the alternative op type to be used for one
or more ops created in that context.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `op_type_map` is not a dictionary mapping strings to
strings.
</td>
</tr>
</table>



<h3 id="is_feedable"><code>is_feedable</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5032-L5034">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_feedable(
    tensor
)
</code></pre>

Returns `True` if and only if `tensor` is feedable.


<h3 id="is_fetchable"><code>is_fetchable</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5040-L5045">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_fetchable(
    tensor_or_op
)
</code></pre>

Returns `True` if and only if `tensor_or_op` is fetchable.


<h3 id="name_scope"><code>name_scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4147-L4258">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>name_scope(
    name
)
</code></pre>

Returns a context manager that creates hierarchical names for operations.

A graph maintains a stack of name scopes. A `with name_scope(...):`
statement pushes a new name onto the stack for the lifetime of the context.

The `name` argument will be interpreted as follows:

* A string (not ending with '/') will create a new name scope, in which
  `name` is appended to the prefix of all operations created in the
  context. If `name` has been used before, it will be made unique by
  calling `self.unique_name(name)`.
* A scope previously captured from a `with g.name_scope(...) as
  scope:` statement will be treated as an "absolute" name scope, which
  makes it possible to re-enter existing scopes.
* A value of `None` or the empty string will reset the current name scope
  to the top-level (empty) name scope.

#### For example:



```python
with tf.Graph().as_default() as g:
  c = tf.constant(5.0, name="c")
  assert c.op.name == "c"
  c_1 = tf.constant(6.0, name="c")
  assert c_1.op.name == "c_1"

  # Creates a scope called "nested"
  with g.name_scope("nested") as scope:
    nested_c = tf.constant(10.0, name="c")
    assert nested_c.op.name == "nested/c"

    # Creates a nested scope called "inner".
    with g.name_scope("inner"):
      nested_inner_c = tf.constant(20.0, name="c")
      assert nested_inner_c.op.name == "nested/inner/c"

    # Create a nested scope called "inner_1".
    with g.name_scope("inner"):
      nested_inner_1_c = tf.constant(30.0, name="c")
      assert nested_inner_1_c.op.name == "nested/inner_1/c"

      # Treats `scope` as an absolute name scope, and
      # switches to the "nested/" scope.
      with g.name_scope(scope):
        nested_d = tf.constant(40.0, name="d")
        assert nested_d.op.name == "nested/d"

        with g.name_scope(""):
          e = tf.constant(50.0, name="e")
          assert e.op.name == "e"
```

The name of the scope itself can be captured by `with
g.name_scope(...) as scope:`, which stores the name of the scope
in the variable `scope`. This value can be used to name an
operation that represents the overall result of executing the ops
in a scope. For example:

```python
inputs = tf.constant(...)
with g.name_scope('my_layer') as scope:
  weights = tf.Variable(..., name="weights")
  biases = tf.Variable(..., name="biases")
  affine = tf.matmul(inputs, weights) + biases
  output = tf.nn.relu(affine, name=scope)
```

NOTE: This constructor validates the given `name`. Valid scope
names match one of the following regular expressions:

    [A-Za-z0-9.][A-Za-z0-9_.\-/]* (for scopes at the root)
    [A-Za-z0-9_.\-/]* (for other scopes)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the scope.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager that installs `name` as a new name scope.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `name` is not a valid scope name, according to the rules
above.
</td>
</tr>
</table>



<h3 id="prevent_feeding"><code>prevent_feeding</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5028-L5030">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>prevent_feeding(
    tensor
)
</code></pre>

Marks the given `tensor` as unfeedable in this graph.


<h3 id="prevent_fetching"><code>prevent_fetching</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5036-L5038">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>prevent_fetching(
    op
)
</code></pre>

Marks the given `op` as unfetchable in this graph.


<h3 id="switch_to_thread_local"><code>switch_to_thread_local</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5047-L5062">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>switch_to_thread_local()
</code></pre>

Make device, colocation and dependencies stacks thread-local.

Device, colocation and dependencies stacks are not thread-local be default.
If multiple threads access them, then the state is shared.  This means that
one thread may affect the behavior of another thread.

After this method is called, the stacks become thread-local.  If multiple
threads access them, then the state is not shared.  Each thread uses its own
value; a thread doesn't affect other threads by mutating such a stack.

The initial value for every thread's stack is set to the current value
of the stack when `switch_to_thread_local()` was first called.

<h3 id="unique_name"><code>unique_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L4262-L4312">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>unique_name(
    name, mark_as_used=(True)
)
</code></pre>

Return a unique operation name for `name`.

Note: You rarely need to call `unique_name()` directly.  Most of
the time you just need to create `with g.name_scope()` blocks to
generate structured names.

`unique_name` is used to generate structured names, separated by
`"/"`, to help identify operations when debugging a graph.
Operation names are displayed in error messages reported by the
TensorFlow runtime, and in various visualization tools such as
TensorBoard.

If `mark_as_used` is set to `True`, which is the default, a new
unique name is created and marked as in use. If it's set to `False`,
the unique name is returned without actually being marked as used.
This is useful when the caller simply wants to know what the name
to be created will be.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The name for an operation.
</td>
</tr><tr>
<td>
`mark_as_used`
</td>
<td>
Whether to mark this name as being used.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A string to be passed to `create_op()` that will be used
to name the operation being created.
</td>
</tr>

</table>





