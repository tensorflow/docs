page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.conv1d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L1685-L1747">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes a 1-D convolution given 3-D input and filter tensors.

### Aliases:

* `tf.compat.v2.nn.conv1d`


``` python
tf.nn.conv1d(
    input,
    filters,
    stride,
    padding,
    data_format='NWC',
    dilations=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given an input tensor of shape
  [batch, in_width, in_channels]
if data_format is "NWC", or
  [batch, in_channels, in_width]
if data_format is "NCW",
and a filter / kernel tensor of shape
[filter_width, in_channels, out_channels], this op reshapes
the arguments to pass them to conv2d to perform the equivalent
convolution operation.

Internally, this op reshapes the input tensors and invokes <a href="../../tf/nn/conv2d"><code>tf.nn.conv2d</code></a>.
For example, if `data_format` does not start with "NC", a tensor of shape
  [batch, in_width, in_channels]
is reshaped to
  [batch, 1, in_width, in_channels],
and the filter is reshaped to
  [1, filter_width, in_channels, out_channels].
The result is then reshaped back to
  [batch, out_width, out_channels]
\(where out_width is a function of the stride and padding as in conv2d\) and
returned to the caller.

#### Args:


* <b>`input`</b>: A 3D `Tensor`.  Must be of type `float16`, `float32`, or `float64`.
* <b>`filters`</b>: A 3D `Tensor`.  Must have the same type as `input`.
* <b>`stride`</b>: An int or list of `ints` that has length `1` or `3`.  The number of
  entries by which the filter is moved right at each step.
* <b>`padding`</b>: 'SAME' or 'VALID'
* <b>`data_format`</b>: An optional `string` from `"NWC", "NCW"`.  Defaults to `"NWC"`,
  the data is stored in the order of [batch, in_width, in_channels].  The
  `"NCW"` format stores data as [batch, in_channels, in_width].
* <b>`dilations`</b>: An int or list of `ints` that has length `1` or `3` which
  defaults to 1. The dilation factor for each dimension of input. If set to
  k > 1, there will be k-1 skipped cells between each filter element on that
  dimension. Dilations in the batch and depth dimensions must be 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`.  Has the same type as input.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is invalid.
