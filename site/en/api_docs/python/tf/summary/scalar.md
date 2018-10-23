

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.summary.scalar

``` python
tf.summary.scalar(
    name,
    tensor,
    collections=None,
    family=None
)
```



Defined in [`tensorflow/python/summary/summary.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/summary/summary.py).

See the guide: [Summary Operations > Generation of Summaries](../../../../api_guides/python/summary#Generation_of_Summaries)

Outputs a `Summary` protocol buffer containing a single scalar value.

The generated Summary has a Tensor.proto containing the input Tensor.

#### Args:

* <b>`name`</b>: A name for the generated node. Will also serve as the series name in
    TensorBoard.
* <b>`tensor`</b>: A real numeric Tensor containing a single value.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
    added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
* <b>`family`</b>: Optional; if provided, used as the prefix of the summary tag name,
    which controls the tab name used for display on Tensorboard.


#### Returns:

A scalar `Tensor` of type `string`. Which contains a `Summary` protobuf.


#### Raises:

* <b>`ValueError`</b>: If tensor has the wrong shape or type.