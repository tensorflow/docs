page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.summary.merge


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/summary.py#L330-L373">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Merges summaries.

``` python
tf.compat.v1.summary.merge(
    inputs,
    collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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
  added to these collections. Defaults to `[]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer resulting from the merging.



#### Raises:


* <b>`RuntimeError`</b>: If called with eager mode enabled.



#### Eager Compatibility
Not compatible with eager execution. To write TensorBoard
summaries under eager execution, use `tf.contrib.summary` instead.
