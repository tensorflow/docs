page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.merge

Merges summaries.

### Aliases:

* `tf.compat.v1.summary.merge`
* `tf.summary.merge`

``` python
tf.summary.merge(
    inputs,
    collections=None,
    name=None
)
```



Defined in [`python/summary/summary.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/summary/summary.py).

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
summaries under eager execution, use <a href="../../tf/contrib/summary"><code>tf.contrib.summary</code></a> instead.

