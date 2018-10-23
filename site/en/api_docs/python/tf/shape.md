

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.shape

### `tf.shape`

``` python
shape(
    input,
    name=None,
    out_type=tf.int32
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/array_ops.py).

See the guide: [Tensor Transformations > Shapes and Shaping](../../../api_guides/python/array_ops#Shapes_and_Shaping)

Returns the shape of a tensor.

This operation returns a 1-D integer tensor representing the shape of `input`.

For example:

```python
# 't' is [[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]]
shape(t) ==> [2, 2, 3]
```

#### Args:

* <b>`input`</b>: A `Tensor` or `SparseTensor`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`out_type`</b>: (Optional) The specified output type of the operation
    (`int32` or `int64`). Defaults to `tf.int32`.


#### Returns:

  A `Tensor` of type `out_type`.