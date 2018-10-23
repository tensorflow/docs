

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.summary.get_summary_description

``` python
tf.summary.get_summary_description(node_def)
```



Defined in [`tensorflow/python/summary/summary.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/summary/summary.py).

See the guide: [Summary Operations > Utilities](../../../../api_guides/python/summary#Utilities)

Given a TensorSummary node_def, retrieve its SummaryDescription.

When a Summary op is instantiated, a SummaryDescription of associated
metadata is stored in its NodeDef. This method retrieves the description.

#### Args:

* <b>`node_def`</b>: the node_def_pb2.NodeDef of a TensorSummary op


#### Returns:

a summary_pb2.SummaryDescription


#### Raises:

* <b>`ValueError`</b>: if the node is not a summary op.

@compatibility(eager)
Not compatible with eager execution. To write TensorBoard
summaries under eager execution, use `tf.contrib.summary` instead.
@end_compatbility