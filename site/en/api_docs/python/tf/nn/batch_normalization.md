page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.batch_normalization


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_impl.py#L1382-L1442">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Batch normalization.

### Aliases:

* `tf.compat.v1.nn.batch_normalization`
* `tf.compat.v2.nn.batch_normalization`


``` python
tf.nn.batch_normalization(
    x,
    mean,
    variance,
    offset,
    scale,
    variance_epsilon,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Normalizes a tensor by `mean` and `variance`, and applies (optionally) a
`scale` \\(\gamma\\) to it, as well as an `offset` \\(\beta\\):

\\(\frac{\gamma(x-\mu)}{\sigma}+\beta\\)

`mean`, `variance`, `offset` and `scale` are all expected to be of one of two
shapes:

  * In all generality, they can have the same number of dimensions as the
    input `x`, with identical sizes as `x` for the dimensions that are not
    normalized over (the 'depth' dimension(s)), and dimension 1 for the
    others which are being normalized over.
    `mean` and `variance` in this case would typically be the outputs of
    <a href="../../tf/nn/moments"><code>tf.nn.moments(..., keep_dims=True)</code></a> during training, or running averages
    thereof during inference.
  * In the common case where the 'depth' dimension is the last dimension in
    the input tensor `x`, they may be one dimensional tensors of the same
    size as the 'depth' dimension.
    This is the case for example for the common `[batch, depth]` layout of
    fully-connected layers, and `[batch, height, width, depth]` for
    convolutions.
    `mean` and `variance` in this case would typically be the outputs of
    <a href="../../tf/nn/moments"><code>tf.nn.moments(..., keep_dims=False)</code></a> during training, or running averages
    thereof during inference.

See Source: [Batch Normalization: Accelerating Deep Network Training by
Reducing Internal Covariate Shift; S. Ioffe, C. Szegedy]
(http://arxiv.org/abs/1502.03167).

#### Args:


* <b>`x`</b>: Input `Tensor` of arbitrary dimensionality.
* <b>`mean`</b>: A mean `Tensor`.
* <b>`variance`</b>: A variance `Tensor`.
* <b>`offset`</b>: An offset `Tensor`, often denoted \\(\beta\\) in equations, or
  None. If present, will be added to the normalized tensor.
* <b>`scale`</b>: A scale `Tensor`, often denoted \\(\gamma\\) in equations, or
  `None`. If present, the scale is applied to the normalized tensor.
* <b>`variance_epsilon`</b>: A small float number to avoid dividing by 0.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

the normalized, scaled, offset tensor.
