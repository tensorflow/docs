page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.deprecated.scalar_summary


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/logging_ops.py#L644-L677">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Outputs a `Summary` protocol buffer with scalar values. (deprecated)

``` python
tf.contrib.deprecated.scalar_summary(
    tags,
    values,
    collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-11-30.
Instructions for updating:
Please switch to tf.summary.scalar. Note that tf.summary.scalar uses the node name instead of the tag. This means that TensorFlow will automatically de-duplicate summary names based on the scope they are created in. Also, passing a tensor or list of tags to a scalar summary op is no longer supported.

This ops is deprecated. Please switch to tf.summary.scalar.
For an explanation of why this op was deprecated, and information on how to
migrate, look
['here'](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/deprecated/__init__.py)

The input `tags` and `values` must have the same shape.  The generated
summary has a summary value for each tag-value pair in `tags` and `values`.

#### Args:


* <b>`tags`</b>: A `string` `Tensor`.  Tags for the summaries.
* <b>`values`</b>: A real numeric Tensor.  Values for the summaries.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
  added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.
