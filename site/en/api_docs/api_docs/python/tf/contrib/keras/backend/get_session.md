

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.get_session

``` python
get_session()
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Returns the TF session to be used by the backend.

If a default TensorFlow session is available, we will return it.

Else, we will return the global Keras session.

If no global Keras session exists at this point:
we will create a new global session.

Note that you can manually set the global session
via `K.set_session(sess)`.

#### Returns:

    A TensorFlow session.