page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.with_same_shape

Assert tensors are the same shape, from the same graph.

``` python
tf.contrib.framework.with_same_shape(
    expected_tensor,
    tensor
)
```



Defined in [`contrib/framework/python/framework/tensor_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/framework/tensor_util.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`expected_tensor`</b>: Tensor with expected shape.
* <b>`tensor`</b>: Tensor of actual values.

#### Returns:

The original tensor argument, possibly with assert ops added.
