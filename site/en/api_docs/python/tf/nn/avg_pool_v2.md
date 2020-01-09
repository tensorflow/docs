page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.avg_pool_v2


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L3480-L3539">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Performs the avg pooling on the input.

### Aliases:

* <a href="/api_docs/python/tf/nn/avg_pool_v2"><code>tf.compat.v1.nn.avg_pool_v2</code></a>
* <a href="/api_docs/python/tf/nn/avg_pool_v2"><code>tf.compat.v2.nn.avg_pool</code></a>


``` python
tf.nn.avg_pool_v2(
    input,
    ksize,
    strides,
    padding,
    data_format=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

#### Args:


* <b>`input`</b>:  Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape +
  [num_channels]` if `data_format` does not start with "NC" (default), or
  `[batch_size, num_channels] + input_spatial_shape` if data_format starts
  with "NC". Pooling happens over the spatial dimensions only.
* <b>`ksize`</b>: An int or list of `ints` that has length `1`, `N` or `N+2`. The size
  of the window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `N` or `N+2`. The
  stride of the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
  the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string. Specifies the channel dimension. For N=1 it can be
  either "NWC" (default) or "NCW", for N=2 it can be either "NHWC" (default)
  or "NCHW" and for N=3 either "NDHWC" (default) or "NCDHW".
* <b>`name`</b>: Optional name for the operation.


#### Returns:

A `Tensor` of format specified by `data_format`.
The average pooled output tensor.
