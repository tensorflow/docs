

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.deprecated.merge_all_summaries

``` python
merge_all_summaries(key=tf.GraphKeys.SUMMARIES)
```



Defined in [`tensorflow/python/ops/logging_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/logging_ops.py).

Merges all summaries collected in the default graph. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2016-11-30.
Instructions for updating:
Please switch to tf.summary.merge_all.

This op is deprecated. Please switch to tf.summary.merge_all, which has
identical behavior.

#### Args:

* <b>`key`</b>: `GraphKey` used to collect the summaries.  Defaults to
    `GraphKeys.SUMMARIES`.


#### Returns:

If no summaries were collected, returns None.  Otherwise returns a scalar
`Tensor` of type `string` containing the serialized `Summary` protocol
buffer resulting from the merging.