page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.experimental.load_from_saved_model


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/experimental/load_from_saved_model">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/saving/saved_model_experimental.py#L373-L428">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads a keras Model from a SavedModel created by `export_saved_model()`. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/keras/experimental/load_from_saved_model"><code>tf.compat.v1.keras.experimental.load_from_saved_model</code></a>
* <a href="/api_docs/python/tf/keras/experimental/load_from_saved_model"><code>tf.compat.v2.keras.experimental.load_from_saved_model</code></a>
* <a href="/api_docs/python/tf/keras/experimental/load_from_saved_model"><code>tf.contrib.saved_model.load_keras_model</code></a>


``` python
tf.keras.experimental.load_from_saved_model(
    saved_model_path,
    custom_objects=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
The experimental save and load functions have been  deprecated. Please switch to <a href="../../../tf/keras/models/load_model"><code>tf.keras.models.load_model</code></a>.

This function reinstantiates model state by:
1) loading model topology from json (this will eventually come
   from metagraph).
2) loading model weights from checkpoint.

#### Example:



```python
import tensorflow as tf

# Create a tf.keras model.
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=[10]))
model.summary()

# Save the tf.keras model in the SavedModel format.
path = '/tmp/simple_keras_model'
tf.keras.experimental.export_saved_model(model, path)

# Load the saved keras model back.
new_model = tf.keras.experimental.load_from_saved_model(path)
new_model.summary()
```

#### Args:


* <b>`saved_model_path`</b>: a string specifying the path to an existing SavedModel.
* <b>`custom_objects`</b>: Optional dictionary mapping names
    (strings) to custom classes or functions to be
    considered during deserialization.


#### Returns:

a keras.Model instance.
