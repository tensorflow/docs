

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.one_hot

### `tf.contrib.keras.backend.one_hot`

``` python
one_hot(
    indices,
    num_classes
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Computes the one-hot representation of an integer tensor.

#### Arguments:

    indices: nD integer tensor of shape
        `(batch_size, dim1, dim2, ... dim(n-1))`
    num_classes: Integer, number of classes to consider.


#### Returns:

    (n + 1)D one hot representation of the input
    with shape `(batch_size, dim1, dim2, ... dim(n-1), num_classes)`


#### Returns:

    The one-hot tensor.