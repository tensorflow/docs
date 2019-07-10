page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.deprecated.merge_all_summaries

Merges all summaries collected in the default graph. (deprecated)

``` python
tf.contrib.deprecated.merge_all_summaries(key=tf.GraphKeys.SUMMARIES)
```



Defined in [`python/ops/logging_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/logging_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-11-30.
Instructions for updating:
Please switch to tf.summary.merge_all.

This op is deprecated. Please switch to tf.compat.v1.summary.merge_all, which
has
identical behavior.

#### Args:


* <b>`key`</b>: `GraphKey` used to collect the summaries.  Defaults to
  `GraphKeys.SUMMARIES`.


#### Returns:

If no summaries were collected, returns None.  Otherwise returns a scalar
`Tensor` of type `string` containing the serialized `Summary` protocol
buffer resulting from the merging.
