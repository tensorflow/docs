page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.softsign


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_nn_ops.py`



Computes softsign: `features / (abs(features) + 1)`.

### Aliases:

* `tf.compat.v1.math.softsign`
* `tf.compat.v1.nn.softsign`
* `tf.compat.v2.math.softsign`
* `tf.compat.v2.nn.softsign`
* `tf.math.softsign`


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
