page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.guarantee_const


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Gives a guarantee to the TF runtime that the input tensor is a constant.

### Aliases:

* `tf.compat.v1.guarantee_const`
* `tf.compat.v2.guarantee_const`


``` python
tf.guarantee_const(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The runtime is then free to make optimizations based on this.

Only accepts value typed tensors as inputs and rejects resource variable handles
as input.

Returns the input tensor without modification.

#### Args:


* <b>`input`</b>: A `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
