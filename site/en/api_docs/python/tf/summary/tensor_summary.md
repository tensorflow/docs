

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.summary.tensor_summary

### `tf.summary.tensor_summary`

``` python
tensor_summary(
    name,
    tensor,
    summary_description=None,
    collections=None
)
```



Defined in [`tensorflow/python/ops/summary_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/summary_ops.py).

See the guide: [Summary Operations > Generation of Summaries](../../../../api_guides/python/summary#Generation_of_Summaries)

Outputs a `Summary` protocol buffer with a serialized tensor.proto.

The generated
[`Summary`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/core/framework/summary.proto)
has one summary value containing the input tensor.

#### Args:

* <b>`name`</b>: A name for the generated node. Will also serve as the series name in
    TensorBoard.
* <b>`tensor`</b>: A tensor of any type and shape to serialize.
* <b>`summary_description`</b>: Optional summary_pb2.SummaryDescription()
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
    added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.


#### Returns:

  A scalar `Tensor` of type `string`. The serialized `Summary` protocol
  buffer.