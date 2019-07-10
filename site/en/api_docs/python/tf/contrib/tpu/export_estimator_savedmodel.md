page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.export_estimator_savedmodel

Export `Estimator` trained model for TPU inference.

``` python
tf.contrib.tpu.export_estimator_savedmodel(
    estimator,
    export_dir_base,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None
)
```



Defined in [`python/estimator/tpu/tpu_estimator.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_estimator.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`estimator`</b>: `Estimator` with which model has been trained.
* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported SavedModels.
* <b>`serving_input_receiver_fn`</b>: A function that takes no argument and returns a
  `ServingInputReceiver` or `TensorServingInputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported SavedModel, or `None` if no extra assets are needed.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.


#### Returns:

The string path to the exported directory.
