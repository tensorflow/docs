


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.graph_editor.Transformer

### `class tf.contrib.graph_editor.Transformer`

See the guide: [Graph Editor (contrib) > Module: transform](../../../../../api_guides/python/contrib.graph_editor#Module_transform)

Transform a subgraph into another one.

By default, the constructor create a transform which copy a subgraph and
replaces inputs with placeholders. This behavior can be modified by changing
the handlers.

## Methods

<h3 id="__init__"><code>__init__()</code></h3>

Transformer constructor.

The following members can be modified:
transform_op_handler: handle the transformation of a `tf.Operation`.
  This handler defaults to a simple copy.
assign_collections_handler: handle the assignment of collections.
  This handler defaults to assigning new collections created under the
  given name-scope.
transform_external_input_handler: handle the transform of the inputs to
  the given subgraph. This handler defaults to creating placeholders
  instead of the ops just before the input tensors of the subgraph.
transform_external_hidden_input_handler: handle the transform of the
  hidden inputs of the subgraph, that is, the inputs which are not listed
  in sgv.inputs. This handler defaults to a transform which keep the same
  input if the source and destination graphs are the same, otherwise
  use placeholders.
transform_original_op_handler: handle the transform of original_op. This
  handler defaults to transforming original_op only if they are in the
  subgraph, otherwise they are ignored.





Defined in [`tensorflow/contrib/graph_editor/transform.py`](https://www.tensorflow.org/code/tensorflow/contrib/graph_editor/transform.py).

