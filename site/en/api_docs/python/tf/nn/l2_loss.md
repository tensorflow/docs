page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.l2_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/l2_loss">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_nn_ops.py`



L2 Loss.

### Aliases:

* <a href="/api_docs/python/tf/nn/l2_loss"><code>tf.compat.v1.nn.l2_loss</code></a>
* <a href="/api_docs/python/tf/nn/l2_loss"><code>tf.compat.v2.nn.l2_loss</code></a>


``` python
tf.nn.l2_loss(
    t,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Computes half the L2 norm of a tensor without the `sqrt`:

    output = sum(t ** 2) / 2

#### Args:


* <b>`t`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
  Typically 2-D, but may have any dimensions.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `t`.
