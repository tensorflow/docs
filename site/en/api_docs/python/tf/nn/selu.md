page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.selu


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/selu">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_nn_ops.py`



Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

### Aliases:

* <a href="/api_docs/python/tf/nn/selu"><code>tf.compat.v1.nn.selu</code></a>
* <a href="/api_docs/python/tf/nn/selu"><code>tf.compat.v2.nn.selu</code></a>


``` python
tf.nn.selu(
    features,
    name=None
)
```



<!-- Placeholder for "Used in" -->

if < 0, `scale * features` otherwise.

To be used together with
`initializer = tf.variance_scaling_initializer(factor=1.0, mode='FAN_IN')`.
For correct dropout, use <a href="../../tf/contrib/nn/alpha_dropout"><code>tf.contrib.nn.alpha_dropout</code></a>.

See [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)

#### Args:


* <b>`features`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `features`.
