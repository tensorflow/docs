

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.prod

### `tf.contrib.keras.backend.prod`

``` python
prod(
    x,
    axis=None,
    keepdims=False
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Multiplies the values in a tensor, alongside the specified axis.

#### Arguments:

    x: A tensor or variable.
    axis: An integer, the axis to compute the product.
    keepdims: A boolean, whether to keep the dimensions or not.
        If `keepdims` is `False`, the rank of the tensor is reduced
        by 1. If `keepdims` is `True`,
        the reduced dimension is retained with length 1.


#### Returns:

    A tensor with the product of elements of `x`.