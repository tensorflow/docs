page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.erosion2d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L4743-L4809">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the grayscale erosion of 4-D `value` and 3-D `filters` tensors.

### Aliases:

* `tf.compat.v2.nn.erosion2d`


``` python
tf.nn.erosion2d(
    value,
    filters,
    strides,
    padding,
    data_format,
    dilations,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The `value` tensor has shape `[batch, in_height, in_width, depth]` and the
`filters` tensor has shape `[filters_height, filters_width, depth]`, i.e.,
each input channel is processed independently of the others with its own
structuring function. The `output` tensor has shape
`[batch, out_height, out_width, depth]`. The spatial dimensions of the
output tensor depend on the `padding` algorithm. We currently only support the
default "NHWC" `data_format`.

In detail, the grayscale morphological 2-D erosion is given by:

    output[b, y, x, c] =
       min_{dy, dx} value[b,
                          strides[1] * y - dilations[1] * dy,
                          strides[2] * x - dilations[2] * dx,
                          c] -
                    filters[dy, dx, c]

Duality: The erosion of `value` by the `filters` is equal to the negation of
the dilation of `-value` by the reflected `filters`.

#### Args:


* <b>`value`</b>: A `Tensor`. 4-D with shape `[batch, in_height, in_width, depth]`.
* <b>`filters`</b>: A `Tensor`. Must have the same type as `value`.
  3-D with shape `[filters_height, filters_width, depth]`.
* <b>`strides`</b>: A list of `ints` that has length `>= 4`.
  1-D of length 4. The stride of the sliding window for each dimension of
  the input tensor. Must be: `[1, stride_height, stride_width, 1]`.
* <b>`padding`</b>: A `string` from: `"SAME", "VALID"`.
  The type of padding algorithm to use.
* <b>`data_format`</b>: A `string`, only `"NHWC"` is currently supported.
* <b>`dilations`</b>: A list of `ints` that has length `>= 4`.
  1-D of length 4. The input stride for atrous morphological dilation.
  Must be: `[1, rate_height, rate_width, 1]`.
* <b>`name`</b>: A name for the operation (optional). If not specified "erosion2d"
  is used.


#### Returns:

A `Tensor`. Has the same type as `value`.
4-D with shape `[batch, out_height, out_width, depth]`.



#### Raises:


* <b>`ValueError`</b>: If the `value` depth does not match `filters`' shape, or if
  padding is other than `'VALID'` or `'SAME'`.
