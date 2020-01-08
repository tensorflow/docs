page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.saved_model.save_keras_model

``` python
tf.contrib.saved_model.save_keras_model(
    model,
    saved_model_path,
    custom_objects=None,
    as_text=None
)
```



Defined in [`tensorflow/contrib/saved_model/python/saved_model/keras_saved_model.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/saved_model/python/saved_model/keras_saved_model.py).

Save a <a href="../../../tf/keras/models/Model"><code>tf.keras.Model</code></a> into Tensorflow SavedModel format.

`save_model` generates new files/folders under the `saved_model_path` folder:
1) an asset folder containing the json string of the model's
   configuration (topology).
2) a checkpoint containing the model weights.
3) a saved_model.pb file containing the model's MetaGraphs. The prediction
   graph is always exported. The evaluaton and training graphs are exported
   if the following conditions are met:
   - Evaluation: model loss is defined.
   - Training: model is compiled with an optimizer defined under <a href="../../../tf/train"><code>tf.train</code></a>.
     This is because <a href="../../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a> instances cannot be
     saved to checkpoints.

Model Requirements:
- Model must be a sequential model or functional model. Subclassed models can
  not be saved via this function, unless you provide an implementation for
  get_config() and from_config().
- All variables must be saveable by the model. In general, this condition is
  met through the use of layers defined in the keras library. However,
  there is currently a bug with variables created in Lambda layer functions
  not being saved correctly (see
  https://github.com/keras-team/keras/issues/9740).

Note that each mode is exported in separate graphs, so different modes do not
share variables. To use the train graph with evaluation or prediction graphs,
create a new checkpoint if variable values have been updated.

#### Args:

* <b>`model`</b>: A <a href="../../../tf/keras/models/Model"><code>tf.keras.Model</code></a> to be saved.
* <b>`saved_model_path`</b>: a string specifying the path to the SavedModel directory.
    The SavedModel will be saved to a timestamped folder created within this
    directory.
* <b>`custom_objects`</b>: Optional dictionary mapping string names to custom classes
    or functions (e.g. custom loss functions).
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.


#### Returns:

String path to the SavedModel folder, a subdirectory of `saved_model_path`.


#### Raises:

* <b>`NotImplementedError`</b>: If the passed in model is a subclassed model.
