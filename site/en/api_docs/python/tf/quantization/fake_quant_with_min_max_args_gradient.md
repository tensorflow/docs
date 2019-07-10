page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.quantization.fake_quant_with_min_max_args_gradient

Compute gradients for a FakeQuantWithMinMaxArgs operation.

### Aliases:

* `tf.compat.v1.fake_quant_with_min_max_args_gradient`
* `tf.compat.v1.quantization.fake_quant_with_min_max_args_gradient`
* `tf.compat.v2.quantization.fake_quant_with_min_max_args_gradient`
* `tf.fake_quant_with_min_max_args_gradient`
* `tf.quantization.fake_quant_with_min_max_args_gradient`

``` python
tf.quantization.fake_quant_with_min_max_args_gradient(
    gradients,
    inputs,
    min=-6,
    max=6,
    num_bits=8,
    narrow_range=False,
    name=None
)
```



Defined in generated file: `python/ops/gen_array_ops.py`.

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`gradients`</b>: A `Tensor` of type `float32`.
  Backpropagated gradients above the FakeQuantWithMinMaxArgs operation.
* <b>`inputs`</b>: A `Tensor` of type `float32`.
  Values passed as inputs to the FakeQuantWithMinMaxArgs operation.
* <b>`min`</b>: An optional `float`. Defaults to `-6`.
* <b>`max`</b>: An optional `float`. Defaults to `6`.
* <b>`num_bits`</b>: An optional `int`. Defaults to `8`.
* <b>`narrow_range`</b>: An optional `bool`. Defaults to `False`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32`.
