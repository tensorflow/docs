page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.load_model


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/models/load_model">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/saving/save.py#L115-L151">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads a model saved via `save_model`.

### Aliases:

* <a href="/api_docs/python/tf/keras/models/load_model"><code>tf.compat.v1.keras.models.load_model</code></a>
* <a href="/api_docs/python/tf/keras/models/load_model"><code>tf.compat.v2.keras.models.load_model</code></a>


``` python
tf.keras.models.load_model(
    filepath,
    custom_objects=None,
    compile=True
)
```



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
