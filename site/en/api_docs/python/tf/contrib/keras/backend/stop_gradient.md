

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.stop_gradient

### `tf.contrib.keras.backend.stop_gradient`

``` python
stop_gradient(variables)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Returns `variables` but with zero gradient w.r.t. every other variable.

#### Arguments:

    variables: List of variables.


#### Returns:

    The same list of variables.