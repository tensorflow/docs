page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.summary.merge_all


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/summary.py#L376-L406">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Merges all summaries collected in the default graph.

``` python
tf.compat.v1.summary.merge_all(
    key=tf.GraphKeys.SUMMARIES,
    scope=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


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
summaries under eager execution, use `tf.contrib.summary` instead.
