

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.deprecated.histogram_summary

``` python
tf.contrib.deprecated.histogram_summary(
    tag,
    values,
    collections=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/logging_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/logging_ops.py).

Outputs a `Summary` protocol buffer with a histogram. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2016-11-30.
Instructions for updating:
Please switch to tf.summary.histogram. Note that tf.summary.histogram uses the node name instead of the tag. This means that TensorFlow will automatically de-duplicate summary names based on the scope they are created in.

This ops is deprecated. Please switch to tf.summary.histogram.

For an explanation of why this op was deprecated, and information on how to
migrate, look ['here'](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/deprecated/__init__.py)

The generated
[`Summary`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/core/framework/summary.proto)
has one summary value containing a histogram for `values`.

This op reports an `InvalidArgument` error if any value is not finite.

#### Args:

* <b>`tag`</b>: A `string` `Tensor`. 0-D.  Tag to use for the summary value.
* <b>`values`</b>: A real numeric `Tensor`. Any shape. Values to use to
    build the histogram.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
    added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.