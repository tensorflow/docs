page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.load_model


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/saving/save.py#L118-L154">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads a model saved via `save_model`.

### Aliases:

* `tf.compat.v1.keras.models.load_model`
* `tf.compat.v2.keras.models.load_model`


``` python
tf.keras.models.load_model(
    filepath,
    custom_objects=None,
    compile=True
)
```



### Used in the guide:

* [Keras overview](https://www.tensorflow.org/guide/keras/overview)
* [Save and serialize models with Keras](https://www.tensorflow.org/guide/keras/save_and_serialize)
* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)

### Used in the tutorials:

* [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load)
* [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load)




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
