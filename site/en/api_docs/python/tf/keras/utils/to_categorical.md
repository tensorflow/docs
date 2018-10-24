

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.to_categorical

``` python
tf.keras.utils.to_categorical(
    y,
    num_classes=None
)
```



Defined in [`tensorflow/python/keras/utils/np_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/utils/np_utils.py).

Converts a class vector (integers) to binary class matrix.

E.g. for use with categorical_crossentropy.

#### Arguments:

* <b>`y`</b>: class vector to be converted into a matrix
        (integers from 0 to num_classes).
* <b>`num_classes`</b>: total number of classes.


#### Returns:

A binary matrix representation of the input.