

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.fake_quant_with_min_max_args

### `tf.fake_quant_with_min_max_args`

``` python
fake_quant_with_min_max_args(
    inputs,
    min=None,
    max=None,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_array_ops.py`.

See the guide: [Tensor Transformations > Fake quantization](../../../api_guides/python/array_ops#Fake_quantization)

Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same type.

Attributes [min; max] define the clamping range for the 'inputs' data.  Op
divides this range into 255 steps (total of 256 values), then replaces each
'inputs' value with the closest of the quantized step values.

Quantization is called fake since the output is still in floating point.

#### Args:

* <b>`inputs`</b>: A `Tensor` of type `float32`.
* <b>`min`</b>: An optional `float`. Defaults to `-6`.
* <b>`max`</b>: An optional `float`. Defaults to `6`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `float32`.