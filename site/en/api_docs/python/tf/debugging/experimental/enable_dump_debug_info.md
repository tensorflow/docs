description: Enable dumping debugging information from a TensorFlow program.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.experimental.enable_dump_debug_info" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.experimental.enable_dump_debug_info

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/debug/lib/dumping_callback.py#L686-L874">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enable dumping debugging information from a TensorFlow program.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.experimental.enable_dump_debug_info`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.debugging.experimental.enable_dump_debug_info(
    dump_root, tensor_debug_mode=DEFAULT_TENSOR_DEBUG_MODE,
    circular_buffer_size=1000, op_regex=None, tensor_dtypes=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The debugging information is dumped to a directory on the file system
specified as `dump_root`.

The dumped debugging information can be ingested by debugger UIs.

The files in the dump directory contain the following information:
  - TensorFlow Function construction (e.g., compilation of Python functions
    decorated with @tf.function), the op types, names (if available), context,
    the input and output tensors, and the associated stack traces.
  - Execution of TensorFlow operations (ops) and Functions and their stack
    traces, op types, names (if available) and contexts. In addition,
    depending on the value of the `tensor_debug_mode` argument (see Args
    section below), the value(s) of the output tensors or more concise
    summaries of the tensor values will be dumped.
  - A snapshot of Python source files involved in the execution of the
    TensorFlow program.

Once enabled, the dumping can be disabled with the corresponding
`disable_dump_debug_info()` method under the same Python namespace.
Calling this method more than once with the same `dump_root` is idempotent.
Calling this method more than once with different `tensor_debug_mode`s
leads to a `ValueError`.
Calling this method more than once with different `circular_buffer_size`s
leads to a `ValueError`.
Calling this method with a different `dump_root` abolishes the
previously-enabled `dump_root`.

#### Usage example:



```py
tf.debugging.experimental.enable_dump_debug_info('/tmp/my-tfdbg-dumps')

# Code to build, train and run your TensorFlow model...
```

NOTE: If your code is running on TPUs, be sure to call
<a href="../../../tf/config/set_soft_device_placement.md"><code>tf.config.set_soft_device_placement(True)</code></a> before calling
<a href="../../../tf/debugging/experimental/enable_dump_debug_info.md"><code>tf.debugging.experimental.enable_dump_debug_info()</code></a> as this API uses
automatic outside compilation on TPUs. For example:

```py
tf.config.set_soft_device_placement(True)
tf.debugging.experimental.enable_dump_debug_info(
    logdir, tensor_debug_mode="FULL_HEALTH")

resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
strategy = tf.distribute.TPUStrategy(resolver)
with strategy.scope():
  # ...
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dump_root`
</td>
<td>
The directory path where the dumping information will be written.
</td>
</tr><tr>
<td>
`tensor_debug_mode`
</td>
<td>
Debug mode for tensor values, as a string.
The currently supported options are:
- "NO_TENSOR": (Default) Only traces the output tensors of all executed
ops (including those executed eagerly at the Python level or as a part
of a TensorFlow graph) and functions, while not extracting any
information from the values of the tensors.
- "CURT_HEALTH": For each floating-dtype tensor (e.g., tensors of dtypes
such as `float32`, `float64` and `bfloat16`), extracts a binary bit
indicating whether it contains any -infinity, +infinity or NaN.
- "CONCISE_HEALTH": For each floating-dtype tensor, extract total
element count, and counts of -infinity, +infinity and NaN elements.
- "FULL_HEALTH": For each floating-dtype tensor, extracts the dtype,
rank (number of dimensions), total element count, and counts of
-infinity, +infinity and NaN elements.
- "SHAPE": For each tensor (regardless of dtype), extracts its dtype,
rank, total element count and shape.
</td>
</tr><tr>
<td>
`circular_buffer_size`
</td>
<td>
Size of the circular buffers for execution events.
These circular buffers are designed to reduce the overhead of debugging
dumping. They hold the most recent debug events concerning eager execution
of ops and <a href="../../../tf/function.md"><code>tf.function</code></a>s and traces of tensor values computed inside
<a href="../../../tf/function.md"><code>tf.function</code></a>s. They are written to the file system only when the proper
flushing method is called (see description of return values below).
Expected to be an integer. If <= 0, the circular-buffer behavior will be
disabled, i.e., the execution debug events will be written to the file
writers in the same way as non-execution events such as op creations and
source-file snapshots.
</td>
</tr><tr>
<td>
`op_regex`
</td>
<td>
Dump data from only the tensors from op types that matches to the
regular expression (through Python's `re.match()`).
"Op type" refers to the names of the TensorFlow operations (e.g.,
"MatMul", "LogSoftmax"), which may repeat in a TensorFlow
function. It does *not* refer to the names of nodes (e.g.,
"dense/MatMul", "dense_1/MatMul_1") which are unique within a function.
- Example 1: Dump tensor data from only MatMul and Relu ops
`op_regex="^(MatMul|Relu)$"`.
- Example 2: Dump tensors from all ops *except* Relu:
`op_regex="(?!^Relu$)"`.
This filter operates in a logical AND relation with `tensor_dtypes`.
</td>
</tr><tr>
<td>
`tensor_dtypes`
</td>
<td>
Dump data from only the tensors of which the specified
dtypes. This optional argument can be in any of the following format:
- a list or tuple of `DType` objects or strings that can be converted
to `DType` objects via <a href="../../../tf/dtypes/as_dtype.md"><code>tf.as_dtype()</code></a>. Examples:
- `tensor_dtype=[tf.float32, tf.float64]`,
- `tensor_dtype=["float32", "float64"]`,
- `tensor_dtypes=(tf.int32, tf.bool)`,
- `tensor_dtypes=("int32", "bool")`
- a callable that takes a single `DType` argument and returns a Python
`boolean` indicating whether the dtype is to be included in the data
dumping. Examples:
- `tensor_dtype=lambda dtype: dtype.is_integer`.
This filter operates in a logical AND relation with `op_regex`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A DebugEventsWriter instance used by the dumping callback. The caller
may use its flushing methods, including `FlushNonExecutionFiles()` and
`FlushExecutionFiles()`.
</td>
</tr>

</table>

