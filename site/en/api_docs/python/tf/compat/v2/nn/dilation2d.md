page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.nn.dilation2d

Computes the grayscale dilation of 4-D `input` and 3-D `filters` tensors.

``` python
tf.compat.v2.nn.dilation2d(
    input,
    filters,
    strides,
    padding,
    data_format,
    dilations,
    name=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->

The `input` tensor has shape `[batch, in_height, in_width, depth]` and the
`filters` tensor has shape `[filter_height, filter_width, depth]`, i.e., each
input channel is processed independently of the others with its own
structuring function. The `output` tensor has shape
`[batch, out_height, out_width, depth]`. The spatial dimensions of the output
tensor depend on the `padding` algorithm. We currently only support the
default "NHWC" `data_format`.

In detail, the grayscale morphological 2-D dilation is the max-sum correlation
(for consistency with `conv2d`, we use unmirrored filters):

    output[b, y, x, c] =
       max_{dy, dx} input[b,
                          strides[1] * y + rates[1] * dy,
                          strides[2] * x + rates[2] * dx,
                          c] +
                    filters[dy, dx, c]

Max-pooling is a special case when the filter has size equal to the pooling
kernel size and contains all zeros.

Note on duality: The dilation of `input` by the `filters` is equal to the
negation of the erosion of `-input` by the reflected `filters`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`,
  `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`,
  `uint32`, `uint64`.
  4-D with shape `[batch, in_height, in_width, depth]`.
* <b>`filters`</b>: A `Tensor`. Must have the same type as `input`.
  3-D with shape `[filter_height, filter_width, depth]`.
* <b>`strides`</b>: A list of `ints` that has length `>= 4`.
  The stride of the sliding window for each dimension of the input
  tensor. Must be: `[1, stride_height, stride_width, 1]`.
* <b>`padding`</b>: A `string` from: `"SAME", "VALID"`.
  The type of padding algorithm to use.
* <b>`data_format`</b>: A `string`, only `"NCHW"` is currently supported.
* <b>`dilations`</b>: A list of `ints` that has length `>= 4`.
  The input stride for atrous morphological dilation. Must be:
  `[1, rate_height, rate_width, 1]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
