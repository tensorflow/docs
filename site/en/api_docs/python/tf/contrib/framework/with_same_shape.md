page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.with_same_shape

``` python
tf.contrib.framework.with_same_shape(
    expected_tensor,
    tensor
)
```



Defined in [`tensorflow/contrib/framework/python/framework/tensor_util.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/framework/python/framework/tensor_util.py).

Assert tensors are the same shape, from the same graph.

#### Args:

* <b>`expected_tensor`</b>: Tensor with expected shape.
* <b>`tensor`</b>: Tensor of actual values.

#### Returns:

The original tensor argument, possibly with assert ops added.