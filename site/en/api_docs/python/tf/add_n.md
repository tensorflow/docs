

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.add_n

### `tf.add_n`

``` python
add_n(
    inputs,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Basic Math Functions](../../../api_guides/python/math_ops#Basic_Math_Functions)

Adds all input tensors element-wise.

#### Args:

* <b>`inputs`</b>: A list of `Tensor` objects, each with same shape and type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of same shape and type as the elements of `inputs`.


#### Raises:

* <b>`ValueError`</b>: If `inputs` don't all have same shape and dtype or the shape
  cannot be inferred.