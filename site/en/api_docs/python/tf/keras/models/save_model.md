page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.save_model

Saves a model as a TensorFlow SavedModel or HDF5 file.

### Aliases:

* `tf.compat.v1.keras.models.save_model`
* `tf.compat.v2.keras.models.save_model`
* `tf.keras.models.save_model`

``` python
tf.keras.models.save_model(
    model,
    filepath,
    overwrite=True,
    include_optimizer=True,
    save_format=None
)
```



Defined in [`python/keras/saving/save.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/saving/save.py).

<!-- Placeholder for "Used in" -->

The saved model contains:
    - the model's configuration (topology)
    - the model's weights
    - the model's optimizer's state (if any)

Thus the saved model can be reinstantiated in
the exact same state, without any of the code
used for model definition or training.

#### Arguments:


* <b>`model`</b>: Keras model instance to be saved.
* <b>`filepath`</b>: One of the following:
  - String, path where to save the model
  - `h5py.File` object where to save the model
* <b>`overwrite`</b>: Whether we should overwrite any existing model at the target
  location, or instead ask the user with a manual prompt.
* <b>`include_optimizer`</b>: If True, save optimizer's state together.
* <b>`save_format`</b>: Either 'tf' or 'h5', indicating whether to save the model
  to Tensorflow SavedModel or HDF5. The 'tf' option is currently disabled,
  and will be enabled when Keras SavedModel export is no longer
  experimental. (The experimental function is
  tf.keras.experimental.export_saved_model).


#### Raises:


* <b>`ImportError`</b>: If save format is hdf5, and h5py is not available.