

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tfdbg.watch_graph_with_blacklists

``` python
tfdbg.watch_graph_with_blacklists(
    run_options,
    graph,
    debug_ops='DebugIdentity',
    debug_urls=None,
    node_name_regex_blacklist=None,
    op_type_regex_blacklist=None,
    tensor_dtype_regex_blacklist=None,
    tolerate_debug_op_creation_failures=False,
    global_step=-1
)
```



Defined in [`tensorflow/python/debug/lib/debug_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/debug/lib/debug_utils.py).

See the guide: [TensorFlow Debugger > Functions for adding debug watches](../../../api_guides/python/tfdbg#Functions_for_adding_debug_watches)

Add debug tensor watches, blacklisting nodes and op types.

This is similar to `watch_graph()`, but the node names and op types are
blacklisted, instead of whitelisted.

N.B.:
  1. Under certain circumstances, the `Tensor` may not get actually watched
    (e.g., if the node of the `Tensor` is constant-folded during runtime).
  2. For debugging purposes, the `parallel_iteration` attribute of all
    `tf.while_loop`s in the graph are set to 1 to prevent any node from
    being executed multiple times concurrently. This change does not affect
    subsequent non-debugged runs of the same `tf.while_loop`s.

#### Args:

* <b>`run_options`</b>: An instance of `config_pb2.RunOptions` to be modified.
* <b>`graph`</b>: An instance of `ops.Graph`.
* <b>`debug_ops`</b>: (`str` or `list` of `str`) name(s) of the debug op(s) to use.
    See the documentation of `watch_graph` for more details.
* <b>`debug_urls`</b>: URL(s) to send debug values to, e.g.,
    `file:///tmp/tfdbg_dump_1`, `grpc://localhost:12345`.
* <b>`node_name_regex_blacklist`</b>: Regular-expression blacklist for node_name.
    This should be a string, e.g., `"(weight_[0-9]+|bias_.*)"`.
* <b>`op_type_regex_blacklist`</b>: Regular-expression blacklist for the op type of
    nodes, e.g., `"(Variable|Add)"`.
    If both node_name_regex_blacklist and op_type_regex_blacklist
    are set, the two filtering operations will occur in a logical `OR`
    relation. In other words, a node will be excluded if it hits either of
    the two blacklists; a node will be included if and only if it hits
    neither of the blacklists.
* <b>`tensor_dtype_regex_blacklist`</b>: Regular-expression blacklist for Tensor
    data type, e.g., `"^int.*"`.
    This blacklist operates in logical `OR` relations to the two whitelists
    above.
* <b>`tolerate_debug_op_creation_failures`</b>: (`bool`) whether debug op creation
    failures (e.g., due to dtype incompatibility) are to be tolerated by not
    throwing exceptions.
* <b>`global_step`</b>: (`int`) Optional global_step count for this debug tensor
    watch.