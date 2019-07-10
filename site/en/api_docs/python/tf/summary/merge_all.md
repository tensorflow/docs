page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.merge_all

Merges all summaries collected in the default graph.

### Aliases:

* `tf.compat.v1.summary.merge_all`
* `tf.summary.merge_all`

``` python
tf.summary.merge_all(
    key=tf.GraphKeys.SUMMARIES,
    scope=None,
    name=None
)
```



Defined in [`python/summary/summary.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/summary/summary.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`key`</b>: `GraphKey` used to collect the summaries.  Defaults to
  <a href="../../tf/GraphKeys#SUMMARIES"><code>GraphKeys.SUMMARIES</code></a>.
* <b>`scope`</b>: Optional scope used to filter the summary ops, using `re.match`


#### Returns:

If no summaries were collected, returns None.  Otherwise returns a scalar
`Tensor` of type `string` containing the serialized `Summary` protocol
buffer resulting from the merging.



#### Raises:


* <b>`RuntimeError`</b>: If called with eager execution enabled.



#### Eager Compatibility
Not compatible with eager execution. To write TensorBoard
summaries under eager execution, use <a href="../../tf/contrib/summary"><code>tf.contrib.summary</code></a> instead.

