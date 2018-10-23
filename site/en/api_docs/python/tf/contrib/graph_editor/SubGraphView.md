


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.graph_editor.SubGraphView

### `class tf.contrib.graph_editor.SubGraphView`

See the guide: [Graph Editor (contrib) > Module: subgraph](../../../../../api_guides/python/contrib.graph_editor#Module_subgraph)

A subgraph view on an existing `tf.Graph`.

An instance of this class is a subgraph view on an existing `tf.Graph`.
"subgraph" means that it can represent part of the whole `tf.Graph`.
"view" means that it only provides a passive observation and do not to act
on the `tf.Graph`. Note that in this documentation, the term "subgraph" is
often used as substitute to "subgraph view".

A subgraph contains:

* a list of input tensors, accessible via the `inputs` property.
* a list of output tensors, accessible via the `outputs` property.
* and the operations in between, accessible via the "ops" property.

An subgraph can be seen as a function F(i0, i1, ...) -> o0, o1, ... It is a
function which takes as input some input tensors and returns as output some
output tensors. The computation that the function performs is encoded in the
operations of the subgraph.

The tensors (input or output) can be of two kinds:

- connected: a connected tensor connects to at least one operation contained
in the subgraph. One example is a subgraph representing a single operation
and its inputs and outputs: all the input and output tensors of the op
are "connected".
- passthrough: a passthrough tensor does not connect to any operation
contained in the subgraph. One example is a subgraph representing a
single tensor: this tensor is passthrough. By default a passthrough tensor is
present both in the input and output tensors of the subgraph. It can however
be remapped to only appear as an input (or output) only.

The input and output tensors can be remapped. For instance, some input tensor
can be omitted. For instance, a subgraph representing an operation with two
inputs can be remapped to only take one input. Note that this does not change
at all the underlying `tf.Graph` (remember, it is a view). It means that
the other input is being ignored, or is being treated as "given".
The analogy with functions can be extended like this: F(x,y) is the original
function. Remapping the inputs from [x, y] to just [x] means that the subgraph
now represent the function F_y(x) (y is "given").

The output tensors can also be remapped. For instance, some output tensor can
be omitted. Other output tensor can be duplicated as well. As mentioned
before, this does not change at all the underlying `tf.Graph`.
The analogy with functions can be extended like this: F(...)->x,y is the
original function. Remapping the outputs from [x, y] to just [y,y] means that
the subgraph now represent the function M(F(...)) where M is the function
M(a,b)->b,b.

It is useful to describe three other kind of tensors:

* internal: an internal tensor is a tensor connecting operations contained
  in the subgraph. One example in the subgraph representing the two
  operations A and B connected sequentially: -> A -> B ->. The middle arrow
  is an internal tensor.
* actual input: an input tensor of the subgraph, regardless of whether it is
  listed in "inputs" or not (masked-out).
* actual output: an output tensor of the subgraph, regardless of whether it is
  listed in "outputs" or not (masked-out).
* hidden input: an actual input which has been masked-out using an
  input remapping. In other word, a hidden input is a non-internal tensor
  not listed as a input tensor and one of whose consumers belongs to
  the subgraph.
* hidden output: a actual output which has been masked-out using an output
  remapping. In other word, a hidden output is a non-internal tensor
  not listed as an output and one of whose generating operations belongs to
  the subgraph.

Here are some useful guarantees about an instance of a SubGraphView:

* the input (or output) tensors are not internal.
* the input (or output) tensors are either "connected" or "passthrough".
* the passthrough tensors are not connected to any of the operation of
the subgraph.

Note that there is no guarantee that an operation in a subgraph contributes
at all to its inputs or outputs. For instance, remapping both the inputs and
outputs to empty lists will produce a subgraph which still contains all the
original operations. However, the remove_unused_ops function can be used to
make a new subgraph view whose operations are connected to at least one of
the input or output tensors.

An instance of this class is meant to be a lightweight object which is not
modified in-place by the user. Rather, the user can create new modified
instances of a given subgraph. In that sense, the class SubGraphView is meant
to be used like an immutable python object.

A common problem when using views is that they can get out-of-sync with the
data they observe (in this case, a `tf.Graph`). This is up to the user to
ensure that this doesn't happen. To keep on the safe side, it is recommended
that the life time of subgraph views are kept very short. One way to achieve
this is to use subgraphs within a "with make_sgv(...) as sgv:" Python context.

To alleviate the out-of-sync problem, some functions are granted the right to
modified subgraph in place. This is typically the case of graph manipulation
functions which, given some subgraphs as arguments, can modify the underlying
`tf.Graph`. Since this modification is likely to render the subgraph view
invalid, those functions can modify the argument in place to reflect the
change. For instance, calling the function swap_inputs(svg0, svg1) will modify
svg0 and svg1 in place to reflect the fact that their inputs have now being
swapped.

## Properties

<h3 id="connected_inputs"><code>connected_inputs</code></h3>

The connected input tensors of this subgraph view.

<h3 id="connected_outputs"><code>connected_outputs</code></h3>

The connected output tensors of this subgraph view.

<h3 id="graph"><code>graph</code></h3>

The underlying `tf.Graph`.

<h3 id="inputs"><code>inputs</code></h3>

The input tensors of this subgraph view.

<h3 id="ops"><code>ops</code></h3>

The operations in this subgraph view.

<h3 id="outputs"><code>outputs</code></h3>

The output tensors of this subgraph view.

<h3 id="passthroughs"><code>passthroughs</code></h3>

The passthrough tensors, going straight from input to output.



## Methods

<h3 id="__init__"><code>__init__(inside_ops=(), passthrough_ts=())</code></h3>

Create a subgraph containing the given ops and the "passthrough" tensors.

#### Args:

* <b>`inside_ops`</b>: an object convertible to a list of `tf.Operation`. This list
    defines all the operations in the subgraph.
* <b>`passthrough_ts`</b>: an object convertible to a list of `tf.Tensor`. This list
    define all the "passthrough" tensors. A passthrough tensor is a tensor
    which goes directly from the input of the subgraph to it output, without
    any intermediate operations. All the non passthrough tensors are
    silently ignored.
Raises:
* <b>`TypeError`</b>: if inside_ops cannot be converted to a list of `tf.Operation`
    or if `passthrough_ts` cannot be converted to a list of `tf.Tensor`.

<h3 id="consumers"><code>consumers()</code></h3>

Return a Python set of all the consumers of this subgraph view.

A consumer of a subgraph view is a tf.Operation which is a consumer
of one of the output tensors and is not in the subgraph.

#### Returns:

  A list of `tf.Operation` which are the consumers of this subgraph view.

<h3 id="copy"><code>copy()</code></h3>

Return a copy of itself.

Note that this class is a "view", copying it only create another view and
does not copy the underlying part of the tf.Graph.

#### Returns:

  A new instance identical to the original one.

<h3 id="find_op_by_name"><code>find_op_by_name(op_name)</code></h3>

Return the op named op_name.

#### Args:

* <b>`op_name`</b>: the name to search for
Returns:
  The op named op_name.
Raises:
* <b>`ValueError`</b>: if the op_name could not be found.
* <b>`AssertionError`</b>: if the name was found multiple time.

<h3 id="input_index"><code>input_index(t)</code></h3>

Find the input index corresponding to the given input tensor t.

#### Args:

* <b>`t`</b>: the input tensor of this subgraph view.
Returns:
  The index in the self.inputs list.
Raises:
* <b>`Error`</b>: if t in not an input tensor.

<h3 id="is_passthrough"><code>is_passthrough(t)</code></h3>

Check whether a tensor is passthrough.

<h3 id="op"><code>op(op_id)</code></h3>

Get an op by its index.

<h3 id="output_index"><code>output_index(t)</code></h3>

Find the output index corresponding to given output tensor t.

#### Args:

* <b>`t`</b>: the output tensor of this subgraph view.
Returns:
  The index in the self.outputs list.
Raises:
* <b>`Error`</b>: if t in not an output tensor.

<h3 id="remap"><code>remap(new_input_indices=None, new_output_indices=None)</code></h3>

Remap the inputs and outputs of the subgraph.

Note that this is only modifying the view: the underlying tf.Graph is not
affected.

#### Args:

* <b>`new_input_indices`</b>: an iterable of integers representing a mapping between
    the old inputs and the new ones. This mapping can be under-complete and
    must be without repetitions.
* <b>`new_output_indices`</b>: an iterable of integers representing a mapping between
    the old outputs and the new ones. This mapping can be under-complete and
    can have repetitions.
Returns:
  A new modified instance of the original subgraph view with remapped
    inputs and outputs.

<h3 id="remap_default"><code>remap_default(remove_input_map=True, remove_output_map=True)</code></h3>

Remap the inputs and/or outputs to the default mapping.

#### Args:

* <b>`remove_input_map`</b>: if True the input map is reset to the default one.
* <b>`remove_output_map`</b>: if True the output map is reset to the default one.
Returns:
  A new modified instance of the original subgraph view with its
    input and/or output mapping reset to the default one.

<h3 id="remap_inputs"><code>remap_inputs(new_input_indices)</code></h3>

Remap the inputs of the subgraph.

If the inputs of the original subgraph are [t0, t1, t2], remapping to [2,0]
will create a new instance whose inputs is [t2, t0].

Note that this is only modifying the view: the underlying `tf.Graph` is not
affected.

#### Args:

* <b>`new_input_indices`</b>: an iterable of integers representing a mapping between
    the old inputs and the new ones. This mapping can be under-complete and
    must be without repetitions.
Returns:
  A new modified instance of the original subgraph view with remapped
    inputs.

<h3 id="remap_outputs"><code>remap_outputs(new_output_indices)</code></h3>

Remap the output of the subgraph.

If the output of the original subgraph are [t0, t1, t2], remapping to
[1,1,0] will create a new instance whose outputs is [t1, t1, t0].

Note that this is only modifying the view: the underlying tf.Graph is not
affected.

#### Args:

* <b>`new_output_indices`</b>: an iterable of integers representing a mapping between
    the old outputs and the new ones. This mapping can be under-complete and
    can have repetitions.
Returns:
  A new modified instance of the original subgraph view with remapped
    outputs.

<h3 id="remap_outputs_make_unique"><code>remap_outputs_make_unique()</code></h3>

Remap the outputs so that all the tensors appears only once.

<h3 id="remap_outputs_to_consumers"><code>remap_outputs_to_consumers()</code></h3>

Remap the outputs to match the number of consumers.

<h3 id="remove_unused_ops"><code>remove_unused_ops(control_inputs=True)</code></h3>

Remove unused ops.

#### Args:

* <b>`control_inputs`</b>: if True, control inputs are used to detect used ops.
Returns:
  A new subgraph view which only contains used operations.





Defined in [`tensorflow/contrib/graph_editor/subgraph.py`](https://www.tensorflow.org/code/tensorflow/contrib/graph_editor/subgraph.py).

