page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.all_v2_summary_ops

Returns all V2-style summary ops defined in the current default graph.

### Aliases:

* `tf.compat.v1.summary.all_v2_summary_ops`
* `tf.contrib.summary.all_summary_ops`
* `tf.summary.all_v2_summary_ops`

``` python
tf.summary.all_v2_summary_ops()
```



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->

This includes ops from TF 2.0 tf.summary and TF 1.x tf.contrib.summary (except
for <a href="../../tf/contrib/summary/graph"><code>tf.contrib.summary.graph</code></a> and <a href="../../tf/contrib/summary/import_event"><code>tf.contrib.summary.import_event</code></a>), but
does *not* include TF 1.x tf.summary ops.

#### Returns:

List of summary ops, or None if called under eager execution.
