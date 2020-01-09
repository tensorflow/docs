page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.softsign


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/softsign">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_nn_ops.py`



Computes softsign: `features / (abs(features) + 1)`.

### Aliases:

* <a href="/api_docs/python/tf/nn/softsign"><code>tf.compat.v1.math.softsign</code></a>
* <a href="/api_docs/python/tf/nn/softsign"><code>tf.compat.v1.nn.softsign</code></a>
* <a href="/api_docs/python/tf/nn/softsign"><code>tf.compat.v2.math.softsign</code></a>
* <a href="/api_docs/python/tf/nn/softsign"><code>tf.compat.v2.nn.softsign</code></a>
* <a href="/api_docs/python/tf/nn/softsign"><code>tf.math.softsign</code></a>


``` python
tf.nn.softsign(
    features,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`features`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `features`.
