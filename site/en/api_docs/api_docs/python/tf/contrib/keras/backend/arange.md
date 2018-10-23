

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.arange

``` python
arange(
    start,
    stop=None,
    step=1,
    dtype='int32'
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Creates a 1D tensor containing a sequence of integers.

The function arguments use the same convention as
Theano's arange: if only one argument is provided,
it is in fact the "stop" argument.

The default type of the returned tensor is `'int32'` to
match TensorFlow's default.

#### Arguments:

    start: Start value.
    stop: Stop value.
    step: Difference between two successive values.
    dtype: Integer dtype to use.


#### Returns:

    An integer tensor.