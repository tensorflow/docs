page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.add_debug_tensor_watch

``` python
tfdbg.add_debug_tensor_watch(
    run_options,
    node_name,
    output_slot=0,
    debug_ops='DebugIdentity',
    debug_urls=None,
    tolerate_debug_op_creation_failures=False,
    global_step=-1
)
```



Defined in [`tensorflow/python/debug/lib/debug_utils.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/debug/lib/debug_utils.py).

Add watch on a `Tensor` to `RunOptions`.

N.B.:
  1. Under certain circumstances, the `Tensor` may not get actually watched
    (e.g., if the node of the `Tensor` is constant-folded during runtime).
  2. For debugging purposes, the `parallel_iteration` attribute of all
    <a href="../tf/while_loop"><code>tf.while_loop</code></a>s in the graph are set to 1 to prevent any node from
    being executed multiple times concurrently. This change does not affect
    subsequent non-debugged runs of the same <a href="../tf/while_loop"><code>tf.while_loop</code></a>s.

#### Args:

* <b>`run_options`</b>: An instance of `config_pb2.RunOptions` to be modified.
* <b>`node_name`</b>: (`str`) name of the node to watch.
* <b>`output_slot`</b>: (`int`) output slot index of the tensor from the watched node.
* <b>`debug_ops`</b>: (`str` or `list` of `str`) name(s) of the debug op(s). Can be a
    `list` of `str` or a single `str`. The latter case is equivalent to a
    `list` of `str` with only one element.
    For debug op types with customizable attributes, each debug op string can
    optionally contain a list of attribute names, in the syntax of:
      debug_op_name(attr_name_1=attr_value_1;attr_name_2=attr_value_2;...)
* <b>`debug_urls`</b>: (`str` or `list` of `str`) URL(s) to send debug values to,
    e.g., `file:///tmp/tfdbg_dump_1`, `grpc://localhost:12345`.
* <b>`tolerate_debug_op_creation_failures`</b>: (`bool`) Whether to tolerate debug op
    creation failures by not throwing exceptions.
* <b>`global_step`</b>: (`int`) Optional global_step count for this debug tensor
    watch.