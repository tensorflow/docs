

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.watch_graph

``` python
tfdbg.watch_graph(
    run_options,
    graph,
    debug_ops='DebugIdentity',
    debug_urls=None,
    node_name_regex_whitelist=None,
    op_type_regex_whitelist=None,
    tensor_dtype_regex_whitelist=None,
    tolerate_debug_op_creation_failures=False,
    global_step=-1
)
```



Defined in [`tensorflow/python/debug/lib/debug_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/debug/lib/debug_utils.py).

See the guide: [TensorFlow Debugger > Functions for adding debug watches](../../../api_guides/python/tfdbg#Functions_for_adding_debug_watches)

Add debug watches to `RunOptions` for a TensorFlow graph.

To watch all `Tensor`s on the graph, let both `node_name_regex_whitelist`
and `op_type_regex_whitelist` be the default (`None`).

N.B.:
  1. Under certain circumstances, the `Tensor` may not get actually watched
    (e.g., if the node of the `Tensor` is constant-folded during runtime).
  2. For debugging purposes, the `parallel_iteration` attribute of all
    <a href="../tf/while_loop"><code>tf.while_loop</code></a>s in the graph are set to 1 to prevent any node from
    being executed multiple times concurrently. This change does not affect
    subsequent non-debugged runs of the same <a href="../tf/while_loop"><code>tf.while_loop</code></a>s.


#### Args:

* <b>`run_options`</b>: An instance of `config_pb2.RunOptions` to be modified.
* <b>`graph`</b>: An instance of `ops.Graph`.
* <b>`debug_ops`</b>: (`str` or `list` of `str`) name(s) of the debug op(s) to use.
* <b>`debug_urls`</b>: URLs to send debug values to. Can be a list of strings,
    a single string, or None. The case of a single string is equivalent to
    a list consisting of a single string, e.g., `file:///tmp/tfdbg_dump_1`,
    `grpc://localhost:12345`.
    For debug op types with customizable attributes, each debug op name string
    can optionally contain a list of attribute names, in the syntax of:
      debug_op_name(attr_name_1=attr_value_1;attr_name_2=attr_value_2;...)
* <b>`node_name_regex_whitelist`</b>: Regular-expression whitelist for node_name,
    e.g., `"(weight_[0-9]+|bias_.*)"`
* <b>`op_type_regex_whitelist`</b>: Regular-expression whitelist for the op type of
    nodes, e.g., `"(Variable|Add)"`.
    If both `node_name_regex_whitelist` and `op_type_regex_whitelist`
    are set, the two filtering operations will occur in a logical `AND`
    relation. In other words, a node will be included if and only if it
    hits both whitelists.
* <b>`tensor_dtype_regex_whitelist`</b>: Regular-expression whitelist for Tensor
    data type, e.g., `"^int.*"`.
    This whitelist operates in logical `AND` relations to the two whitelists
    above.
* <b>`tolerate_debug_op_creation_failures`</b>: (`bool`) whether debug op creation
    failures (e.g., due to dtype incompatibility) are to be tolerated by not
    throwing exceptions.
* <b>`global_step`</b>: (`int`) Optional global_step count for this debug tensor
    watch.