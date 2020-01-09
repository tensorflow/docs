page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.selu


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_nn_ops.py`



Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

### Aliases:

* `tf.compat.v1.nn.selu`
* `tf.compat.v2.nn.selu`


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
For correct dropout, use `tf.contrib.nn.alpha_dropout`.

See [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)

#### Args:


* <b>`features`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `features`.
