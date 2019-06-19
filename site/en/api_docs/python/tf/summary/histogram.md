

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.histogram

``` python
tf.summary.histogram(
    name,
    values,
    collections=None,
    family=None
)
```



Defined in [`tensorflow/python/summary/summary.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/summary/summary.py).

See the guide: [Summary Operations > Generation of Summaries](../../../../api_guides/python/summary#Generation_of_Summaries)

Outputs a `Summary` protocol buffer with a histogram.

Adding a histogram summary makes it possible to visualize your data's
distribution in TensorBoard. You can see a detailed explanation of the
TensorBoard histogram dashboard
[here](https://www.tensorflow.org/get_started/tensorboard_histograms).

The generated
[`Summary`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/core/framework/summary.proto)
has one summary value containing a histogram for `values`.

This op reports an `InvalidArgument` error if any value is not finite.

#### Args:

* <b>`name`</b>: A name for the generated node. Will also serve as a series name in
    TensorBoard.
* <b>`values`</b>: A real numeric `Tensor`. Any shape. Values to use to
    build the histogram.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
    added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
* <b>`family`</b>: Optional; if provided, used as the prefix of the summary tag name,
    which controls the tab name used for display on Tensorboard.


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.