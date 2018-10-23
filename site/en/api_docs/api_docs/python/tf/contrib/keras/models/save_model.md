

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.models.save_model

``` python
save_model(
    model,
    filepath,
    overwrite=True,
    include_optimizer=True
)
```



Defined in [`tensorflow/contrib/keras/python/keras/models.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/models.py).

Save a model to a HDF5 file.

The saved model contains:
    - the model's configuration (topology)
    - the model's weights
    - the model's optimizer's state (if any)

Thus the saved model can be reinstantiated in
the exact same state, without any of the code
used for model definition or training.

#### Arguments:

    model: Keras model instance to be saved.
    filepath: String, path where to save the model.
    overwrite: Whether we should overwrite any existing
        model at the target location, or instead
        ask the user with a manual prompt.
    include_optimizer: If True, save optimizer's state together.


#### Raises:

    ImportError: if h5py is not available.