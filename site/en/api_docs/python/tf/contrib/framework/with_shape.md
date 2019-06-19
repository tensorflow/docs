page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.with_shape

``` python
tf.contrib.framework.with_shape(
    expected_shape,
    tensor
)
```



Defined in [`tensorflow/contrib/framework/python/framework/tensor_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/framework/python/framework/tensor_util.py).

See the guide: [Framework (contrib)](../../../../../api_guides/python/contrib.framework)

Asserts tensor has expected shape.

If tensor shape and expected_shape, are fully defined, assert they match.
Otherwise, add assert op that will validate the shape when tensor is
evaluated, and set shape on tensor.

#### Args:

* <b>`expected_shape`</b>: Expected shape to assert, as a 1D array of ints, or tensor
      of same.
* <b>`tensor`</b>: Tensor whose shape we're validating.

#### Returns:

tensor, perhaps with a dependent assert operation.

#### Raises:

* <b>`ValueError`</b>: if tensor has an invalid shape.