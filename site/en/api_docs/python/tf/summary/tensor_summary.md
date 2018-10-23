

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.summary.tensor_summary

``` python
tensor_summary(
    name,
    tensor,
    summary_description=None,
    collections=None,
    summary_metadata=None,
    family=None,
    display_name=None
)
```



Defined in [`tensorflow/python/ops/summary_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/summary_ops.py).

See the guide: [Summary Operations > Generation of Summaries](../../../../api_guides/python/summary#Generation_of_Summaries)

Outputs a `Summary` protocol buffer with a serialized tensor.proto.

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