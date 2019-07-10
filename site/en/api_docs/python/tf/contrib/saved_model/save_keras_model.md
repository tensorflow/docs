page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.saved_model.save_keras_model

``` python
tf.contrib.saved_model.save_keras_model(
    model,
    saved_model_path,
    custom_objects=None,
    as_text=None,
    input_signature=None,
    serving_only=False
)
```



Defined in [`tensorflow/contrib/saved_model/python/saved_model/keras_saved_model.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/saved_model/python/saved_model/keras_saved_model.py).

Saves a <a href="../../../tf/keras/models/Model"><code>tf.keras.Model</code></a> into Tensorflow SavedModel format.

`save_model` generates new files/folders under the `saved_model_path` folder:
1) a checkpoint containing the model weights.
2) a saved_model.pb file containing the model's MetaGraphs. The prediction
   graph is always exported. The evaluaton and training graphs are exported
   if the following conditions are met:
   - Evaluation: model loss is defined.
   - Training: model is compiled with an optimizer defined under <a href="../../../tf/train"><code>tf.train</code></a>.
     This is because <a href="../../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a> instances cannot be
     saved to checkpoints.
3) Model's json configuration, if model.get_config() has been implemented.
   This file can be used to reload the model using
   tf.keras.models.model_from_json(). Note that if any custom objects were
   used, they should be passed to the `custom_object` argument when loading
   the model.

Model limitations:
- Sequential and functional models can always be saved.
- Subclassed models can only be saved when `serving_only=True`. This is due to
  the current implementation copying the model in order to export the training
  and evaluation graphs. Because the topology of subclassed models cannot be
  determined, the subclassed models cannot be cloned. Subclassed models will
  be entirely exportable in the future.

Note that each mode is exported in separate graphs, so different modes do not
share variables. To use the train graph with evaluation or prediction graphs,
create a new checkpoint if variable values have been updated.

Example:

```python
import tensorflow as tf

# Create a tf.keras model.
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=[10]))
model.summary()

# Save the tf.keras model in the SavedModel format.
saved_to_path = tf.contrib.saved_model.save_keras_model(
      model, '/tmp/my_simple_tf_keras_saved_model')

# Load the saved keras model back.
model_prime = tf.contrib.saved_model.load_keras_model(saved_to_path)
model_prime.summary()
```

#### Args:

* <b>`model`</b>: A <a href="../../../tf/keras/models/Model"><code>tf.keras.Model</code></a> to be saved. If the model is subclassed, the flag
    `serving_only` must be set to True.
* <b>`saved_model_path`</b>: a string specifying the path to the SavedModel directory.
    The SavedModel will be saved to a timestamped folder created within this
    directory.
* <b>`custom_objects`</b>: Optional dictionary mapping string names to custom classes
    or functions (e.g. custom loss functions).
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format. Currently
    unavailable in serving-only mode.
* <b>`input_signature`</b>: A possibly nested sequence of <a href="../../../tf/TensorSpec"><code>tf.TensorSpec</code></a> objects, used
    to specify the expected model inputs. `input_signature`'s nested structure
    should match the expected nested structure of the inputs to the model. If
    this is not set, this function will attempt to infer the input shapes and
    dtypes from the model. Note that if the model is subclassed, the tensor
    inputs to the call function should be nested in the first argument (this
    is a general requirement for using subclassed models with Keras functions
    .fit(), .predict(), etc.).
* <b>`serving_only`</b>: Export only the outputs produced from calling the model in
    predict mode. The losses, optimizer, and other training configurations are
    not saved. If the SavedModel will only be used for serving (rather than
    retraining), or if the model is subclassed, this can be set to True.


#### Returns:

String path to the SavedModel folder, a subdirectory of `saved_model_path`.


#### Raises:

* <b>`NotImplementedError`</b>: If the model is a subclassed model, and serving_only is
    False.
* <b>`ValueError`</b>: If the input signature cannot be inferred from the model.