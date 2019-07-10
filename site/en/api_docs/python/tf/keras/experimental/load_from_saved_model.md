page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.experimental.load_from_saved_model

Loads a keras Model from a SavedModel created by `export_saved_model()`.

### Aliases:

* `tf.compat.v1.keras.experimental.load_from_saved_model`
* `tf.compat.v2.keras.experimental.load_from_saved_model`
* `tf.contrib.saved_model.load_keras_model`
* `tf.keras.experimental.load_from_saved_model`

``` python
tf.keras.experimental.load_from_saved_model(
    saved_model_path,
    custom_objects=None
)
```



Defined in [`python/keras/saving/saved_model.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/saving/saved_model.py).

<!-- Placeholder for "Used in" -->

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
