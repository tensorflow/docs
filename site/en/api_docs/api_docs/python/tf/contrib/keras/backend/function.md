

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.function

``` python
function(
    inputs,
    outputs,
    updates=None,
    **kwargs
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Instantiates a Keras function.

#### Arguments:

    inputs: List of placeholder tensors.
    outputs: List of output tensors.
    updates: List of update ops.
    **kwargs: Passed to `tf.Session.run`.


#### Returns:

    Output values as Numpy arrays.


#### Raises:

    ValueError: if invalid kwargs are passed in.