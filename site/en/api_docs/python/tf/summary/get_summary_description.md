page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.get_summary_description

Given a TensorSummary node_def, retrieve its SummaryDescription.

### Aliases:

* `tf.compat.v1.summary.get_summary_description`
* `tf.summary.get_summary_description`

``` python
tf.summary.get_summary_description(node_def)
```



Defined in [`python/summary/summary.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/summary/summary.py).

<!-- Placeholder for "Used in" -->

When a Summary op is instantiated, a SummaryDescription of associated
metadata is stored in its NodeDef. This method retrieves the description.

#### Args:


* <b>`node_def`</b>: the node_def_pb2.NodeDef of a TensorSummary op


#### Returns:

a summary_pb2.SummaryDescription



#### Raises:


* <b>`ValueError`</b>: if the node is not a summary op.



#### Eager Compatibility
Not compatible with eager execution. To write TensorBoard
summaries under eager execution, use <a href="../../tf/contrib/summary"><code>tf.contrib.summary</code></a> instead.

