page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.reconstruct_non_debug_graph_def

``` python
tfdbg.reconstruct_non_debug_graph_def(debug_graph_def)
```



Defined in [`tensorflow/python/debug/lib/debug_graphs.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/debug/lib/debug_graphs.py).

Reconstruct original (non-debugger-decorated) partition GraphDef.

This method strips the input <a href="../tf/GraphDef"><code>tf.GraphDef</code></a> of the Copy* and Debug*-type nodes
inserted by the debugger.

The reconstructed partition graph is identical to the original (i.e.,
  non-debugger-decorated) partition graph except in the following respects:
    1) The exact names of the runtime-inserted internal nodes may differ.
       These include _Send, _Recv, _HostSend, _HostRecv, _Retval ops.
    2) As a consequence of 1, the nodes that receive input directly from such
       send- and recv-type ops will have different input names.
    3) The parallel_iteration attribute of while-loop Enter ops are set to 1.

#### Args:

* <b>`debug_graph_def`</b>: The debugger-decorated <a href="../tf/GraphDef"><code>tf.GraphDef</code></a>, with the
    debugger-inserted Copy* and Debug* nodes.


#### Returns:

The reconstructed <a href="../tf/GraphDef"><code>tf.GraphDef</code></a> stripped of the debugger-inserted nodes.