

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.models.load_model

``` python
tf.keras.models.load_model(
    filepath,
    custom_objects=None,
    compile=True
)
```



Defined in [`tensorflow/python/keras/_impl/keras/models.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/models.py).

Loads a model saved via `save_model`.

#### Arguments:

* <b>`filepath`</b>: String, path to the saved model.
* <b>`custom_objects`</b>: Optional dictionary mapping names
        (strings) to custom classes or functions to be
        considered during deserialization.
* <b>`compile`</b>: Boolean, whether to compile the model
        after loading.


#### Returns:

A Keras model instance. If an optimizer was found
as part of the saved model, the model is already
compiled. Otherwise, the model is uncompiled and
a warning will be displayed. When `compile` is set
to False, the compilation is omitted without any
warning.


#### Raises:

* <b>`ImportError`</b>: if h5py is not available.
* <b>`ValueError`</b>: In case of an invalid savefile.