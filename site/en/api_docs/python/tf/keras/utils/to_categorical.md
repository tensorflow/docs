page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.to_categorical

Converts a class vector (integers) to binary class matrix.

### Aliases:

* `tf.compat.v1.keras.utils.to_categorical`
* `tf.compat.v2.keras.utils.to_categorical`
* `tf.keras.utils.to_categorical`

``` python
tf.keras.utils.to_categorical(
    y,
    num_classes=None,
    dtype='float32'
)
```



Defined in [`python/keras/utils/np_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/utils/np_utils.py).

<!-- Placeholder for "Used in" -->

E.g. for use with categorical_crossentropy.

#### Arguments:


* <b>`y`</b>: class vector to be converted into a matrix
    (integers from 0 to num_classes).
* <b>`num_classes`</b>: total number of classes.
* <b>`dtype`</b>: The data type expected by the input. Default: `'float32'`.


#### Returns:

A binary matrix representation of the input. The classes axis is placed
last.
