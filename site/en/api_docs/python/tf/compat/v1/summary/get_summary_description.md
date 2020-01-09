page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.summary.get_summary_description


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/summary.py#L409-L436">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Given a TensorSummary node_def, retrieve its SummaryDescription.

``` python
tf.compat.v1.summary.get_summary_description(node_def)
```



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
summaries under eager execution, use `tf.contrib.summary` instead.
