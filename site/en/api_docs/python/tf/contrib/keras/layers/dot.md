

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.layers.dot

### `tf.contrib.keras.layers.dot`

``` python
dot(
    inputs,
    axes,
    normalize=False,
    **kwargs
)
```



Defined in [`tensorflow/contrib/keras/python/keras/layers/merge.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/layers/merge.py).

Functional interface to the `Dot` layer.

#### Arguments:

    inputs: A list of input tensors (at least 2).
    axes: Integer or tuple of integers,
        axis or axes along which to take the dot product.
    normalize: Whether to L2-normalize samples along the
        dot product axis before taking the dot product.
        If set to True, then the output of the dot product
        is the cosine proximity between the two samples.
    **kwargs: Standard layer keyword arguments.


#### Returns:

    A tensor, the dot product of the samples from the inputs.