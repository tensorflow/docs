


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.graph_editor.ControlOutputs

### `class tf.contrib.graph_editor.ControlOutputs`

See the guide: [Graph Editor (contrib) > Module: util](../../../../../api_guides/python/contrib.graph_editor#Module_util)

The control outputs topology.

## Properties

<h3 id="graph"><code>graph</code></h3>





## Methods

<h3 id="__init__"><code>__init__(graph)</code></h3>

Create a dictionary of control-output dependencies.

#### Args:

* <b>`graph`</b>: a `tf.Graph`.
Returns:
  A dictionary where a key is a `tf.Operation` instance and the
     corresponding value is a list of all the ops which have the key
     as one of their control-input dependencies.
Raises:
* <b>`TypeError`</b>: graph is not a `tf.Graph`.

<h3 id="get"><code>get(op)</code></h3>

return the control outputs of op.

<h3 id="get_all"><code>get_all()</code></h3>



<h3 id="update"><code>update()</code></h3>

Update the control outputs if the graph has changed.





Defined in [`tensorflow/contrib/graph_editor/util.py`](https://www.tensorflow.org/code/tensorflow/contrib/graph_editor/util.py).

