page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.tensor_summary


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/summary/summary.py#L274-L327">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Outputs a `Summary` protocol buffer with a serialized tensor.proto.

### Aliases:

* <a href="/api_docs/python/tf/summary/tensor_summary"><code>tf.compat.v1.summary.tensor_summary</code></a>


``` python
tf.summary.tensor_summary(
    name,
    tensor,
    summary_description=None,
    collections=None,
    summary_metadata=None,
    family=None,
    display_name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: A name for the generated node. If display_name is not set, it will
  also serve as the tag name in TensorBoard. (In that case, the tag
  name will inherit tf name scopes.)
* <b>`tensor`</b>: A tensor of any type and shape to serialize.
* <b>`summary_description`</b>: A long description of the summary sequence. Markdown
  is supported.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
  added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
* <b>`summary_metadata`</b>: Optional SummaryMetadata proto (which describes which
  plugins may use the summary value).
* <b>`family`</b>: Optional; if provided, used as the prefix of the summary tag,
  which controls the name used for display on TensorBoard when
  display_name is not set.
* <b>`display_name`</b>: A string used to name this data in TensorBoard. If this is
  not set, then the node name will be used instead.


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.
