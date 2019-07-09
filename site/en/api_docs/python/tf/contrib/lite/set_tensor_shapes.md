page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.set_tensor_shapes

``` python
tf.contrib.lite.set_tensor_shapes(
    tensors,
    shapes
)
```



Defined in [`tensorflow/contrib/lite/python/convert_saved_model.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/lite/python/convert_saved_model.py).

Sets Tensor shape for each tensor if the shape is defined.

#### Args:

* <b>`tensors`</b>: TensorFlow ops.Tensor.
* <b>`shapes`</b>: Dict of strings representing input tensor names to list of
    integers representing input shapes (e.g., {"foo": : [1, 16, 16, 3]}).