page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.deprecated.merge_summary

Merges summaries. (deprecated)

``` python
tf.contrib.deprecated.merge_summary(
    inputs,
    collections=None,
    name=None
)
```



Defined in [`python/ops/logging_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/logging_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-11-30.
Instructions for updating:
Please switch to tf.summary.merge.

This op is deprecated. Please switch to tf.compat.v1.summary.merge, which has
identical
behavior.

This op creates a
[`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
protocol buffer that contains the union of all the values in the input
summaries.

When the Op is run, it reports an `InvalidArgument` error if multiple values
in the summaries to merge use the same tag.

#### Args:


* <b>`inputs`</b>: A list of `string` `Tensor` objects containing serialized `Summary`
  protocol buffers.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
  added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer resulting from the merging.
