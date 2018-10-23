


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.fake_quant_with_min_max_args_gradient

### `tf.fake_quant_with_min_max_args_gradient`

```
tf.fake_quant_with_min_max_args_gradient(gradients, inputs, min=None, max=None, name=None)
```


See the guide: [Tensor Transformations > Fake quantization](../../../api_guides/python/array_ops#Fake_quantization)

Compute gradients for a FakeQuantWithMinMaxArgs operation.

#### Args:

* <b>`gradients`</b>: A `Tensor` of type `float32`.
    Backpropagated gradients above the FakeQuantWithMinMaxArgs operation.
* <b>`inputs`</b>: A `Tensor` of type `float32`.
    Values passed as inputs to the FakeQuantWithMinMaxArgs operation.
* <b>`min`</b>: An optional `float`. Defaults to `-6`.
* <b>`max`</b>: An optional `float`. Defaults to `6`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `float32`.
  Backpropagated gradients below the FakeQuantWithMinMaxArgs operation:
  `gradients * (inputs >= min && inputs <= max)`.

Defined in `tensorflow/python/ops/gen_array_ops.py`.

