

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.summary.scalar

### `tf.summary.scalar`

``` python
scalar(
    name,
    tensor,
    collections=None
)
```



Defined in [`tensorflow/python/summary/summary.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/summary/summary.py).

See the guide: [Summary Operations > Generation of Summaries](../../../../api_guides/python/summary#Generation_of_Summaries)

Outputs a `Summary` protocol buffer containing a single scalar value.

The generated Summary has a Tensor.proto containing the input Tensor.

#### Args:

* <b>`name`</b>: A name for the generated node. Will also serve as the series name in
    TensorBoard.
* <b>`tensor`</b>: A real numeric Tensor containing a single value.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
    added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.


#### Returns:

  A scalar `Tensor` of type `string`. Which contains a `Summary` protobuf.


#### Raises:

* <b>`ValueError`</b>: If tensor has the wrong shape or type.