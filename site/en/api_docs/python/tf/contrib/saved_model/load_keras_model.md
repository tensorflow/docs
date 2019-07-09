page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.saved_model.load_keras_model

``` python
tf.contrib.saved_model.load_keras_model(saved_model_path)
```



Defined in [`tensorflow/contrib/saved_model/python/saved_model/keras_saved_model.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/saved_model/python/saved_model/keras_saved_model.py).

Loads a keras.Model from SavedModel.

load_model reinstantiates model state by:
1) loading model topology from json (this will eventually come
   from metagraph).
2) loading model weights from checkpoint.

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

* <b>`saved_model_path`</b>: a string specifying the path to an existing SavedModel.


#### Returns:

a keras.Model instance.