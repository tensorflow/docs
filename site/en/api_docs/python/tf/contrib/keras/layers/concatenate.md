

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.layers.concatenate

### `tf.contrib.keras.layers.concatenate`

``` python
concatenate(
    inputs,
    axis=-1,
    **kwargs
)
```



Defined in [`tensorflow/contrib/keras/python/keras/layers/merge.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/layers/merge.py).

Functional interface to the `Concatenate` layer.

#### Arguments:

    inputs: A list of input tensors (at least 2).
    axis: Concatenation axis.
    **kwargs: Standard layer keyword arguments.


#### Returns:

    A tensor, the concatenation of the inputs alongside axis `axis`.