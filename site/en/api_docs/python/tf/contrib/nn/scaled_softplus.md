page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.nn.scaled_softplus


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/nn/python/ops/scaled_softplus.py#L37-L112">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns `y = alpha * ln(1 + exp(x / alpha))` or `min(y, clip)`.

``` python
tf.contrib.nn.scaled_softplus(
    x,
    alpha,
    clip=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This can be seen as a softplus applied to the scaled input, with the output
appropriately scaled. As `alpha` tends to 0, `scaled_softplus(x, alpha)` tends
to `relu(x)`. The clipping is optional. As alpha->0, scaled_softplus(x, alpha)
tends to relu(x), and scaled_softplus(x, alpha, clip=6) tends to relu6(x).

Note: the gradient for this operation is defined to depend on the backprop
inputs as well as the outputs of this operation.

#### Args:


* <b>`x`</b>: A `Tensor` of inputs.
* <b>`alpha`</b>: A `Tensor`, indicating the amount of smoothness. The caller
    must ensure that `alpha > 0`.
* <b>`clip`</b>: (optional) A `Tensor`, the upper bound to clip the values.
* <b>`name`</b>: A name for the scope of the operations (optional).


#### Returns:

A tensor of the size and type determined by broadcasting of the inputs.
