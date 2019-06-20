page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.Operation

## Class `Operation`





Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/framework/ops.py).

See the guide: [Building Graphs > Core graph data structures](../../../api_guides/python/framework#Core_graph_data_structures)

Represents a graph node that performs computation on tensors.

An `Operation` is a node in a TensorFlow `Graph` that takes zero or
more `Tensor` objects as input, and produces zero or more `Tensor`
objects as output. Objects of type `Operation` are created by
calling a Python op constructor (such as
<a href="../tf/matmul"><code>tf.matmul</code></a>)
or <a href="../tf/Graph#create_op"><code>tf.Graph.create_op</code></a>.

For example `c = tf.matmul(a, b)` creates an `Operation` of type
"MatMul" that takes tensors `a` and `b` as input, and produces `c`
as output.

After the graph has been launched in a session, an `Operation` can
be executed by passing it to
<a href="../tf/Session#run"><code>tf.Session.run</code></a>.
`op.run()` is a shortcut for calling `tf.get_default_session().run(op)`.

## Properties

<h3 id="control_inputs"><code>control_inputs</code></h3>

The `Operation` objects on which this op has a control dependency.

Before this op is executed, TensorFlow will ensure that the
operations in `self.control_inputs` have finished executing. This
mechanism can be used to run ops sequentially for performance
reasons, or to ensure that the side effects of an op are observed
in the correct order.

#### Returns:

A list of `Operation` objects.

<h3 id="device"><code>device</code></h3>

The name of the device to which this op has been assigned, if any.

#### Returns:

The string name of the device to which this op has been
assigned, or an empty string if it has not been assigned to a
device.

<h3 id="graph"><code>graph</code></h3>

The `Graph` that contains this operation.

<h3 id="inputs"><code>inputs</code></h3>

The list of `Tensor` objects representing the data inputs of this op.

<h3 id="name"><code>name</code></h3>

The full name of this operation.

<h3 id="node_def"><code>node_def</code></h3>

Returns the `NodeDef` representation of this operation.

#### Returns:

A
[`NodeDef`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/core/framework/node_def.proto)
protocol buffer.

<h3 id="op_def"><code>op_def</code></h3>

Returns the `OpDef` proto that represents the type of this op.

#### Returns:

An
[`OpDef`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/core/framework/op_def.proto)
protocol buffer.

<h3 id="outputs"><code>outputs</code></h3>

The list of `Tensor` objects representing the outputs of this op.

<h3 id="traceback"><code>traceback</code></h3>

Returns the call stack from when this operation was constructed.

<h3 id="traceback_with_start_lines"><code>traceback_with_start_lines</code></h3>

Same as traceback but includes start line of function definition.

#### Returns:

A list of 5-tuples (filename, lineno, name, code, func_start_lineno).

<h3 id="type"><code>type</code></h3>

The type of the op (e.g. `"MatMul"`).



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    node_def,
    g,
    inputs=None,
    output_types=None,
    control_inputs=None,
    input_types=None,
    original_op=None,
    op_def=None
)
```

Creates an `Operation`.

NOTE: This constructor validates the name of the `Operation` (passed
as `node_def.name`). Valid `Operation` names match the following
regular expression:

    [A-Za-z0-9.][A-Za-z0-9_.\\-/]*

#### Args:

* <b>`node_def`</b>: `node_def_pb2.NodeDef`.  `NodeDef` for the `Operation`.
    Used for attributes of `node_def_pb2.NodeDef`, typically `name`,
    `op`, and `device`.  The `input` attribute is irrelevant here
    as it will be computed when generating the model.
* <b>`g`</b>: `Graph`. The parent graph.
* <b>`inputs`</b>: list of `Tensor` objects. The inputs to this `Operation`.
* <b>`output_types`</b>: list of `DType` objects.  List of the types of the
    `Tensors` computed by this operation.  The length of this list indicates
    the number of output endpoints of the `Operation`.
* <b>`control_inputs`</b>: list of operations or tensors from which to have a
    control dependency.
* <b>`input_types`</b>: List of `DType` objects representing the
    types of the tensors accepted by the `Operation`.  By default
    uses `[x.dtype.base_dtype for x in inputs]`.  Operations that expect
    reference-typed inputs must specify these explicitly.
* <b>`original_op`</b>: Optional. Used to associate the new `Operation` with an
    existing `Operation` (for example, a replica with the op that was
    replicated).
* <b>`op_def`</b>: Optional. The `op_def_pb2.OpDef` proto that describes the
    op type that this `Operation` represents.


#### Raises:

* <b>`TypeError`</b>: if control inputs are not Operations or Tensors,
    or if `node_def` is not a `NodeDef`,
    or if `g` is not a `Graph`,
    or if `inputs` are not tensors,
    or if `inputs` and `input_types` are incompatible.
* <b>`ValueError`</b>: if the `node_def` name is not valid.

<h3 id="colocation_groups"><code>colocation_groups</code></h3>

``` python
colocation_groups()
```

Returns the list of colocation groups of the op.

<h3 id="get_attr"><code>get_attr</code></h3>

``` python
get_attr(name)
```

Returns the value of the attr of this op with the given `name`.

#### Args:

* <b>`name`</b>: The name of the attr to fetch.


#### Returns:

The value of the attr, as a Python object.


#### Raises:

* <b>`ValueError`</b>: If this op does not have an attr with the given `name`.

<h3 id="run"><code>run</code></h3>

``` python
run(
    feed_dict=None,
    session=None
)
```

Runs this operation in a `Session`.

Calling this method will execute all preceding operations that
produce the inputs needed for this operation.

*N.B.* Before invoking `Operation.run()`, its graph must have been
launched in a session, and either a default session must be
available, or `session` must be specified explicitly.

#### Args:

* <b>`feed_dict`</b>: A dictionary that maps `Tensor` objects to feed values.
    See <a href="../tf/Session#run"><code>tf.Session.run</code></a>
    for a description of the valid feed values.
* <b>`session`</b>: (Optional.) The `Session` to be used to run to this operation. If
    none, the default session will be used.

<h3 id="values"><code>values</code></h3>

``` python
values()
```

DEPRECATED: Use outputs.



