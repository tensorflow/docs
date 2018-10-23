

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.utils.to_categorical

### `tf.contrib.keras.utils.to_categorical`

``` python
to_categorical(
    y,
    num_classes=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/utils/np_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/utils/np_utils.py).

Converts a class vector (integers) to binary class matrix.

E.g. for use with categorical_crossentropy.

#### Arguments:

    y: class vector to be converted into a matrix
        (integers from 0 to num_classes).
    num_classes: total number of classes.


#### Returns:

    A binary matrix representation of the input.