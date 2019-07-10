page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.initialize

Initializes summary writing for graph execution mode.

### Aliases:

* `tf.compat.v1.summary.initialize`
* `tf.contrib.summary.initialize`
* `tf.summary.initialize`

``` python
tf.summary.initialize(
    graph=None,
    session=None
)
```



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->

This operation is a no-op when executing eagerly.

This helper method provides a higher-level alternative to using
<a href="../../tf/contrib/summary/summary_writer_initializer_op"><code>tf.contrib.summary.summary_writer_initializer_op</code></a> and
<a href="../../tf/contrib/summary/graph"><code>tf.contrib.summary.graph</code></a>.

Most users will also want to call <a href="../../tf/train/create_global_step"><code>tf.compat.v1.train.create_global_step</code></a>
which can happen before or after this function is called.

#### Args:


* <b>`graph`</b>: A <a href="../../tf/Graph"><code>tf.Graph</code></a> or <a href="../../tf/GraphDef"><code>tf.compat.v1.GraphDef</code></a> to output to the writer.
  This function will not write the default graph by default. When
  writing to an event log file, the associated step will be zero.
* <b>`session`</b>: So this method can call <a href="../../tf/Session#run"><code>tf.Session.run</code></a>. This defaults
  to <a href="../../tf/get_default_session"><code>tf.compat.v1.get_default_session</code></a>.


#### Raises:


* <b>`RuntimeError`</b>: If  the current thread has no default
  <a href="../../tf/compat/v2/summary/SummaryWriter"><code>tf.contrib.summary.SummaryWriter</code></a>.
* <b>`ValueError`</b>: If session wasn't passed and no default session.