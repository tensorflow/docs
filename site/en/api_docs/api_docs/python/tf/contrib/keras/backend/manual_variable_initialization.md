

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.manual_variable_initialization

``` python
manual_variable_initialization(value)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Sets the manual variable initialization flag.

This boolean flag determines whether
variables should be initialized
as they are instantiated (default), or if
the user should handle the initialization
(e.g. via `tf.initialize_all_variables()`).

#### Arguments:

    value: Python boolean.