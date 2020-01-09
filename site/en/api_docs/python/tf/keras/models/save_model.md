page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.save_model


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/models/save_model">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/saving/save.py#L46-L112">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Saves a model as a TensorFlow SavedModel or HDF5 file.

### Aliases:

* <a href="/api_docs/python/tf/keras/models/save_model"><code>tf.compat.v1.keras.models.save_model</code></a>
* <a href="/api_docs/python/tf/keras/models/save_model"><code>tf.compat.v2.keras.models.save_model</code></a>


``` python
tf.keras.models.save_model(
    model,
    filepath,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None
)
```



<!-- Placeholder for "Used in" -->

The saved model contains:
    - the model's configuration (topology)
    - the model's weights
    - the model's optimizer's state (if any)

Thus the saved model can be reinstantiated in
the exact same state, without any of the code
used for model definition or training.

_SavedModel serialization_ (not yet added)

The SavedModel serialization path uses <a href="../../../tf/saved_model/save"><code>tf.saved_model.save</code></a> to save the model
and all trackable objects attached to the model (e.g. layers and variables).
`@tf.function`-decorated methods are also saved. Additional trackable objects
and functions are added to the SavedModel to allow the model to be
loaded back as a Keras Model object.

#### Arguments:


* <b>`model`</b>: Keras model instance to be saved.
* <b>`filepath`</b>: One of the following:
  - String, path where to save the model
  - `h5py.File` object where to save the model
* <b>`overwrite`</b>: Whether we should overwrite any existing model at the target
  location, or instead ask the user with a manual prompt.
* <b>`include_optimizer`</b>: If True, save optimizer's state together.
* <b>`save_format`</b>: Either 'tf' or 'h5', indicating whether to save the model
  to Tensorflow SavedModel or HDF5. Defaults to 'tf' in TF 2.X, and 'h5'
  in TF 1.X.
* <b>`signatures`</b>: Signatures to save with the SavedModel. Applicable to the 'tf'
  format only. Please see the `signatures` argument in
  <a href="../../../tf/saved_model/save"><code>tf.saved_model.save</code></a> for details.


#### Raises:


* <b>`ImportError`</b>: If save format is hdf5, and h5py is not available.
