description: Represents a graph node that performs computation on tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.Operation" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="colocation_groups"/>
<meta itemprop="property" content="get_attr"/>
<meta itemprop="property" content="run"/>
<meta itemprop="property" content="values"/>
</div>

# tf.Operation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L1862-L2596">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents a graph node that performs computation on tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.Operation`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.Operation(
    node_def, g, inputs=None, output_types=None, control_inputs=None,
    input_types=None, original_op=None, op_def=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An `Operation` is a node in a <a href="../tf/Graph.md"><code>tf.Graph</code></a> that takes zero or more `Tensor`
objects as input, and produces zero or more `Tensor` objects as output.
Objects of type `Operation` are created by calling a Python op constructor
(such as <a href="../tf/linalg/matmul.md"><code>tf.matmul</code></a>) within a <a href="../tf/function.md"><code>tf.function</code></a> or under a <a href="../tf/Graph.md#as_default"><code>tf.Graph.as_default</code></a>
context manager.

For example, within a <a href="../tf/function.md"><code>tf.function</code></a>, `c = tf.matmul(a, b)` creates an
`Operation` of type "MatMul" that takes tensors `a` and `b` as input, and
produces `c` as output.

If a <a href="../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> is used, an `Operation` of a <a href="../tf/Graph.md"><code>tf.Graph</code></a> can be
executed by passing it to `tf.Session.run`. `op.run()` is a shortcut for
calling `tf.compat.v1.get_default_session().run(op)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`node_def`
</td>
<td>
`node_def_pb2.NodeDef`.  `NodeDef` for the `Operation`. Used for
attributes of `node_def_pb2.NodeDef`, typically `name`, `op`, and
`device`.  The `input` attribute is irrelevant here as it will be
computed when generating the model.
</td>
</tr><tr>
<td>
`g`
</td>
<td>
`Graph`. The parent graph.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
list of `Tensor` objects. The inputs to this `Operation`.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
list of `DType` objects.  List of the types of the `Tensors`
computed by this operation.  The length of this list indicates the
number of output endpoints of the `Operation`.
</td>
</tr><tr>
<td>
`control_inputs`
</td>
<td>
list of operations or tensors from which to have a control
dependency.
</td>
</tr><tr>
<td>
`input_types`
</td>
<td>
List of `DType` objects representing the types of the tensors
accepted by the `Operation`.  By default uses `[x.dtype.base_dtype for x
in inputs]`.  Operations that expect reference-typed inputs must specify
these explicitly.
</td>
</tr><tr>
<td>
`original_op`
</td>
<td>
Optional. Used to associate the new `Operation` with an
existing `Operation` (for example, a replica with the op that was
replicated).
</td>
</tr><tr>
<td>
`op_def`
</td>
<td>
Optional. The `op_def_pb2.OpDef` proto that describes the op type
that this `Operation` represents.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if control inputs are not Operations or Tensors,
or if `node_def` is not a `NodeDef`,
or if `g` is not a `Graph`,
or if `inputs` are not tensors,
or if `inputs` and `input_types` are incompatible.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if the `node_def` name is not valid.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`control_inputs`
</td>
<td>
The `Operation` objects on which this op has a control dependency.

Before this op is executed, TensorFlow will ensure that the
operations in `self.control_inputs` have finished executing. This
mechanism can be used to run ops sequentially for performance
reasons, or to ensure that the side effects of an op are observed
in the correct order.
</td>
</tr><tr>
<td>
`device`
</td>
<td>
The name of the device to which this op has been assigned, if any.
</td>
</tr><tr>
<td>
`graph`
</td>
<td>
The `Graph` that contains this operation.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
The sequence of `Tensor` objects representing the data inputs of this op.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The full name of this operation.
</td>
</tr><tr>
<td>
`node_def`
</td>
<td>
Returns the `NodeDef` representation of this operation.
</td>
</tr><tr>
<td>
`op_def`
</td>
<td>
Returns the `OpDef` proto that represents the type of this op.
</td>
</tr><tr>
<td>
`outputs`
</td>
<td>
The list of `Tensor` objects representing the outputs of this op.
</td>
</tr><tr>
<td>
`traceback`
</td>
<td>
Returns the call stack from when this operation was constructed.
</td>
</tr><tr>
<td>
`type`
</td>
<td>
The type of the op (e.g. `"MatMul"`).
</td>
</tr>
</table>



## Methods

<h3 id="colocation_groups"><code>colocation_groups</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L2054-L2071">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>colocation_groups()
</code></pre>

Returns the list of colocation groups of the op.


<h3 id="get_attr"><code>get_attr</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L2516-L2553">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_attr(
    name
)
</code></pre>

Returns the value of the attr of this op with the given `name`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The name of the attr to fetch.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The value of the attr, as a Python object.
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
If this op does not have an attr with the given `name`.
</td>
</tr>
</table>



<h3 id="run"><code>run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L2580-L2596">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    feed_dict=None, session=None
)
</code></pre>

Runs this operation in a `Session`.

Calling this method will execute all preceding operations that
produce the inputs needed for this operation.

*N.B.* Before invoking <a href="../tf/Operation.md#run"><code>Operation.run()</code></a>, its graph must have been
launched in a session, and either a default session must be
available, or `session` must be specified explicitly.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`feed_dict`
</td>
<td>
A dictionary that maps `Tensor` objects to feed values. See
`tf.Session.run` for a description of the valid feed values.
</td>
</tr><tr>
<td>
`session`
</td>
<td>
(Optional.) The `Session` to be used to run to this operation. If
none, the default session will be used.
</td>
</tr>
</table>



<h3 id="values"><code>values</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L2073-L2075">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>values()
</code></pre>

DEPRECATED: Use outputs.




