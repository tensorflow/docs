page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.nn.crelu


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L2748-L2771">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes Concatenated ReLU.

``` python
tf.compat.v1.nn.crelu(
    features,
    name=None,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->

Concatenates a ReLU which selects only the positive part of the activation
with a ReLU which selects only the *negative* part of the activation.
Note that as a result this non-linearity doubles the depth of the activations.
Source: [Understanding and Improving Convolutional Neural Networks via
Concatenated Rectified Linear Units. W. Shang, et
al.](https://arxiv.org/abs/1603.05201)

#### Args:


* <b>`features`</b>: A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
  `int16`, or `int8`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`axis`</b>: The axis that the output values are concatenated along. Default is -1.


#### Returns:

A `Tensor` with the same type as `features`.
