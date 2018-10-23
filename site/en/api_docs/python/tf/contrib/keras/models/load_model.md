

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.models.load_model

### `tf.contrib.keras.models.load_model`

``` python
load_model(
    filepath,
    custom_objects=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/models.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/models.py).

Loads a model saved via `save_model`.

#### Arguments:

    filepath: String, path to the saved model.
    custom_objects: Optional dictionary mapping names
        (strings) to custom classes or functions to be
        considered during deserialization.


#### Returns:

    A Keras model instance. If an optimizer was found
    as part of the saved model, the model is already
    compiled. Otherwise, the model is uncompiled and
    a warning will be displayed.


#### Raises:

    ImportError: if h5py is not available.
    ValueError: In case of an invalid savefile.