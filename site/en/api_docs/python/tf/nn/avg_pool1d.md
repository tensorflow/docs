page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.avg_pool1d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/avg_pool1d">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L3625-L3667">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Performs the average pooling on the input.

### Aliases:

* <a href="/api_docs/python/tf/nn/avg_pool1d"><code>tf.compat.v1.nn.avg_pool1d</code></a>
* <a href="/api_docs/python/tf/nn/avg_pool1d"><code>tf.compat.v2.nn.avg_pool1d</code></a>


``` python
tf.nn.avg_pool1d(
    input,
    ksize,
    strides,
    padding,
    data_format='NWC',
    name=None
)
```



<!-- Placeholder for "Used in" -->

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

Note internally this op reshapes and uses the underlying 2d operation.

#### Args:


* <b>`input`</b>: A 3-D `Tensor` of the format specified by `data_format`.
* <b>`ksize`</b>: An int or list of `ints` that has length `1` or `3`. The size of the
  window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1` or `3`. The stride of
  the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
  the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: An optional string from: "NWC", "NCW". Defaults to "NWC".
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of format specified by `data_format`.
The max pooled output tensor.
