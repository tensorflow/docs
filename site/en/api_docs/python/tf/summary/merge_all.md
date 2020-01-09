page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.merge_all

``` python
tf.summary.merge_all(
    key=tf.GraphKeys.SUMMARIES,
    scope=None,
    name=None
)
```



Defined in [`tensorflow/python/summary/summary.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/summary/summary.py).

See the guide: [Upgrade to TensorFlow 1.0 > Upgrading your code manually](../../../../api_guides/python/upgrade#Upgrading_your_code_manually)

Merges all summaries collected in the default graph.

#### Args:

* <b>`key`</b>: `GraphKey` used to collect the summaries.  Defaults to
    `GraphKeys.SUMMARIES`.
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

