page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.softplus


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_nn_ops.py`



Computes softplus: `log(exp(features) + 1)`.

### Aliases:

* `tf.compat.v1.math.softplus`
* `tf.compat.v1.nn.softplus`
* `tf.compat.v2.math.softplus`
* `tf.compat.v2.nn.softplus`
* `tf.nn.softplus`


``` python
tf.math.softplus(
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
