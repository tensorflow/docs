

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.with_same_shape

``` python
with_same_shape(
    expected_tensor,
    tensor
)
```



Defined in [`tensorflow/contrib/framework/python/framework/tensor_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/framework/python/framework/tensor_util.py).

See the guide: [Framework (contrib)](../../../../../api_guides/python/contrib.framework)

Assert tensors are the same shape, from the same graph.

#### Args:

* <b>`expected_tensor`</b>: Tensor with expected shape.
* <b>`tensor`</b>: Tensor of actual values.

#### Returns:

  Tuple of (actual_tensor, label_tensor), possibly with assert ops added.