page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.graph

``` python
tf.contrib.summary.graph(
    param,
    step=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/summary_ops_v2.py).

Writes a TensorFlow graph to the summary interface.

The graph summary is, strictly speaking, not a summary. Conditions
like <a href="../../../tf/contrib/summary/never_record_summaries"><code>tf.contrib.summary.never_record_summaries</code></a> do not apply. Only
a single graph can be associated with a particular run. If multiple
graphs are written, then only the last one will be considered by
TensorBoard.

When not using eager execution mode, the user should consider passing
the `graph` parameter to <a href="../../../tf/contrib/summary/initialize"><code>tf.contrib.summary.initialize</code></a> instead of
calling this function. Otherwise special care needs to be taken when
using the graph to record the graph.

#### Args:

* <b>`param`</b>: A <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> containing a serialized graph proto. When
    eager execution is enabled, this function will automatically
    coerce <a href="../../../tf/Graph"><code>tf.Graph</code></a>, <a href="../../../tf/GraphDef"><code>tf.GraphDef</code></a>, and string types.
* <b>`step`</b>: The global step variable. This doesn't have useful semantics
    for graph summaries, but is used anyway, due to the structure of
    event log files. This defaults to the global step.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created <a href="../../../tf/Operation"><code>tf.Operation</code></a> or a <a href="../../../tf/no_op"><code>tf.no_op</code></a> if summary writing has
not been enabled for this context.


#### Raises:

* <b>`TypeError`</b>: If `param` isn't already a <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> in graph mode.