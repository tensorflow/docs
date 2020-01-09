page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.nn.max_pool


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L3770-L3815">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Performs the max pooling on the input.

``` python
tf.compat.v1.nn.max_pool(
    value,
    ksize,
    strides,
    padding,
    data_format='NHWC',
    name=None,
    input=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`value`</b>: A 4-D `Tensor` of the format specified by `data_format`.
* <b>`ksize`</b>: An int or list of `ints` that has length `1`, `2` or `4`.
  The size of the window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `2` or `4`.
  The stride of the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm.
  See the "returns" section of <a href="../../../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string. 'NHWC', 'NCHW' and 'NCHW_VECT_C' are supported.
* <b>`name`</b>: Optional name for the operation.
* <b>`input`</b>: Alias for value.


#### Returns:

A `Tensor` of format specified by `data_format`.
The max pooled output tensor.
