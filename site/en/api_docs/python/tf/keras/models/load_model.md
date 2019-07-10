page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.load_model

Loads a model saved via `save_model`.

### Aliases:

* `tf.compat.v1.keras.models.load_model`
* `tf.compat.v2.keras.models.load_model`
* `tf.keras.models.load_model`

``` python
tf.keras.models.load_model(
    filepath,
    custom_objects=None,
    compile=True
)
```



Defined in [`python/keras/saving/save.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/saving/save.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`filepath`</b>: One of the following:
    - String, path to the saved model
    - `h5py.File` object from which to load the model
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


* <b>`ImportError`</b>: if loading from an hdf5 file and h5py is not available.
* <b>`IOError`</b>: In case of an invalid savefile.