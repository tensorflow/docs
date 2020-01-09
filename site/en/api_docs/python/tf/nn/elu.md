page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.elu


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/elu">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_nn_ops.py`



Computes exponential linear: `exp(features) - 1` if < 0, `features` otherwise.

### Aliases:

* <a href="/api_docs/python/tf/nn/elu"><code>tf.compat.v1.nn.elu</code></a>
* <a href="/api_docs/python/tf/nn/elu"><code>tf.compat.v2.nn.elu</code></a>


``` python
tf.nn.elu(
    features,
    name=None
)
```



<!-- Placeholder for "Used in" -->

See [Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)
](http://arxiv.org/abs/1511.07289)

#### Args:


* <b>`features`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `features`.
